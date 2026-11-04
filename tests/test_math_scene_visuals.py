"""The new visual dialect must render facts while preserving legacy assets."""
from copy import deepcopy
import hashlib
import json

from PIL import Image
import pytest

from app.services.exercise.math_scene_visuals import render_scene, validate_scene
from app.services.exercise.visual_assets import VisualSpec, render


EXAMPLES = [
    {'kind':'table','title':'Data koefisien','headers':['Koefisien','Nilai'],'rows':[['a',3],['b',-4],['c',2]]},
    {'kind':'coordinate_graph','title':'Grafik fungsi dan titik','x_range':[-4,4],'y_range':[-4,8],
     'tick_step':[1,2],'functions':[{'coefficients':[-1,0,1],'label':'f'}],
     'points':[{'x':2,'y':3,'label':'P'}]},
    {'kind':'geometry','title':'Segitiga siku-siku','points':[{'x':0,'y':0,'label':'A'},{'x':6,'y':0,'label':'B'},{'x':0,'y':4,'label':'C'}],
     'segments':[{'start':0,'end':1,'label':'6 cm'},{'start':1,'end':2},{'start':2,'end':0,'label':'4 cm'}]},
    {'kind':'geometry','title':'Lingkaran berpusat O','points':[{'x':0,'y':0,'label':'O'},{'x':5,'y':0,'label':'A'}],
     'segments':[{'start':0,'end':1,'label':'5 cm'}], 'circles':[{'center':[0,0],'radius':5}]},
    {'kind':'mapping','title':'Pemetaan A ke B','left':[1,2,3],'right':[3,5,7],'arrows':[[0,0],[1,1],[2,2]]},
    {'kind':'probability_tree','title':'Pengambilan tanpa pengembalian',
     'nodes':[{'id':'root','label':'Mulai','x':0,'y':.5},
              {'id':'red','label':'Merah','x':.5,'y':.15},
              {'id':'blue','label':'Biru','x':.5,'y':.85},
              {'id':'rr','label':'Merah','x':1,'y':0},
              {'id':'rb','label':'Biru','x':1,'y':.3},
              {'id':'br','label':'Merah','x':1,'y':.7},
              {'id':'bb','label':'Biru','x':1,'y':1}],
     'edges':[{'from':'root','to':'red','label':'3/5'},{'from':'root','to':'blue','label':'2/5'},
              {'from':'red','to':'rr','label':'2/4'},{'from':'red','to':'rb','label':'2/4'},
              {'from':'blue','to':'br','label':'3/4'},{'from':'blue','to':'bb','label':'1/4'}]},
]


@pytest.mark.parametrize('scene', EXAMPLES)
def test_all_diagrams_render_both_formats_without_clipped_labels(scene,tmp_path):
    spec={'kind':'math_scene','scene':scene}
    VisualSpec.model_validate(spec)
    path,provenance=render(spec,tmp_path)
    png=tmp_path/path
    with Image.open(png) as image:
        image.verify()
    assert png.with_suffix('.svg').read_text(encoding='utf-8').startswith('<svg')
    assert provenance['semanticSpec']==scene
    assert provenance['pngSha256']==hashlib.sha256(png.read_bytes()).hexdigest()
    assert provenance['visualEssentialStatus']=='pending_local_semantic_review'
    before={p.name:p.read_bytes() for p in png.parent.iterdir()}
    assert render(spec,tmp_path)==(path,provenance)
    assert before=={p.name:p.read_bytes() for p in png.parent.iterdir()}


def test_fact_change_changes_asset_and_immutable_content_cannot_be_overwritten(tmp_path):
    scene=deepcopy(EXAMPLES[0]);path,proof=render_scene(scene,tmp_path)
    scene['rows'][0][1]+=1;other,changed=render_scene(scene,tmp_path)
    assert path!=other and proof['pngSha256']!=changed['pngSha256']
    (tmp_path/path).write_bytes(b'corrupt')
    with pytest.raises(ValueError,match='immutable'):
        render_scene(EXAMPLES[0],tmp_path)


@pytest.mark.parametrize('value',[float('nan'),float('inf'),float('-inf'),True,10**20])
def test_nonfinite_or_unbounded_numbers_are_rejected(value):
    scene=deepcopy(EXAMPLES[0]);scene['rows'][0][1]=value
    with pytest.raises(ValueError):validate_scene(scene)


def test_reject_answer_leakage_and_invalid_graph_or_tree():
    scene=deepcopy(EXAMPLES[0]);scene['rows'][0][1]={'answer':2}
    with pytest.raises(ValueError,match='answer'):validate_scene(scene)
    scene=deepcopy(EXAMPLES[1]);scene['points'][0]['x']=5
    with pytest.raises(ValueError,match='outside'):validate_scene(scene)
    scene=deepcopy(EXAMPLES[-1]);scene['edges'].append({'from':'rr','to':'root'})
    with pytest.raises(ValueError,match='rooted tree'):validate_scene(scene)


def test_legacy_content_address_does_not_include_new_dialect(tmp_path):
    spec={'kind':'object_groups','groups':[{'label':'A','shape':'circle','count':3}]}
    path,_=render(spec,tmp_path)
    payload=VisualSpec.model_validate(spec).model_dump(mode='json');payload.pop('scene')
    expected=hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()[:24]
    assert path=='assets/'+expected+'.png'
