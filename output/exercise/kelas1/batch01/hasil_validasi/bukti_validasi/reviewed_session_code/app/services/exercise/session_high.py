"""Local session-bank candidates with explicit curriculum/content judgements."""
from __future__ import annotations
import ast
from copy import deepcopy
import re
import sympy as s

from . import session_high_basic as basic
from .session_high_trace import capture,solve as solve_recipe
from .targeted_math import solve_certificate as solve_targeted
from .replenishment_math import m,numeric

POLICY='codex-session-content-v3'


def _iter_strings(value,path=()):
    if isinstance(value,str):yield path,value
    elif isinstance(value,list):
        for i,t in enumerate(value):yield from _iter_strings(t,path+(i,))
    elif isinstance(value,dict):
        for key,t in value.items():
            if key not in {'type','variables','positive','aggregate','mode'}:yield from _iter_strings(t,path+(key,))


def _at(root,path):
    for key in path:root=root[key]
    return root


def _put(root,path,value):
    for key in path[:-1]:root=root[key]
    root[path[-1]]=value


def solve(cert):
    kind=cert['type']
    if kind.startswith('session_basic'):return basic.solve(cert)
    if kind=='session_expression':return solve_recipe(cert)
    if kind.startswith('session_sma'):
        from .session_high_sma import solve as sma_solve
        return sma_solve(cert)
    if kind=='session_targeted_visual':
        base=deepcopy(cert['base']);path=cert['replace_path'];old=cert['original'];new=cert['inputs']['visible'];power=cert.get('power',1)
        class Replace(ast.NodeTransformer):
            def visit_Constant(self,node):return ast.Constant(new**power) if type(node.value) is int and node.value==old else node
        tree=Replace().visit(ast.parse(_at(base,path),mode='eval'));ast.fix_missing_locations(tree);_put(base,path,ast.unparse(tree.body))
        return solve(base)
    if kind=='session_parameter_visual':
        base=deepcopy(cert['base']);base['inputs'][cert['parameter']]=cert['inputs']['visible'];return solve(base)
    if kind=='session_finite_factor_pairs':
        p=cert['inputs'];product=p['gcd']*p['lcm'];pairs=[(a,product//a) for a in s.divisors(product) if a<=product//a<=p['limit'] and a<=p['cap'] and s.gcd(a,product//a)==p['gcd']]
        assert pairs;return s.Integer(max(a+b for a,b in pairs))
    if kind=='session_common_bags':
        p=cert['inputs'];ks=[n for n in range(1,p['cap']+1) if p['fruit_a']%n==p['fruit_b']%n==0]
        return s.Rational(p['fruit_a']+p['fruit_b'],max(ks))
    if kind=='session_bar_reallocate':
        p=cert['inputs'];values=[p['a']-p['move'],p['b']+p['move'],p['c']+p['extra']]
        return s.Integer(max(values)-min(values))
    if kind=='session_data_audit':
        p=cert['inputs'];correct_total=p['reported']-p['duplicate']+p['missing'];return s.Integer(correct_total-p['other'])
    if kind=='session_scientific_inverse':
        p=cert['inputs'];a=s.Rational(p['first'],10)**p['power_a'];b=s.Rational(p['second'],10)**p['power_b'];return s.simplify(a/b*10**p['exponent'])
    if kind=='session_geometry_shared':
        p=cert['inputs'];width=p['outer']/2-p['length_a']-p['length_b'];return s.Rational(2*(p['length_a']+width))
    if kind=='session_45_pythagoras':
        p=cert['inputs'];a=s.sympify(p['perimeter'])/(2+s.sqrt(2));return s.simplify(a*a/2-p['removed'])
    if kind=='session_distance_ratio':
        p=cert['inputs'];distance=s.sqrt(p['dx']**2+p['dy']**2);return s.simplify(distance*(p['ratio_a']+p['ratio_b'])/p['ratio_a'])
    if kind=='session_place_order_inverse':
        p=cert['inputs'];difference=s.Rational(p['difference'],9000);a=(p['sum']+difference)/2;b=(p['sum']-difference)/2
        values=[p['prefix']*100000+10000*a+1000*b+p['tail'],p['prefix']*100000+10000*b+1000*a+p['tail'],p['other']]
        return sorted(values)[1]
    if kind=='session_cube_tunnels':
        p=cert['inputs'];height=s.Rational(p['total'],p['length']*p['width']);return s.simplify(p['total']-p['length']*height-p['width']*height+height)
    if kind=='session_spatial_minimum':
        from itertools import product
        p=cert['inputs'];front=[p['f1'],p['f2']];side=[p['s1'],p['s2']];maximum=max(front+side);values=[]
        for a,b,c,d in product(range(maximum+1),repeat=4):
            if [max(a,c),max(b,d)]==front and [max(a,b),max(c,d)]==side:values.append(a+b+c+d)
        assert values;return s.Integer(min(values))
    if kind=='session_urn_inverse':
        p=cert['inputs'];red=s.Rational(p['numerator'],p['denominator'])*(p['total']+p['added'])-p['added'];assert red>p['removed']
        return s.simplify((red-p['removed'])/(p['total']-p['removed']))
    return solve_targeted(cert)


def assess(model,grade):
    cert=model['certificate'];kind=cert['type']
    if kind.startswith('session_basic'):return basic.assess(model,grade)
    if kind.startswith('session_sma'):
        from .session_high_sma import assess as sma_assess
        return sma_assess(model,grade)
    if kind in {'session_targeted_visual','session_parameter_visual'}:return assess({**model,'certificate':cert['base']},grade)
    if kind in {'session_finite_factor_pairs','session_common_bags','session_bar_reallocate','session_data_audit','session_scientific_inverse','session_geometry_shared','session_45_pythagoras','session_distance_ratio','session_place_order_inverse','session_cube_tunnels','session_spatial_minimum','session_urn_inverse'}:
        reason='Menggabungkan kendala, menilai kemungkinan atau membalik informasi sebelum menentukan kuantitas akhir.'
    elif kind in {'symbolic_constraints','finite_constraints','restricted_bijection','digit_arrangements','committee','conditional_urn','finite_probability'}:
        if not model['kind'].startswith('v2_'):raise ValueError('Unreviewed constraint template')
        # These are the individually authored inverse/constraint families, not
        # targeted_math.constant(), which merely stores a supplied answer.
        if kind=='symbolic_constraints':
            assert cert['equations'] and cert['variables']
            assert not (len(cert['variables'])==1 and cert['equations']==[cert['variables'][0]+' - '+str(solve(cert))]),'A given output is not a constraint problem'
        reason='Menyusun dan menghubungkan kendala pada parameter tersembunyi, memilih cabang atau kemungkinan yang sah, lalu mengevaluasi hasil yang diminta.'
    else:raise ValueError('Unreviewed session content '+kind)
    return {'assessedLevel':'hard','reason':reason,'steps':4,'flags':[],'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,'apiCalls':0}


def _make(stem,cert,family,explanation):
    value=solve(cert);draft=numeric(stem,value,explanation+' Hasilnya '+m(value)+'.',family)
    model={'question':draft.question,'answer':draft.answer,'wrong':draft.distractors,'explanation':draft.explanation,'kind':family,'steps':4,'rationale':'Menggabungkan beberapa kendala dan membalik hubungan yang diberikan.','scene':None,'certificate':cert}
    model['assessment']=assess(model,0);return model


def hard_special(grade,bab,code,r):
    if grade==5 and bab==9 and code=='B':
        a=r.randint(4,9);b=r.randint(1,a-1);tail=r.randint(100,999);prefix=r.randint(1,8);difference=9000*(a-b);first=prefix*100000+10000*a+1000*b+tail;second=prefix*100000+10000*b+1000*a+tail;other=r.randint(max(100000,second-12000),min(999999,first+12000))
        return _make(f'Dua bilangan enam angka ditulis {prefix}AB{tail} dan {prefix}BA{tail}. A,B digit bukan nol, A>B, dan A+B={a+b}. Bilangan pertama lebih besar {difference} daripada kedua. Jika keduanya diurutkan bersama {other}, berapa bilangan di posisi tengah?',{'type':'session_place_order_inverse','inputs':{'prefix':prefix,'sum':a+b,'difference':difference,'tail':tail,'other':other}},'session_urut_enam_digit_balik','Selisih bilangan menentukan 9000(A−B). Gabungkan dengan jumlah digit untuk mendapatkan A dan B, susun kedua bilangan enam angka lalu urutkan bersama bilangan ketiga')
    if grade==5 and bab==2 and code in 'DE':
        if code=='E':
            g=r.randint(2,16);u,v=r.choice([(2,3),(3,5),(4,5),(5,7),(3,8),(7,9)]);limit=g*u*v;cap=r.randint(g,limit//2)
            cert={'type':'session_finite_factor_pairs','inputs':{'gcd':g,'lcm':limit,'cap':cap,'limit':limit}}
            return _make(f'Dua bilangan positif A dan B memenuhi A≤B. FPB-nya {g} dan KPK-nya {limit}. A tidak lebih dari {cap}. Berapa nilai A+B terbesar yang mungkin?',cert,'session_fpb_kpk_inverse','Daftar pasangan faktor dari FPB×KPK, periksa FPB dan KPK tiap pasangan serta batas A, kemudian pilih jumlah terbesar')
        a=r.randint(3,18);b=r.randint(3,18);g=r.randint(3,20);cap=r.randint(2,g+3)
        return _make(f'Ada {a*g} apel dan {b*g} jeruk yang seluruhnya dibagi ke kantong tanpa sisa. Isi apel antar kantong sama, demikian pula jeruk. Tersedia paling banyak {cap} kantong. Jika kantong dipakai sebanyak mungkin, berapa banyak buah tiap kantong?',{'type':'session_common_bags','inputs':{'fruit_a':a*g,'fruit_b':b*g,'cap':cap}},'session_faktor_persekutuan_batas','Cari faktor persekutuan yang tidak melebihi batas jumlah kantong. Pilih yang terbesar lalu bagi kedua jenis buah dengannya')
    if grade==5 and bab==4 and code=='E':
        a,b=r.randint(10,35),r.randint(10,35);w=r.randint(5,18);outer=2*(a+b+w)
        return _make(f'Dua persegi panjang panjangnya {a} cm dan {b} cm. Lebar pertama x cm dan lebar kedua x−2 cm. Keduanya ditempel tanpa tumpang tindih pada seluruh sisi lebar kedua. Keliling gabungannya {outer} cm. Berapa keliling persegi panjang pertama setelah keduanya dipisah?',{'type':'session_geometry_shared','inputs':{'length_a':a,'length_b':b,'outer':outer}},'session_keliling_gabungan_balik','Keliling gabungan 2(a+x)+2(b+x−2)−2(x−2)=2(a+b+x). Tentukan x, lalu hitung 2(a+x)')
    if grade==6 and bab==3:
        if code=='A':
            length,width,height=r.randint(4,12),r.randint(4,12),r.randint(3,10);total=length*width*height
            return _make(f'Balok kubus satuan mempunyai alas {length}×{width} kubus dan berisi {total} kubus. Satu terowongan tegak berukuran satu baris kubus sepanjang arah panjang dan satu lagi sepanjang arah lebar dibuat menembus seluruh tingginya. Kedua terowongan berpotongan pada satu kolom. Berapa kubus yang tersisa?',{'type':'session_cube_tunnels','inputs':{'length':length,'width':width,'total':total}},'session_konstruksi_terowongan','Tentukan tinggi dari banyak kubus dan luas alas. Kurangi dua bidang terowongan lalu tambahkan kembali kolom perpotongan yang sempat terhitung dua kali')
        if code=='B':
            maximum=r.randint(3,8);low1=r.randint(1,maximum-1);low2=r.randint(1,maximum-1)
            return _make(f'Empat menara kubus disusun pada petak 2×2. Tampak depan menunjukkan tinggi maksimum kolom pertama {maximum} dan kolom kedua {low1}. Tampak samping menunjukkan maksimum baris pertama {low2} dan baris kedua {maximum}. Menara boleh kosong. Berapa jumlah kubus paling sedikit yang memenuhi kedua tampak?',{'type':'session_spatial_minimum','inputs':{'f1':maximum,'f2':low1,'s1':low2,'s2':maximum}},'session_spasial_dua_tampak_minimum','Setiap tinggi menara dibatasi maksimum baris dan kolom. Cari susunan yang memenuhi kedua tampak dengan jumlah tinggi sekecil mungkin')
    if grade==6 and bab==4:
        red,blue=r.randint(8,30),r.randint(8,30);added=r.randint(2,9);removed=r.randint(1,red-1);fraction=s.Rational(red+added,red+blue+added)
        return _make(f'Kantong semula berisi {red+blue} bola merah dan biru. Setelah ditambah {added} bola merah, peluang merah menjadi {m(fraction)}. Kantong dikembalikan ke keadaan semula, kemudian {removed} bola merah diambil. Berapa peluang merah setelah pengambilan?',{'type':'session_urn_inverse','inputs':{'total':red+blue,'added':added,'removed':removed,'numerator':int(fraction.p),'denominator':int(fraction.q)}},'session_peluang_balik_perubahan','Gunakan peluang setelah penambahan untuk menentukan banyak merah semula. Kembalikan total awal, kurangi merah yang diambil pada pembilang dan penyebut, lalu sederhanakan')
    if grade==7 and bab==1 and code=='C':
        a,b,g=r.randint(3,15),r.randint(3,15),r.randint(3,18);cap=r.randint(2,g+4)
        return _make(f'Dua pita panjangnya {a*g} cm dan {b*g} cm dipotong tanpa sisa menjadi potongan sama panjang. Panjang setiap potongan harus bilangan bulat dan tidak boleh melebihi {cap} cm. Jika potongan dibuat sepanjang mungkin, berapa jumlah potongan seluruhnya?',{'type':'session_common_bags','inputs':{'fruit_a':a*g,'fruit_b':b*g,'cap':cap}},'session_faktor_bulat_potongan_batas','Panjang potongan adalah faktor persekutuan kedua panjang dengan batas atas. Pilih yang terbesar lalu hitung dan jumlahkan banyak potongan kedua pita')
    if (grade==5 and bab==8 and code=='C') or (grade==7 and bab==6 and code in 'CD'):
        a,b,c=r.randint(25,80),r.randint(20,70),r.randint(15,65);move=r.randint(3,12);extra=r.randint(2,11)
        return _make(f'Diagram mencatat kelompok A={a}, B={b}, dan C={c}. Sebanyak {move} anggota A pindah ke B, lalu C menerima {extra} anggota baru. Setelah semua perubahan, berapa selisih kelompok terbanyak dan tersedikit?',{'type':'session_bar_reallocate','inputs':{'a':a,'b':b,'c':c,'move':move,'extra':extra}},'session_diagram_urut_ulang','Perbarui ketiga frekuensi, tentukan kembali kelompok terbesar dan terkecil karena urutan dapat berubah, lalu cari selisihnya')
    if grade==7 and bab==6 and code=='F':
        n=r.randint(60,180);duplicate=r.randint(4,16);missing=r.randint(3,14);other=r.randint(10,n//2)
        return _make(f'Untuk memilih diagram frekuensi kategori, petugas mengaudit data. Laporan awal memuat {n} respons, tetapi {duplicate} di antaranya tercatat dua kali dan {missing} respons belum dimasukkan. Setelah koreksi, kategori selain olahraga berjumlah {other}. Berapa tinggi batang kategori olahraga yang harus digambar?',{'type':'session_data_audit','inputs':{'reported':n,'duplicate':duplicate,'missing':missing,'other':other}},'session_diagram_audit_sumber','Perbaiki jumlah respons dari duplikasi dan data hilang, lalu kurangi kategori lain untuk mendapatkan frekuensi batang olahraga')
    if grade==7 and bab==4 and code=='C':
        from .targeted_math import system
        a,b=s.symbols('a b',real=True);fee=r.randint(5,20);rate=r.randint(3,12);t1=r.randint(2,6);t2=t1+r.randint(2,5);budget=r.randint(80,180)
        cert=system(['a','b'],[a+t1*b-fee-t1*rate,a+t2*b-fee-t2*rate],s.floor((budget-a)/b),[a,b])
        return _make(f'Biaya sewa alat terdiri atas biaya tetap dan tarif per jam. Sewa {t1} jam biayanya {fee+t1*rate} ribu rupiah, sedangkan {t2} jam {fee+t2*rate} ribu rupiah. Dengan anggaran {budget} ribu rupiah, berapa jam penuh paling banyak yang dapat disewa?',cert,'v2_model_aljabar_dua_tarif','Dua data membentuk dua persamaan. Selisihnya menentukan tarif, substitusi menentukan biaya tetap, lalu evaluasi anggaran dan ambil jam penuh')
    if grade==8 and bab==1 and code=='C':
        a,b=r.randint(11,89),r.randint(11,89);pa,pb=r.randint(2,4),r.randint(2,3);e=r.randint(-3,3)
        return _make(f'Besaran P dan Q dalam bentuk baku adalah ({a}/10)×10^{pa} dan ({b}/10)×10^{pb}. Tentukan nilai (P/10^{pa})^{pa} dibagi (Q/10^{pb})^{pb}, lalu dikalikan 10^{e}. Tuliskan nilai eksaknya.',{'type':'session_scientific_inverse','inputs':{'first':a,'second':b,'power_a':pa,'power_b':pb,'exponent':e}},'session_bentuk_baku_operasi_bertingkat','Pisahkan koefisien bentuk baku dari pangkat sepuluh, terapkan pangkat pada masing-masing koefisien, lalu gabungkan pembagian dan faktor sepuluh')
    if grade==8 and bab==2 and code=='C':
        a=r.randint(6,30);removed=r.randint(1,a*a//3);perimeter=a*(2+s.sqrt(2))
        return _make('Segitiga siku-siku sama kaki mempunyai keliling '+m(perimeter)+' cm. Dari daerah itu dipotong bagian seluas '+str(removed)+' cm². Berapa luas daerah yang tersisa?',{'type':'session_45_pythagoras','inputs':{'perimeter':str(perimeter),'removed':removed}},'session_segitiga_istimewa_balik','Dengan kaki a, keliling a(2+√2). Tentukan a, hitung luas a²/2, lalu kurangi bagian yang dipotong')
    if grade==8 and bab==2 and code=='E':
        u,v,h=r.choice([(3,4,5),(5,12,13),(8,15,17)]);scale=r.randint(2,14);ra,rb=r.randint(2,7),r.randint(2,7)
        return _make(f'Titik A=(0,0) dan B=({u*scale},{v*scale}) berada pada ruas AC. B terletak di antara A dan C dan AB:BC={ra}:{rb}. Berapa panjang AC?',{'type':'session_distance_ratio','inputs':{'dx':u*scale,'dy':v*scale,'ratio_a':ra,'ratio_b':rb}},'session_jarak_koordinat_rasio','Hitung AB dengan rumus jarak, tentukan panjang per bagian rasio, lalu hitung seluruh bagian AC')
    return None


def essential_visual(model):
    """Move one pivotal observed datum into a factual table, preserving its recipe."""
    cert=model['certificate'];question=model['question']
    if cert.get('inputs'):
        for key,old in cert['inputs'].items():
            if type(old) is not int or old<3:continue
            matches=list(re.finditer(r'(?<![\w.])'+str(old)+r'(?!\w|\.\d)',question))
            if len(matches)!=1:continue
            wrapped={'type':'session_parameter_visual','base':cert,'parameter':key,'inputs':{'visible':old}}
            try:
                initial=solve(wrapped)
                for change in [old+1,old+2,old-1,old+3,old+max(2,old//3),max(1,old//2),old*2]:
                    altered=deepcopy(wrapped);altered['inputs']['visible']=change
                    try:
                        if s.simplify(solve(altered)-initial)!=0:break
                    except (ValueError,TypeError,AssertionError,ZeroDivisionError):continue
                else:continue
            except (ValueError,TypeError,AssertionError,ZeroDivisionError):continue
            match=matches[0];inside=question[:match.start()].count('$')%2==1;replacement='T_1' if inside else '$T_1$'
            updated=deepcopy(model);updated['question']='Gunakan nilai $T_1$ pada tabel gambar sebagai data soal. '+question[:match.start()]+replacement+question[match.end():]
            updated['scene']={'kind':'table','headers':['Data','Nilai'],'rows':[['T1',old]]};updated['visual_kind']='math_scene';updated['certificate']=wrapped;wrapped['visual_bindings']=[{'input':'visible','path':['rows',0,1],'alternatives':[change]}]
            return updated
    options=[]
    for match in re.finditer(r'(?<![\w.])([1-9][0-9]*)(?!\w|\.\d)',question):
        old=int(match.group(1))
        if old<3 or len(re.findall(r'(?<![\w.])'+str(old)+r'(?!\w|\.\d)',question))!=1:continue
        for path,text in _iter_strings(cert):
            try:tree=ast.parse(text,mode='eval')
            except (SyntaxError,ValueError):continue
            count=sum(isinstance(n,ast.Constant) and type(n.value) is int and n.value==old for n in ast.walk(tree))
            if count==1:options.append((match,old,path,old,1));break
            squared=sum(isinstance(n,ast.Constant) and type(n.value) is int and n.value==old**2 for n in ast.walk(tree))
            if squared==1:options.append((match,old,path,old**2,2));break
    for match,old,path,replaced,power in options:
        wrapped={'type':'session_targeted_visual','base':cert,'replace_path':list(path),'original':replaced,'power':power,'inputs':{'visible':old}}
        try:
            value=solve(wrapped)
            for change in [old+1,old+2,old-1,old+3,old+max(2,old//3),max(1,old//2),old*2]:
                altered=deepcopy(wrapped);altered['inputs']['visible']=change
                try:
                    if s.simplify(solve(altered)-value)!=0:break
                except (AssertionError,ValueError,TypeError,ZeroDivisionError):continue
            else:continue
        except (AssertionError,ValueError,TypeError,ZeroDivisionError):continue
        inside=question[:match.start()].count('$')%2==1;replacement='T_1' if inside else '$T_1$'
        model=deepcopy(model);model['question']='Gunakan nilai $T_1$ pada tabel gambar sebagai data soal. '+question[:match.start()]+replacement+question[match.end():]
        model['scene']={'kind':'table','headers':['Data','Nilai'],'rows':[['T₁',old]]};model['visual_kind']='math_scene';model['certificate']=wrapped;wrapped['visual_bindings']=[{'input':'visible','path':['rows',0,1],'alternatives':[change]}]
        return model
    return None


def check_visual(model):
    scene=model.get('scene')
    if not scene:return {'status':'text_question'}
    from .math_scene_visuals import validate_scene
    validate_scene(scene);cert=model['certificate'];initial=solve(cert);passed=[]
    if cert['type']=='session_basic_linked':
        for side,offset in [('left',0),('right',len(cert['left']['inputs']))]:
            for index,(key,value) in enumerate(cert[side]['inputs'].items()):
                assert s.sympify(scene['rows'][offset+index][2])==s.sympify(value),'Scene and retained input differ'
                for change in [s.sympify(value)+1,s.sympify(value)+2,s.sympify(value)-1]:
                    altered=deepcopy(cert);altered[side]['inputs'][key]=str(change)
                    try:
                        if s.simplify(solve(altered)-initial)!=0:passed.append([side,key]);break
                    except (ValueError,TypeError,ZeroDivisionError):continue
    else:
        for binding in cert.get('visual_bindings',[]):
            value=cert['inputs'][binding['input']];visible=_at(scene,binding['path']);assert s.sympify(value)==s.sympify(visible)
            for change in binding.get('alternatives',[s.sympify(value)+1,s.sympify(value)+2,s.sympify(value)-1]):
                altered=deepcopy(cert);altered['inputs'][binding['input']]=str(change) if isinstance(value,str) else int(change)
                try:
                    if s.simplify(solve(altered)-initial)!=0:passed.append(binding['input']);break
                except (ValueError,TypeError,ZeroDivisionError,AssertionError):continue
    assert passed,('Image has no pivotal facts',model['kind'])
    return {'status':'verified_locally','pivotalFacts':passed,'independentVisionValidation':False}


def generate(name,bab,code,level,r,visual,index):
    grade=int(name.split('_')[0][5:])
    if grade>=10:
        from .session_high_sma import generate as sma_generate
        candidate=sma_generate(name,bab,code,level,r,visual,index)
        if candidate is not None:return candidate
    elif level in ('easy','medium'):
        return basic.generate(grade,bab,code,level,r,visual,index)
    special=hard_special(grade,bab,code,r) if grade<10 else None
    if special is not None:model=special
    else:
        from scripts.generate_targeted_replenishment import factory
        try:authored=factory(name,bab,code,'hard',r)
        except (AssertionError,ValueError,ZeroDivisionError):return None
        d=authored.draft;model={'question':d.question,'answer':d.answer,'wrong':d.distractors,'explanation':d.explanation,'kind':d.kind,'steps':authored.steps,'rationale':authored.rationale,'scene':None,'certificate':authored.certificate}
        try:model['assessment']=assess(model,grade)
        except (AssertionError,ValueError):return None
    if model['assessment']['assessedLevel']!=level:return None
    if visual:
        model=essential_visual(model)
        if model is None:return None
    return model
