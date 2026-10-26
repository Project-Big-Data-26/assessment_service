from copy import deepcopy
import json
from pathlib import Path
import sqlite3
from types import SimpleNamespace

import pytest

from scripts import nightly_pipeline as nightly
from scripts import validate_exercise_batch as exercise
from app.assessment.store import AssessmentStore


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    monkeypatch.setattr(nightly, 'ROOT', tmp_path)
    monkeypatch.setattr(exercise, 'ROOT', tmp_path)
    p = exercise.paths('kelas7', 'batch01')
    p['exercise'].mkdir(parents=True)
    (p['exercise'] / 'soal_exercise_db.json').write_text('{"items": []}', encoding='utf-8')
    (p['exercise'] / 'soal_exercise_meta.json').write_text('{}', encoding='utf-8')
    return tmp_path, p


def config():
    return {'schemaVersion': 'nightly-exercise-v1', 'timezone': 'Asia/Jakarta', 'schedule': '01:00',
            'classes': ['kelas7'], 'bootstrapJobs': [], 'maxApiCalls': 10,
            'maxOutputTokens': 4096, 'irtModel': 'rasch', 'screeningRequests': []}


def ready_marker(p):
    identity = nightly.source_identity('kelas7', 'batch01')
    document = {**identity, 'schemaVersion': 'extraction-ready-v1', 'completedAt': '2026-10-20T01:00:00+07:00'}
    (p['exercise'] / 'extraction_ready.json').write_text(json.dumps(document), encoding='utf-8')
    return identity


def test_only_completed_handoffs_are_discovered_and_mutation_blocks_bootstrap(workspace):
    _, p = workspace
    cfg = config()
    assert nightly.discover_jobs(cfg) == ([], [])
    identity = ready_marker(p)
    assert nightly.discover_jobs(cfg) == ([identity], [])
    (p['exercise'] / 'soal_exercise_db.json').write_text('{"items": [1]}', encoding='utf-8')
    cfg['bootstrapJobs'] = [{'class': 'kelas7', 'batch': 'batch01'}]
    jobs, errors = nightly.discover_jobs(cfg)
    assert not jobs and len(errors) == 1


def test_marker_cannot_spoof_class_or_use_naive_timestamp(workspace):
    _, p = workspace
    ready_marker(p)
    marker = p['exercise'] / 'extraction_ready.json'
    data = json.loads(marker.read_text())
    for update in ({'class': 'kelas5'}, {'completedAt': '2026-10-20T01:00:00'}):
        marker.write_text(json.dumps({**data, **update}))
        assert nightly.discover_jobs(config())[1]


def test_completed_jobs_reverify_evidence_without_paid_calls(workspace, monkeypatch):
    root, _ = workspace
    job = nightly.source_identity('kelas7', 'batch01')
    monkeypatch.setattr(nightly, 'job_identity', lambda *args: 'policy-1')
    verified = []
    monkeypatch.setattr(nightly, 'verify_completed', lambda p: verified.append('ai'))
    monkeypatch.setattr(nightly, 'verify_operational_export', lambda p: verified.append('balance'))
    monkeypatch.setattr(nightly.subprocess, 'run', lambda *a, **k: pytest.fail('duplicate paid run'))
    state = {'kelas7/batch01': {'identity': 'policy-1', 'status': 'completed', 'operational': {'directory': str(root)}}}
    result, budget = nightly.validate_job(job, config(), state, 10, root)
    assert result['reused'] and budget == 10 and verified == ['ai', 'balance']
    monkeypatch.setattr(nightly, 'verify_completed', lambda p: (_ for _ in ()).throw(ValueError('tampered')))
    with pytest.raises(ValueError, match='tampered'):
        nightly.validate_job(job, config(), state, 10, root)


def test_budget_stop_and_partial_validation_never_publish_balance(workspace, monkeypatch):
    root, _ = workspace
    job = nightly.source_identity('kelas7', 'batch01')
    monkeypatch.setattr(nightly, 'job_identity', lambda *args: 'policy-1')
    monkeypatch.setattr(nightly, 'publish_balance', lambda *args: pytest.fail('partial must not publish'))
    monkeypatch.setattr(nightly.subprocess, 'run', lambda *a, **k: SimpleNamespace(returncode=3))
    result, _ = nightly.validate_job(job, config(), {}, 0, root)
    assert result['status'] == 'waiting_for_budget'
    result, _ = nightly.validate_job(job, config(), {}, 10, root)
    assert result['status'] == 'validation_incomplete'


def test_source_change_during_validation_is_rejected(workspace, monkeypatch):
    root, p = workspace
    job = nightly.source_identity('kelas7', 'batch01')
    monkeypatch.setattr(nightly, 'job_identity', lambda *args: 'policy-1')
    def process(*a, **k):
        (p['exercise'] / 'soal_exercise_meta.json').write_text('{"changed": true}')
        return SimpleNamespace(returncode=0)
    monkeypatch.setattr(nightly.subprocess, 'run', process)
    with pytest.raises(ValueError, match='source changed'):
        nightly.validate_job(job, config(), {}, 10, root)


def test_irt_runs_even_when_validation_fails_and_failure_remains_visible(workspace, monkeypatch):
    root, _ = workspace
    cfg = config()
    cfg['bootstrapJobs'] = [{'class': 'kelas7', 'batch': 'batch01'}]
    monkeypatch.setattr(nightly, 'validate_job', lambda *args: (_ for _ in ()).throw(ValueError('bad source')))
    calls = []
    def screen(*args):
        calls.append(True)
        return {'status': 'waiting_for_data', 'assessments': []}
    monkeypatch.setattr(nightly, 'screen_assessments', screen)
    report = nightly.run(cfg, root / 'runs/nightly')
    assert not report['success'] and calls == [True]
    assert report['jobs']['kelas7/batch01']['errorType'] == 'ValueError'
    assert (root / 'runs/nightly/latest.json').exists()


def test_os_lock_rejects_overlap_and_can_resume_after_release(tmp_path):
    path = tmp_path / 'pipeline.lock'
    with nightly.run_lock(path):
        with pytest.raises(RuntimeError, match='another nightly'):
            with nightly.run_lock(path):
                pytest.fail('overlap')
    with nightly.run_lock(path):
        pass


def analysis_fixture():
    return {'dataOrigin': 'server_scored', 'readiness': {'passed': True}, 'irt': {'status': 'estimated'},
            'assessmentId': 'a1', 'populationId': 'pop1', 'assessmentFamily': 'math7', 'grade': 7,
            'snapshotId': 'psy-1', 'snapshotHash': 'a' * 64, 'policyHash': 'b' * 64,
            'items': [{'questionId': 'q1', 'questionVersionId': 'q1:v1', 'contentHash': 'c' * 64,
                       'intendedDifficulty': 'Easy', 'irt': {'empiricalDifficulty': 'Hard'},
                       'recommendedRouting': 'observation_only', 'reviewFlags': ['intended_empirical_disagreement']}]}


def test_effective_label_updates_from_irt_and_preserves_original_labels():
    analysis = analysis_fixture()
    before = deepcopy(analysis)
    result = nightly.effective_labels(analysis, [{'questionVersionId': 'q1:v1', 'action': 'retain'}])
    row = result['items'][0]
    assert row['effectiveDifficulty'] == 'Hard' and row['intendedDifficulty'] == 'Easy'
    assert row['difficultySource'] == 'irt' and result['populationId'] == 'pop1'
    assert analysis == before


def test_collect_more_events_keeps_initial_label_available_for_more_responses():
    analysis = analysis_fixture()
    analysis['irt']['status'] = 'waiting_for_data'
    result = nightly.effective_labels(analysis, [{'questionVersionId': 'q1:v1', 'action': 'collect_more_events'}])
    assert result['items'][0]['deliveryAllowed']
    assert result['items'][0]['difficultySource'] == 'intended'


@pytest.mark.parametrize('scenario', ['warnings', 'missing_data', 'assumptions', 'held', 'external', 'weak', 'other_version'])
def test_unsupported_or_unsafe_estimates_do_not_replace_initial_difficulty(scenario):
    analysis = analysis_fixture()
    decisions = [{'questionVersionId': 'q1:v1', 'action': 'retain'}]
    if scenario == 'warnings': analysis['irt']['status'] = 'estimated_with_warnings'
    if scenario == 'missing_data': analysis['readiness']['passed'] = False
    if scenario == 'assumptions': analysis['irt']['status'] = 'waiting_for_assumption_review'
    if scenario == 'held': decisions[0]['action'] = 'needs_ai_review'
    if scenario == 'external': analysis['dataOrigin'] = 'synthetic'
    if scenario == 'weak': analysis['items'][0]['recommendedRouting'] = 'collect_more_events'
    if scenario == 'other_version': decisions[0]['questionVersionId'] = 'q1:v2'
    row = nightly.effective_labels(analysis, decisions)['items'][0]
    assert row['effectiveDifficulty'] == 'Easy' and row['empiricalDifficulty'] is None


def test_missing_database_is_not_created(workspace, monkeypatch):
    root, _ = workspace
    monkeypatch.setenv('ASSESSMENT_DB_PATH', str(root / 'missing.sqlite3'))
    result = nightly.screen_assessments(config(), root / 'output')
    assert result['status'] == 'waiting_for_data' and not (root / 'missing.sqlite3').exists()


def test_real_store_without_student_sessions_waits_without_synthetic_data(workspace, monkeypatch):
    root, _ = workspace
    path = root / 'assessments.sqlite3'
    monkeypatch.setenv('ASSESSMENT_DB_PATH', str(path))
    monkeypatch.delenv('ASSESSMENT_SUBJECT_SECRET', raising=False)
    store = AssessmentStore(path)
    with store.connection() as db:
        db.execute('INSERT INTO assessments VALUES (?,?,?)', ('a7', 'hash', json.dumps(
            {'assessmentId': 'a7', 'grade': 7, 'subjectTrack': 'regular'})))
    result = nightly.screen_assessments(config(), root / 'output')
    assert result['assessments'][0]['status'] == 'waiting_for_data'
    with sqlite3.connect(path) as db:
        assert db.execute('SELECT count(*) FROM responses').fetchone()[0] == 0
        assert db.execute('SELECT count(*) FROM snapshots').fetchone()[0] == 0
