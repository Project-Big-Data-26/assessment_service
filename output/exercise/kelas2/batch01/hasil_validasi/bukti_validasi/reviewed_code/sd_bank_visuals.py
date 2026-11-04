"""Local SD diagrams with one geometry stream for PNG and retained SVG.

The scene describes visible facts, never an answer or a difficulty label.
Assets are content-addressed, immutable, and do not require any network service.
"""
from __future__ import annotations

from html import escape
from io import BytesIO
import hashlib
import json
import math
from pathlib import Path
import re
from typing import Any

from PIL import Image, ImageDraw, ImageFont

from .workflow import atomic_json, digest

VERSION = "sd-scenes-v1"
KINDS = {"groups", "cards", "table", "fraction", "fraction_grid", "grid", "area_grid",
         "volume_blocks", "chart", "bars", "bar_chart", "pictogram", "tally", "ruler",
         "numberline", "pattern", "shapes", "lines", "clock", "balance", "panels"}
INK = "#172b40"
BLUE = "#b8daf0"
COLORS = ["#b8daf0", "#ffd49b", "#bee7c8", "#e4c8ef", "#ffc7c7", "#c9d5ff"]


def _integer(value: Any, minimum: int, maximum: int, name: str) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise ValueError(f"{name} must be an integer in {minimum}..{maximum}")
    return value


def validate_scene(scene: dict) -> dict:
    if not isinstance(scene, dict) or scene.get("kind") not in KINDS:
        raise ValueError("unknown SD scene kind")
    encoded = json.dumps(scene, ensure_ascii=False, allow_nan=False)
    if len(encoded) > 30000 or any(k in scene for k in ("answer", "correct_answer", "jawaban_benar")):
        raise ValueError("scene is too large or contains an answer key")
    kind = scene["kind"]
    if kind == "groups":
        groups = scene.get("groups", [])
        if not 1 <= len(groups) <= 6: raise ValueError("groups need 1..6 visible groups")
        for group in groups:
            count = _integer(group["count"], 0, 100, "count")
            _integer(group.get("crossed", 0), 0, count, "crossed")
    elif kind in {"fraction", "fraction_grid", "grid", "area_grid"}:
        rows = _integer(scene.get("rows", 1), 1, 12, "rows")
        cols = _integer(scene.get("cols", scene.get("denominator", 4)), 1, 20, "cols")
        _integer(scene.get("shaded", scene.get("numerator", 0)), 0, rows*cols, "shaded")
        if any(len(v) != 2 or not (0 <= v[0] < rows and 0 <= v[1] < cols) for v in scene.get("cells", [])):
            raise ValueError("highlighted cells must be inside the grid")
    elif kind == "volume_blocks":
        for key in ("length", "width", "height"):_integer(scene[key], 1, 10, key)
    elif kind in {"chart", "bars", "bar_chart", "pictogram", "tally"}:
        values = scene.get("values", [])
        if not 1 <= len(values) <= 8 or len(values) != len(scene.get("labels", [])):
            raise ValueError("charts need 1..8 equally many labels and values")
        for value in values:
            if isinstance(value, bool) or not isinstance(value, (float, int)) or not 0 <= value <= 10000:
                raise ValueError("chart values must be nonnegative finite counts")
        unit = scene.get("unit", 1)
        if not isinstance(unit, (float, int)) or unit <= 0:raise ValueError("pictogram unit must be positive")
        if kind in {"pictogram", "tally"} and any(v != int(v) for v in values):
            raise ValueError("tallies and pictograms require whole counts")
    elif kind in {"numberline", "ruler"}:
        start,end,step = scene.get("start",0),scene.get("end",10),scene.get("step",1)
        if not all(isinstance(v,(float,int)) and not isinstance(v,bool) for v in [start,end,step]):raise ValueError("numeric ruler limits required")
        if end <= start or step <= 0 or (end-start)/step > 30:raise ValueError("ruler needs increasing bounds and at most 31 ticks")
        for key in ["object_start","object_end"]:
            if key in scene and not start <= scene[key] <= end:raise ValueError("ruler object endpoint lies outside the scale")
    elif kind == "clock":
        _integer(scene.get("hour",0), 0, 23, "hour");_integer(scene.get("minute",0), 0, 59, "minute")
    elif kind == "table":
        headers = scene.get("headers",[]);rows=scene.get("rows",[])
        if not 1 <= len(headers) <= 8 or not 1 <= len(rows) <= 20 or any(len(row)!=len(headers) for row in rows):
            raise ValueError("table needs 1..8 columns and rectangular 1..20 rows")
    elif kind == "cards":
        if not 1 <= len(scene.get('cards',[])) <= 16:raise ValueError('cards need 1..16 values')
    elif kind == "pattern":
        if not 1 <= len(scene.get('items',[])) <= 24:raise ValueError('pattern needs 1..24 items')
    elif kind == "shapes":
        if not 1 <= len(scene.get('items',[])) <= 12:raise ValueError('shapes need 1..12 items')
    elif kind == "panels":
        if not 1 <= len(scene.get("panels",[])) <= 4:raise ValueError("panels need 1..4 children")
        for child in scene["panels"]:
            if child.get("kind")=="panels":raise ValueError("nested panels are not supported")
            validate_scene(child)
    return scene


def _font(size):
    for path in ("C:/Windows/Fonts/arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        if Path(path).is_file():return ImageFont.truetype(path,size)
    return ImageFont.load_default(size=size)


def _plain(value):
    value=str(value).replace("$", "")
    value=re.sub(r"\\(?:d?frac)\{([^{}]+)\}\{([^{}]+)\}",r"\1/\2",value)
    return value.replace(r"\times","×").replace(r"\div","÷").replace("^{2}","²").replace("^{3}","³")


class Canvas:
    def __init__(self,width,height):
        self.width,self.height=width,height
        self.image=Image.new("RGB",(width,height),"white");self.draw=ImageDraw.Draw(self.image)
        self.svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">','<rect width="100%" height="100%" fill="white"/>']

    def text(self,x,y,value,size=27,width=None,fill=INK):
        value=_plain(value)
        while width and self.draw.textlength(value,font=_font(size))>width and size>18:size-=1
        if width and self.draw.textlength(value,font=_font(size))>width:
            words=value.split();lines=[];line=""
            for word in words:
                candidate=(line+" "+word).strip()
                if line and self.draw.textlength(candidate,font=_font(size))>width:lines.append(line);line=word
                else:line=candidate
            if line:lines.append(line)
        else:lines=[value]
        if len(lines)>3:raise ValueError("diagram label is too long")
        for i,line in enumerate(lines):
            yy=y+(i-(len(lines)-1)/2)*(size+4)
            box=self.draw.textbbox((x,yy),line,font=_font(size),anchor="mm")
            if min(box)<-2 or box[2]>self.width+2 or box[3]>self.height+2:raise ValueError("diagram text would be clipped")
            self.draw.text((x,yy),line,font=_font(size),fill=fill,anchor="mm")
            self.svg.append(f'<text x="{x}" y="{yy}" text-anchor="middle" dominant-baseline="central" font-family="Arial, sans-serif" font-size="{size}" fill="{fill}">{escape(line)}</text>')

    def line(self,x1,y1,x2,y2,width=3,fill=INK):
        self.draw.line((x1,y1,x2,y2),fill=fill,width=width)
        self.svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{fill}" stroke-width="{width}"/>')

    def rect(self,x,y,w,h,fill=BLUE,outline=INK,width=3):
        self.draw.rectangle((x,y,x+w,y+h),fill=fill,outline=outline,width=width)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{outline}" stroke-width="{width}"/>')

    def ellipse(self,x,y,w,h,fill=BLUE,outline=INK,width=3):
        self.draw.ellipse((x,y,x+w,y+h),fill=fill,outline=outline,width=width)
        self.svg.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill or "none"}" stroke="{outline}" stroke-width="{width}"/>')

    def polygon(self,points,fill=BLUE,outline=INK,width=3):
        self.draw.polygon(points,fill=fill);self.draw.line([*points,points[0]],fill=outline,width=width)
        self.svg.append(f'<polygon points="{" ".join(str(x)+","+str(y) for x,y in points)}" fill="{fill}" stroke="{outline}" stroke-width="{width}"/>')

    def shape(self,x,y,shape="circle",radius=17,fill=BLUE):
        if shape in {"circle","apple","ball","sphere"}:self.ellipse(x-radius,y-radius,2*radius,2*radius,fill)
        elif shape in {"square","box","cube"}:self.rect(x-radius,y-radius,2*radius,2*radius,fill)
        elif shape=="triangle":self.polygon([(x,y-radius-3),(x-radius-2,y+radius),(x+radius+2,y+radius)],fill)
        elif shape=="right_triangle":self.polygon([(x-radius,y-radius),(x-radius,y+radius),(x+radius,y+radius)],fill)
        elif shape=="?":self.text(x,y,"?",size=34)
        else:self.shape(x,y,"circle",radius,fill)


def _dimensions(scene):
    kind=scene['kind']
    if kind=='groups':return 960,110+sum(max(1,math.ceil(g['count']/12))*60+65 for g in scene['groups'])
    if kind=='table':return 960,100+84*(len(scene['rows'])+1)
    if kind in {'chart','bars','bar_chart'}:return 960,570
    if kind in {'pictogram','tally'}:
        groups=max(math.ceil(max(scene['values'],default=0)/scene.get('unit',1)/14),1)
        return 960,140+len(scene['values'])*(60*groups+50)
    if kind=='cards':return 960,100+140*math.ceil(len(scene.get('cards',[]))/4)
    if kind=='pattern':return 960,110+140*math.ceil(len(scene.get('items',[]))/8)
    if kind=='shapes':return 960,110+330*math.ceil(len(scene.get('items',[]))/3)
    if kind in {'grid','area_grid','fraction','fraction_grid'}:return 960,150+min(65,760/scene.get('cols',scene.get('denominator',4)))*scene.get('rows',1)
    if kind=='panels':return 960,sum(_dimensions(child)[1] for child in scene['panels'])
    return 960,510


def _draw(scene,canvas,offset_y=0):
    kind=scene['kind'];c=canvas;top=offset_y+75
    if scene.get('title'):c.text(480,offset_y+30,scene['title'],size=27,width=890)
    if kind=='panels':
        position=offset_y
        for child in scene['panels']:_draw(child,c,position);position+=_dimensions(child)[1]
    elif kind=='groups':
        y=top
        for i,g in enumerate(scene['groups']):
            c.text(72,y+16,g.get('label',chr(65+i)),size=26,width=125)
            n=g['count'];crossed=g.get('crossed',0)
            for index in range(n):
                xx=175+index%12*61;yy=y+index//12*60
                c.shape(xx,yy,g.get('shape','circle'),17,COLORS[i%len(COLORS)])
                if index>=n-crossed:c.line(xx-16,yy-17,xx+16,yy+17,4);c.line(xx+16,yy-17,xx-16,yy+17,4)
            if n==0:c.text(350,y,'Tidak ada benda',size=25)
            y+=max(1,math.ceil(n/12))*60+65
    elif kind=='cards':
        for i,card in enumerate(scene.get('cards',[])):
            card=card if isinstance(card,dict) else {'value':card}
            xx=30+(i%4)*234;yy=top+(i//4)*140
            c.rect(xx,yy,210,102,fill=COLORS[i%len(COLORS)])
            c.text(xx+105,yy+38,card.get('value','?'),size=34,width=190)
            if card.get('label') is not None:c.text(xx+105,yy+79,card['label'],size=22,width=190)
    elif kind=='table':
        data=[scene['headers'],*scene['rows']];cw=880/len(data[0]);left=40
        for row,values in enumerate(data):
            for col,value in enumerate(values):
                xx=left+col*cw;yy=top+row*84
                c.rect(xx,yy,cw,84,fill=BLUE if row==0 else 'white',width=2)
                c.text(xx+cw/2,yy+42,value,size=26,width=cw-14)
    elif kind in {'fraction','fraction_grid','grid','area_grid'}:
        rows=scene.get('rows',1);cols=scene.get('cols',scene.get('denominator',4));cell=min(65,760/cols)
        left=(960-cols*cell)/2;shaded=scene.get('shaded',scene.get('numerator',0));cells={tuple(v) for v in scene.get('cells',[])}
        for row in range(rows):
            for col in range(cols):
                chosen=(row,col) in cells if 'cells' in scene else row*cols+col<shaded
                c.rect(left+col*cell,top+row*cell,cell,cell,fill=BLUE if chosen else 'white',width=2)
        if scene.get('cell_label'):c.text(480,top+rows*cell+40,scene['cell_label'],size=25)
    elif kind in {'chart','bars','bar_chart'}:
        labels=scene['labels'];values=scene['values'];n=len(values);maximum=max(max(values,default=1),1)
        step=max(1,math.ceil(maximum/5));upper=step*math.ceil(maximum/step);left=95;bottom=top+355
        for val in range(0,upper+1,step):
            yy=bottom-val/upper*310;c.line(left,yy,915,yy,1,'#d6dce3');c.text(55,yy,str(val),size=23,width=65)
        c.line(left,bottom,left,top+40);c.line(left,bottom,920,bottom)
        for i,(label,value) in enumerate(zip(labels,values)):
            width=780/n;xx=left+18+i*width;bar_h=value/upper*310
            c.rect(xx,bottom-bar_h,width-30,bar_h,fill=COLORS[i%len(COLORS)],width=2)
            if scene.get('show_values',True):c.text(xx+(width-30)/2,bottom-bar_h-19,value,size=24,width=width-12)
            c.text(xx+(width-30)/2,bottom+38,label,size=24,width=width-10)
    elif kind in {'pictogram','tally'}:
        y=top;unit=scene.get('unit',1)
        for row,(label,value) in enumerate(zip(scene['labels'],scene['values'])):
            c.text(85,y+5,label,size=24,width=140)
            if kind=='pictogram':
                full=int(value//unit);partial=value/unit-full
                if full>150:raise ValueError('pictogram is too dense; choose a larger legend unit')
                total=full+bool(partial)
                for i in range(total):
                    xx=195+i%14*50;yy=y+i//14*60
                    if i<full:c.shape(xx,yy,scene.get('shape','circle'),16,COLORS[row%len(COLORS)])
                    else:
                        if partial!=0.5:raise ValueError('only half-symbol fractions are supported')
                        fill=COLORS[row%len(COLORS)]
                        c.draw.pieslice((xx-16,yy-16,xx+16,yy+16),90,270,fill=fill)
                        c.svg.append(f'<path d="M {xx} {yy-16} A 16 16 0 0 0 {xx} {yy+16} Z" fill="{fill}"/>')
                        c.ellipse(xx-16,yy-16,32,32,fill=None)
                y+=max(1,math.ceil(total/14))*60+50
            else:
                if value>100:raise ValueError('tally is too dense')
                for i in range(int(value)):
                    block=i//5;member=i%5;xx=190+block%10*70;yy=y+block//10*65
                    if member<4:c.line(xx+member*12,yy-20,xx+member*12,yy+20,3)
                    else:c.line(xx-4,yy+15,xx+40,yy-15,3)
                y+=max(1,math.ceil(value/50))*65+50
        if kind=='pictogram':c.text(480,y-10,f'Satu simbol utuh mewakili {unit} {scene.get("unit_label","benda")}.',size=24,width=870)
    elif kind in {'numberline','ruler'}:
        start,end,step=scene.get('start',0),scene.get('end',10),scene.get('step',1);left=90;right=880;yy=top+205
        project=lambda value:left+(value-start)/(end-start)*(right-left)
        c.line(left,yy,right,yy,4)
        marks=scene.get('marks',[]);hide=set(scene.get('hide_labels',[]))
        for i in range(math.floor((end-start)/step+1e-8)+1):
            value=start+i*step;xx=project(value);c.line(xx,yy-12,xx,yy+12,3)
            if value not in hide:c.text(xx,yy+38,int(value) if value==int(value) else value,size=24,width=max(35,(right-left)/max(1,(end-start)/step)-3))
        for i,mark in enumerate(marks):
            xx=project(mark['value']);c.line(xx,yy-15,xx,yy-85,4);c.text(xx,yy-110,mark.get('label',chr(65+i)),size=27)
        if kind=='ruler' and 'object_start' in scene and 'object_end' in scene:
            aa,bb=project(scene['object_start']),project(scene['object_end']);c.rect(min(aa,bb),yy-105,abs(bb-aa),38,fill='#ffd49b')
            c.text(480,yy+100,scene.get('unit','cm'),size=26)
    elif kind=='pattern':
        for i,item in enumerate(scene.get('items',[])):
            xx=75+i%8*115;yy=top+45+i//8*140
            if isinstance(item,dict):c.shape(xx,yy,item.get('shape','circle'),23,item.get('color',BLUE))
            elif item in {'circle','square','triangle','?'}:c.shape(xx,yy,item,23,COLORS[i%3] if scene.get('vary_color') else BLUE)
            else:c.text(xx,yy,item,size=32,width=100)
    elif kind=='volume_blocks':
        length,width,height=scene['length'],scene['width'],scene['height'];scale=min(38,650/(length+width),300/(height+width*0.45));ox=260;oy=top+340
        def p(i,j,k):return (ox+(i-j*0.65)*scale,oy-(k+j*0.45)*scale)
        c.polygon([p(0,0,height),p(length,0,height),p(length,width,height),p(0,width,height)],fill='#e2f0fb',width=2)
        c.polygon([p(0,0,0),p(0,width,0),p(0,width,height),p(0,0,height)],fill='#85b6da',width=2)
        c.polygon([p(0,0,0),p(length,0,0),p(length,0,height),p(0,0,height)],fill=BLUE,width=2)
        for i in range(1,length):
            c.line(*p(i,0,0),*p(i,0,height),2);c.line(*p(i,0,height),*p(i,width,height),2)
        for j in range(1,width):
            c.line(*p(0,j,0),*p(0,j,height),2);c.line(*p(0,j,height),*p(length,j,height),2)
        for k in range(1,height):
            c.line(*p(0,0,k),*p(length,0,k),2);c.line(*p(0,0,k),*p(0,width,k),2)
        c.text(650,top+90,f'Panjang: {length} kubus',size=25,width=340);c.text(650,top+145,f'Lebar: {width} kubus',size=25,width=340);c.text(650,top+200,f'Tinggi: {height} kubus',size=25,width=340)
    elif kind=='clock':
        cx,cy,r=480,top+185,165;c.ellipse(cx-r,cy-r,2*r,2*r,fill='white',width=4)
        for number in range(1,13):
            angle=math.radians(number*30-90);c.text(cx+135*math.cos(angle),cy+135*math.sin(angle),number,size=27)
        for angle,length,thick in [(scene['minute']*6-90,115,5),((scene['hour']%12)*30+scene['minute']/2-90,80,9)]:
            rad=math.radians(angle);c.line(cx,cy,cx+length*math.cos(rad),cy+length*math.sin(rad),thick)
        c.ellipse(cx-6,cy-6,12,12,fill=INK)
    elif kind=='balance':
        left=scene.get('left','?');right=scene.get('right','?');yy=top+140
        c.line(200,yy,760,yy,6);c.polygon([(480,yy),(430,yy+150),(530,yy+150)],fill='#dce9f2')
        for xx,value in [(245,left),(715,right)]:
            c.line(xx,yy,xx-100,yy+100);c.line(xx,yy,xx+100,yy+100);c.line(xx-100,yy+100,xx+100,yy+100,5)
            c.rect(xx-75,yy+35,150,60,fill=BLUE);c.text(xx,yy+65,value,size=26,width=135)
        if scene.get('unit'):c.text(480,yy+220,scene['unit'],size=26)
    elif kind=='lines':
        segments=scene.get('segments',[]);points=[p for seg in segments for p in seg]
        if not points:raise ValueError('lines need segments')
        xmin=min(p[0] for p in points);xmax=max(p[0] for p in points);ymin=min(p[1] for p in points);ymax=max(p[1] for p in points)
        sx=650/max(xmax-xmin,1);sy=280/max(ymax-ymin,1);scale=min(sx,sy)
        project=lambda p:(150+(p[0]-xmin)*scale,top+320-(p[1]-ymin)*scale)
        for i,seg in enumerate(segments):
            p,q=map(project,seg);c.line(*p,*q,4)
            if i<len(scene.get('labels',[])):c.text(q[0]+25,q[1]-20,scene['labels'][i],size=25)
    elif kind=='shapes':
        for i,item in enumerate(scene.get('items',[])):
            x=165+(i%3)*315;y=top+125+(i//3)*330;shape=item.get('shape','rectangle');w=180;h=120
            if shape=='circle':c.ellipse(x-70,y-70,140,140,fill=COLORS[i%6])
            elif shape=='square':c.rect(x-65,y-65,130,130,fill=COLORS[i%6])
            elif shape=='rectangle':c.rect(x-w/2,y-h/2,w,h,fill=COLORS[i%6])
            elif shape=='triangle':c.polygon([(x,y-70),(x-85,y+65),(x+85,y+65)],fill=COLORS[i%6])
            elif shape=='right_triangle':c.polygon([(x-80,y-65),(x-80,y+65),(x+85,y+65)],fill=COLORS[i%6])
            elif shape in {'rhombus','diamond'}:c.polygon([(x,y-75),(x+85,y),(x,y+75),(x-85,y)],fill=COLORS[i%6])
            elif shape=='parallelogram':c.polygon([(x-55,y-60),(x+90,y-60),(x+55,y+60),(x-90,y+60)],fill=COLORS[i%6])
            elif shape=='trapezoid':c.polygon([(x-50,y-60),(x+50,y-60),(x+95,y+60),(x-95,y+60)],fill=COLORS[i%6])
            elif shape in {'pentagon','hexagon','octagon'}:
                count={'pentagon':5,'hexagon':6,'octagon':8}[shape];c.polygon([(x+77*math.cos(2*math.pi*j/count-math.pi/2),y+77*math.sin(2*math.pi*j/count-math.pi/2)) for j in range(count)],fill=COLORS[i%6])
            elif shape in {'cube','cuboid'}:
                ww=120 if shape=='cube' else 175;hh=120;c.rect(x-ww/2,y-hh/2,ww,hh,fill=COLORS[i%6]);c.polygon([(x-ww/2,y-hh/2),(x-ww/2+35,y-hh/2-35),(x+ww/2+35,y-hh/2-35),(x+ww/2,y-hh/2)],fill='#e2f0fb');c.polygon([(x+ww/2,y-hh/2),(x+ww/2+35,y-hh/2-35),(x+ww/2+35,y+hh/2-35),(x+ww/2,y+hh/2)],fill='#85b6da')
            elif shape=='sphere':
                c.ellipse(x-70,y-70,140,140,fill=COLORS[i%6]);c.ellipse(x-70,y-22,140,44,fill=COLORS[i%6],outline='#52728c',width=2)
            elif shape=='cylinder':
                c.rect(x-60,y-55,120,110,fill=COLORS[i%6]);c.ellipse(x-60,y+35,120,40,fill=COLORS[i%6]);c.ellipse(x-60,y-75,120,40,fill='#e2f0fb')
            elif shape=='cone':
                c.polygon([(x,y-80),(x-65,y+60),(x+65,y+60)],fill=COLORS[i%6]);c.ellipse(x-65,y+40,130,40,fill=COLORS[i%6])
            elif shape=='polygon' and item.get('points'):
                points=item['points'];xs=[p[0] for p in points];ys=[p[1] for p in points];sc=min(180/max(max(xs)-min(xs),1),140/max(max(ys)-min(ys),1))
                c.polygon([(x+(xx-(max(xs)+min(xs))/2)*sc,y-(yy-(max(ys)+min(ys))/2)*sc) for xx,yy in points],fill=COLORS[i%6])
            else:raise ValueError('unsupported geometric shape '+shape)
            if item.get('label') is not None:c.text(x,y+113,item['label'],size=27,width=280)
            if item.get('show_dimensions'):
                if 'length' in item:c.text(x,y-110,str(item['length'])+' '+item.get('unit','cm'),size=25,width=230)
                if 'width' in item:c.text(x,y+78,str(item['width'])+' '+item.get('unit','cm'),size=25,width=230)


def render_scene(scene: dict, base: Path):
    scene=validate_scene(scene);payload=json.loads(json.dumps(scene,ensure_ascii=False))
    checksum=hashlib.sha256(json.dumps({'renderer':VERSION,'scene':payload},sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    assets=Path(base)/'assets';assets.mkdir(parents=True,exist_ok=True);prefix=assets/checksum[:24]
    width,height=_dimensions(scene);canvas=Canvas(width,int(math.ceil(height)));_draw(scene,canvas)
    svg='\n'.join([*canvas.svg,'</svg>']);stream=BytesIO();canvas.image.save(stream,format='PNG');png=stream.getvalue()
    for destination,content in [(prefix.with_suffix('.svg'),svg.encode()),(prefix.with_suffix('.png'),png)]:
        if destination.exists():
            if destination.read_bytes()!=content:raise ValueError('immutable SD visual differs')
        else:destination.write_bytes(content)
    provenance={'source':'generated_svg','rendererVersion':VERSION,'semanticSpec':payload,'specHash':checksum,
                'pngSha256':digest(prefix.with_suffix('.png')),'svgSha256':digest(prefix.with_suffix('.svg')),
                'visualEssentialStatus':'pending_local_semantic_review','width':width,'height':canvas.height,
                'description':'Diagram '+scene['kind']+': '+json.dumps(payload,ensure_ascii=False,sort_keys=True)}
    meta=prefix.with_suffix('.json')
    if meta.exists():
        if json.loads(meta.read_text(encoding='utf-8'))!=provenance:raise ValueError('immutable SD visual metadata differs')
    else:atomic_json(meta,provenance)
    return prefix.with_suffix('.png').relative_to(base).as_posix(),provenance
