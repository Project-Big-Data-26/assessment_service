"""Capacity, publication preservation and recovery for offline session rounds."""
from copy import deepcopy
import json
import random
from types import SimpleNamespace

import pytest
import sympy as s

from app.ingestion.question_sync import coverage,SourceQuestion
from app.services.exercise import session_expansion as expansion
from scripts import generate_sd_bank_local as bank
from test_sd_difficulty_review import fixture as primary_fixture


def test_session_coverage_uses_actual_active_labels():
    questions=[SourceQuestion({'_id':str(i),'status':status,'cognitive_level':level},'kelas1',1,'A',kind,'test')
               for i,(status,level,kind) in enumerate([('active','easy','exercise')]*10+[('inactive','hard','exercise')]*40+[('active','medium','pretest')]*40)]
    catalog=[{'class_key':'kelas1','chapter_no':1,'code':'A','name':'Bilangan'}]
    assert coverage(questions,catalog)['rows'][0]['level_shortfalls']=={'easy':0,'medium':10,'hard':10}
    result=coverage(questions,catalog,sessions=3)
    assert result['rows'][0]['level_shortfalls']=={'easy':20,'medium':30,'hard':30}
    for bad in (0,-1,True,1.5):
        with pytest.raises(ValueError):coverage(questions,catalog,sessions=bad)


def provider():
    def generate(name,bab,code,level,r,visual,index):
        a=r.randint(1,19);b=r.randint(1,19)
        expression={'easy':'a+b','medium':'2*a+b','hard':'3*a+b+2'}[level]
        value=s.sympify(expression).subs({'a':a,'b':b})
        return {'question':f'Perhatikan kelompok pada gambar. Hitung bentuk {expression}.' if visual else f'Gunakan a={a} dan b={b} untuk bentuk {expression}.',
                'answer':f'${value}$','wrong':[f'${value+i}$' for i in (1,2,3)],'explanation':f'Gabungkan kuantitas sesuai hubungan; hasilnya ${value}$.',
                'kind':'test_'+level,'steps':{'easy':1,'medium':2,'hard':4}[level],'rationale':'Hubungan kuantitas dinilai berdasarkan bentuk yang selesai.',
                'scene':{'kind':'groups','groups':[{'label':'A','count':a},{'label':'B','count':b}]} if visual else None,
                'certificate':{'expression':expression,'inputs':{'a':a,'b':b}}}
    return SimpleNamespace(generate=generate,solve=lambda cert:s.sympify(cert['expression']).subs(cert['inputs']),
        assess=lambda model,g:{'assessedLevel':model['kind'].split('_')[1],'steps':model['steps'],'reason':model['rationale'],'apiCalls':0},
        check_visual=lambda model:{'status':'local_semantic_counterfactual_pass'})


def setup(tmp_path,monkeypatch):
    base,old_plan=primary_fixture(tmp_path,monkeypatch)
    def checked_latex(questions,path):
        bank.atomic_json(path,[])
        return {'checked':0,'errors':[]}
    monkeypatch.setattr(bank,'check_latex',checked_latex)
    monkeypatch.setattr(expansion,'ROOT',tmp_path);monkeypatch.setattr(expansion,'RUN',tmp_path/'session_run')
    monkeypatch.setattr(expansion,'report_catalog',lambda path:[{'class_key':'kelas1','chapter_no':1,'code':'A','name':'Bilangan'}])
    monkeypatch.setattr(expansion,'provider',lambda name:provider())
    expansion._review_cached.cache_clear()
    return base,expansion.prepare()


def test_session_round_preserves_old_rows_and_resume_is_idempotent(tmp_path,monkeypatch):
    base,plan=setup(tmp_path,monkeypatch)
    old=bank.load(base/'hasil_validasi/validation_results.json');oldmeta=bank.load(base/'hasil_validasi/validation_results_meta.json')
    expansion.generate_class('kelas1',plan,pilot=True)
    assert bank.load(base/'hasil_validasi/validation_results.json')==old
    result=expansion.generate_class('kelas1',plan)
    assert result['active']==90 and result['added']==60
    expansion.verify_publication(base/'hasil_validasi')
    now={q['_id']:q for q in bank.load(base/'hasil_validasi/validation_results.json')}
    newmeta=bank.load(base/'hasil_validasi/validation_results_meta.json')
    assert all(now[q['_id']]==q and newmeta[q['_id']]==oldmeta[q['_id']] for q in old)
    frozen={p:p.read_bytes() for p in base.rglob('*') if p.is_file() and p.name!='.workflow.lock'}
    expansion.generate_class('kelas1',plan)
    assert all(p.read_bytes()==data for p,data in frozen.items())


def test_failed_publication_restores_raw_master_and_canonical(tmp_path,monkeypatch):
    base,plan=setup(tmp_path,monkeypatch)
    expansion.generate_class('kelas1',plan,pilot=True)
    old={p:p.read_bytes() for p in base.rglob('*.json')};verify=expansion.verify_publication
    def fail(bundle):
        if bundle==base/'hasil_validasi':raise RuntimeError('injected after canonical replacement')
        return verify(bundle)
    monkeypatch.setattr(expansion,'verify_publication',fail)
    with pytest.raises(RuntimeError,match='injected'):expansion.publish_class('kelas1',plan)
    assert all(p.read_bytes()==data for p,data in old.items())
    assert expansion.load(expansion.RUN/'staging/kelas1/publication_journal.json')['phase']=='rolled_back'


def test_interrupted_prepare_recovers_before_resuming(tmp_path,monkeypatch):
    base,plan=setup(tmp_path,monkeypatch)
    path=base/'soal_exercise_meta.json';before=path.read_bytes()
    expansion.atomic_json(path,{'interrupted':True})
    expansion.atomic_json(expansion.RUN/'staging/kelas1/publication_journal.json',{'phase':'prepared','mutated':['soal_exercise_meta.json'],'roundId':plan['roundId']})
    expansion.recover('kelas1')
    assert path.read_bytes()==before
