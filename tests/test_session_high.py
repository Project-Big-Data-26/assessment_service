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
    assert high.solve(model['certificate'])==min(pairs)


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
            value=high.solve(item['certificate'])
            assert isinstance(value,str) or value.is_finite
            checked+=1
    assert checked==303


def test_chart_choice_really_assesses_representation_and_truncated_axis():
    model=high.generate('kelas7',6,'F','hard',random.Random(9),True,1);cert=model['certificate'];p=cert['inputs']
    assert cert['task']=='axis_audit' and p['origin']>0
    assert s.Rational(p['origin']+p['b'],p['origin']+p['a'])!=2
    assert high.solve(cert)==model['answer'] and 'Diagram' in model['answer']
    assert high.check_visual(model)['pivotalFacts']


def test_data_corrections_that_cancel_are_not_called_hard():
    model={'kind':'session_data_audit','certificate':{'type':'session_data_audit','inputs':{'reported':170,'duplicate':4,'missing':4,'other':20}}}
    decision=high.assess(model,7)
    assert decision['assessedLevel']=='easy' and 'numerical_shortcut' in decision['flags']


def test_hidden_scientific_exponents_are_reconstructed_from_two_observations():
    model=high.generate('kelas8',1,'C','hard',random.Random(7),False,1);p=model['certificate']['inputs']
    candidates=[]
    for a in range(1,10):
        for b in range(1,10):
            if a+b==p['sum_exponents'] and s.Rational(p['coefficient_a']*10**a,p['coefficient_b']*10**b)==s.Rational(p['ratio_num'],p['ratio_den']):candidates.append(p['coefficient_a']*10**a-p['coefficient_b']*10**b)
    assert len(candidates)==1 and high.solve(model['certificate'])==candidates[0]


def test_hard_urn_probability_distractors_remain_probabilities():
    from scripts.generate_sd_bank_local import answer_identity
    for seed in range(8):
        model=high.generate('kelas6',4,'A','hard',random.Random(seed),False,1)
        for option in [model['answer'],*model['wrong']]:
            value=s.sympify(answer_identity(option).split(':',1)[1]);assert 0<=value<=1


def test_place_value_picture_uses_only_observed_number_not_known_position():
    model=high.generate('kelas5',1,'A','easy',random.Random(7),True,1)
    cert=model['certificate'];inputs=cert['inputs']
    assert model['scene']['rows']==[['N',str(inputs['N'])]]
    assert [item['input'] for item in cert['visual_bindings']]==['N']
    assert inputs['N']+inputs['P'] in cert['visual_bindings'][0]['alternatives']
    assert inputs['N']+10*inputs['P'] in cert['visual_bindings'][0]['alternatives']
    assert high.check_visual(model)['pivotalFacts']==['N']


def test_linked_place_value_picture_uses_retained_row_bindings_after_filtering():
    model=high.generate('kelas5',9,'A','medium',random.Random(7),True,1)
    cert=model['certificate']
    assert len(model['scene']['rows'])==2
    assert all(row[1]=='N' for row in model['scene']['rows'])
    assert [binding['certificate_path'] for binding in cert['visual_bindings']]==[
        ['left','inputs','N'],['right','inputs','N']]
    assert [binding['path'] for binding in cert['visual_bindings']]==[
        ['rows',0,2],['rows',1,2]]
    assert high.check_visual(model)['pivotalFacts']
    tampered=deepcopy(model);tampered['scene']['rows'][1][2]='999'
    with pytest.raises(AssertionError,match='Scene and retained input differ'):
        high.check_visual(tampered)


def test_generated_parameter_card_labels_use_readable_ascii():
    model=high.generate('kelas5',1,'A','hard',random.Random(41),True,1)
    assert model is not None and model['scene']['rows'][0][0]=='T1'


def test_piecewise_inequality_checks_both_tariff_branches_and_budget():
    for seed in range(12):
        item=high.generate('kelas8',3,'C','hard',random.Random(seed),False,1)
        p=item['certificate']['inputs'];expected=[]
        for duration in range(1,p['limit']+1):
            a=p['fixed_a']+p['rate_a']*duration
            b=p['flat_b'] if duration<=p['threshold'] else p['flat_b']+p['rate_b']*(duration-p['threshold'])
            if b<a and b<=p['budget']:expected.append(duration)
        assert any(t<=p['threshold'] for t in expected)
        assert any(t>p['threshold'] for t in expected)
        assert high.solve(item['certificate'])==len(expected)


def test_piecewise_inequality_has_more_than_three_session_visual_capacity():
    rng=random.Random(41);identities=set()
    for serial in range(90):
        item=high.generate('kelas8',3,'C','hard',rng,True,serial)
        assert item is not None and high.check_visual(item)['pivotalFacts']
        identities.add(item['question'])
    assert len(identities)>=60
