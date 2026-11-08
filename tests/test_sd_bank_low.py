"""Boundary and semantic checks for the primary 1--2 local authoring model."""
from copy import deepcopy
import random

import sympy as s
import pytest

from app.services.exercise.sd_bank_low import generate,solve_certificate


def test_pattern_counts_repetitions_after_prefix_is_hidden():
    cert={'type':'sd_low_pattern','inputs':{'period':['circle','triangle','square'],'target':'triangle','start':2,'end':11}}
    # Ordinal positions 5, 8, 11 are triangles; position 2 is hidden.
    assert solve_certificate(cert)==3


def test_grid_moves_follow_cells_in_order():
    cert={'type':'sd_low_grid','inputs':{'grid':[[7,9,1],[2,8,5],[6,4,3]],'start':[1,1],'moves':[[0,-1],[-1,0],[0,1]]}}
    assert solve_certificate(cert)==9
    changed=deepcopy(cert);changed['inputs']['grid'][0][1]=6
    assert solve_certificate(changed)==6


@pytest.mark.parametrize('seed',range(5))
def test_restore_question_does_not_cancel_the_hidden_initial_quantity(seed):
    question=generate(1,3,'A','hard',random.Random(seed),True,1);certificate=question['certificate'];original=solve_certificate(certificate)
    changed=deepcopy(certificate);changed['inputs']['a']+=1
    assert solve_certificate(changed)==original+1


def test_place_value_exchange_preserves_number_and_changes_unbundled_ones():
    cert={'type':'sd_low_expression','inputs':{'a':37,'t':4},'expression':'Mod(a,10)+10-t'}
    assert solve_certificate(cert)==13
    assert 2*10+13 == 37-4


def test_half_and_quarter_panels_require_both_corrections():
    cert={'type':'sd_low_expression','inputs':{'n':4,'k':3,'a':1,'b':8,'d':4},'expression':'Abs(n*k/d-a)+Abs(b-n*k/d)'}
    # Each whole has 12 equal pieces, target 3. Add 2 to A, clear 5 from B.
    assert solve_certificate(cert)==7


def test_grade_two_counting_uses_two_digit_quantities():
    for cap_bab in [1,7]:
        model=generate(2,cap_bab,'A','easy',random.Random(18),True,1)
        assert model['scene']['groups'][0]['count']>10


def test_grade_one_second_counting_chapter_exercises_eleven_to_twenty():
    for seed in range(15):
        model=generate(1,5,'A','medium',random.Random(seed),True,1)
        counts=[group['count'] for group in model['scene']['groups']]
        assert counts[0]>=11 and sum(counts)<=20


def test_early_grade_one_composition_does_not_exceed_ten_triangles():
    for seed in range(20):
        model=generate(1,4,'C','hard',random.Random(seed),True,1)
        assert model['scene']['groups'][0]['count']<=10


def test_ruler_is_in_nonstandard_units_for_grade_one():
    model=generate(1,7,'B','hard',random.Random(42),True,1)
    assert model['scene']['unit']=='satuan'
    assert 'cm' not in model['question']


def test_fraction_options_are_not_equivalent():
    model=generate(2,5,'A','easy',random.Random(7),True,1)
    assert model['answer']==r'$\frac{1}{2}$'
    assert len(set([model['answer'],*model['wrong']]))==4
    assert solve_certificate(model['certificate'])==s.Rational(1,2)


def test_clock_easy_can_supply_seven_distinct_visual_questions():
    hours={generate(2,6,'B','easy',random.Random(seed),True,1)['scene']['hour'] for seed in range(60)}
    assert len(hours)>=7
    assert all(1<=hour<=12 for hour in hours)
