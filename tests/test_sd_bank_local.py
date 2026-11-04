"""Offline publication safety and semantic contracts for the SD bank."""
from copy import deepcopy
import json
from pathlib import Path
import random
import pytest
import sympy as s

from scripts import generate_sd_bank_local as bank
from app.services.exercise.workflow import atomic_json,require_validation
from app.services.exercise.replenishment_math import m


def test_equivalent_fraction_and_decimal_options_are_not_distinct():
    assert bank.answer_identity('$\\frac{2}{4}$')==bank.answer_identity('$\\frac{1}{2}$')
    assert bank.answer_identity('$0{,}5$')==bank.answer_identity('$\\frac{1}{2}$')
    assert bank.answer_identity('$0,5$')==bank.answer_identity('$\\frac{1}{2}$')
    assert bank.answer_identity('$4$')!=bank.answer_identity('$5$')


def test_counterfactual_rejects_picture_irrelevant_to_answer():
    model={'kind':'constant','scene':{'kind':'cards','cards':[{'label':'A','value':4}]},'certificate':{'type':'sd_low_expression','inputs':{'a':4},'expression':'a-a+3','visual_bindings':[{'input':'a','path':['cards',0,'value']}]}}
    with pytest.raises(AssertionError,match='no tested pivotal'):bank.visual_check(model)
    model['certificate']['expression']='a+3'
    result=bank.visual_check(model)
    assert result['checks'][0]['counterfactualResult']!=result['checks'][0]['originalResult']


def test_counterfactual_rejects_scene_model_disagreement():
    model={'kind':'mismatch','scene':{'kind':'cards','cards':[{'label':'A','value':4}]},'certificate':{'type':'sd_low_expression','inputs':{'a':5},'expression':'a+2','visual_bindings':[{'input':'a','path':['cards',0,'value']}]}}
    with pytest.raises(AssertionError,match='Scene/model disagreement'):bank.visual_check(model)


def fixture(tmp_path,monkeypatch):
    monkeypatch.setattr(bank,'ROOT',tmp_path);monkeypatch.setattr(bank,'RUN',tmp_path/'run');bank.RUN.mkdir()
    (tmp_path/'scripts').mkdir();(tmp_path/'scripts/generate_sd_bank_local.py').write_text('# retained test code\n')
    ref={'id':'a'*24,'class':'kelas1','chapter':1,'code':'A','topic':'Bilangan','text':'Ada tiga benda.','answer':'3'}
    atomic_json(bank.RUN/'pretest_blueprints.json',{'references':[ref]})
    job={'class_key':'kelas1','chapter_no':1,'code':'A','name':'Bilangan'}
    plan={'schemaVersion':bank.SCHEMA,'catalog':[job],'referenceHash':bank.digest(bank.RUN/'pretest_blueprints.json'),'targetQuestions':30,'questionsPerLevel':10,'visualPerLevel':7,'textPerLevel':3,'apiCalls':0}
    plan['planHash']=bank.fingerprint(plan);bank.initialize(1,plan)
    def factory(grade,bab,code,level,r,visual,index):
        n=r.randint(10,900);value=n+2
        return {'question':f'Kartu untuk kegiatan {level} milik peserta {index}. Berapa nilainya setelah ditambah dua?' if visual else f'Pada kegiatan {level}, sebanyak {n} benda ditambah dua. Berapa totalnya?',
          'answer':m(value),'wrong':[m(value+1),m(value-1),m(value+2)],'explanation':f'Nilai awal {n}; tambah 2 menjadi {value}.','kind':'sd_low_test_model','steps':{'easy':1,'medium':2,'hard':3}[level],'rationale':'Mengikuti model dan konteks soal yang diperiksa.',
          'scene':{'kind':'cards','cards':[{'label':'A','value':n}]} if visual else None,
          'certificate':{'type':'sd_low_expression','inputs':{'n':n},'expression':'n+2','visual_bindings':[{'input':'n','path':['cards',0,'value']}] if visual else []}}
    monkeypatch.setattr(bank,'factory',factory);monkeypatch.setattr(bank,'check_latex',lambda qs,path:{'checked':0,'errors':[]})
    return job,plan


def test_resume_does_not_duplicate_and_local_mode_blocks_api(tmp_path,monkeypatch):
    job,plan=fixture(tmp_path,monkeypatch)
    bank.generate_file(job,'easy',plan);base=bank.base_for(1);raw=base/'bab01/A_easy.json';before=raw.read_bytes()
    assert bank.generate_file(job,'easy',plan) is False and raw.read_bytes()==before
    data=bank.load(raw);assert len(data['soal'])==10 and sum(bool(q.get('gambar')) for q in data['soal'])==7
    with pytest.raises(ValueError,match='external API'):require_validation(base)
    raw.write_text(raw.read_text(encoding='utf-8')+'\n',encoding='utf-8')
    with pytest.raises(AssertionError):bank.generate_file(job,'easy',plan)


def test_publication_labels_only_locally_and_preserves_standard_export(tmp_path,monkeypatch):
    job,plan=fixture(tmp_path,monkeypatch)
    for level in bank.LEVELS:bank.generate_file(job,level,plan)
    bank.publish(1,plan);base=bank.base_for(1);bank.verify(base/'hasil_validasi')
    rows=bank.load(base/'hasil_validasi/validation_results.json');meta=bank.load(base/'hasil_validasi/validation_results_meta.json')
    assert len(rows)==30 and sum(bool(q['image_url']) for q in rows)==21
    assert all(q['confidence_score']==0 and q['status']=='active' for q in rows)
    assert all(m['validasi']['training_evidence_qualified'] is False and m['validasi']['api_runs']==0 for m in meta.values())
    before=(base/'soal_exercise_db.json').read_bytes();bank.publish(1,plan)
    assert (base/'soal_exercise_db.json').read_bytes()==before


def test_failed_publication_rolls_back_master_metadata_and_canonical(tmp_path,monkeypatch):
    job,plan=fixture(tmp_path,monkeypatch)
    for level in bank.LEVELS:bank.generate_file(job,level,plan)
    base=bank.base_for(1);verify=bank.verify
    def fail(path):
        if path==base/'hasil_validasi':raise RuntimeError('simulated final check failure')
        verify(path)
    monkeypatch.setattr(bank,'verify',fail)
    with pytest.raises(RuntimeError,match='simulated'):bank.publish(1,plan)
    assert not (base/'soal_exercise_db.json').exists()
    assert not (base/'soal_exercise_meta.json').exists()
    assert not (base/'hasil_validasi').exists()
