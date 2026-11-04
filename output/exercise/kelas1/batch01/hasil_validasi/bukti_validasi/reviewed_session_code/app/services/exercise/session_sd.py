"""Primary-school variations for the offline three-session authoring round.

The requested level chooses an authoring family only. ``assess`` judges the
finished problem and mathematical model without seeing a target or a quota.
Existing banks, assessment policies and immutable diagram renderers are reused.
"""
from copy import deepcopy
import hashlib
import json
import sympy as s

from . import sd_bank_low as low, sd_bank_high as high
from . import sd_review_additions as reviewed
from .sd_difficulty_review import assess as old_assess

POLICY = 'codex-primary-three-session-content-v1'


def semantic_identity(model):
    """Fingerprint mathematical facts and representations, not people/colours.

    Callers should scope this to a curriculum location: the same arithmetic
    model can legitimately teach different concepts in different subchapters.
    """
    ignored={'title','label','labels','unit_label','fill','color','colour',
             'expected','assessment','intended_level'}
    def facts(value):
        if isinstance(value,dict):return {k:facts(v) for k,v in value.items() if k not in ignored}
        if isinstance(value,list):return [facts(v) for v in value]
        return value
    payload={'family':model['kind'],'certificate':facts(model['certificate']),
             'scene':facts(model.get('scene'))}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,ensure_ascii=False).encode()).hexdigest()


def solve(cert):
    if cert['type'].startswith('sd_review'):
        return reviewed.solve_certificate(cert)
    if cert['type'].startswith('sd_low'):
        return low.solve_certificate(cert)
    return high.solve_certificate(cert)


def assess(model, grade):
    family = model['kind']; cert = model['certificate']; p = cert.get('inputs', {})
    reason = None
    shortcuts = {
        'sd_low_membilang_pindah_banding': (
            p.get('a') == p.get('b') or p.get('a') == p.get('t'), 'medium',
            'Jika awal kedua kelompok sama, selisih cukup dua kali perpindahan; jika A habis, hanya jumlah B yang perlu dihitung.'),
        'sd_low_banding_dua_perubahan': (
            p.get('g') == 2*p.get('t',-1), 'easy',
            'Tambahan pada selisih akibat perpindahan dibatalkan tepat oleh pemberian; cukup membandingkan dua jumlah awal.'),
        'sd_low_berat_pindah_tambah': (
            p.get('g') == 2*p.get('t',-1), 'easy',
            'Pengaruh perpindahan pada selisih dibatalkan oleh tambahan; selisih akhir sama dengan selisih awal.'),
        'sd_low_pasangan_ubah_banding': (
            p.get('n') == 2*p.get('a',-1), 'medium',
            'Kedua kelompok mula-mula sama banyak, sehingga selisih akhir cukup dua kali perpindahan.'),
        'sd_low_setengah_setelah_perubahan': (
            p.get('t') in (p.get('a'),p.get('b')), 'easy',
            'Jumlah yang diambil sama dengan satu kelompok lengkap; tinggal menentukan setengah kelompok lainnya.'),
        'sd_low_data_koreksi_kategori': (
            p.get('t') == p.get('g'), 'easy',
            'Kedua kategori bertambah sama banyak, sehingga selisihnya sama dengan selisih semula.'),
    }
    if family in shortcuts and shortcuts[family][0]:
        _,level,reason=shortcuts[family]
        return {'assessedLevel':level,'reason':reason,'flags':['numerical_shortcut'],
                'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,
                'apiCalls':0,'steps':{'easy':1,'medium':2}[level]}
    if family in {'sd_low_perbaiki_dua_pecahan_setengah','sd_low_perbaiki_dua_pecahan_seperempat'}:
        level='medium'
        reason='Target jumlah petak sama pada kedua kue dan terletak di antara kedua jumlah awal; dua perbaikan menyederhana menjadi selisih jumlah petak awal.'
        return {'assessedLevel':level,'reason':reason,'flags':['shared_target_cancellation'],
                'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,'apiCalls':0,'steps':2}
    if family in {'session_sd_units_read', 'session_sd_place_compose',
                  'session_sd_unit_fraction_groups', 'session_sd_fraction_quantity',
                  'session_sd_clock_minutes','session_sd_add_pair','session_sd_subtract_pair'}:
        level = 'easy'
        reason = 'Membaca satu representasi atau menentukan satu bagian sama besar melalui satu konsep langsung.'
    elif family == 'session_sd_identical_shape_property':
        props = {'triangle': (3,0), 'right_triangle': (3,1), 'square': (4,4),
                 'rectangle': (4,4), 'pentagon': (5,0), 'hexagon': (6,0)}
        assert int(p['p']) == props[cert['shape']][cert['property']]
        level = 'easy'
        reason = 'Semua bangun sejenis: gunakan satu sifat yang sudah dikenal dan satu perkalian langsung, tanpa penyaringan atau perubahan keadaan.'
    elif family == 'session_sd_compare_updated':
        # Both quantities must genuinely change before they are compared.
        if int(p['x']) == 0 or int(p['y']) == 0:
            level = 'medium'
        elif int(p['x']) == int(p['y']):
            level = 'easy'
            reason = 'Perubahan kedua kelompok sama besar sehingga saling menghapus dalam perbandingan.'
        else:
            level = 'hard'
        reason = reason or 'Perbarui dua keadaan yang berbeda, tentukan hasil masing-masing, kemudian bandingkan hasil akhirnya.'
    elif family == 'session_sd_two_fraction_repairs':
        assert p['n1']*p['k1'] != p['n2']*p['k2']
        assert 0<=p['a']<p['n1']*p['k1']/p['d']<p['n1']*p['k1']
        assert p['n2']*p['k2']/p['d']<p['b']<=p['n2']*p['k2']
        level='hard'
        reason='Tentukan target pecahan pada dua pembagian petak yang berbeda; satu kue perlu ditambah dan yang lain dikurangi, lalu gabungkan kedua perbaikan.'
    else:
        d = old_assess(model['question'], cert, family, grade, model.get('scene'))
        return {**d, 'policyVersion': POLICY, 'basePolicyVersion': d['policyVersion']}
    return {'assessedLevel': level, 'reason': reason, 'flags': [],
            'policyVersion': POLICY, 'confidenceScore': 0,
            'confidenceMeasured': False, 'apiCalls': 0,
            'steps': {'easy': 1, 'medium': 2, 'hard': 4}[level]}


def check_visual(model):
    # This implementation has no new certificate types: all evidence can be
    # checked by the retained arithmetic/geometry solvers and visual bindings.
    from scripts.generate_sd_bank_local import visual_check
    return visual_check(model)


def _make(q, expression, inputs, explanation, family, scene, bindings=(), cert=None):
    cert = cert or {'type': 'sd_low_expression', 'inputs': inputs,
                    'expression': expression}
    if bindings:
        cert['visual_bindings'] = [
            {'input': name, 'path': path} for name, path in bindings]
    value = solve(cert)
    candidates = ([1-value, value/2, (value+1)/2, s.Rational(1,3),
                   s.Rational(2,3), 1, 0] if 0 < value < 1 else
                  [value+1, value-1, value+2, value-2, value+3, value+4])
    wrong = []
    for n in candidates:
        n = s.simplify(n)
        if n < 0 or n == value or n in wrong:
            continue
        wrong.append(n)
        if len(wrong) == 3:
            break
    fmt = low._fmt
    return {'question': q, 'answer': fmt(value), 'wrong': list(map(fmt, wrong)),
            'explanation': explanation + ' Hasilnya ' + fmt(value) + '.',
            'kind': family, 'steps': 1, 'rationale': '',
            'scene': scene, 'certificate': cert}


def _representation(model, r):
    """Change the information representation, never just a name or a colour."""
    model = deepcopy(model); scene = model.get('scene')
    if not scene:
        return model
    bindings = model['certificate'].get('visual_bindings', [])
    variant = r.randrange(3)
    if scene['kind'] == 'cards' and variant == 1:
        model['scene'] = {'kind': 'table', 'headers': ['Keterangan', 'Nilai'],
                          'rows': [[v['label'], v['value']] for v in scene['cards']]}
        for b in bindings:
            if b['path'][:1] == ['cards'] and b['path'][-1] == 'value':
                b['path'] = ['rows', b['path'][1], 1]
        # The wording identifies the data source rather than inventing a
        # different context while keeping the same mathematical instance.
        wording = model['question']
        # Change the information source, not every physical-card noun. For
        # example, "memakai setiap kartu" must never become "setiap tabel".
        replacements = [
            ('kartu nilai tempat pada gambar', 'tabel nilai tempat pada gambar'),
            ('kartu angka pada gambar', 'angka pada tabel'),
            ('kartu P,Q,R pada gambar', 'baris P, Q, dan R pada tabel'),
            ('Kartu A dan B menyatakan', 'Baris A dan B pada tabel menyatakan'),
            ('kedua kartu', 'kedua baris tabel'),
            ('Kartu menunjukkan', 'Tabel menunjukkan'),
            ('kartu gambar', 'tabel pada gambar'),
            ('pada kartu', 'pada tabel'),
            ('memakai setiap kartu', 'memakai setiap angka'),
        ]
        for original, replacement in replacements:
            wording = wording.replace(original, replacement)
        model['question'] = wording
    elif scene['kind'] == 'groups' and all(g.get('shape') == 'circle' for g in scene['groups']) and variant:
        kind = 'pictogram' if variant == 1 else 'tally'
        model['scene'] = {'kind': kind, 'labels': [g['label'] for g in scene['groups']],
                          'values': [g['count'] for g in scene['groups']], 'unit': 1}
        for b in bindings:
            if b['path'][:1] == ['groups'] and b['path'][-1] == 'count':
                b['path'] = ['values', b['path'][1]]
    return model


def _place_easy(grade, r, visual):
    tens = 1 if grade == 1 else r.randint(1, 4)
    units = r.randint(0, 9); n = tens*10+units
    if r.randrange(2):
        scene = low._cards([tens, units], ['Ikatan sepuluh', 'Satuan lepas']) if visual else None
        intro = 'Gambar menunjukkan banyak ikatan sepuluh lidi dan lidi satuan lepas.' if visual else f'Ada {tens} ikatan sepuluh lidi dan {units} lidi lepas.'
        return _make(intro+' Berapa seluruh lidi?', '10*t+u', {'t':tens,'u':units},
                     f'Setiap ikatan berisi 10. Jumlah seluruh lidi {tens} kali 10 ditambah {units}.',
                     'session_sd_place_compose', scene,
                     [('t',['cards',0,'value']),('u',['cards',1,'value'])] if visual else [])
    scene = low._cards([n], ['Bilangan']) if visual else None
    intro = 'Baca bilangan pada gambar.' if visual else f'Perhatikan bilangan {n}.'
    return _make(intro+' Berapa satuan lepas jika lidi dikelompokkan menjadi ikatan sepuluh?',
                 'Mod(n,10)', {'n':n}, f'Pisahkan {tens} puluhan dan {units} satuan.',
                 'session_sd_units_read', scene, [('n',['cards',0,'value'])] if visual else [])


def _direct_operation(bab,code,r,visual):
    subtract=bab==3
    if subtract:
        a=r.randint(2,10);b=r.randint(1,a);expr='a-b'
        question='Sebanyak {b} benda diambil. Berapa benda yang tersisa?'.format(b=b)
        text=f'Mula-mula ada {a} benda.'
        scene=low._groups([a]) if visual else None
        binding=[('a',['groups',0,'count'])] if visual else []
        family='session_sd_subtract_pair';explanation=f'Kurangi {a} dengan {b}'
    else:
        a=r.randint(1,9);b=r.randint(1,10-a);expr='a+b'
        question='Kedua kelompok disatukan. Berapa jumlah seluruh benda?'
        text=f'Kelompok A berisi {a} benda dan kelompok B {b} benda.'
        scene=low._groups([a,b]) if visual else None
        binding=low._bind_groups(['a','b']) if visual else []
        family='session_sd_add_pair';explanation=f'Gabungkan {a} dengan {b}'
    intro='Banyak benda awal terlihat pada gambar.' if visual else text
    return _make(intro+' '+question,expr,{'a':a,'b':b},explanation,family,scene,binding)


def _fraction_quantity(code, r, visual):
    divisor = 4 if code == 'C' else 2
    # Concrete counts remain inside the primary two-digit number domain.
    # These fraction chapters precede the grade-two chapter introducing 100;
    # retain the already introduced whole-number bound of 50.
    part = r.randint(1, 12 if divisor == 4 else 25); total = divisor*part
    variant = r.randrange(2)
    if visual and variant:
        scene = low._groups([total]); binding=[('n',['groups',0,'count'])]
        intro = 'Benda pada gambar merupakan satu kumpulan utuh.'
    elif visual:
        scene = low._cards([total], ['Panjang pita (satuan)']); binding=[('n',['cards',0,'value'])]
        intro = 'Panjang satu pita utuh tercantum pada gambar.'
    else:
        scene = None; binding=[]; intro=f'Satu pita utuh panjangnya {total} satuan.'
    word = 'seperempat' if divisor == 4 else 'setengah'
    noun = 'benda' if visual and variant else 'satuan'
    return _make(intro+f' Berapa {noun} dalam {word} bagian utuh tersebut?',
                 'n/d', {'n':total,'d':divisor},
                 f'Bagilah {total} menjadi {divisor} bagian yang sama besar.',
                 'session_sd_fraction_quantity', scene, binding)


def _unit_fraction_easy(r, visual):
    den = r.randint(2,12)
    if r.randrange(2):
        scene = low._groups([1,den-1]) if visual else None
        intro = 'Semua benda di A dan B merupakan satu kumpulan utuh; hanya benda di A yang dipilih.' if visual else f'Satu kumpulan berisi {den} benda sama jenis. Hanya satu benda dipilih.'
        return _make(intro+' Berapa pecahan kumpulan yang dipilih?', 'a/(a+b)',
                     {'a':1,'b':den-1}, f'Seluruh benda {den}, yang dipilih satu.',
                     'session_sd_unit_fraction_groups', scene,
                     [('a',['groups',0,'count']),('b',['groups',1,'count'])] if visual else [])
    return high.generate(4,2,'A','easy',r,visual,1)


def _unit_fraction_hard(r, visual):
    den=r.randint(5,12);initial=r.randint(1,(den-1)//2)
    scene={'kind':'fraction_grid','rows':1,'cols':den,'shaded':initial} if visual else None
    intro='Satu benda dibagi menjadi bagian sama besar seperti pada gambar; beberapa bagian sudah diwarnai.' if visual else f'Satu benda dibagi {den} bagian sama besar, {initial} bagian sudah diwarnai.'
    cert={'type':'sd_review_fraction_minimum','inputs':{'denominator':den,'shaded':initial}}
    if visual:cert['visual_bindings']=[{'input':'denominator','path':['cols']},{'input':'shaded','path':['shaded']}]
    return _make(intro+' Bagian berwarna harus lebih banyak daripada bagian putih dan jumlah bagian berwarna harus genap. Berapa pecahan tambahan paling sedikit yang perlu diwarnai?',
                 None,{},f'Cari jumlah genap terkecil yang melebihi setengah {den}; kurangi {initial} bagian yang sudah berwarna, lalu nyatakan terhadap seluruh benda.',
                 'sd_review_fraction_minimum',scene,cert=cert)


def _updated_comparison(grade,bab,code,r,visual):
    cap=10 if grade==1 and bab in (1,2,3) else 19 if grade==1 else 50
    subtraction=bab==3 or grade==1 and bab==6 and code=='C' or grade==2 and bab==2 and code=='B'
    a=r.randint(4,cap);b=r.randint(4,cap)
    x=r.randint(1,min(3,a-1));y=r.choice([v for v in range(1,min(3,b-1)+1) if v!=x])
    if not subtraction:
        a=min(a,cap-x);b=min(b,cap-y)
    scene=low._groups([a,b]) if visual else None
    binding=low._bind_groups(['a','b']) if visual else []
    intro='Dua kelompok benda A dan B tampak pada gambar.' if visual else f'A mula-mula berisi {a} benda dan B {b} benda.'
    if subtraction:
        expr='Abs((a-x)-(b-y))';action=f'Dari A diambil {x} benda dan dari B diambil {y} benda.'
        explanation=f'A tersisa {a-x}, B tersisa {b-y}. Bandingkan kedua sisa tersebut'
    else:
        expr='Abs((a+x)-(b+y))';action=f'A mendapat {x} benda lagi, sedangkan B mendapat {y} benda lagi.'
        explanation=f'A menjadi {a+x}, B menjadi {b+y}. Bandingkan kedua hasil tersebut'
    return _make(intro+' '+action+' Berapa selisih banyak benda kedua kelompok pada akhir kegiatan?',
                 expr,{'a':a,'b':b,'x':x,'y':y},explanation,
                 'session_sd_compare_updated',scene,binding)


def _clock_easy(r, visual):
    hour=r.randint(1,11);minute=r.choice([0,30])
    scene={'kind':'clock','hour':hour,'minute':minute} if visual else None
    intro='Perhatikan jam pada gambar.' if visual else f'Jam menunjukkan pukul {hour:02d}.{minute:02d}.'
    return _make(intro+f' Berapa menit telah lewat sejak pukul {hour:02d}.00?',
                 'm',{'m':minute},f'Jarum panjang menunjukkan {minute} menit sejak jam penuh.',
                 'session_sd_clock_minutes',scene,[('m',['minute'])] if visual else [])


def _two_fraction_repairs(code,r,visual):
    divisor=4 if code=='C' else 2
    k1,k2=r.sample(range(2,6),2);n1=n2=divisor
    total1=n1*k1;total2=n2*k2
    a=r.randrange(k1);b=r.randint(k2+1,total2)
    scene={'kind':'panels','panels':[
        {'kind':'fraction_grid','rows':n1,'cols':k1,'shaded':a,'title':'Kue A'},
        {'kind':'fraction_grid','rows':n2,'cols':k2,'shaded':b,'title':'Kue B'}]} if visual else None
    intro='Kue A dan B pada gambar mempunyai pembagian petak berbeda. Pada masing-masing kue, semua petak sama luas.' if visual else f'Kue A dibagi {total1} petak sama luas dan {a} petak berwarna. Kue B dibagi {total2} petak sama luas dan {b} petak berwarna.'
    word='seperempat' if divisor==4 else 'setengah'
    binding=[('a',['panels',0,'shaded']),('b',['panels',1,'shaded']),
             ('n1',['panels',0,'rows']),('k1',['panels',0,'cols']),
             ('n2',['panels',1,'rows']),('k2',['panels',1,'cols'])] if visual else []
    return _make(intro+f' Agar masing-masing tepat {word} berwarna, petak putih boleh diwarnai atau warna petak boleh dihapus. Berapa jumlah petak paling sedikit yang harus diubah pada kedua kue?',
                 'Abs(n1*k1/d-a)+Abs(b-n2*k2/d)',
                 {'n1':n1,'k1':k1,'n2':n2,'k2':k2,'a':a,'b':b,'d':divisor},
                 f'Target A {k1} petak, sehingga tambah {k1-a}. Target B {k2} petak, sehingga hapus {b-k2}. Jumlahkan kedua perubahan',
                 'session_sd_two_fraction_repairs',scene,binding)


def _shape_easy(grade,code,r,visual):
    prop=1 if grade==3 and code=='B' else 0
    pool=['square','rectangle','right_triangle'] if prop else ['triangle','square','rectangle','pentagon','hexagon']
    shape=r.choice(pool);count=r.randint(2,9)
    props={'triangle':(3,0),'right_triangle':(3,1),'square':(4,4),'rectangle':(4,4),'pentagon':(5,0),'hexagon':(6,0)}
    words={'triangle':'segitiga','right_triangle':'segitiga siku-siku','square':'persegi','rectangle':'persegi panjang','pentagon':'segi lima','hexagon':'segi enam'}
    scene={'kind':'groups','groups':[{'label':'A','count':count,'shape':shape}]} if visual else None
    intro='Perhatikan kumpulan bangun sejenis pada gambar.' if visual else f'Ada {count} bangun {words[shape]} yang terpisah.'
    noun='sudut siku-siku' if prop else 'sisi';per=props[shape][prop]
    model=_make(intro+f' Berapa jumlah {noun} pada semua bangun tersebut?',
                'n*p',{'n':count,'p':per},f'Satu {words[shape]} mempunyai {per} {noun}. Ada {count} bangun terpisah, jadi hitung {count} kali {per}',
                'session_sd_identical_shape_property',scene,[('n',['groups',0,'count'])] if visual else [])
    model['certificate'].update(shape=shape,property=prop)
    return model


def generate(name,bab,code,level,r,visual,index):
    grade=int(str(name).split('_')[0].replace('kelas',''))
    assert 1<=grade<=4
    base=low.generate if grade<=2 else high.generate
    # Alternate reviewed representations and authoring families; choosing a
    # family cannot force the assessment of its actual numerical instance.
    for attempt in range(8):
        if grade<=2 and ((grade==1 and bab==5 and code=='C') or (grade==2 and bab==1 and code=='B')) and level=='easy':
            model=_place_easy(grade,r,visual)
        elif grade==1 and bab in (2,3) and level=='easy' and r.randrange(2):
            model=_direct_operation(bab,code,r,visual)
        elif grade==2 and bab==5 and code in 'AC' and level=='easy' and r.randrange(2):
            model=_fraction_quantity(code,r,visual)
        elif grade==2 and bab==5 and code in 'AC' and level=='hard':
            model=_two_fraction_repairs(code,r,visual)
        elif grade==4 and bab==2 and code=='A' and level=='easy':
            model=_unit_fraction_easy(r,visual)
        elif grade==4 and bab==2 and code=='A' and level=='hard':
            model=_unit_fraction_hard(r,visual)
        elif grade<=2 and level=='hard' and ((grade==1 and (bab in (2,3) or bab==6 and code in 'BC')) or (grade==2 and bab==2)) and r.randrange(2):
            model=_updated_comparison(grade,bab,code,r,visual)
        elif grade==2 and bab==6 and code=='B' and level=='easy' and r.randrange(2):
            model=_clock_easy(r,visual)
        elif level=='easy' and ((grade==3 and bab==4 and code in 'AB') or (grade==4 and bab==5 and code=='A')) and r.randrange(2):
            model=_shape_easy(grade,code,r,visual)
        else:
            factory=reviewed.generate if r.randrange(2) else base
            model=factory(grade,bab,code,level,r,visual,index)
        if model is None:
            continue
        model=_representation(model,r) if visual else model
        d=assess(model,grade)
        if d['assessedLevel']!=level:
            continue
        if visual:
            try:
                check_visual(model)
            except (AssertionError, ValueError, ZeroDivisionError):
                continue
        model.update(assessment=d,steps=d['steps'],rationale=d['reason'])
        return model
    return None
