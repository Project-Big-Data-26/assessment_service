"""Substantive primary capacity and quota-independent content judgements."""
from copy import deepcopy
import json
import random

import pytest

from app.services.exercise import session_sd as bank


CHAPTER_SIZES={1:[4,3,4,3,4,3,2,2],2:[3,3,3,2,3,2,2,2],
               3:[7,2,4,3,2],4:[9,5,2,2,2,2]}
SLOTS=[(g,b,chr(65+c),level) for g,sizes in CHAPTER_SIZES.items()
       for b,n in enumerate(sizes,1) for c in range(n)
       for level in ('easy','medium','hard')]


@pytest.mark.parametrize('grade,bab,code,level',SLOTS)
def test_every_primary_location_has_an_actually_assessed_family(grade,bab,code,level):
    rng=random.Random(grade*10000+bab*100+ord(code))
    for index in range(12,32):
        model=bank.generate('kelas'+str(grade),bab,code,level,rng,True,index)
        if model is not None:
            break
    assert model is not None,(grade,bab,code,level)
    assert bank.assess(model,grade)['assessedLevel']==level
    assert model['assessment']['confidenceScore']==0
    assert len(set([model['answer'],*model['wrong']]))==4
    bank.check_visual(model)


@pytest.mark.parametrize('grade,bab,code,level',[
    (1,5,'C','easy'),(2,5,'A','easy'),(2,6,'B','easy'),(2,6,'B','medium'),
    (3,4,'A','easy'),(3,4,'B','easy'),(4,2,'A','easy'),
    (4,2,'A','hard'),(4,5,'A','easy')])
def test_previously_finite_families_have_real_visual_and_text_capacity(grade,bab,code,level):
    for visual,minimum in [(True,21),(False,9)]:
        rng=random.Random(grade*10000+bab*100+ord(code));seen=set()
        for index in range(11,181):
            model=bank.generate('kelas'+str(grade),bab,code,level,rng,visual,index)
            if model is None:
                continue
            # Do not count changing a name, object word, or shuffled options.
            seen.add(bank.semantic_identity(model))
            if len(seen)>=minimum:
                break
        assert len(seen)>=minimum,(grade,bab,code,level,visual,len(seen))


def test_cancelling_updates_cannot_be_called_hard_by_target_or_metadata():
    m=bank._updated_comparison(1,3,'A',random.Random(7),False)
    m['intended_level']='hard';m['certificate']['inputs']['y']=m['certificate']['inputs']['x']
    assert bank.assess(m,1)['assessedLevel']=='easy'


@pytest.mark.parametrize('inputs',[
    {'a':2,'b':2,'t':2}, {'a':2,'b':4,'t':2}, {'a':5,'b':5,'t':1}])
def test_equal_or_emptied_count_groups_do_not_force_hard(inputs):
    model={'kind':'sd_low_membilang_pindah_banding','question':'Perbandingan sesudah perpindahan.',
           'certificate':{'type':'sd_low_expression','inputs':inputs,'expression':'Abs((a-t)-(b+t))'}}
    assert bank.assess(model,1)['assessedLevel']=='medium'


@pytest.mark.parametrize('family,inputs',[
    ('sd_low_banding_dua_perubahan',{'a':3,'b':7,'t':1,'g':2}),
    ('sd_low_berat_pindah_tambah',{'a':8,'b':4,'t':1,'g':2}),
    ('sd_low_data_koreksi_kategori',{'a':3,'b':5,'c':6,'t':2,'g':2})])
def test_opposing_changes_cannot_artificially_make_a_hard_problem(family,inputs):
    model={'kind':family,'question':'Perbandingan data.',
           'certificate':{'type':'sd_low_expression','inputs':inputs,'expression':'a'}}
    assert bank.assess(model,2)['assessedLevel']=='easy'


def test_two_fraction_repairs_retain_two_distinct_targets():
    m=bank._two_fraction_repairs('C',random.Random(4),True);p=m['certificate']['inputs']
    assert p['n1']*p['k1']!=p['n2']*p['k2']
    assert bank.solve(m['certificate'])==p['k1']-p['a']+p['b']-p['k2']
    assert bank.assess(m,2)['assessedLevel']=='hard'
    bank.check_visual(m)


def test_name_or_colours_do_not_create_another_semantic_variation():
    original=bank._place_easy(1,random.Random(2),True);altered=deepcopy(original)
    altered['question']='Nama orang diganti seluruhnya.'
    altered['scene']['title']='Warna lain';altered['scene']['cards'][0]['label']='Nama baru'
    assert bank.semantic_identity(original)==bank.semantic_identity(altered)


def test_shape_evidence_checks_the_geometric_property_before_labelling():
    m=bank._shape_easy(3,'B',random.Random(3),True)
    broken=deepcopy(m);broken['certificate']['inputs']['p']+=1
    with pytest.raises(AssertionError):bank.assess(broken,3)
    bank.check_visual(m)


def test_new_fraction_constraints_use_actual_initial_shading():
    for seed in range(12):
        m=bank._unit_fraction_hard(random.Random(seed),True)
        p=m['certificate']['inputs'];n=p['denominator'];already=p['shaded']
        final=min(k for k in range(already,n+1) if k%2==0 and 2*k>n)
        assert bank.solve(m['certificate'])==(final-already)/bank.s.Integer(n)
        assert bank.assess(m,4)['assessedLevel']=='hard'
        bank.check_visual(m)


def test_diagram_representation_changes_preserve_facts_and_bindings():
    original=bank._place_easy(1,random.Random(3),True)
    for seed in range(20):
        transformed=bank._representation(original,random.Random(seed))
        assert bank.solve(transformed['certificate'])==bank.solve(original['certificate'])
        bank.check_visual(transformed)


def test_table_representation_does_not_turn_each_digit_card_into_a_table():
    original=bank.high.generate(3,1,'A','hard',random.Random(7),True,1)
    transformed=bank._representation(original,random.Random(0))
    assert transformed['scene']['kind']=='table'
    assert 'angka pada tabel' in transformed['question']
    assert 'memakai setiap angka tepat sekali' in transformed['question']
    assert 'setiap tabel' not in transformed['question']
    assert bank.solve(transformed['certificate'])==bank.solve(original['certificate'])
    bank.check_visual(transformed)
