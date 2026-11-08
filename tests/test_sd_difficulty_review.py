"""Content judgements and independent math checks for the second SD review."""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import hashlib
import random
import pytest
import sympy as s

from app.services.exercise.sd_difficulty_review import assess
from app.services.exercise.sd_review_additions import generate,solve_certificate
from app.services.exercise.sd_bank_low import generate as low
from app.services.exercise.sd_bank_high import generate as high
from scripts import generate_sd_bank_local as bank
from scripts import review_sd_difficulty_local as review


def test_a_target_hard_cannot_override_a_cancelling_instance():
    cert={'type':'sd_low_expression','inputs':{'a':8,'p':2,'q':2,'t':1},'expression':'a-p+q-t'}
    d=assess('Memberi 2, menerima 2, memberi 1. Berapa sisa?',cert,'sd_low_pengurangan_tiga_perubahan',1)
    assert d['assessedLevel']=='easy' and 'numerical_shortcut' in d['flags']
    cert['inputs']['q']=3;cert['inputs']['t']=2
    assert assess('Soal yang sama',cert,'sd_low_pengurangan_tiga_perubahan',1)['assessedLevel']=='hard'


def test_original_audit_dispatches_to_reviewed_inventory(tmp_path,monkeypatch):
    monkeypatch.setattr(bank,'ROOT',tmp_path)
    for grade in range(1,5):
        bank.atomic_json(bank.base_for(grade)/'hasil_validasi/manifest.json',{'schemaVersion':review.SCHEMA})
    expected={'active':2911,'shortfall':0}
    monkeypatch.setattr(review,'audit_all',lambda:expected)
    assert bank.audit({})==expected


def test_original_refresh_cannot_discard_reviewed_additions(tmp_path,monkeypatch):
    monkeypatch.setattr(bank,'ROOT',tmp_path);base=bank.base_for(1)
    bank.atomic_json(base/'reference_replenishment_state.json',{})
    bank.atomic_json(base/'hasil_validasi/manifest.json',{'schemaVersion':review.SCHEMA})
    bank.atomic_json(base/'bab01/A_easy.json',{'soal':[{'id':'preserve'}]})
    with pytest.raises(ValueError,match='newer difficulty review'):
        bank.refresh_owned(1,{})
    assert bank.load(base/'bab01/A_easy.json')['soal']==[{'id':'preserve'}]


def test_repeated_pattern_is_not_hard_just_because_more_symbols_are_counted():
    model=low(2,4,'B','hard',random.Random(19),True,1)
    assert assess(model['question'],model['certificate'],model['kind'],2,model['scene'])['assessedLevel']=='medium'


def test_cancelled_route_is_direct_and_combined_line_count_is_withheld():
    model=low(2,4,'A','hard',random.Random(2),True,1)
    assert assess(model['question'],model['certificate'],model['kind'],2,model['scene'])['assessedLevel']=='easy'
    lines=high(3,4,'C','hard',random.Random(2),True,1)
    d=assess(lines['question'],lines['certificate'],lines['kind'],3,lines['scene'])
    assert d['assessedLevel'] is None and d['flags']==['image_independent_constant_answer']


def test_new_fraction_minimum_honours_parity_and_majority_together():
    for seed in range(8):
        model=generate(4,2,'A','hard',random.Random(seed),True,11);cert=model['certificate'];n=cert['inputs']['denominator'];initial=cert['inputs']['shaded']
        possible=[k for k in range(initial,n+1) if k%2==0 and k>n-k]
        assert solve_certificate(cert)==s.Rational(min(possible)-initial,n)
        bank.visual_check(model)


def test_minimum_pattern_piece_requires_both_count_and_last_shape():
    model=generate(2,4,'B','hard',random.Random(7),True,11);cert=model['certificate'];p=cert['inputs'];n=int(solve_certificate(cert))
    def valid(length):
        seq=[p['unit'][(p['skip']+i)%len(p['unit'])] for i in range(length)]
        return seq.count(p['symbol'])>=p['goal'] and seq[-1]==p['last']
    assert valid(n) and not any(valid(j) for j in range(1,n))
    bank.visual_check(model)


def test_new_line_task_uses_distinct_weights_instead_of_constant_pair_total():
    answers=set()
    for seed in range(16):
        model=generate(3,4,'C','hard',random.Random(seed),True,11);cert=model['certificate'];segments=cert['inputs']['segments'];removed=cert['inputs']['removed']
        vec=[(t[1][0]-t[0][0],t[1][1]-t[0][1]) for i,t in enumerate(segments) if i!=removed]
        total=0
        for i,u in enumerate(vec):
            for v in vec[i+1:]:
                if u[0]*v[1]==u[1]*v[0]:total+=2
                if u[0]*v[0]+u[1]*v[1]==0:total+=1
        assert solve_certificate(cert)==total
        answers.add(total);bank.visual_check(model)
    assert len(answers)>1


def fixture(tmp_path,monkeypatch):
    monkeypatch.setattr(bank,'ROOT',tmp_path);monkeypatch.setattr(bank,'RUN',tmp_path/'generation')
    monkeypatch.setattr(review,'ROOT',tmp_path);monkeypatch.setattr(review,'RUN',tmp_path/'review')
    bank.RUN.mkdir();review.RUN.mkdir()
    for file in ['scripts/generate_sd_bank_local.py','app/services/exercise/sd_difficulty_review.py','app/services/exercise/sd_review_additions.py']:
        path=tmp_path/file;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('# retained code\n')
    ref={'id':'a'*24,'class':'kelas1','chapter':1,'code':'A','topic':'Bilangan','text':'Tiga benda pada gambar.','answer':'3'}
    bank.atomic_json(bank.RUN/'pretest_blueprints.json',{'references':[ref]})
    job={'class_key':'kelas1','chapter_no':1,'code':'A','name':'Bilangan'}
    plan={'schemaVersion':bank.SCHEMA,'catalog':[job],'referenceHash':bank.digest(bank.RUN/'pretest_blueprints.json'),'questionsPerLevel':10,'visualPerLevel':7,'textPerLevel':3}
    plan['planHash']=bank.fingerprint(plan);bank.initialize(1,plan)
    monkeypatch.setattr(bank,'check_latex',lambda *args:{'checked':0,'errors':[]})
    for level in bank.LEVELS:bank.generate_file(job,level,plan)
    bank.publish(1,plan)
    return bank.base_for(1),plan


def test_reassessment_relabels_preserves_content_and_adds_real_capacity(tmp_path,monkeypatch):
    base,plan=fixture(tmp_path,monkeypatch);old=bank.load(base/'hasil_validasi/validation_results.json');old_by={q['_id']:q for q in old}
    result=review.run_class(1);review.verify(base/'hasil_validasi')
    assert result['added']>0
    rows=bank.load(base/'hasil_validasi/validation_results.json');meta=bank.load(base/'hasil_validasi/validation_results_meta.json')
    assert {q['_id'] for q in old} <= {q['_id'] for q in rows}
    for row in rows:
        if row['_id'] in old_by:
            assert {k:v for k,v in row.items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}=={k:v for k,v in old_by[row['_id']].items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}
    assert all(v>=10 for v in Counter(q['cognitive_level'] for q in rows if q['status']=='active').values())
    assert all(q['confidence_score']==0 for q in rows)
    before=(base/'soal_exercise_db.json').read_bytes();review.run_class(1)
    assert (base/'soal_exercise_db.json').read_bytes()==before


def test_review_publication_failure_restores_old_rows_and_raw_files(tmp_path,monkeypatch):
    base,plan=fixture(tmp_path,monkeypatch);before={p:p.read_bytes() for p in base.rglob('*.json')};verify=review.verify
    def fail(path):
        if path==base/'hasil_validasi':raise RuntimeError('simulated verification failure')
        verify(path)
    monkeypatch.setattr(review,'verify',fail)
    with pytest.raises(RuntimeError,match='simulated'):review.run_class(1)
    assert all(p.read_bytes()==data for p,data in before.items())
