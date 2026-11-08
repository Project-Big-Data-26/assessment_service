"""Curriculum routing, semantic visual data and independently checked SMA maths."""
from copy import deepcopy
from pathlib import Path
import random

import pytest
import sympy as s

from app.ingestion.question_sync import report_catalog
from app.services.exercise import session_high_sma as bank


ROOT=Path(__file__).resolve().parents[1]
JOBS=[j for j in report_catalog(ROOT/'API_DOCUMENTATION/Pesan_eror.md') if int(j['class_key'][5:].split('_')[0])>=10]


@pytest.mark.parametrize('job',JOBS,ids=lambda j:f"{j['class_key']}-{j['chapter_no']}-{j['code']}")
@pytest.mark.parametrize('level',['easy','medium'])
@pytest.mark.parametrize('visual',[False,True])
def test_every_sma_topic_has_appropriate_local_capacity(job,level,visual):
    model=bank.generate(job['class_key'],job['chapter_no'],job['code'],level,random.Random(32),visual,1)
    assert model is not None
    assert model['assessment']['assessedLevel']==level
    assert bank.solve(model['certificate']).is_finite
    assert len(set([model['answer'],*model['wrong']]))==4
    assert not any(ord(c)<32 for c in model['question'])
    assert model['question'].count('$')%2==0
    if visual:bank.check_visual(model)
    else:assert model['scene'] is None
    altered=deepcopy(model);altered.update(requestedLevel='hard',quota=999)
    assert bank.assess(altered,12)==bank.assess(model,12)


def test_product_rule_is_recomputed_from_the_actual_function():
    model=bank.generate('kelas12_tl',2,'B','medium',random.Random(8),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x=s.Symbol('x')
    f=(p['a']*x+p['b'])*(p['c']*x+p['d'])
    assert bank.solve(model['certificate'])==s.diff(f,x).subs(x,p['t'])


def test_definite_integral_is_recomputed_from_both_limits():
    model=bank.generate('kelas12_tl',3,'B','medium',random.Random(18),False,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x=s.Symbol('x')
    assert bank.solve(model['certificate'])==s.integrate(p['a']*x*x+p['b']*x+p['c'],(x,p['L'],p['U']))


def test_matrix_product_uses_the_shared_inner_dimension():
    model=bank.generate('kelas11_tl',1,'D','medium',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()}
    left=s.Matrix([[p['a'],p['b']]]);middle=s.Matrix([[p['c'],p['d']],[p['e'],p['f']]]);right=s.Matrix([[p['g']],[p['h']]])
    assert bank.solve(model['certificate'])==(left*middle*right)[0]


HARD=[('kelas10',1,'B'),('kelas10',1,'D'),('kelas10',5,'A'),('kelas12',1,'B'),('kelas12',2,'C'),('kelas12',2,'D'),('kelas12',3,'B'),('kelas12',3,'C'),('kelas12',3,'D'),('kelas12',4,'B'),('kelas11_tl',1,'A'),('kelas11_tl',1,'B'),('kelas11_tl',1,'C'),('kelas11_tl',1,'D'),('kelas11_tl',2,'B'),('kelas11_tl',2,'C'),('kelas11_tl',2,'D'),('kelas11_tl',3,'E'),('kelas11_tl',4,'C'),('kelas11_tl',6,'A'),('kelas12_tl',4,'F'),('kelas12_tl',4,'G')]


@pytest.mark.parametrize('args',HARD)
def test_previous_hard_routing_holes_have_reconstruction_models(args):
    model=bank.generate(*args,'hard',random.Random(31),True,1)
    assert model['assessment']['assessedLevel']=='hard'
    assert model['certificate']['expression'] not in [str(model['certificate']['inputs'][k]) for k in model['certificate']['inputs']]
    bank.check_visual(model)


def test_normal_reconstruction_uses_normal_table_not_binomial_fallback():
    model=bank.generate('kelas12_tl',4,'G','hard',random.Random(31),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()}
    sd=(p['B']-p['A'])/3;mean=p['A']+sd;z=(p['C']-mean)/sd
    table={-1:p['F1'],1:p['F2'],2:p['F3']}
    assert bank.solve(model['certificate'])==1-table[z]
    assert 'binomial' not in model['certificate']['expression']


def test_conditional_probability_reconstructs_both_event_probabilities():
    model=bank.generate('kelas12',4,'B','hard',random.Random(35),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()}
    A,B=s.symbols('A B');solution=s.solve([A+B-p['I']-p['U'],A-p['k']*B],[A,B])
    assert bank.solve(model['certificate'])==(solution[A]-p['I'])/(1-solution[B])
    assert 0<=bank.solve(model['certificate'])<=1


def test_digit_pool_is_real_decimal_digits_and_image_contains_the_actual_pool():
    for seed in range(100):
        model=bank.generate('kelas12',3,'A','medium',random.Random(seed),True,1)
        digits=list(map(int,model['scene']['rows'][0][1].split(', ')))
        p=model['certificate']['inputs']
        assert len(digits)==len(set(digits))==p['n']
        assert all(1<=v<=9 for v in digits)
        assert sum(v%2==0 for v in digits)==p['e']<=4
        assert 2<=p['k']<=p['n']
        bank.check_visual(model)


def test_scalar_matrix_family_uses_type_conditions_without_determinant_prerequisite():
    model=bank.generate('kelas11_tl',1,'A','hard',random.Random(16),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x,y=s.symbols('x y')
    solution=s.solve([x+p['a']*y-p['S']/2,p['c']*x+p['d']*y-p['S']/2],[x,y])
    assert bank.solve(model['certificate'])==solution[x]**2+solution[y]**2
    assert 'determinan' not in model['question'].lower()


def test_polynomial_remainders_reconstruct_the_actual_monic_cubic():
    model=bank.generate('kelas11_tl',2,'C','hard',random.Random(31),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x=s.Symbol('x');a,b,c=s.symbols('a b c');poly=x**3+a*x*x+b*x+c
    solution=s.solve([poly.subs(x,1)-p['U'],poly.subs(x,-1)-p['V'],poly.subs(x,p['t'])],[a,b,c])
    assert bank.solve(model['certificate'])==poly.subs(solution).subs(x,p['q'])


def test_radical_reconstruction_uses_two_consistent_constraints():
    model=bank.generate('kelas10',1,'D','hard',random.Random(31),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};u=(p['S']+p['D']/p['S'])/2;v=(p['S']-p['D']/p['S'])/2
    assert u>v>0
    assert bank.solve(model['certificate'])==u/v+v/u


def test_binomial_moment_inference_uses_valid_integer_trial_count():
    model=bank.generate('kelas12_tl',4,'F','hard',random.Random(31),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};prob=1-p['V']/p['M'];n=p['M']/prob
    assert n.is_Integer and 0<prob<1
    assert bank.solve(model['certificate'])==s.binomial(n,p['k'])*prob**p['k']*(1-prob)**(n-p['k'])


def test_ordinary_sector_is_bounded_and_neither_club_wording_is_unambiguous():
    for seed in range(100):
        model=bank.generate('kelas11',2,'A','medium',random.Random(seed),True,1)
        p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()}
        assert 0<p['s']<2*s.pi*p['r']
    model=bank.generate('kelas10',7,'B','medium',random.Random(2),True,1)
    assert 'tidak mengikuti klub A maupun klub B' in model['question']


def test_new_dice_conditional_probability_enumerates_the_reconstructed_sample_space():
    model=bank.generate('kelas10',7,'A','hard',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};n=int(s.sqrt(2/p['p']))
    eligible=[(a,b) for a in range(int(p['t']),n+1) for b in range(1,n+1)]
    expected=s.Rational(sum(a+b==p['s'] for a,b in eligible),len(eligible))
    assert bank.solve(model['certificate'])==expected


def test_hidden_urn_size_is_reconstructed_before_probability_update():
    model=bank.generate('kelas10',7,'C','hard',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};n=s.simplify((p['p']-p['q'])/(p['p']**2-p['q']));red=p['p']*n
    assert n.is_Integer and red.is_Integer
    assert bank.solve(model['certificate'])==(red-1)/(n-2)


def test_chord_root_selection_is_physical_and_uses_the_supplied_boundary():
    model=bank.generate('kelas11',2,'C','hard',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x=s.Symbol('x')
    roots=s.solve(x*(x+p['a'])-(x-p['b'])*p['c'],x)
    selected=[v for v in roots if v>p['t'] and v-p['b']>0 and v+p['a']>0]
    assert len(selected)==1
    assert bank.solve(model['certificate'])==2*selected[0]+p['a']


def test_reconstructed_unit_circle_values_obey_the_stated_quadrant():
    model=bank.generate('kelas11_tl',3,'A','hard',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};difference=s.sqrt(2-p['S']**2);sin=(p['S']+difference)/2;cos=(p['S']-difference)/2
    assert sin>0 and cos<0 and s.simplify(sin*sin+cos*cos)==1
    assert bank.solve(model['certificate'])==sin-p['k']*cos


def test_integral_area_crossing_the_horizontal_line_uses_three_intervals():
    model=bank.generate('kelas12_tl',3,'C','hard',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x=s.Symbol('x');a=6*p['T']/p['L']**3;curve=a*x*(p['L']-x)
    roots=sorted(s.solve(curve-p['H'],x));lo,hi=roots
    expected=s.integrate(p['H']-curve,(x,0,lo))+s.integrate(curve-p['H'],(x,lo,hi))+s.integrate(p['H']-curve,(x,hi,p['L']))
    assert s.simplify(bank.solve(model['certificate'])-expected)==0


def test_loan_annuity_reconstructs_balances_and_total_interest_consistently():
    model=bank.generate('kelas12',2,'E','hard',random.Random(3),True,1)
    p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};factor=(p['W']-p['V'])/(p['V']-p['U']);payment=p['U']*factor-p['V'];initial=(p['U']+payment)/factor
    balance=initial;interest=0
    for _ in range(3):interest+=balance*(factor-1);balance=balance*factor-payment
    assert balance==p['W']
    assert bank.solve(model['certificate'])==interest


def test_derivative_extrema_family_reconstructs_a_real_cubic_from_all_constraints():
    for seed in range(12):
        model=bank.generate('kelas12_tl',2,'C','hard',random.Random(seed),True,1)
        p={k:s.sympify(v) for k,v in model['certificate']['inputs'].items()};x=s.Symbol('x');a,b,c=s.symbols('a b c');f=a*x**3+b*x*x+c*x;df=s.diff(f,x)
        solution=s.solve([df.subs(x,p['u']),df.subs(x,p['v']),f.subs(x,p['w'])-p['Z']],[a,b,c])
        actual=f.subs(solution);second=s.diff(actual,x,2)
        assert solution[a]>0 and second.subs(x,p['u'])<0 and second.subs(x,p['v'])>0
        assert bank.solve(model['certificate'])==actual.subs(x,p['u'])-actual.subs(x,p['v'])
        bank.check_visual(model)


@pytest.mark.parametrize('args',[('kelas11',3,'A','easy'),('kelas11',3,'A','medium'),('kelas10',3,'B','easy'),('kelas11',2,'B','easy')])
def test_actual_exercises_use_graphs_or_geometry_with_consistent_derived_facts(args):
    model=bank.generate(*args,random.Random(41),True,1)
    assert model['scene']['kind'] in {'coordinate_graph','geometry'}
    bank.check_visual(model)
    broken=deepcopy(model);broken['scene']['points'][0]['label']='inconsistent'
    with pytest.raises(ValueError,match='Derived diagram'):
        bank.check_visual(broken)
