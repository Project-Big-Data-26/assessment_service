import json
from copy import deepcopy
from pathlib import Path

import pytest

from app.services.exercise.replenishment_format import standard_question,distractor_reason
from app.services.exercise.workflow import (
    atomic_json,digest,approve_validation,require_validation,reference_manifest_paths,
)


def test_standard_question_keeps_common_contract_and_id_last():
    question={'id':'q','tipe_generate':'variasi','pertanyaan':'Tanya',
              'jawaban_benar':'4','gambar':[],'dipaksa_kuota':False,'catatan':None}
    original=deepcopy(question)
    normalized=standard_question(question)
    assert list(normalized)[-1]=='id'
    assert 'gambar' not in normalized and 'dipaksa_kuota' not in normalized
    assert normalized['pertanyaan']=='Tanya' and question==original


def test_external_audit_binding_detects_changed_snapshot_and_rejects_escape(tmp_path):
    base=tmp_path/'output/exercise/kelas5/batch01';audit=tmp_path/'runs/audit/blueprints.json'
    atomic_json(base/'soal_exercise_meta.json',{})
    atomic_json(audit,{'original':1})
    manifest={'files':{'soal_exercise_meta.json':digest(base/'soal_exercise_meta.json')},
              'auditFiles':{'runs/audit/blueprints.json':digest(audit)}}
    atomic_json(base/'reference_replenishment_manifest.json',manifest)
    checksum=digest(base/'reference_replenishment_manifest.json')
    atomic_json(base/'reference_replenishment_state.json',
                {'class':'kelas5','batch':'batch01','phase':'generation_complete','manifestSha256':checksum})
    approve_validation(base,checksum);require_validation(base)
    atomic_json(audit,{'original':2})
    with pytest.raises(ValueError,match='changed'):require_validation(base)
    with pytest.raises(ValueError,match='outside'):
        reference_manifest_paths(base,{'auditFiles':{'../other.json':'x'}})


def test_specific_reason_checks_number_of_available_negative_integers():
    question={'jenis_soal':'urutan_bilangan_bulat',
              'pertanyaan':'Terdapat 4 bilangan bulat negatif berbeda yang semuanya lebih besar daripada -16.',
              'jawaban_benar':'$-12$','distraktor':[{'teks':'$-13$'},{'teks':'$-11$'}]}
    proof={'check':'exact_value_and_four_distinct_options','value':'-12','options':['-12','-13','-11']}
    low=distractor_reason(question,0,proof);high=distractor_reason(question,1,proof)
    assert 'hanya ada 3' in low and 'belum cukup' in low
    assert 'bukan nilai terkecil' in high and '-15' in high and '-12' in high


def test_standardization_preserves_ids_keys_and_old_rows_with_native_progress_paths(tmp_path,monkeypatch):
    from scripts import generate_replenishment_codex as runner
    from scripts import standardize_replenishment_format as formatting
    for module in (runner,formatting):
        monkeypatch.setattr(module,'ROOT',tmp_path)
        monkeypatch.setattr(module,'RUN',tmp_path/'run')
    base=tmp_path/'output/exercise/kelas5/batch01';qid='a'*24
    original={'_id':qid,'kelas_id':'kelas5','subbab_id':'Faktor','soal_text':'Banyak faktor 12?',
              'options':[{'option_id':'A','text':'6'}],'jawaban':'A','status':None,'cognitive_level':None}
    metadata={qid:{'id':'original','bab_id':'SD5-B2','subbab_kode':'C','level_target':'medium'}}
    atomic_json(base/'soal_exercise_db.json',{'book':'kelas5','batch':1,'items':[original]})
    atomic_json(base/'soal_exercise_meta.json',metadata)
    atomic_json(base/'hasil_validasi/validation_results.json',[{**original,'status':'active','cognitive_level':'hard'}])
    progress={'target':1,'classes':{cl:{'target':int(cl=='kelas5'),'added':0,'status':'queued'} for cl in runner.CLASSES},'jobs':{}}
    job={'class_key':'kelas5','chapter_no':2,'code':'C','level_target':'hard','shortfall':1,
         'job_id':'kelas5-b02-C-hard','subchapter_name':'Faktor'}
    runner.run_class('kelas5',progress,[job])
    raw_path=base/'bab02/C_hard.json';before=json.loads(raw_path.read_text(encoding='utf-8'))['soal'][0]
    assert formatting.standardize_class('kelas5',progress)==1
    after=json.loads(raw_path.read_text(encoding='utf-8'))['soal'][0]
    assert after['id']==before['id'] and after['jawaban_benar']==before['jawaban_benar']
    assert list(after)[-1]=='id' and '_replenishment/' not in after['acuan']['snapshot']
    assert json.loads((base/'soal_exercise_db.json').read_text(encoding='utf-8'))['items'][0]==original
    assert json.loads((base/'soal_exercise_meta.json').read_text(encoding='utf-8'))[qid]==metadata[qid]
