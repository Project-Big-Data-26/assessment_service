"""Independent arithmetic and visual binding checks for the three-session bank."""
from copy import deepcopy
from pathlib import Path
import random
import pytest
import sympy as s

from app.ingestion.question_sync import report_catalog
from app.services.exercise import session_high as high
from app.services.exercise.session_high_trace import capture,solve as replay


def test_recipe_keeps_inputs_and_operations_rather_than_a_claimed_constant():
    draft=capture('kelas8',6,'A','easy',random.Random(41));cert=draft.proof['session_certificate']
    assert len(cert['inputs'])==2 and 'Rational' in cert['expression'] and 'sum' in cert['expression']
    a=cert['inputs']['input_a_0'];step=cert['inputs']['input_step_1']
    assert replay(cert)==s.Rational(5*a+7*step,5)
    changed=deepcopy(cert);changed['inputs']['input_a_0']+=3
    assert replay(changed)==replay(cert)+3


def test_basic_family_reassessment_is_independent_of_request_labels():
    model=high.generate('kelas7',3,'A','easy',random.Random(2),True,1)
    model['requested_level']='hard';model['steps']=99;model['rationale']='hard';model['assessment']={'assessedLevel':'hard'}
    assert high.assess(model,7)['assessedLevel']=='easy'
    assert high.check_visual(model)['pivotalFacts']
    tampered=deepcopy(model);tampered['scene']['rows'][0][1]='999'
    with pytest.raises(AssertionError):high.check_visual(tampered)


def test_linked_arithmetic_is_recomputed_from_two_distinct_sets_of_facts():
    model=high.generate('kelas9',4,'B','medium',random.Random(12),True,1);cert=model['certificate']
    left,right=cert['left']['inputs'],cert['right']['inputs']
    expected=s.Rational(left['F'],left['N'])-s.Rational(right['F'],right['N'])
    assert high.solve(cert)==expected and high.assess(model,9)['assessedLevel']=='medium'
    assert high.check_visual(model)['pivotalFacts']


def test_unregistered_constraint_family_is_not_accepted_as_hard():
    model={'kind':'v2_unreviewed','certificate':{'type':'symbolic_constraints','variables':['x'],'equations':['x-3'],'query':'x','positive':[]}}
    with pytest.raises(ValueError,match='Unreviewed'):high.assess(model,8)


def test_fpb_kpk_reconstruction_uses_actual_factor_pairs():
    model=high.generate('kelas5',2,'E','hard',random.Random(3),False,1);p=model['certificate']['inputs'];pairs=[]
    for a in range(1,p['cap']+1):
        if p['gcd']*p['lcm']%a:continue
        b=p['gcd']*p['lcm']//a
        if a<=b and s.gcd(a,b)==p['gcd'] and s.ilcm(a,b)==p['lcm']:pairs.append(a+b)
    assert high.solve(model['certificate'])==max(pairs)


def test_sample_never_exceeds_population_and_has_integer_stratum_allocation():
    for seed in range(12):
        model=high.generate('kelas9',4,'D','easy',random.Random(seed),True,1);p=model['certificate']['inputs']
        assert 0<p['S']<=p['N'] and 0<p['A']<=p['N']
        assert high.solve(model['certificate']).is_Integer


def test_all_sd5_to_smp_locations_have_direct_linked_and_constraint_candidates():
    root=Path(__file__).resolve().parents[1]
    rows=report_catalog(root/'API_DOCUMENTATION/Pesan_eror.md');checked=0
    for row in rows:
        grade=int(row['class_key'].split('_')[0][5:])
        if not 5<=grade<=9:continue
        for level in ('easy','medium','hard'):
            item=None
            for seed in (41,42,43):
                item=high.generate(row['class_key'],row['chapter_no'],row['code'],level,random.Random(seed),False,1)
                if item is not None:break
            assert item is not None,(row,level)
            assert high.assess(item,grade)['assessedLevel']==level
            assert high.solve(item['certificate']).is_finite
            checked+=1
    assert checked==303
