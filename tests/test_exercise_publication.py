"""Publication remains complete while Windows readers hold the previous file."""
import mmap

import pytest

from scripts import validate_exercise_batch as exercise


def test_tree_publication_waits_for_windows_reader_without_truncation(tmp_path, monkeypatch):
    source = tmp_path / "snapshot"
    target = tmp_path / "published"
    source.mkdir()
    target.mkdir()
    old_file = target / "validation_results.json"
    old_file.write_bytes(b'["old"]')
    (source / old_file.name).write_bytes(b'["new", "complete"]')
    reader = old_file.open("rb")
    mapped = mmap.mmap(reader.fileno(), 0, access=mmap.ACCESS_READ)

    def release_reader(_):
        assert mapped[:] == b'["old"]'
        assert old_file.read_bytes() == b'["old"]'
        mapped.close()
        reader.close()

    monkeypatch.setattr(exercise.time, "sleep", release_reader)
    try:
        exercise.shutil.copytree(source, target, dirs_exist_ok=True, copy_function=exercise.copy_publication_file)
        assert old_file.read_bytes() == b'["new", "complete"]'
    finally:
        mapped.close()
        reader.close()
    assert not list(target.glob(".publish-*.tmp"))


def test_publication_retries_transient_windows_lock(tmp_path, monkeypatch):
    source, target = tmp_path / "source.json", tmp_path / "target.json"
    source.write_bytes(b"new")
    target.write_bytes(b"old")
    replace = exercise.os.replace
    attempts = []

    def locked_once(temporary, destination):
        attempts.append(temporary)
        assert target.read_bytes() == b"old"
        if len(attempts) == 1:
            error = OSError("mapped section still open")
            error.winerror = 1224
            raise error
        return replace(temporary, destination)

    monkeypatch.setattr(exercise.os, "replace", locked_once)
    monkeypatch.setattr(exercise.time, "sleep", lambda _: None)
    exercise.copy_publication_file(source, target)
    assert len(attempts) == 2
    assert target.read_bytes() == b"new"


def test_failed_publication_preserves_previous_bytes(tmp_path, monkeypatch):
    source, target = tmp_path / "source.json", tmp_path / "target.json"
    source.write_bytes(b"new")
    target.write_bytes(b"old")

    def blocked(*args):
        error = OSError("mapped section still open")
        error.winerror = 1224
        raise error

    monkeypatch.setattr(exercise.os, "replace", blocked)
    monkeypatch.setattr(exercise.time, "sleep", lambda _: None)
    with pytest.raises(OSError):
        exercise.copy_publication_file(source, target)
    assert target.read_bytes() == b"old"
    assert not list(tmp_path.glob(".publish-*.tmp"))
