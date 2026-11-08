"""Verify visible mathematical facts, not just image-file existence."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

from PIL import Image
import pytest

from app.services.exercise.sd_bank_visuals import BLUE, render_scene, validate_scene
from app.services.exercise.visual_assets import VisualSpec, render
from app.services.exercise.workflow import digest, safe_asset

NS = {'s': 'http://www.w3.org/2000/svg'}


def svg_for(base, relative):
    return ET.parse((base / relative).with_suffix('.svg')).getroot()


def test_object_counts_and_crossed_marks_match_svg_and_png(tmp_path):
    scene = {'kind': 'groups', 'groups': [
        {'label': 'A', 'count': 9, 'shape': 'circle', 'crossed': 2},
        {'label': 'B', 'count': 4, 'shape': 'triangle'},
    ]}
    path, proof = render_scene(scene, tmp_path)
    svg = svg_for(tmp_path, path)
    assert len(svg.findall('s:ellipse', NS)) == 9
    assert len(svg.findall('s:polygon', NS)) == 4
    assert len(svg.findall('s:line', NS)) == 4  # Two crossed circles, two strokes each.
    with Image.open(tmp_path / path) as image:
        assert image.size == (proof['width'], proof['height'])
        assert image.getpixel((175, 75)) == (184, 218, 240)
    assert proof['semanticSpec'] == scene
    assert safe_asset(tmp_path, path) == (tmp_path / path).resolve()


def test_fraction_area_exactly_matches_the_shaded_cells(tmp_path):
    scene = {'kind': 'fraction_grid', 'rows': 2, 'cols': 5, 'shaded': 3}
    path, _ = render_scene(scene, tmp_path)
    rects = svg_for(tmp_path, path).findall('s:rect', NS)
    cells = [r for r in rects if r.attrib.get('width') != '100%']
    assert len(cells) == 10
    assert sum(r.attrib['fill'] == BLUE for r in cells) == 3
    assert len({(r.attrib['width'], r.attrib['height']) for r in cells}) == 1


def test_composition_triangles_really_are_right_isosceles(tmp_path):
    path,_=render_scene({'kind':'groups','groups':[{'label':'A','count':2,'shape':'right_triangle'}]},tmp_path)
    triangles=svg_for(tmp_path,path).findall('s:polygon',NS)
    assert len(triangles)==2
    for triangle in triangles:
        points=[tuple(map(float,p.split(','))) for p in triangle.attrib['points'].split()]
        # The right angle is the second vertex; both perpendicular legs are equal.
        v1=(points[0][0]-points[1][0],points[0][1]-points[1][1])
        v2=(points[2][0]-points[1][0],points[2][1]-points[1][1])
        assert v1[0]*v2[0]+v1[1]*v2[1]==0
        assert v1[0]**2+v1[1]**2==v2[0]**2+v2[1]**2


def test_scene_counterfactual_changes_actual_pixels_and_retained_hash(tmp_path):
    first = {'kind': 'fraction_grid', 'rows': 1, 'cols': 8, 'shaded': 3}
    changed = deepcopy(first)
    changed['shaded'] = 4
    p1, proof1 = render_scene(first, tmp_path)
    p2, proof2 = render_scene(changed, tmp_path)
    assert p1 != p2 and proof1['specHash'] != proof2['specHash']
    assert proof1['pngSha256'] != proof2['pngSha256']
    assert (tmp_path / p1).read_bytes() != (tmp_path / p2).read_bytes()
    assert proof1['semanticSpec']['shaded'] == 3
    assert proof2['semanticSpec']['shaded'] == 4


def test_bar_heights_encode_proportions_and_axis_begins_at_zero(tmp_path):
    path, _ = render_scene({'kind': 'bars', 'labels': ['A', 'B'], 'values': [4, 8]}, tmp_path)
    svg = svg_for(tmp_path, path)
    bars = [r for r in svg.findall('s:rect', NS) if r.attrib.get('fill') in (BLUE, '#ffd49b')]
    assert len(bars) == 2
    assert float(bars[1].attrib['height']) == 2 * float(bars[0].attrib['height'])
    bottoms = [float(r.attrib['y']) + float(r.attrib['height']) for r in bars]
    assert bottoms[0] == bottoms[1]
    labels = [t.text for t in svg.findall('s:text', NS)]
    assert '0' in labels and '4' in labels and '8' in labels


def test_pictogram_counts_respect_legend_units(tmp_path):
    scene = {'kind': 'pictogram', 'labels': ['A', 'B'], 'values': [4, 6], 'unit': 2}
    path, _ = render_scene(scene, tmp_path)
    svg = svg_for(tmp_path, path)
    assert len(svg.findall('s:ellipse', NS)) == 5
    assert any('mewakili 2' in (t.text or '') for t in svg.findall('s:text', NS))


def test_tally_uses_one_diagonal_in_every_group_of_five(tmp_path):
    path, _ = render_scene({'kind': 'tally', 'labels': ['A'], 'values': [12]}, tmp_path)
    lines = svg_for(tmp_path, path).findall('s:line', NS)
    assert len(lines) == 12
    assert sum(line.attrib['x1'] != line.attrib['x2'] for line in lines) == 2


def test_deterministic_rerender_keeps_both_formats_and_provenance(tmp_path):
    scene = {'kind': 'ruler', 'start': 0, 'end': 12, 'step': 1,
             'object_start': 3, 'object_end': 10}
    path, first = render_scene(scene, tmp_path)
    png_before = (tmp_path / path).read_bytes()
    svg_before = (tmp_path / path).with_suffix('.svg').read_bytes()
    path_again, second = render(VisualSpec(kind='sd_scene', scene=scene), tmp_path)
    assert path_again == path and first == second
    assert png_before == (tmp_path / path).read_bytes()
    assert svg_before == (tmp_path / path).with_suffix('.svg').read_bytes()
    assert first['pngSha256'] == digest(tmp_path / path)
    assert first['svgSha256'] == digest((tmp_path / path).with_suffix('.svg'))
    assert json.loads((tmp_path / path).with_suffix('.json').read_text(encoding='utf-8')) == first


def test_tampered_asset_is_rejected_instead_of_silently_overwritten(tmp_path):
    scene = {'kind': 'clock', 'hour': 8, 'minute': 30}
    path, _ = render_scene(scene, tmp_path)
    (tmp_path / path).write_bytes(b'changed')
    with pytest.raises(ValueError, match='immutable SD visual differs'):
        render_scene(scene, tmp_path)
    assert (tmp_path / path).read_bytes() == b'changed'


def test_oversized_label_fails_before_an_unreadable_png_is_saved(tmp_path):
    scene = {'kind': 'cards', 'cards': [{'value': 'X' * 1000}]}
    with pytest.raises(ValueError, match='clipped'):
        render_scene(scene, tmp_path)
    assert not list(tmp_path.rglob('*.png'))


def test_legacy_visual_spec_keeps_original_semantic_hash_and_renderer(tmp_path):
    legacy = {'kind': 'object_groups', 'groups': [{'label': 'A', 'shape': 'circle', 'count': 3}],
              'pattern': [], 'hour': None, 'minute': None}
    expected = hashlib.sha256(json.dumps(legacy, sort_keys=True).encode()).hexdigest()
    path, proof = render(legacy, tmp_path)
    assert proof['semanticSpec'] == legacy
    assert proof['specHash'] == expected
    assert proof['rendererVersion'] == 'math-diagrams-v1'
    assert Path(path).stem == expected[:24]


@pytest.mark.parametrize('scene', [
    {'kind': 'fraction_grid', 'rows': 1, 'cols': 4, 'shaded': 5},
    {'kind': 'groups', 'groups': [{'count': 4, 'crossed': 5}]},
    {'kind': 'pictogram', 'labels': ['A'], 'values': [3], 'unit': 0},
    {'kind': 'bars', 'labels': ['A', 'B'], 'values': [3]},
    {'kind': 'ruler', 'start': 0, 'end': 10, 'object_end': 11},
    {'kind': 'table', 'headers': ['A', 'B'], 'rows': [[1]]},
    {'kind': 'clock', 'hour': 8, 'minute': 70},
    {'kind': 'cards', 'cards': [2], 'correct_answer': 2},
])
def test_invalid_or_answer_leaking_specs_are_rejected(scene):
    with pytest.raises(ValueError):validate_scene(scene)


def test_sd_scene_cannot_be_mixed_with_legacy_spec_fields():
    with pytest.raises(ValueError, match='legacy visual fields'):
        VisualSpec(kind='sd_scene', scene={'kind': 'clock', 'hour': 2, 'minute': 0}, hour=2)
