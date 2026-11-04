"""Round-three asset immutability, legacy guards, and semantic export checks."""
from copy import deepcopy
from pathlib import Path

import pytest
from PIL import Image

from app.services.exercise import session_expansion as expansion
from scripts import generate_sd_bank_local as bank
from scripts import generate_targeted_replenishment as targeted
from scripts import refresh_ai_validation_reports as reports
from scripts import review_replenishment_local as review
from scripts import validate_exercise_batch as packager
from test_session_expansion import setup


@pytest.mark.parametrize('suffix,lf',[
    ('.svg',b'<svg width="10" height="10">\n<path d="M0 0L10 10"/>\n</svg>\n'),
    ('.json',b'{\n  "semanticSpec": {"count": 3},\n  "pngSha256": "old"\n}\n'),
])
def test_existing_git_crlf_assets_retain_their_exact_bytes(tmp_path,suffix,lf):
    source=tmp_path/('generated'+suffix);existing=tmp_path/'assets'/('existing'+suffix)
    source.write_bytes(lf);existing.parent.mkdir();original=lf.replace(b'\n',b'\r\n');existing.write_bytes(original)
    before=bank.digest(existing)
    expansion.copy_asset(source,existing)
    assert existing.read_bytes()==original and bank.digest(existing)==before
    assert source.read_bytes()==lf


@pytest.mark.parametrize('suffix,source_bytes,old_bytes',[
    ('.svg',b'<svg><circle r="3"/></svg>\n',b'<svg><circle r="4"/></svg>\r\n'),
    ('.json',b'{"semanticSpec":{"count":3}}\n',b'{"semanticSpec":{"count":4}}\r\n'),
])
def test_normalizing_line_endings_does_not_hide_geometry_or_fact_changes(tmp_path,suffix,source_bytes,old_bytes):
    source=tmp_path/('generated'+suffix);existing=tmp_path/('immutable'+suffix)
    source.write_bytes(source_bytes);existing.write_bytes(old_bytes)
    with pytest.raises(AssertionError,match='immutable|geometry'):
        expansion.copy_asset(source,existing)
    assert existing.read_bytes()==old_bytes


def test_real_pixel_conflicts_are_rejected_and_old_png_is_untouched(tmp_path):
    source=tmp_path/'generated.png';existing=tmp_path/'immutable.png'
    Image.new('RGB',(4,4),'blue').save(source);Image.new('RGB',(4,4),'red').save(existing)
    before=existing.read_bytes()
    with pytest.raises(AssertionError,match='PNG pixels'):
        expansion.copy_asset(source,existing)
    assert existing.read_bytes()==before


def test_first_publication_copies_an_asset_without_reencoding(tmp_path):
    source=tmp_path/'generated.svg';destination=tmp_path/'batch01/assets/new.svg'
    original=b'<svg>\r\n<rect width="10" height="20"/>\r\n</svg>\r\n';source.write_bytes(original)
    expansion.copy_asset(source,destination)
    assert destination.read_bytes()==original


def test_frozen_baseline_drift_is_blocked_before_any_publication(tmp_path,monkeypatch):
    base,plan=setup(tmp_path,monkeypatch)
    frozen=expansion.RUN/'baseline/kelas1/batch01'
    assert (frozen/'snapshot_complete.json').exists()
    expansion.verify_baseline('kelas1',plan,live=True)
    canonical_before=(base/'hasil_validasi/validation_results.json').read_bytes()
    source=frozen/'soal_exercise_db.json';changed=bank.load(source)
    changed['items'][0]['soal_text']='Changed only in the frozen baseline.'
    bank.atomic_json(source,changed)
    with pytest.raises(AssertionError,match='Baseline snapshot changed'):
        expansion.verify_baseline('kelas1',plan,live=True)
    assert (base/'hasil_validasi/validation_results.json').read_bytes()==canonical_before


def test_legacy_ai_packager_cannot_replace_a_v3_local_publication(tmp_path,monkeypatch):
    final=tmp_path/'batch01/hasil_validasi';bank.atomic_json(final/'manifest.json',{'schemaVersion':expansion.SCHEMA})
    protected=final/'validation_results.json';protected.write_bytes(b'preserve exact canonical bytes')
    # Missing checkpoint/source deliberately prove that protection is checked
    # before any legacy checkpoint can be read or repackaged.
    monkeypatch.setattr(packager,'paths',lambda name,batch:{'final':final})
    with pytest.raises(ValueError,match='must not be overwritten'):
        packager.package('kelas1','batch01')
    assert protected.read_bytes()==b'preserve exact canonical bytes'


@pytest.mark.parametrize('entrypoint',['reports','local_review','sd_bank','targeted_bank'])
def test_legacy_verifiers_dispatch_v3_to_the_round_verifier(tmp_path,monkeypatch,entrypoint):
    final=tmp_path/'batch01/hasil_validasi';bank.atomic_json(final/'manifest.json',{'schemaVersion':expansion.SCHEMA})
    seen=[]
    monkeypatch.setattr(expansion,'verify_publication',lambda bundle:seen.append(Path(bundle)))
    if entrypoint=='reports':reports.verify_bundle(tmp_path/'unused_source.json',final)
    elif entrypoint=='local_review':review.verify_local_publication(final)
    elif entrypoint=='sd_bank':bank.verify(final)
    else:targeted.verify(final)
    assert seen==[final]


def test_serialized_wrong_answer_is_rejected_even_when_all_hashes_match(tmp_path,monkeypatch):
    base,plan=setup(tmp_path,monkeypatch)
    def retain_render_fixture(questions,path):
        bank.atomic_json(path,[])
        return {'checked':0,'errors':[]}
    monkeypatch.setattr(bank,'check_latex',retain_render_fixture)
    expansion.generate_class('kelas1',plan)
    bundle=base/'hasil_validasi';proof=bank.load(bundle/'bukti_validasi/codex_session_review.json')
    item=proof['items'][0];qid=item['questionId'];rows=bank.load(bundle/'validation_results.json')
    sources=bank.load(base/'soal_exercise_db.json');meta=bank.load(bundle/'validation_results_meta.json')
    row=next(r for r in rows if r['_id']==qid);source=next(r for r in sources['items'] if r['_id']==qid)
    # Simulate a serializer selecting a different option letter while leaving
    # all mathematical model data and the displayed raw answer unchanged.
    wrong=next(o['option_id'] for o in row['options'] if o['option_id']!=row['jawaban'])
    row['jawaban']=source['jawaban']=wrong
    item['publishedHash']=expansion.h(row);item['sourceHash']=expansion.h(source)
    meta[qid]['local_review']=deepcopy(item);meta[qid]['validasi']['source_hash']=item['sourceHash']
    bank.atomic_json(bundle/'validation_results.json',rows);bank.atomic_json(base/'soal_exercise_db.json',sources)
    bank.atomic_json(bundle/'validation_results_meta.json',meta);bank.atomic_json(bundle/'bukti_validasi/codex_session_review.json',proof)
    manifest=bank.load(bundle/'manifest.json')
    manifest['inputs']={rel:bank.digest(base/rel) for rel in manifest['inputs']}
    manifest['outputs']={rel:bank.digest(bundle/rel) for rel in manifest['outputs']}
    bank.atomic_json(bundle/'manifest.json',manifest)
    assert all(bank.digest(base/rel)==sha for rel,sha in manifest['inputs'].items())
    assert all(bank.digest(bundle/rel)==sha for rel,sha in manifest['outputs'].items())
    with pytest.raises(AssertionError):expansion.verify_publication(bundle)


def test_resume_completes_an_asset_triplet_interrupted_after_png_copy(tmp_path,monkeypatch):
    base,plan=setup(tmp_path,monkeypatch)
    expansion.generate_class('kelas1',plan,pilot=True)
    stage=expansion.RUN/'staging/kelas1'
    candidates=[c for p in (stage/'jobs').glob('*.json') for c in bank.load(p)['items']]
    asset=next(c['source']['image_url'][0] for c in candidates if c['source']['image_url'] and not (base/c['source']['image_url'][0]).exists())
    png=base/asset;png.parent.mkdir(exist_ok=True);png.write_bytes((stage/asset).read_bytes())
    assert not png.with_suffix('.svg').exists() and not png.with_suffix('.json').exists()
    expansion.publish_class('kelas1',plan)
    expansion.verify_publication(base/'hasil_validasi')
    assert png.with_suffix('.svg').is_file() and png.with_suffix('.json').is_file()
