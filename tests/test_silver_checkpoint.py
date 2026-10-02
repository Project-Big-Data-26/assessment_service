import json

import pytest

from scripts import generate_silver_labels_kelas1 as generator


def windows_lock_error():
    error = PermissionError("checkpoint is temporarily locked")
    error.winerror = 5
    return error


def test_checkpoint_survives_a_transient_windows_reader_lock(tmp_path, monkeypatch):
    path = tmp_path / "silver.json"
    path.write_text('{"previous": true}', encoding="utf-8")
    replacement = generator.os.replace
    attempts = []

    def locked_replace(source, destination):
        attempts.append(source)
        if len(attempts) <= 2:
            assert json.loads(path.read_text(encoding="utf-8")) == {"previous": True}
            raise windows_lock_error()
        replacement(source, destination)

    monkeypatch.setattr(generator.os, "replace", locked_replace)
    monkeypatch.setattr(generator.time, "sleep", lambda _: None)
    generator.atomic_write({"successfulRuns": 42}, path)
    assert len(attempts) == 3
    assert json.loads(path.read_text(encoding="utf-8")) == {"successfulRuns": 42}
    assert not path.with_suffix(".json.tmp").exists()


def test_persistent_lock_preserves_previous_and_new_checkpoint(tmp_path, monkeypatch):
    path = tmp_path / "silver.json"
    path.write_text('{"previous": true}', encoding="utf-8")
    attempts = []

    def locked_replace(*_):
        attempts.append(1)
        raise windows_lock_error()

    monkeypatch.setattr(generator.os, "replace", locked_replace)
    monkeypatch.setattr(generator.time, "sleep", lambda _: None)
    with pytest.raises(PermissionError):
        generator.atomic_write({"successfulRuns": 42}, path)
    assert len(attempts) == 6
    assert json.loads(path.read_text(encoding="utf-8")) == {"previous": True}
    assert json.loads(path.with_suffix(".json.tmp").read_text(encoding="utf-8")) == {"successfulRuns": 42}


def test_unrelated_permission_error_is_not_retried(tmp_path, monkeypatch):
    attempts = []

    def denied_replace(*_):
        attempts.append(1)
        raise PermissionError("permanent permission failure")

    monkeypatch.setattr(generator.os, "replace", denied_replace)
    with pytest.raises(PermissionError):
        generator.atomic_write({"successfulRuns": 42}, tmp_path / "silver.json")
    assert len(attempts) == 1
