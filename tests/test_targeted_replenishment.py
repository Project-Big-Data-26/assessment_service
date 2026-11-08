"""Independent boundary cases and transaction safety for local authoring v2."""
from copy import deepcopy
from itertools import product
import json
import random
import re
from pathlib import Path
import pytest
import sympy as s

from app.services.exercise.targeted_math import solve_certificate,system,checked
from app.services.exercise.targeted_smp import generate as smp
from app.services.exercise.targeted_sd import generate as sd
from scripts import generate_targeted_replenishment as runner
from app.services.exercise.workflow import atomic_json


def test_certificate_rejects_ambiguity_and_impossible_constraints():
    x=s.Symbol('x',real=True)
    with pytest.raises(AssertionError,match='uniquely'):solve_certificate(system(['x'],[x*x-4],x))
    with pytest.raises(AssertionError,match='uniquely'):solve_certificate(system(['x'],[x*x+1],x,[x]))
    assert solve_certificate(system(['x'],[x*x-4],x,[x]))==2


def test_exact_probabilities_count_ordered_pairs_and_conditioning():
    cert={'type':'finite_probability','variables':['a','b'],'ranges':[[1,6],[1,6]],'event':'a+b>=8','condition':'Eq(Mod(a+b,2),0)'}
    # Even totals 8,10,12 give 5+3+1 outcomes, out of 18 even sums.
    assert solve_certificate(cert)==s.Rational(1,2)
    draft=checked('Berapa peluang?',s.Rational(1,2),'Hasil 1/2.','probability','medium',system(['x'],[s.Symbol('x',real=True)-s.Rational(1,2)],s.Symbol('x',real=True))).draft
    assert len(set(draft.proof['options']))==4
    assert all(0<=s.sympify(v)<=1 for v in draft.proof['options'])


@pytest.mark.parametrize('seed',range(8))
def test_pie_chart_student_counts_are_integral(seed):
    item=smp(7,6,'E','hard',random.Random(seed));q=item.draft.question
    total=int(re.search(r'memuat (\d+)',q)[1]);angle=int(re.search(r'pusat (\d+)',q)[1]);difference=int(re.search(r'adalah (\d+)',q)[1])
    remaining=s.Rational(total)*(360-angle)/360
    students=(remaining+difference)/2
    assert students.is_Integer and 0<students<remaining
    assert s.sympify(item.draft.proof['value'])==360*students/total


@pytest.mark.parametrize('seed',[1,5,9])
def test_primary_spatial_answer_matches_enumerated_physical_stacks(seed):
    item=sd(6,3,'B','hard',random.Random(seed));q=item.draft.question
    front=tuple(map(int,re.search(r'kolom \((\d+),(\d+)\)',q).groups()))
    side=tuple(map(int,re.search(r'baris \((\d+),(\d+)\)',q).groups()))
    fixed=int(re.search(r'b=(\d+)',q)[1]);maximum=max(*front,*side)
    feasible=[sum(v) for v in product(range(1,maximum+1),repeat=4) if (max(v[0],v[2]),max(v[1],v[3]))==front and (max(v[0],v[1]),max(v[2],v[3]))==side and v[1]==fixed]
    assert min(feasible)==int(item.draft.proof['value'])


def test_three_tunnels_count_union_instead_of_double_removal():
    item=sd(6,3,'A','hard',random.Random(33));q=item.draft.question
    n=int(re.search(r'Kubus (\d+)',q)[1]);k=int(re.search(r'penampang (\d+)',q)[1]);start=(n-k)//2;middle=set(range(start,start+k))
    removed={(i,j,z) for i,j,z in product(range(n),repeat=3) if (i in middle and j in middle) or (i in middle and z in middle) or (j in middle and z in middle)}
    assert n**3-len(removed)==int(item.draft.proof['value'])


def test_derivative_explanation_keeps_entire_latex_formula_delimited():
    from app.services.exercise.targeted_tl12 import generate
    from app.presentation.latex import MATH
    item=generate(2,'B','hard',random.Random(5))
    assert r'\left' in item.draft.explanation
    assert '\\' not in MATH.sub('',item.draft.explanation)


def prepare(tmp_path,monkeypatch):
    monkeypatch.setattr(runner,'ROOT',tmp_path);monkeypatch.setattr(runner,'RUN',tmp_path/'run');runner.RUN.mkdir()
    base=tmp_path/'output/exercise/kelas5/batch01';final=base/'hasil_validasi';qid='a'*24
    old={'_id':qid,'kelas_id':'kelas5','subbab_id':'Bilangan','soal_text':'Berapa 2+3?', 'image_url':[],
         'options':[{'option_id':k,'text':str(v),'alasan':'lama'} for k,v in zip('ABCD',[5,4,6,7])],
         'jawaban':'A','status':'active','cognitive_level':'easy','cognitive_score':600,'confidence_score':98}
    meta={qid:{'bab_id':'SD5-B1','subbab_kode':'A','id':'lama','validasi':{'validation_method':'blind_n3'}}}
    atomic_json(base/'soal_exercise_db.json',{'book':'kelas5','batch':1,'items':[old]});atomic_json(base/'soal_exercise_meta.json',meta)
    atomic_json(final/'validation_results.json',[old]);atomic_json(final/'validation_results_meta.json',meta);atomic_json(final/'manifest.json',{'schemaVersion':'old'})
    atomic_json(base/'reference_replenishment_manifest.json',{'files':{},'added':0});atomic_json(base/'reference_replenishment_state.json',{})
    raw=base/'bab01/A_hard.json';atomic_json(raw,{'book':'kelas5','bab_no':1,'subbab':'A','level':'hard','batch':1,'skill_versi':'v1','soal':[]})
    (runner.RUN/'backups/kelas5').mkdir(parents=True)
    monkeypatch.setattr(runner,'verify_local_publication',lambda path:None)
    class Render:
        stdout='{"errors": []}'
    monkeypatch.setattr(runner.subprocess,'run',lambda *a,**k:Render())
    def factory(*args):
        a,b=s.symbols('a b',real=True)
        return checked('Dua bilangan berjumlah 10 dan berselisih 4. Berapa hasil kalinya?',21,'Bilangan 7 dan 3; hasil kali 21.','inverse_numbers','hard',system(['a','b'],[a+b-10,a-b-4],a*b))
    monkeypatch.setattr(runner,'factory',factory)
    job={'class_key':'kelas5','chapter_no':1,'code':'A','subchapter_name':'Bilangan','level_target':'hard','active_now':0,'required':1,'shortfall':1}
    return base,old,meta,[job]


def test_publication_preserves_old_answers_and_is_idempotent(tmp_path,monkeypatch):
    base,old,oldmeta,jobs=prepare(tmp_path,monkeypatch)
    runner.run_class('kelas5',jobs,True);runner.verify(base/'hasil_validasi')
    rows=runner.load(base/'hasil_validasi/validation_results.json');meta=runner.load(base/'hasil_validasi/validation_results_meta.json')
    assert rows[0]==old and meta[old['_id']]==oldmeta[old['_id']]
    assert len(rows)==2 and rows[1]['confidence_score']==0
    assert meta[rows[1]['_id']]['validasi']['training_evidence_qualified'] is False
    before=(base/'soal_exercise_db.json').read_bytes();runner.run_class('kelas5',jobs,True)
    assert (base/'soal_exercise_db.json').read_bytes()==before
    # Re-hashing a modified paid answer cannot bypass preservation checks.
    rows[0]['jawaban']='B';atomic_json(base/'hasil_validasi/validation_results.json',rows)
    manifest=runner.load(base/'hasil_validasi/manifest.json');manifest['outputs']['validation_results.json']['sha256']=runner.digest(base/'hasil_validasi/validation_results.json');atomic_json(base/'hasil_validasi/manifest.json',manifest)
    with pytest.raises(AssertionError,match='Existing published'):runner.verify(base/'hasil_validasi')


def test_failed_publication_restores_all_mutated_question_files(tmp_path,monkeypatch):
    base,old,meta,jobs=prepare(tmp_path,monkeypatch)
    before={p:p.read_bytes() for p in base.rglob('*.json')};verify=runner.verify
    def fail(path,check_live=True):
        if path==base/'hasil_validasi':raise RuntimeError('simulated final verification failure')
        verify(path,check_live)
    monkeypatch.setattr(runner,'verify',fail)
    with pytest.raises(RuntimeError,match='simulated'):runner.run_class('kelas5',jobs,True)
    assert all(p.read_bytes()==data for p,data in before.items())
    assert runner.load(base/'hasil_validasi/validation_results.json')==[old]
