"""Domain and curriculum regressions for elementary and SMP session drafts."""
import random
import sympy as s

from app.services.exercise import session_high_basic as basic
from scripts.generate_sd_bank_local import answer_identity


def test_endpoint_probability_options_stay_inside_probability_domain():
    item=basic.direct(6,4,'B',random.Random(13),False)
    assert basic.solve(item['certificate'])==0
    values=[s.sympify(answer_identity(v)[7:]) for v in item['wrong']]
    assert len(set(values))==3 and all(0<=v<=1 for v in values)


def test_elementary_cacah_linked_results_are_unsigned_differences():
    for seed in range(20):
        item=basic.generate(5,1,'D','medium',random.Random(seed),False,1)
        cert=item['certificate'];a=basic.solve(cert['left']);b=basic.solve(cert['right'])
        assert cert['operation']=='absolute_difference'
        assert basic.solve(cert)==abs(a-b)>=0
        assert 'hasil yang lebih kecil' in item['question']


def test_elementary_text_has_actual_data_without_floor_or_mod_procedures():
    item=basic.direct(5,1,'A',random.Random(7),False)
    assert 'Diketahui' not in item['question']
    assert 'bmod' not in item['question'] and 'dibulatkan ke bawah' not in item['question']
    p=item['certificate']['inputs'];expected=(p['N']//p['P'])%10*p['P']
    assert basic.solve(item['certificate'])==expected
    assert str(p['N']) in item['question']


def test_area_perimeter_relation_uses_given_perimeter():
    item=basic.direct(5,5,'D',random.Random(11),False);p=item['certificate']['inputs']
    assert 'Keliling' in item['question'] and 'luas' in item['question']
    assert basic.solve(item['certificate'])==(p['K']//4)**2


def test_constructed_ray_stays_inside_protractor_scale():
    for seed in range(30):
        item=basic.direct(5,6,'D',random.Random(seed),False);p=item['certificate']['inputs']
        assert 'melukis' in item['question']
        assert basic.solve(item['certificate'])==p['A']+p['B']<=180


def test_factor_recipe_counts_actual_positive_divisors():
    for seed in range(15):
        item=basic.direct(5,2,'C',random.Random(seed),False);n=item['certificate']['inputs']['N']
        expected=sum(n%d==0 for d in range(1,n+1))
        assert basic.solve(item['certificate'])==expected


def test_zero_count_can_still_have_three_nonnegative_wrong_options():
    assert len(basic._wrong_options(s.Integer(0),nonnegative=True))==3


def test_linked_probability_domains_are_explicit():
    for grade,lo in [(6,0),(9,-1)]:
        for seed in range(12):
            item=basic.generate(grade,4,'A','medium',random.Random(seed),False,1)
            assert lo<=basic.solve(item['certificate'])<=1
            # Parse the generated LaTeX through the repository's arithmetic
            # option parser instead of a second implementation of fractions.
            from scripts.generate_sd_bank_local import answer_identity
            values=[s.sympify(answer_identity(v)[7:]) for v in item['wrong']]
            assert all(lo<=v<=1 for v in values)
