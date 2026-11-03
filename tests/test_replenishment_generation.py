from pathlib import Path
import json
import random
import pytest

from scripts import generate_replenishment_codex as runner
from app.services.exercise.workflow import approve_validation,digest,require_validation,validation_allowed


def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value),encoding='utf-8')


def test_batch01_append_preserves_old_rows_and_evidence_and_defers_validation(tmp_path,monkeypatch):
    monkeypatch.setattr(runner,'ROOT',tmp_path);monkeypatch.setattr(runner,'RUN',tmp_path/'run')
    base=tmp_path/'output/exercise/kelas5/batch01';qid='a'*24
    original={'_id':qid,'kelas_id':'kelas5','subbab_id':'Faktor','soal_text':'Faktor positif dari 12 ada berapa?',
              'options':[{'option_id':'A','text':'6'}],'jawaban':'A','status':None,'cognitive_level':None}
    meta={qid:{'id':'original','bab_id':'SD5-B2','subbab_kode':'C','level_target':'medium'}}
    write(base/'soal_exercise_db.json',{'book':'kelas5','batch':1,'items':[original]})
    write(base/'soal_exercise_meta.json',meta)
    final={**original,'status':'active','cognitive_level':'hard'}
    write(base/'hasil_validasi/validation_results.json',[final])
    original_final=(base/'hasil_validasi/validation_results.json').read_bytes()
    original_master=(base/'soal_exercise_db.json').read_bytes()
    progress={'target':1,'classes':{cl:{'target':1 if cl=='kelas5' else 0,'added':0,'status':'queued'} for cl in runner.CLASSES},'jobs':{}}
    job={'class_key':'kelas5','chapter_no':2,'code':'C','level_target':'hard','shortfall':1,
         'job_id':'kelas5-b02-C-hard','subchapter_name':'Faktor'}
    runner.run_class('kelas5',progress,[job])
    master=json.loads((base/'soal_exercise_db.json').read_text())
    assert master['items'][0]==original and len(master['items'])==2
    assert master['items'][1]['status']=='inactive' and master['items'][1]['cognitive_level'] is None
    assert (base/'hasil_validasi/validation_results.json').read_bytes()==original_final
    assert (tmp_path/'run/backups/kelas5/soal_exercise_db.json').read_bytes()==original_master
    assert json.loads((base/'soal_exercise_meta.json').read_text())[qid]==meta[qid]
    assert not validation_allowed(base)
    assert progress['classes']['kelas5']['added']==1
    from app.ingestion.question_sync import load_sources
    from scripts.plan_exercise_replenishment import pending_generation
    pending,files=pending_generation(tmp_path/'output',load_sources(tmp_path/'output'))
    assert len(pending)==1 and pending[0]['generation_mode']=='batch01_additions'
    assert base/'reference_replenishment_manifest.json' in files
    # Resume cannot append another copy of a completed job.
    runner.run_class('kelas5',progress,[job]);assert len(json.loads((base/'soal_exercise_db.json').read_text())['items'])==2
    checksum=digest(base/'reference_replenishment_manifest.json')
    approve_validation(base,checksum);require_validation(base)
    path=base/'bab02/C_hard.json';path.write_text(path.read_text()+'\n')
    with pytest.raises(ValueError,match='changed'):require_validation(base)


@pytest.mark.parametrize('book,bab,code,level',[
    ('kelas5',2,'C','hard'),('kelas6',1,'B','hard'),('kelas7',6,'F','hard'),
    ('kelas8',4,'A','hard'),('kelas9',3,'C','easy'),('kelas10',4,'B','hard'),
    ('kelas11',2,'C','hard'),('kelas11_tl',1,'E','medium'),('kelas12',2,'A','hard'),
    ('kelas12_tl',3,'C','hard'),('kelas12_tl',4,'F','medium'),('kelas12_tl',4,'G','hard')])
def test_math_families_return_four_choices_and_well_delimited_formulas(book,bab,code,level):
    draft=runner.factory(book,bab,code,level,random.Random(726))
    assert len(set([draft.answer,*draft.distractors]))==4
    assert draft.proof['independent_ai_validation']=='pending'
    for field in [draft.question,draft.answer,*draft.distractors,draft.explanation]:
        assert field.count('$')%2==0 and '$$' not in field


def test_normal_tail_uses_complement_and_triangle_radius_is_not_assumed():
    draft=runner.factory('kelas12_tl',4,'G','hard',random.Random(23))
    assert '1-' in draft.explanation
    assert draft.proof['value'] in {'57/2500','1587/10000','8413/10000','2443/2500'}


def test_sd_data_collection_counts_frequencies_without_introducing_mean():
    import re
    from collections import Counter
    draft=runner.factory('kelas5',8,'A','hard',random.Random(263))
    match=re.search(r'adalah (.+?)\. Penjual.*sedikit (\d+) siswa',draft.question)
    data=list(map(int,match[1].split(', ')));minimum=int(match[2])
    expected=sum(count for count in Counter(data).values() if count<minimum)
    assert int(draft.proof['value'])==expected and 'rata-rata' not in draft.question


def test_decimal_topic_uses_decimal_notation_and_place_value_uses_familiar_name():
    draft=runner.factory('kelas6',1,'C','easy',random.Random(123))
    assert ',' in draft.question and '\\frac' not in draft.question
    assert ',' in draft.answer or draft.answer.isdigit()
    draft=runner.factory('kelas5',1,'A','medium',random.Random(123))
    assert any(word in draft.question for word in ['puluhan','ratusan','ribuan'])
    assert '10^' not in draft.question
