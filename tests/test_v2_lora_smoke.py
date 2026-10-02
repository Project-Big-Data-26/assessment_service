import torch
from transformers import BertConfig, BertModel, BertTokenizer
from safetensors.torch import save_file

from app.classification.v2.model import (
    CONDITIONED_DIFFICULTY_ARCHITECTURE,
    GRADE_AWARE_ORDINAL_ARCHITECTURE,
    GradeAwareOrdinalDifficultyHead,
    ThreeHeadIndoBERT,
)
from app.classification.v2.artifact import CalibrationSpec, new_manifest, sha256_file, write_manifest
from app.classification.v2.contracts import HEAD_LABELS, V2ClassificationRequest
from app.classification.v2.runtime import V2ClassifierRuntime


def test_only_lora_and_heads_receive_gradients_and_tiny_fixture_overfits(tmp_path):
    torch.manual_seed(7)
    config = BertConfig(
        vocab_size=64,
        hidden_size=24,
        num_hidden_layers=1,
        num_attention_heads=4,
        intermediate_size=32,
        max_position_embeddings=32,
    )
    BertModel(config).save_pretrained(tmp_path, safe_serialization=True)
    model = ThreeHeadIndoBERT.from_pretrained_with_lora(
        str(tmp_path),
        local_files_only=True,
        rank=4,
        alpha=8,
        dropout=0.0,
    )
    trainable = {name for name, parameter in model.named_parameters() if parameter.requires_grad}
    assert trainable
    assert all("lora_" in name or name.startswith("heads.") for name in trainable)
    assert any("lora_" in name for name in trainable)
    assert any(name.startswith("heads.") for name in trainable)

    input_ids = torch.tensor(
        [[1, value, value, 2, 0, 0] for value in (4, 8, 12, 16)] * 2,
        dtype=torch.long,
    )
    attention_mask = (input_ids != 0).long()
    labels = {
        "mathCognitiveDomain": torch.tensor([0, 1, 2, 0] * 2),
        "knowledgeDimension": torch.tensor([0, 1, 2, 3] * 2),
        "intendedDifficulty": torch.tensor([0, 1, 2, 0] * 2),
    }
    optimizer = torch.optim.AdamW(
        [parameter for parameter in model.parameters() if parameter.requires_grad], lr=0.03
    )
    loss_fn = torch.nn.CrossEntropyLoss()

    def loss_value():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        return sum(loss_fn(outputs[head], target) for head, target in labels.items())

    initial = float(loss_value().detach())
    for _ in range(60):
        loss = loss_value()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    final = float(loss_value().detach())
    assert final < initial * 0.35


def test_conditioned_difficulty_uses_soft_head_probabilities_without_backpropagating_into_heads(tmp_path):
    torch.manual_seed(8)
    config = BertConfig(
        vocab_size=32,
        hidden_size=16,
        num_hidden_layers=1,
        num_attention_heads=4,
        intermediate_size=24,
        max_position_embeddings=32,
    )
    BertModel(config).save_pretrained(tmp_path, safe_serialization=True)
    model = ThreeHeadIndoBERT.from_pretrained_with_lora(
        str(tmp_path),
        local_files_only=True,
        rank=4,
        alpha=8,
        dropout=0.0,
        architecture_version=CONDITIONED_DIFFICULTY_ARCHITECTURE,
    )
    assert model.heads["intendedDifficulty"].in_features == 16 + 3 + 4
    input_ids = torch.tensor([[1, 5, 6, 2]], dtype=torch.long)
    attention_mask = torch.ones_like(input_ids)
    output = model(input_ids=input_ids, attention_mask=attention_mask)
    assert output["mathCognitiveDomain"].shape == (1, 3)
    assert output["knowledgeDimension"].shape == (1, 4)
    assert output["intendedDifficulty"].shape == (1, 3)

    model.zero_grad(set_to_none=True)
    output["intendedDifficulty"].sum().backward()
    assert model.heads["intendedDifficulty"].weight.grad is not None
    assert model.heads["mathCognitiveDomain"].weight.grad is None
    assert model.heads["knowledgeDimension"].weight.grad is None


def test_grade_aware_ordinal_head_has_ordered_cutpoints_and_valid_probabilities(tmp_path):
    torch.manual_seed(12)
    config = BertConfig(
        vocab_size=32,
        hidden_size=16,
        num_hidden_layers=1,
        num_attention_heads=4,
        intermediate_size=24,
        max_position_embeddings=32,
    )
    BertModel(config).save_pretrained(tmp_path, safe_serialization=True)
    model = ThreeHeadIndoBERT.from_pretrained_with_lora(
        str(tmp_path),
        local_files_only=True,
        rank=4,
        alpha=8,
        dropout=0.0,
        architecture_version=GRADE_AWARE_ORDINAL_ARCHITECTURE,
        grade_embedding_dim=6,
    )
    model.eval()
    output = model(
        input_ids=torch.tensor([[1, 5, 6, 2], [1, 6, 7, 2]], dtype=torch.long),
        attention_mask=torch.ones((2, 4), dtype=torch.long),
        grades=torch.tensor([1, 6]),
    )
    probabilities = output["intendedDifficulty"].exp()
    assert probabilities.shape == (2, 3)
    assert torch.all(probabilities >= 0)
    assert torch.allclose(probabilities.sum(dim=-1), torch.ones(2), atol=1e-6)
    cutpoints = model.heads["intendedDifficulty"].ordered_cutpoints()
    assert cutpoints[1] > cutpoints[0]
    output["intendedDifficultyOrdinalLogits"].sum().backward()
    assert model.heads["intendedDifficulty"].scorer.weight.grad is not None
    state = {key: value.detach().clone() for key, value in model.heads.state_dict().items()}
    clone = ThreeHeadIndoBERT.from_pretrained_with_lora(
        str(tmp_path),
        local_files_only=True,
        rank=4,
        alpha=8,
        dropout=0.0,
        architecture_version=GRADE_AWARE_ORDINAL_ARCHITECTURE,
        grade_embedding_dim=6,
    )
    clone.heads.load_state_dict(state, strict=True)
    clone.eval()
    assert torch.allclose(
        clone.heads["intendedDifficulty"].ordered_cutpoints(), cutpoints.detach()
    )
    clone_output = clone(
        input_ids=torch.tensor([[1, 5, 6, 2], [1, 6, 7, 2]], dtype=torch.long),
        attention_mask=torch.ones((2, 4), dtype=torch.long),
        grades=torch.tensor([1, 6]),
    )["intendedDifficulty"].exp()
    assert torch.allclose(clone_output, probabilities.detach(), atol=1e-6)


def test_ordinal_label_mapping_has_easy_medium_and_hard_regions():
    head = GradeAwareOrdinalDifficultyHead(hidden_size=1, grade_embedding_dim=1)
    with torch.no_grad():
        head.grade_embedding.weight.zero_()
        head.scorer.weight.zero_()
        head.first_cutpoint.fill_(-1.0)
        head.cutpoint_gap.fill_(torch.log(torch.expm1(torch.tensor(2.0))))
    pooled = torch.zeros((1, 1))
    grade = torch.tensor([1])
    labels = []
    for score in (-5.0, 0.0, 5.0):
        with torch.no_grad():
            head.scorer.bias.fill_(score)
            log_probabilities, _ = head(pooled, grade)
        labels.append(int(log_probabilities.argmax(dim=-1).item()))
    assert labels == [0, 1, 2]


def test_packaged_adapter_heads_and_tokenizer_load_fully_offline(tmp_path):
    torch.manual_seed(9)
    artifact = tmp_path / "artifact"
    base_path = artifact / "base_model"
    adapter_path = artifact / "adapter"
    tokenizer_path = artifact / "tokenizer"
    config = BertConfig(
        vocab_size=32,
        hidden_size=16,
        num_hidden_layers=1,
        num_attention_heads=4,
        intermediate_size=24,
        max_position_embeddings=128,
    )
    BertModel(config).save_pretrained(base_path, safe_serialization=True)
    model = ThreeHeadIndoBERT.from_pretrained_with_lora(
        str(base_path),
        local_files_only=True,
        rank=4,
        alpha=8,
        dropout=0.0,
        architecture_version=CONDITIONED_DIFFICULTY_ARCHITECTURE,
    )
    model.encoder.save_pretrained(adapter_path, safe_serialization=True)
    save_file(
        {key: value.detach().contiguous() for key, value in model.heads.state_dict().items()},
        str(artifact / "heads.safetensors"),
    )
    vocab = ["[PAD]", "[UNK]", "[CLS]", "[SEP]", "[MASK]", "kelas", "soal", "pilihan", "hitung"]
    vocab.extend(f"token{index}" for index in range(32 - len(vocab)))
    vocab_path = tmp_path / "vocab.txt"
    vocab_path.write_text("\n".join(vocab), encoding="utf-8")
    BertTokenizer(vocab_file=str(vocab_path)).save_pretrained(tokenizer_path)
    files = {
        path.relative_to(artifact).as_posix(): sha256_file(path)
        for path in artifact.rglob("*")
        if path.is_file()
    }
    manifest = new_manifest(
        modelVersion="tiny-offline-v1",
        baseModel="local-tiny-bert",
        baseRevision="fixture",
        datasetSnapshot="fixture-snapshot",
        datasetHash="a" * 64,
        splitManifestHash="b" * 64,
        rubricVersion="math-rubric-3x4x3-v1",
        calibrationVersion="fixture-cal-v1",
        inputRepresentation="solution",
        architectureVersion=CONDITIONED_DIFFICULTY_ARCHITECTURE,
        routingPolicyVersion="confidence-entropy-v1",
        calibration={
            head: CalibrationSpec(
                temperature=1.0,
                confidenceThreshold=0.99,
                entropyThreshold=0.25,
            )
            for head in HEAD_LABELS
        },
        maxLength=64,
        loraRank=4,
        files=files,
        gitCommit="fixture",
    )
    write_manifest(manifest, artifact)
    runtime = V2ClassifierRuntime(artifact)
    request = V2ClassificationRequest.model_validate(
        {
            "questionId": "q-tiny",
            "contentVersion": 1,
            "contentHash": "c" * 64,
            "grade": 2,
            "topic": "Bilangan",
            "subtopic": None,
            "questionType": "multiple_choice",
            "stimulus": None,
            "stem": "Hitung 1 + 1.",
            "options": [{"label": "A", "text": "1"}, {"label": "B", "text": "2"}],
            "verifiedMinimalSolution": "1 + 1 = 2",
            "detectedKko": ["menghitung"],
            "visualTranscript": None,
            "provenanceStatus": {
                "contentQualified": True,
                "answerKeyVerified": True,
                "solutionVerified": True,
                "visualEssential": False,
                "visualTranscriptVerified": False,
            },
        }
    )
    response = runtime.predict(request)
    assert response.reviewRequired is True
    for head in HEAD_LABELS:
        result = getattr(response, head)
        assert set(result.probabilities) == set(HEAD_LABELS[head])
        assert abs(sum(result.probabilities.values()) - 1.0) < 1e-6
