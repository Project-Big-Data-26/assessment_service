"""Bounded, deterministic mathematics diagrams rendered locally to PNG and SVG.

Scenes contain visible facts only, never a solution or difficulty annotation.
Polynomial coefficients are in ascending order: c0 + c1*x + c2*x**2.
"""
from __future__ import annotations

from io import BytesIO
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from .sd_bank_visuals import Canvas, INK, COLORS
from .workflow import atomic_json, digest

VERSION = "math-scenes-v1"
KINDS = {"table", "coordinate_graph", "geometry", "mapping", "probability_tree"}
FORBIDDEN = {"answer", "correct_answer", "jawaban_benar", "difficulty", "assessedLevel"}


def _number(value: Any, name: str, limit: float = 1e8) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or abs(value) > limit:
        raise ValueError(name + " must be a bounded finite number")
    return float(value)


def _label(value: Any, name: str = "label", maximum: int = 64) -> str:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        _number(value, name)
    elif not isinstance(value, str):
        raise ValueError(name + " must be text or a finite number")
    text = str(value)
    if not text or len(text) > maximum or any(ord(c) < 32 for c in text):
        raise ValueError(name + " is empty, too long, or contains control characters")
    return text


def _pair(value: Any, name: str) -> tuple[float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError(name + " needs two numbers")
    return _number(value[0], name), _number(value[1], name)


def _sequence(value: Any, name: str, minimum: int, maximum: int) -> list:
    if not isinstance(value, list) or not minimum <= len(value) <= maximum:
        raise ValueError(f"{name} needs {minimum}..{maximum} entries")
    return value


def _inspect(value: Any, depth: int = 0) -> None:
    if depth > 12:
        raise ValueError("scene nesting exceeds the limit")
    if isinstance(value, dict):
        if FORBIDDEN.intersection(value):
            raise ValueError("a scene cannot contain an answer or assessment")
        for item in value.values():
            _inspect(item, depth + 1)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _inspect(item, depth + 1)
    elif isinstance(value, (int, float)):
        _number(value, "scene value")


def validate_scene(scene: dict) -> dict:
    if not isinstance(scene, dict) or scene.get("kind") not in KINDS:
        raise ValueError("unknown mathematics scene kind")
    _inspect(scene)
    if len(json.dumps(scene, ensure_ascii=False, allow_nan=False)) > 40000:
        raise ValueError("mathematics scene is too large")
    if "title" in scene:
        _label(scene["title"], "title", 96)
    kind = scene["kind"]
    if kind == "table":
        headers = _sequence(scene.get("headers"), "headers", 1, 8)
        for value in headers:
            _label(value, "header")
        for row in _sequence(scene.get("rows"), "rows", 1, 20):
            if not isinstance(row, list) or len(row) != len(headers):
                raise ValueError("table must be rectangular")
            for value in row:
                _label(value, "table cell")
    elif kind == "coordinate_graph":
        for axis in ("x_range", "y_range"):
            low, high = _pair(scene.get(axis), axis)
            if high <= low or high - low < 1e-6:
                raise ValueError("graph bounds must increase")
        step = scene.get("tick_step", [(scene["x_range"][1] - scene["x_range"][0]) / 10,
                                      (scene["y_range"][1] - scene["y_range"][0]) / 10])
        for (lo, hi), tick in zip([scene["x_range"], scene["y_range"]], _pair(step, "tick_step")):
            if tick <= 0 or (hi - lo) / tick > 24:
                raise ValueError("graph requires positive ticks and at most 25 grid lines")
        points = _sequence(scene.get("points", []), "points", 0, 40)
        for point in points:
            _number(point["x"], "point x"); _number(point["y"], "point y")
            if not scene["x_range"][0] <= point["x"] <= scene["x_range"][1] or not scene["y_range"][0] <= point["y"] <= scene["y_range"][1]:
                raise ValueError("graph point lies outside the plotted range")
            if point.get("label"):
                _label(point["label"])
        functions = _sequence(scene.get("functions", []), "functions", 0, 5)
        for function in functions:
            for coefficient in _sequence(function.get("coefficients"), "coefficients", 1, 7):
                _number(coefficient, "coefficient", 1e5)
            if function.get("label"):
                _label(function["label"])
        polylines = _sequence(scene.get("polylines", []), "polylines", 0, 8)
        for line in polylines:
            for point in _sequence(line, "polyline points", 2, 100):
                _pair(point, "polyline point")
        if not (points or functions or polylines):
            raise ValueError("graph needs visible data")
    elif kind == "geometry":
        points = _sequence(scene.get("points", []), "points", 0, 20)
        for point in points:
            _number(point["x"], "point x"); _number(point["y"], "point y")
            if point.get("label"):
                _label(point["label"])
        segments = _sequence(scene.get("segments", []), "segments", 0, 32)
        for segment in segments:
            if any(type(segment.get(k)) is not int or not 0 <= segment[k] < len(points) for k in ("start", "end")) or segment["start"] == segment["end"]:
                raise ValueError("segment endpoints must identify two different points")
            if segment.get("label"):
                _label(segment["label"])
        circles = _sequence(scene.get("circles", []), "circles", 0, 6)
        for circle in circles:
            _pair(circle.get("center"), "circle center")
            if _number(circle.get("radius"), "circle radius") <= 0:
                raise ValueError("circle radius must be positive")
            if circle.get("label"):
                _label(circle["label"])
        if not (segments or circles):
            raise ValueError("geometry needs a segment or circle")
        if "bounds" in scene:
            bounds = scene["bounds"]
            if not isinstance(bounds, list) or len(bounds) != 4:
                raise ValueError("bounds need xmin,xmax,ymin,ymax")
            for value in bounds:
                _number(value, "geometry bounds")
            if not bounds[0] < bounds[1] or not bounds[2] < bounds[3]:
                raise ValueError("geometry bounds must increase")
            for point in points:
                if not bounds[0] <= point["x"] <= bounds[1] or not bounds[2] <= point["y"] <= bounds[3]:
                    raise ValueError("geometry point lies outside the scene")
            for circle in circles:
                x, y = circle["center"]; r = circle["radius"]
                if x - r < bounds[0] or x + r > bounds[1] or y - r < bounds[2] or y + r > bounds[3]:
                    raise ValueError("circle lies outside the scene")
    elif kind == "mapping":
        left = _sequence(scene.get("left"), "left", 1, 8)
        right = _sequence(scene.get("right"), "right", 1, 8)
        for value in left + right:
            _label(value)
        if len(set(map(str, left))) != len(left) or len(set(map(str, right))) != len(right):
            raise ValueError("mapping elements must be distinct within each set")
        for pair in _sequence(scene.get("arrows"), "arrows", 1, 24):
            if not isinstance(pair, list) or len(pair) != 2 or any(type(n) is not int for n in pair) or not 0 <= pair[0] < len(left) or not 0 <= pair[1] < len(right):
                raise ValueError("mapping arrow points outside a set")
    else:
        nodes = _sequence(scene.get("nodes"), "nodes", 2, 24)
        ids = set()
        for node in nodes:
            node_id = _label(node.get("id"), "node id", 32)
            if node_id in ids:
                raise ValueError("tree node IDs must be unique")
            ids.add(node_id); _label(node.get("label"), "node label", 40)
            if not 0 <= _number(node.get("x"), "node x") <= 1 or not 0 <= _number(node.get("y"), "node y") <= 1:
                raise ValueError("tree coordinates must be normalized to 0..1")
        edges = _sequence(scene.get("edges"), "edges", 1, 30)
        incoming = {node_id: 0 for node_id in ids}
        adjacency = {node_id: [] for node_id in ids}
        for edge in edges:
            a, b = edge.get("from"), edge.get("to")
            if a not in ids or b not in ids or a == b:
                raise ValueError("tree edge has an unknown endpoint")
            incoming[b] += 1; adjacency[a].append(b)
            if edge.get("label"):
                _label(edge["label"], "branch label", 32)
        roots = [key for key, count in incoming.items() if count == 0]
        if len(roots) != 1 or any(count > 1 for count in incoming.values()) or len(edges) != len(nodes) - 1:
            raise ValueError("probability scene must be a rooted tree")
        visited = set()
        def visit(node):
            if node in visited:
                raise ValueError("tree contains a cycle")
            visited.add(node)
            for child in adjacency[node]: visit(child)
        visit(roots[0])
        if visited != ids:
            raise ValueError("tree contains disconnected nodes")
    return scene


def _fmt(number):
    return str(int(number)) if float(number).is_integer() else f"{number:.5g}".replace(".", ",")


def _arrow(canvas, x1, y1, x2, y2, color=INK, width=3):
    canvas.line(x1, y1, x2, y2, fill=color, width=width)
    angle = math.atan2(y2-y1, x2-x1)
    size = 10
    canvas.line(x2, y2, x2-size*math.cos(angle-.5), y2-size*math.sin(angle-.5), fill=color, width=width)
    canvas.line(x2, y2, x2-size*math.cos(angle+.5), y2-size*math.sin(angle+.5), fill=color, width=width)


def _clip(a, b, bounds):
    """Liang-Barsky clipping keeps curves and SVG strokes inside plot bounds."""
    x1,y1=a; x2,y2=b; xmin,xmax,ymin,ymax=bounds; dx=x2-x1;dy=y2-y1
    t0,t1=0.,1.
    for p,q in [(-dx,x1-xmin),(dx,xmax-x1),(-dy,y1-ymin),(dy,ymax-y1)]:
        if p == 0:
            if q < 0: return None
        else:
            t=q/p
            if p < 0: t0=max(t0,t)
            else: t1=min(t1,t)
            if t0 > t1:return None
    return (x1+t0*dx,y1+t0*dy),(x1+t1*dx,y1+t1*dy)


def _draw_graph(scene, canvas):
    xmin,xmax=scene['x_range']; ymin,ymax=scene['y_range']; bounds=(xmin,xmax,ymin,ymax)
    def p(x,y): return 115+(x-xmin)/(xmax-xmin)*740, 550-(y-ymin)/(ymax-ymin)*430
    steps=scene.get('tick_step',[(xmax-xmin)/10,(ymax-ymin)/10])
    xzero=min(max(0,xmin),xmax); yzero=min(max(0,ymin),ymax)
    for axis,(low,high),step in zip((0,1),[(xmin,xmax),(ymin,ymax)],steps):
        start=math.ceil((low-1e-10)/step)*step
        for n in range(int((high-start)/step+1e-9)+1):
            value=start+n*step
            if axis==0:
                x,_=p(value,yzero);canvas.line(x,120,x,550,width=1,fill='#dce4eb');canvas.text(x,580,_fmt(value),size=20,width=65)
            else:
                _,y=p(xzero,value);canvas.line(115,y,855,y,width=1,fill='#dce4eb');canvas.text(70,y,_fmt(value),size=20,width=75)
    xaxis=p(xzero,yzero)[0];yaxis=p(xzero,yzero)[1]
    _arrow(canvas,115,yaxis,875,yaxis);_arrow(canvas,xaxis,550,xaxis,102)
    canvas.text(897,yaxis,'x',size=23);canvas.text(xaxis,80,'y',size=23)
    colors=['#1660a6','#a33a32','#247342','#873b90','#995a05']
    paths=[]
    for i,function in enumerate(scene.get('functions',[])):
        coeff=function['coefficients'];path=[]
        for n in range(401):
            x=xmin+(xmax-xmin)*n/400;y=sum(c*x**j for j,c in enumerate(coeff));path.append((x,y))
        paths.append((path,colors[i],function.get('label')))
    for i,path in enumerate(scene.get('polylines',[])):
        paths.append((path,colors[i%len(colors)],None))
    for i,(path,color,label) in enumerate(paths):
        for a,b in zip(path,path[1:]):
            clipped=_clip(a,b,bounds)
            if clipped:
                aa,bb=clipped;canvas.line(*p(*aa),*p(*bb),width=3,fill=color)
        if label:canvas.text(160+i*160,630,label,size=21,width=150,fill=color)
    for point in scene.get('points',[]):
        x,y=p(point['x'],point['y']);canvas.ellipse(x-5,y-5,10,10,fill=INK,width=1)
        if point.get('label'):canvas.text(min(855,max(125,x+18)),max(105,y-24),point['label'],size=20,width=95)


def _draw_geometry(scene,canvas):
    points=scene.get('points',[]);circles=scene.get('circles',[])
    xs=[v['x'] for v in points];ys=[v['y'] for v in points]
    for circle in circles:
        x,y=circle['center'];r=circle['radius'];xs.extend([x-r,x+r]);ys.extend([y-r,y+r])
    xmin,xmax,ymin,ymax=scene.get('bounds',[min(xs),max(xs),min(ys),max(ys)])
    dx=max(xmax-xmin,1);dy=max(ymax-ymin,1);scale=min(690/dx,390/dy)
    cx=(xmin+xmax)/2;cy=(ymin+ymax)/2
    def p(x,y):return 480+(x-cx)*scale,340-(y-cy)*scale
    for circle in circles:
        x,y=p(*circle['center']);r=circle['radius']*scale;canvas.ellipse(x-r,y-r,2*r,2*r,fill=None)
        if circle.get('label'):canvas.text(x,y,circle['label'],width=180,size=24)
    for segment in scene.get('segments',[]):
        a=points[segment['start']];b=points[segment['end']];x1,y1=p(a['x'],a['y']);x2,y2=p(b['x'],b['y'])
        canvas.line(x1,y1,x2,y2,width=3)
        if segment.get('label'):
            length=max(math.hypot(x2-x1,y2-y1),1);canvas.text((x1+x2)/2-(y2-y1)/length*24,(y1+y2)/2+(x2-x1)/length*24,segment['label'],size=23,width=155)
    for point in points:
        x,y=p(point['x'],point['y']);canvas.ellipse(x-3,y-3,6,6,fill=INK,width=1)
        if point.get('label'):canvas.text(x+17,y-24,point['label'],size=23,width=100)


def _draw(scene,canvas):
    if scene.get('title'):canvas.text(480,37,scene['title'],size=27,width=880)
    kind=scene['kind']
    if kind=='table':
        headers=scene['headers'];cw=880/len(headers);top=85;rh=82
        for i,row in enumerate([headers,*scene['rows']]):
            for j,value in enumerate(row):
                x=40+j*cw;y=top+i*rh;canvas.rect(x,y,cw,rh,fill='#b8daf0' if i==0 else 'white',width=2);canvas.text(x+cw/2,y+rh/2,value,size=26,width=cw-16)
    elif kind=='coordinate_graph':_draw_graph(scene,canvas)
    elif kind=='geometry':_draw_geometry(scene,canvas)
    elif kind=='mapping':
        for side,x in [(scene['left'],230),(scene['right'],730)]:
            height=max(240,60*len(side)+40);canvas.ellipse(x-145,330-height/2,290,height,fill=None,width=2)
        def y(i,side):return 330+(i-(len(side)-1)/2)*60
        for a,b in scene['arrows']:_arrow(canvas,365,y(a,scene['left']),595,y(b,scene['right']))
        for side,x in [(scene['left'],230),(scene['right'],730)]:
            for i,value in enumerate(side):canvas.text(x,y(i,side),value,size=27,width=230)
        canvas.text(230,85,'A',size=28);canvas.text(730,85,'B',size=28)
    else:
        nodes={n['id']:n for n in scene['nodes']}
        def p(node):return 130+node['x']*700,110+node['y']*420
        for edge in scene['edges']:
            a,b=nodes[edge['from']],nodes[edge['to']];x1,y1=p(a);x2,y2=p(b);canvas.line(x1,y1,x2,y2,width=2)
            if edge.get('label'):canvas.text((x1+x2)/2,(y1+y2)/2-19,edge['label'],size=21,width=130)
        for node in nodes.values():
            x,y=p(node);canvas.rect(x-60,y-20,120,40,fill='white',width=1);canvas.text(x,y,node['label'],size=22,width=112)


def render_scene(scene: dict, base: Path):
    """Return an immutable relative PNG path and renderer provenance."""
    validate_scene(scene);base=Path(base)
    payload={'rendererVersion':VERSION,'scene':scene}
    spec_hash=hashlib.sha256(json.dumps(payload,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')).hexdigest()
    assets=base/'assets';assets.mkdir(parents=True,exist_ok=True);prefix=assets/spec_hash[:24]
    height=100+82*(len(scene['rows'])+1) if scene['kind']=='table' else 680
    canvas=Canvas(960,height);_draw(scene,canvas);svg='\n'.join([*canvas.svg,'</svg>'])
    image=BytesIO();canvas.image.save(image,format='PNG');png=image.getvalue()
    for path,data in [(prefix.with_suffix('.svg'),svg.encode('utf-8')),(prefix.with_suffix('.png'),png)]:
        if path.exists() and path.read_bytes()!=data:raise ValueError('immutable mathematics asset differs: '+path.name)
        if not path.exists():path.write_bytes(data)
    provenance={'source':'generated_svg','rendererVersion':VERSION,'semanticSpec':scene,'specHash':spec_hash,
                'pngSha256':digest(prefix.with_suffix('.png')),'svgSha256':digest(prefix.with_suffix('.svg')),
                'visualEssentialStatus':'pending_local_semantic_review','width':960,'height':height,
                'description':scene.get('title','Diagram '+scene['kind'].replace('_',' '))}
    metadata=prefix.with_suffix('.json')
    if metadata.exists() and json.loads(metadata.read_text(encoding='utf-8'))!=provenance:raise ValueError('immutable mathematics provenance differs')
    if not metadata.exists():atomic_json(metadata,provenance)
    return prefix.with_suffix('.png').relative_to(base).as_posix(),provenance
