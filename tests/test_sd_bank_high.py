"""Independent content regressions for the grade 3--4 bank."""
from itertools import permutations
import random
import sympy as s
from app.services.exercise.sd_bank_high import generate,solve_certificate
from scripts.generate_sd_bank_local import answer_identity,visual_check,path_value


def test_digit_card_bound_requires_reading_available_digits():
    for grade in (3,4):
        for seed in range(12):
            model=generate(grade,1,'A','hard',random.Random(seed),True,1);cert=model['certificate']
            digits=[card['value'] for card in model['scene']['cards']]
            candidates=[int(''.join(map(str,p))) for p in permutations(digits) if p[0]!=0 and p[-1]%2==0 and int(''.join(map(str,p)))<cert['bound']]
            assert max(candidates)==solve_certificate(cert)
            assert solve_certificate(cert)!=cert['bound']-1


def test_equal_volume_dimensions_keep_distinct_semantic_bindings():
    found=False
    for seed in range(100):
        model=generate(4,4,'B','medium',random.Random(seed),True,1);scene=model['scene']
        if scene['length']!=scene['height']:continue
        found=True;binding={b['input']:b['path'] for b in model['certificate']['visual_bindings']}
        assert binding['l']==['length'] and binding['h']==['height'] and binding['w']==['width']
        assert solve_certificate(model['certificate'])==scene['length']*scene['width']*(scene['height']-1)
        visual_check(model);break
    assert found


def test_proper_fraction_options_do_not_give_away_the_only_possible_range():
    for code in ('A','B'):
        for level in ('easy','medium','hard'):
            model=generate(4,2,code,level,random.Random(19),True,1)
            for option in [model['answer'],*model['wrong']]:
                identity=answer_identity(option);assert identity.startswith('number:')
                assert 0<=s.sympify(identity.removeprefix('number:'))<=1


def test_decimal_answers_remain_decimal_and_choices_match_exact_values():
    for level in ('easy','medium','hard'):
        model=generate(4,2,'D',level,random.Random(5),True,1)
        assert '\\frac' not in model['answer']
        actual=s.sympify(answer_identity(model['answer']).removeprefix('number:'))
        assert actual==solve_certificate(model['certificate'])


def test_grade3_text_line_relations_use_descriptions_not_cartesian_coordinates():
    for level in ('easy','medium','hard'):
        model=generate(3,4,'C',level,random.Random(7),False,8)
        assert 'mendatar' in model['question'] and 'tegak' in model['question']
        assert '[[' not in model['question']


def test_perpendicular_lines_visibly_intersect_every_counted_horizontal():
    for seed in range(12):
        model=generate(3,4,'C','medium',random.Random(seed),True,1);segments=model['scene']['segments']
        vertical=next(p for p in segments if p[0][0]==p[1][0])
        for horizontal in (p for p in segments if p[0][1]==p[1][1]):
            assert min(vertical[0][1],vertical[1][1])<horizontal[0][1]<max(vertical[0][1],vertical[1][1])


def test_shading_changes_are_physically_possible():
    for seed in range(20):
        model=generate(4,2,'D','hard',random.Random(seed),True,1);inputs=model['certificate']['inputs']
        n=int(inputs['n']);erase=int(inputs['erase']);add=int(inputs['add'])
        assert 0<=erase<=n and n-erase+add<=100
        visual_check(model)
