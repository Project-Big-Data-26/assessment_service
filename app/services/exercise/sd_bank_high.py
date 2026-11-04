"""Grade 3–4 authored variations, keyed to the stored 40 curriculum locations.

No provider calls or file writes. Visuals supply actual problem data, not decoration.
"""
from itertools import permutations
from collections import Counter
from decimal import Decimal
import math
import sympy as s


def fmt(v):
    return '$'+s.latex(s.sympify(v))+'$'


def solve_certificate(cert):
    kind=cert['type']
    if kind=='sd_high_expression':
        names={k:s.sympify(v) for k,v in cert['inputs'].items()}
        names.update(Max=s.Max,Min=s.Min,Abs=s.Abs,floor=s.floor,ceiling=s.ceiling,Mod=s.Mod,GCD=s.igcd)
        return s.simplify(s.sympify(cert['expression'],locals=names))
    if kind=='sd_high_digits':
        digits=[int(cert.get('inputs',{}).get('d'+str(i),v)) for i,v in enumerate(cert['digits'])]
        values=[int(''.join(map(str,p))) for p in permutations(digits) if p[0]!=0]
        eligible=[v for v in values if v%2==0 and v<cert['bound']]
        return s.Integer(max(eligible))
    if kind=='sd_high_frequency':
        data=[int(cert.get('inputs',{}).get('v'+str(i),v)) for i,v in enumerate(cert['data'])]
        counts=Counter(data)
        return s.Integer(counts[cert['target']])
    if kind=='sd_high_shapes':
        props={'triangle':(3,0,0),'right_triangle':(3,1,0),'square':(4,4,2),
               'rectangle':(4,4,2),'parallelogram':(4,0,2),'rhombus':(4,0,2),
               'trapezoid':(4,0,1),'pentagon':(5,0,0),'hexagon':(6,0,3)}
        shapes=[cert.get('inputs',{}).get('shape'+str(i),v) for i,v in enumerate(cert['shapes'])]
        values=[props[v] for v in shapes]
        field=cert['property']
        if cert['query']=='sum':return s.Integer(sum(v[field] for v in values))
        if cert['query']=='filtered_sum':return s.Integer(sum(v[0] for v in values if v[1]>0))
        if cert['query']=='difference':return s.Integer(sum(v[0] for v in values)-sum(v[1] for v in values))
    if kind=='sd_high_lines':
        segments=[[list(map(s.sympify,v)) for v in pair] for pair in cert['segments']]
        if 'end_y' in cert.get('inputs',{}):segments[0][1][1]=int(cert['inputs']['end_y'])
        vectors=[(p[1][0]-p[0][0],p[1][1]-p[0][1]) for p in segments]
        eligible=[(i,j) for i in range(len(vectors)) for j in range(i+1,len(vectors)) if i not in cert.get('removed',[]) and j not in cert.get('removed',[])]
        parallel=sum(vectors[i][0]*vectors[j][1]-vectors[i][1]*vectors[j][0]==0 for i,j in eligible)
        right=sum(vectors[i][0]*vectors[j][0]+vectors[i][1]*vectors[j][1]==0 for i,j in eligible)
        return s.Integer(parallel if cert['query']=='parallel' else right if cert['query']=='right' else parallel+right)
    if kind=='sd_high_pattern':
        pattern=list(cert['unit']);length=cert['length'];k=cert['skip']
        if 'first' in cert.get('inputs',{}):pattern[0]=cert['inputs']['first']
        return s.Integer(sum(pattern[(i+k)%len(pattern)]==cert['target'] for i in range(length)))
    if kind=='sd_high_factors':
        a=int(cert['inputs']['a']);b=int(cert['inputs']['b']);capacity=cert['capacity']
        best=max(d for d in range(1,capacity+1) if a%d==b%d==0)
        return s.Rational(a+b,best)
    raise ValueError(kind)


def _numeric_paths(value,path=()):
    if isinstance(value,dict):
        for k,v in value.items():yield from _numeric_paths(v,(*path,k))
    elif isinstance(value,list):
        for k,v in enumerate(value):yield from _numeric_paths(v,(*path,k))
    elif isinstance(value,(int,float)) and not isinstance(value,bool):yield list(path),value


def _semantic_paths(scene,inputs):
    """Bind meanings, never coincidentally equal numbers from unrelated fields."""
    kind=scene['kind'];mapping={}
    if kind=='cards':
        labels=[str(v['label']) for v in scene['cards']]
        mapping.update({f'd{i}':['cards',i,'value'] for i in range(len(labels))})
        for variable,label in [('th','Ribuan'),('h','Ratusan'),('t','Puluhan'),('u','Satuan')]:
            if label in labels:mapping[variable]=['cards',labels.index(label),'value']
        if 'place' in inputs and 'd' in inputs:
            places={1000:'Ribuan',100:'Ratusan',10:'Puluhan',1:'Satuan'}
            label=places[int(inputs['place'])]
            mapping['d']=['cards',labels.index(label),'value']
        templates=[(['P','Q','R'],{'p':0,'q':1,'t':2}),(['Kotak A','Kotak B'],{'a':0,'b':1}),
                   (['Stok awal','Dikirim pertama'],{'n':0,'a':1}),(['Mula-mula','Akhir'],{'start':0,'end':1}),
                   (['Seluruh benda','Banyak penerima'],{'n':0,'g':1}),(['Persediaan','Cadangan'],{'n':0,'r':1}),
                   (['Jeruk','Apel'],{'a':0,'b':1}),(['1','2','3','4'],{'a':0,'b':1,'c':2,'d':3})]
        for expected,variables in templates:
            if labels==expected:mapping.update({k:['cards',i,'value'] for k,i in variables.items()})
    elif kind=='table':
        labels=[str(row[0]) for row in scene['rows']]
        templates=[(['Kotak','Isi tiap kotak'],{'g':0,'p':1}),(['Kilogram','Gram tambahan'],{'k':0,'g':1}),
                   (['Meter','Sentimeter'],{'m':0,'c':1}),(['5','6','7','8'],{'a':0,'b':1,'c':2,'d':3}),
                   (['P','Q','Penyebut sama'],{'p':0,'q':1,'d':2})]
        for expected,variables in templates:
            if labels==expected:mapping.update({k:['rows',i,1] for k,i in variables.items()})
    elif kind in ['bars','pictogram']:
        mapping={k:['values',i] for i,k in enumerate(['a','b','c','d'][:len(scene['values'])])}
    elif kind=='fraction_grid':
        mapping={'n':['shaded']}
        if scene['rows']==1:mapping['d']=['cols']
    elif kind=='ruler':mapping={'start':['object_start'],'end':['object_end']}
    elif kind=='area_grid':mapping={'l':['cols'],'w':['rows']}
    elif kind=='volume_blocks':mapping={'l':['length'],'w':['width'],'h':['height']}
    return {key:path for key,path in mapping.items() if key in inputs}


def make(question,expression,inputs,explanation,kind,level,scene=None,wrong=None,certificate=None):
    cert=certificate or {'type':'sd_high_expression','expression':expression,'inputs':{k:str(v) for k,v in inputs.items()}}
    value=solve_certificate(cert)
    assert not value.free_symbols and value.is_real and value.is_finite
    defaults=([1-value,value/2,(1+value)/2,value**2,s.Rational(1,3),s.Rational(2,3)] if not value.is_Integer and 0<value<1 else [])
    if kind.startswith('sd4_desimal_'):
        defaults=[v for v in [value+s.Rational(1,100),value-s.Rational(1,100),value+s.Rational(2,100),value-s.Rational(2,100),value+s.Rational(3,100)] if 0<=v<=1]
    proposals=list(wrong or [])+defaults+[value+1,value-1,value+2,value+3,value*2,value/2,value+5]
    distractors=[]
    for v in proposals:
        v=s.sympify(v)
        if v<0 or s.simplify(v-value)==0 or any(s.simplify(v-z)==0 for z in distractors):continue
        distractors.append(v)
        if len(distractors)==3:break
    assert len(distractors)==3
    if scene and cert['type']=='sd_high_expression':
        # Each binding is a real displayed input on which the result depends.
        bindings=[]
        for variable,path in _semantic_paths(scene,inputs).items():
            number=inputs[variable];visible=scene
            for part in path:visible=visible[part]
            assert s.sympify(number)==s.sympify(visible),(kind,variable,path,number,visible)
            changed={**cert,'inputs':{**cert['inputs'],variable:str(s.sympify(number)+1)}}
            try:different=solve_certificate(changed)!=value
            except (ValueError,TypeError,ZeroDivisionError):different=False
            if different:bindings.append({'input':variable,'path':path})
        assert bindings, (kind,'visual lacks a decisive numeric binding')
        cert['visual_bindings']=bindings
    elif scene and cert['type']=='sd_high_shapes':
        cert['visual_bindings']=[{'input':'shapes','input_path':[i],'path':['items',i,'shape'],
                                 'alternatives':['triangle','square','pentagon']} for i in range(len(cert['shapes']))]
    elif scene and cert['type']=='sd_high_frequency':
        cert['visual_bindings']=[{'input':'data','input_path':[i],'path':['rows',i,1]} for i,v in enumerate(cert['data']) if v==cert['target']]
        assert cert['visual_bindings']
    elif scene and cert['type']=='sd_high_lines':
        cert['visual_bindings']=[{'input':'segments','input_path':[i,1,1],'path':['segments',i,1,1]} for i in range(len(cert['segments'])) if i not in cert['removed']]
    elif scene and cert['type']=='sd_high_pattern':
        cert['visual_bindings']=[{'input':'unit','input_path':[i],'path':['items',i],
                                 'alternatives':['circle','square','triangle']} for i in range(len(cert['unit']))]
    cert['expected']=str(value)
    def answer_format(v):
        if kind.startswith('sd4_desimal_'):
            v=s.Rational(v);return '$'+format(Decimal(int(v.p))/Decimal(int(v.q)),'f')+'$'
        return fmt(v)
    return {'question':question,'answer':answer_format(value),'wrong':[answer_format(v) for v in distractors],
            'explanation':explanation,'kind':kind,'steps':{'easy':1,'medium':3,'hard':4}[level],
            'rationale':{'easy':'Membaca satu representasi dan menerapkan satu konsep langsung.',
                         'medium':'Menghubungkan pembacaan data dengan dua atau tiga langkah rutin.',
                         'hard':'Menentukan informasi yang diperlukan, menggabungkan beberapa syarat, lalu memeriksa hasil dalam konteks.'}[level],
            'scene':scene,'certificate':cert,'intended_level':level}


def table(headers,rows,title='Data untuk soal'):
    return {'kind':'table','headers':headers,'rows':rows,'title':title}


def cards(labels,values):
    return {'kind':'cards','cards':[{'label':str(k),'value':v} for k,v in zip(labels,values)]}


def generate(grade,bab,code,level,r,visual,index):
    assert grade in (3,4)
    names=['Rani','Dika','Sita','Beni','Lina','Adi','Nina','Wawan','Mira','Tono']
    name=names[(index-1)%len(names)]
    # Integer representations, place values, comparison, composition.
    if bab==1 and (code in 'ABC' or grade==4 and code=='D'):
        places=3 if grade==3 else 4
        digits=[r.randint(1,8),*[r.randint(1,9) for _ in range(places-1)]]
        number=sum(v*10**(places-i-1) for i,v in enumerate(digits));labels=['Ratusan','Puluhan','Satuan'] if places==3 else ['Ribuan','Ratusan','Puluhan','Satuan']
        scene=cards(labels,digits) if visual else None
        listing='; '.join(str(v)+' '+label.lower() for label,v in zip(labels,digits))
        data='kartu nilai tempat pada gambar' if visual else listing
        inputs={'n':number,'h':digits[-3],'t':digits[-2],'u':digits[-1]}
        if code=='A':
            if level=='easy':
                expr='+'.join(f'd{i}*{10**(places-i-1)}' for i in range(places));iv={f'd{i}':v for i,v in enumerate(digits)}
                return make(f'{name} menyusun bilangan dari {data}. Berapa bilangan yang terbentuk?',expr,iv,f'Kalikan setiap digit dengan nilai tempatnya lalu jumlahkan. Bilangan yang terbentuk adalah {number}.',f'sd{grade}_lambang_nilai_tempat',level,scene)
            if level=='medium':
                increment=r.randint(1,3);expr='+'.join(f'd{i}*{10**(places-i-1)}' for i in range(places))+f'+{increment}*10-1';iv={f'd{i}':v for i,v in enumerate(digits)}
                return make(f'Bilangan {name} ditunjukkan oleh {data}. Bilangan itu ditambah {increment} puluhan, lalu dikurangi satu. Berapa hasilnya?',expr,iv,f'Bilangan awal {number}. Tambah {10*increment} dan kurangi 1, hasil {number+10*increment-1}.',f'sd{grade}_lambang_perubahan',level,scene)
            d=r.sample(range(1,10),places-1)+[0];all_even=sorted({int(''.join(map(str,p))) for p in permutations(d) if p[0] and p[-1]%2==0});gaps=[(lo,hi) for lo,hi in zip(all_even,all_even[1:]) if hi-lo>=4];lo,hi=r.choice(gaps);bound=r.randint(lo+3,hi);answer=max(z for z in all_even if z<bound)
            scene=cards(['Kartu '+str(i+1) for i in range(places)],d) if visual else None
            source='kartu angka pada gambar' if visual else 'kartu angka '+', '.join(map(str,d))
            cert={'type':'sd_high_digits','digits':d,'bound':bound,'inputs':{'d'+str(i):v for i,v in enumerate(d)},'visual_bindings':[{'input':'d'+str(i),'path':['cards',i,'value']} for i in range(places)] if visual else []}
            return make(f'Dari {source}, {name} memakai setiap kartu tepat sekali untuk membentuk bilangan {places} angka. Angka nol tidak boleh di depan. Berapa bilangan genap terbesar yang lebih kecil dari {bound}?','',{},f'Tentukan kartu satuan yang genap, larang nol sebagai digit pertama, lalu bandingkan susunan yang masih di bawah {bound}. Susunan terbesar yang memenuhi adalah {answer}.',f'sd{grade}_lambang_susun_bersyarat',level,scene,certificate=cert)
        if code=='B':
            pos=r.randint(0,places-1);value=digits[pos]*10**(places-pos-1)
            if level=='easy':return make(f'Perhatikan {data}. Berapa nilai digit pada tempat {labels[pos].lower()}?','d*place',{'d':digits[pos],'place':10**(places-pos-1)},f'Digit {digits[pos]} menempati {labels[pos].lower()}, sehingga nilainya {value}.',f'sd{grade}_nilai_digit',level,scene)
            if level=='medium':
                expr='Abs(90*(h-t))'
                return make(f'Bilangan awal berasal dari {data}. Digit ratusan dan puluhan ditukar. Berapa selisih mutlak bilangan sebelum dan sesudah pertukaran?',expr,{'h':digits[-3],'t':digits[-2]},f'Nilai ratusan dan puluhan semula {digits[-3]*100+digits[-2]*10}; setelah ditukar {digits[-2]*100+digits[-3]*10}. Selisih mutlak {abs(90*(digits[-3]-digits[-2]))}. Digit lainnya tetap.',f'sd{grade}_nilai_tempat_tukar',level,scene)
            taken=r.randint(2,5);added=r.randint(1,3);value=digits[-3]*10+digits[-2]-taken+added
            return make(f'Perhatikan banyak ikatan ratusan dan puluhan pada {data}. Semua ikatan ratusan ditukar menjadi ikatan puluhan. Kemudian {taken} ikatan puluhan diambil dan {added} ikatan puluhan ditambahkan. Berapa ikatan puluhan sekarang? Satuan dan ribuan tidak ikut ditukar.','10*h+t-taken+added',{'h':digits[-3],'t':digits[-2],'taken':taken,'added':added},f'Tiap ratusan menjadi 10 puluhan. Setelah penukaran ada {digits[-3]*10+digits[-2]} ikatan puluhan; setelah perubahan menjadi {value}.',f'sd{grade}_nilai_tempat_regroup',level,scene)
        if code=='C':
            limit=1000 if grade==3 else 10000;vals=r.sample(range(100,limit),3);scene=cards(['P','Q','R'],vals) if visual else None;source='kartu P,Q,R pada gambar' if visual else f'P={vals[0]}, Q={vals[1]}, R={vals[2]}'
            if level=='easy':return make(f'Perhatikan {source}. Berapa bilangan terbesar?','Max(p,q,t)',dict(zip(['p','q','t'],vals)),f'Bandingkan mulai digit paling kiri. Bilangan terbesar {max(vals)}.',f'sd{grade}_banding_terbesar',level,scene)
            if level=='medium':return make(f'Perhatikan {source}. Berapa selisih bilangan terbesar dan terkecil?','Max(p,q,t)-Min(p,q,t)',dict(zip(['p','q','t'],vals)),f'Urutannya {sorted(vals)}. Kurangi {max(vals)} dengan {min(vals)}; selisih {max(vals)-min(vals)}.',f'sd{grade}_banding_jangkauan',level,scene)
            extra=r.randint(2,9);middle=sorted(vals)[1];value=max(vals)-middle+extra
            return make(f'Urutkan bilangan pada {source} dari kecil ke besar. Bilangan tengah dinaikkan {extra}. Berapa selisih mutlak bilangan terbesar semula dan bilangan tengah yang baru?','Abs(Max(p,q,t)-(p+q+t-Max(p,q,t)-Min(p,q,t)+extra))',{**dict(zip(['p','q','t'],vals)),'extra':extra},f'Urutan {sorted(vals)}, jadi bilangan tengah {middle}. Setelah ditambah {extra} menjadi {middle+extra}; selisih mutlak dengan {max(vals)} adalah {abs(max(vals)-middle-extra)}.',f'sd{grade}_urut_perubahan_tengah',level,scene)
        # Grade4 composition/decomposition: regrouping an arbitrary 4-digit quantity.
        if level=='easy':
            expr='+'.join(f'd{i}*{10**(places-i-1)}' for i in range(places));iv={f'd{i}':v for i,v in enumerate(digits)}
            return make(f'Susun satu bilangan dari {data}. Berapa hasil komposisinya?',expr,iv,f'Jumlahkan nilai ribuan, ratusan, puluhan, dan satuan: hasil {number}.','sd4_komposisi_lengkap',level,scene)
        if level=='medium':
            return make(f'Perhatikan {data}. Satu ribuan ditukar menjadi ratusan, lalu seluruh ratusan dihitung. Berapa banyak ratusan sekarang? Ribuan lainnya, puluhan, dan satuan tetap.','10+h',{'h':digits[-3]},f'Satu ribuan setara 10 ratusan. Tambah ratusan awal {digits[-3]}, jadi {digits[-3]+10}.','sd4_dekomposisi_ribuan',level,scene)
        return make(f'Perhatikan {data}. Semua ribuan ditukar menjadi ratusan. Setelah dua ratusan disisihkan, seluruh ratusan yang tersisa ditukar menjadi puluhan. Berapa ikatan puluhan sekarang, termasuk puluhan lama? Satuan tidak ditukar.','10*(10*th+h-2)+t',{'th':digits[0],'h':digits[-3],'t':digits[-2]},f'Tukar {digits[0]} ribuan menjadi {10*digits[0]} ratusan; bersama yang lama menjadi {10*digits[0]+digits[-3]}. Sisihkan 2 ratusan, lalu tiap ratusan tersisa menjadi 10 puluhan. Tambah puluhan lama {digits[-2]}, hasil {10*(10*digits[0]+digits[-3]-2)+digits[-2]}.','sd4_dekomposisi_bertingkat',level,scene)
    # Four arithmetic operations, bounded by the curriculum quantities.
    arithmetic=(grade==3 and bab==1 and code in 'DEFG') or (grade==4 and bab==1 and code in 'EFGH')
    if arithmetic:
        operation={'D':'add','E':'sub','F':'mul','G':'div'}[code] if grade==3 else {'E':'add','F':'sub','G':'mul','H':'div'}[code]
        limit=100 if grade==3 or operation in ['mul','div'] else 1000
        if operation in ['add','sub']:
            v1=r.randint(limit//10,limit//3);v2=r.randint(limit//10,limit//3);extra=r.randint(2,9);scene=cards(['Kotak A','Kotak B'],[v1,v2]) if visual else None;source='banyak buku pada gambar' if visual else f'{v1} buku di kotak A dan {v2} di B'
            if operation=='add':
                if level=='easy':return make(f'{name} menggabungkan {source}. Berapa jumlah buku?','a+b',{'a':v1,'b':v2},f'Jumlahkan kedua kotak: {v1}+{v2}={v1+v2}.',f'sd{grade}_penjumlahan_dua_stok',level,scene)
                if level=='medium':return make(f'{name} menggabungkan {source}, lalu menerima {extra} buku lagi. Berapa buku seluruhnya?','a+b+extra',{'a':v1,'b':v2,'extra':extra},f'Gabungan awal {v1+v2}, lalu ditambah {extra}, hasil {v1+v2+extra}.',f'sd{grade}_penjumlahan_tiga_stok',level,scene)
                donated=r.randint(2,9);missing=r.randint(8,17);target=v1+v2+missing-donated
                return make(f'Persediaan awal {name} adalah {source}. Sebelum menyumbangkan {donated} buku, ia harus menerima tambahan buku sehingga persediaan setelah sumbangan tepat {target}. Berapa buku tambahan yang diperlukan?','target+donated-a-b',{'target':target,'donated':donated,'a':v1,'b':v2},f'Agar setelah sumbangan tersisa {target}, sebelum sumbangan harus ada {target+donated}. Persediaan awal {v1+v2}; selisih yang perlu ditambahkan {missing}.',f'sd{grade}_penjumlahan_balik_stok',level,scene)
            total=v1+v2;scene=cards(['Stok awal','Dikirim pertama'],[total,v1]) if visual else None;source='stok awal dan kiriman pertama pada gambar' if visual else f'stok awal {total} dan kiriman pertama {v1}'
            if level=='easy':return make(f'Perhatikan {source}. Berapa buku tersisa sesudah kiriman pertama?','n-a',{'n':total,'a':v1},f'Kurangi kiriman dari stok: {total}-{v1}={v2}.',f'sd{grade}_pengurangan_stok',level,scene)
            if level=='medium':return make(f'Perhatikan {source}. Sesudah kiriman pertama, dikirim lagi {extra} buku. Berapa tersisa?','n-a-extra',{'n':total,'a':v1,'extra':extra},f'Sisa pertama {v2}, kurangi kiriman kedua {extra}; sisa {v2-extra}.',f'sd{grade}_pengurangan_dua_tahap',level,scene)
            returned=r.randint(1,5);damage=r.randint(1,min(4,v2-extra+returned));final=v2-extra+returned-damage
            return make(f'Perhatikan {source}. Sesudah itu {extra} buku dikirim lagi. Dari kiriman pertama, {returned} buku dikembalikan ke stok. Lalu {damage} buku di stok rusak dan disisihkan. Berapa buku layak yang masih tersedia?','n-a-extra+returned-damage',{'n':total,'a':v1,'extra':extra,'returned':returned,'damage':damage},f'Sisa pertama {v2}; setelah kiriman kedua {v2-extra}; setelah kembali {v2-extra+returned}; keluarkan yang rusak, sisa layak {final}.',f'sd{grade}_pengurangan_audit_perubahan',level,scene)
        groups=r.randint(3,8);per=r.randint(3,9);total=groups*per
        if operation=='mul':
            scene=table(['Keterangan','Banyak'],[['Kotak',groups],['Isi tiap kotak',per]],'Persediaan alat tulis') if visual else None;source='data kotak pada gambar' if visual else f'{groups} kotak, masing-masing berisi {per} pensil'
            if level=='easy':return make(f'Dari {source}, berapa jumlah seluruh pensil?','g*p',{'g':groups,'p':per},f'Jumlah = banyak kotak × isi tiap kotak = {groups}×{per}={total}.',f'sd{grade}_perkalian_kelompok',level,scene)
            if level=='medium':return make(f'Dari {source}, 2 pensil tiap kotak dibagikan. Berapa pensil yang masih berada di seluruh kotak?','g*(p-2)',{'g':groups,'p':per},f'Tiap kotak tersisa {per-2}; seluruh kotak menyisakan {groups}×{per-2}={groups*(per-2)}.',f'sd{grade}_perkalian_sisa_perkelompok',level,scene)
            people=r.randint(2,groups);each=r.randint(1,max(1,total//people//2));reserve=r.randint(1,max(1,total-people*each-1));value=total-people*each-reserve
            return make(f'Persediaan {name} sesuai {source}. Sebanyak {people} anak masing-masing menerima {each} pensil. Sesudah pembagian, {reserve} pensil harus disimpan sebagai cadangan. Berapa pensil yang masih bebas digunakan?','g*p-people*each-reserve',{'g':groups,'p':per,'people':people,'each':each,'reserve':reserve},f'Stok {total}; kebutuhan anak {people*each}; sisa sesudah pembagian {total-people*each}. Kurangi cadangan {reserve}; bebas digunakan {value}.',f'sd{grade}_perkalian_kebutuhan_cadangan',level,scene)
        reserve=r.randint(1,5);partA=r.randint(3,total-3);partB=total-partA
        if level=='easy':
            scene=cards(['Seluruh benda','Banyak penerima'],[total,groups]) if visual else None;source='data pembagian pada gambar' if visual else f'{total} permen untuk {groups} anak'
            return make(f'Perhatikan {source}. Semua dibagi sama banyak tanpa sisa. Berapa permen tiap anak?','n/g',{'n':total,'g':groups},f'Bagian tiap anak {total}/{groups}={per}.',f'sd{grade}_pembagian_rata',level,scene)
        if level=='medium':
            scene=cards(['Persediaan','Cadangan'],[total+reserve,reserve]) if visual else None;source='persediaan dan cadangan pada gambar' if visual else f'persediaan {total+reserve}, cadangan {reserve}'
            return make(f'Dari {source}, cadangan tidak dibagikan. Sisanya dibagi rata kepada {groups} anak. Berapa tiap anak?','(n-r)/g',{'n':total+reserve,'r':reserve,'g':groups},f'Setelah cadangan disisihkan tersisa {total}; bagi {groups}, tiap anak {per}.',f'sd{grade}_pembagian_setelah_cadangan',level,scene)
        scene=cards(['Kotak A','Kotak B'],[partA+reserve,partB]) if visual else None;source='banyak permen dalam kotak A dan B pada gambar' if visual else f'{partA+reserve} permen di A, {partB} di B'
        return make(f'{name} menggabungkan {source}. Sebanyak {reserve} disimpan, sisanya dibagi rata kepada {groups} kelompok. Setiap kelompok harus menyisihkan satu permen. Berapa permen tiap kelompok yang boleh dimakan?','(a+b-r)/g-1',{'a':partA+reserve,'b':partB,'r':reserve,'g':groups},f'Gabungan {total+reserve}, setelah cadangan {total}. Bagian kelompok {per}, dan sesudah menyisihkan satu boleh dimakan {per-1}.',f'sd{grade}_pembagian_gabungan_cadangan',level,scene)
    if grade==4 and bab==1 and code=='I':
        base=r.randint(3,9);a=base*r.randint(3,9);b=base*r.randint(3,9);scene=cards(['Jeruk','Apel'],[a,b]) if visual else None;source='persediaan buah pada gambar' if visual else f'{a} jeruk dan {b} apel'
        if level=='easy':
            divisor=r.choice(s.divisors(a));return make(f'Jumlah jeruk pada {source} dibagi ke {divisor} kantong sama banyak. Berapa jeruk tiap kantong?','a/d',{'a':a,'d':divisor},f'{divisor} merupakan faktor {a}; jeruk tiap kantong {a//divisor}.','sd4_faktor_pembagian_langsung',level,scene)
        gcd=int(s.igcd(a,b))
        if level=='medium':return make(f'Dari {source}, kedua jenis buah dibagi tanpa sisa ke kantong identik. Berapa kantong terbanyak?','GCD(a,b)',{'a':a,'b':b},f'Banyak kantong harus faktor kedua jumlah. FPB({a},{b})={gcd}; itulah kantong terbanyak.','sd4_faktor_persekutuan',level,scene)
        # Explicit finite divisor check is retained rather than copied constants.
        capacity=r.randint(2,max(2,gcd));valid=[d for d in range(1,capacity+1) if a%d==0 and b%d==0];best=max(valid);expr='(a+b)/best'
        cert={'type':'sd_high_factors','inputs':{'a':a,'b':b},'capacity':capacity,'visual_bindings':[{'input':'a','path':['cards',0,'value']},{'input':'b','path':['cards',1,'value']}] if visual else []}
        return make(f'Dari {source}, semua buah dimasukkan ke kantong dengan isi setiap jenis sama dan tanpa sisa. Hanya tersedia {capacity} kantong. Jika kantong yang dipakai sebanyak mungkin, berapa total buah dalam tiap kantong?',expr,{'a':a,'b':b,'best':best},f'Faktor bersama yang tidak melebihi {capacity}: {valid}. Pilih {best} kantong. Isi setiap kantong {a//best}+{b//best}={(a+b)//best}.','sd4_faktor_kantong_terbatas',level,scene,certificate=cert)
    # Grade3 mathematical sentences: the unknown is an amount, not a formal variable.
    if grade==3 and bab==2:
        initial=r.randint(20,45);added=r.randint(10,25);removed=r.randint(3,9);target=initial+added-removed;scene=cards(['Mula-mula','Akhir'],[initial,target]) if visual else None;source='catatan jumlah awal dan akhir pada gambar' if visual else f'awal {initial}, akhir {target}'
        if code=='A':
            if level=='easy':return make(f'Perhatikan {source}. Jika tidak ada yang diambil, berapa tambahan agar jumlah awal menjadi jumlah akhir?','end-start',{'end':target,'start':initial},f'Kalimat penjumlahan {initial}+□={target}, jadi □={target-initial}.','sd3_kalimat_penjumlahan_kosong',level,scene)
            if level=='medium':return make(f'Perhatikan {source}. Sesudah penambahan, {removed} benda diambil. Berapa benda yang ditambahkan?','end+removed-start',{'end':target,'removed':removed,'start':initial},f'Sebelum pengambilan jumlahnya {target+removed}. Tambahan = {target+removed}-{initial}={added}.','sd3_kalimat_penjumlahan_balik',level,scene)
            more=r.randint(2,6)
            return make(f'Perhatikan {source}. Sesudah tambahan pertama, {removed} benda diambil. Kemudian ditambah {more} benda lagi sehingga mencapai jumlah akhir pada gambar. Berapa tambahan pertama?','end+removed-more-start',{'end':target,'removed':removed,'more':more,'start':initial},f'Balikkan perubahan: sebelum tambahan terakhir {target-more}, sebelum pengambilan {target-more+removed}. Kurangi awal {initial}; tambahan pertama {added-more}.','sd3_kalimat_penjumlahan_urutan_balik',level,scene)
        if level=='easy':return make(f'Perhatikan {source}. Berapa yang harus diambil dari jumlah akhir agar kembali ke jumlah awal?','end-start',{'end':target,'start':initial},f'Kalimat pengurangan {target}-□={initial}; □={target-initial}.','sd3_kalimat_pengurangan_kosong',level,scene)
        if level=='medium':return make(f'Perhatikan {source}. Jumlah awal mendapat tambahan {added}. Sebagian diambil hingga tersisa jumlah akhir pada gambar. Berapa yang diambil?','start+added-end',{'start':initial,'added':added,'end':target},f'Sebelum pengambilan {initial+added}; dikurangi akhir {target}, yang diambil {removed}.','sd3_kalimat_pengurangan_balik',level,scene)
        returned=r.randint(1,5)
        return make(f'Perhatikan {source}. Jumlah awal ditambah {added} benda. Lalu sebagian diambil, tetapi {returned} benda dari yang diambil dikembalikan. Jumlah terakhir sama dengan catatan akhir. Berapa benda yang semula diambil?','start+added+returned-end',{'start':initial,'added':added,'returned':returned,'end':target},f'Sebelum dikembalikan jumlah harus {target-returned}; sebelum diambil {initial+added}. Selisihnya {removed+returned}. Periksa: {initial}+{added}-{removed+returned}+{returned}={target}.','sd3_kalimat_pengurangan_kembali',level,scene)
    # Grade3 measurement: ruler zero-offsets and metric conversions.
    if grade==3 and bab==3:
        if code in 'AB':
            start=r.randint(2,7);length=r.randint(7,16);end=start+length
            scene={'kind':'ruler','start':0,'end':end+2,'step':1,'object_start':start,'object_end':end} if visual else None;source='posisi kedua ujung pita pada penggaris' if visual else f'ujung pita pada {start} cm dan {end} cm'
            if code=='A':
                if level=='easy':return make(f'Perhatikan {source}. Berapa panjang pita dalam cm?','end-start',{'end':end,'start':start},f'Panjang adalah selisih posisi ujung: {end}-{start}={length} cm.','sd3_panjang_penggaris_offset',level,scene)
                if level=='medium':return make(f'Panjang pita berasal dari {source}. Sebanyak {2} cm dipotong dari tiap ujung. Berapa panjang sisanya?','end-start-4',{'end':end,'start':start},f'Panjang awal {length}; dua ujung memotong total 4 cm. Sisa {length-4} cm.','sd3_panjang_potong_dua_ujung',level,scene)
                added=r.randint(4,9);overlap=r.randint(1,3);cut=r.randint(1,3)
                return make(f'Pita pertama ditunjukkan oleh {source}. Pita itu disambung dengan pita {added} cm, bertumpuk {overlap} cm. Lalu {cut} cm dipotong dari hasil sambungan. Berapa panjang akhir?','end-start+added-overlap-cut',{'end':end,'start':start,'added':added,'overlap':overlap,'cut':cut},f'Pita awal {length}. Sambungan tanpa tumpang tindih berjumlah {length+added}; kurangi bagian ganda {overlap}, lalu potongan {cut}. Hasil {length+added-overlap-cut} cm.','sd3_panjang_sambung_tumpang',level,scene)
            meters=r.randint(1,6);cm=r.randint(5,80);scene=table(['Ukuran','Nilai'],[['Meter',meters],['Sentimeter',cm]],'Panjang pita') if visual else None;source='ukuran pita pada tabel gambar' if visual else f'{meters} m {cm} cm'
            if level=='easy':return make(f'Nyatakan {source} dalam cm.','100*m+c',{'m':meters,'c':cm},f'1 m=100 cm, jadi {meters} m {cm} cm = {100*meters+cm} cm.','sd3_konversi_meter_cm',level,scene)
            if level=='medium':return make(f'Dari panjang {source}, dipotong {length} cm. Berapa panjang tersisa dalam cm?','100*m+c-cut',{'m':meters,'c':cm,'cut':length},f'Ubah ke cm menjadi {100*meters+cm}, kurangi {length}; sisa {100*meters+cm-length} cm.','sd3_konversi_potong_panjang',level,scene)
            pieces=r.randint(2,5);reserve=(100*meters+cm-length)%pieces or pieces;value=100*meters+cm-length-reserve
            return make(f'Panjang awal sesuai {source}. Sebanyak {length} cm dipakai untuk simpul dan {reserve} cm disimpan. Sisa dipotong menjadi {pieces} bagian sama panjang. Berapa panjang tiap bagian dalam cm?','(100*m+c-used-reserve)/pieces',{'m':meters,'c':cm,'used':length,'reserve':reserve,'pieces':pieces},f'Ubah panjang awal ke cm: {100*meters+cm}. Sisihkan simpul dan cadangan, sisa {value}. Tiap potongan = {value}/{pieces} cm.','sd3_konversi_panjang_pembagian',level,scene)
        kg=r.randint(1,6);gram=r.randint(1,8)*100;pack=r.randint(1,4)*100
        scene=table(['Bagian','Massa'],[['Kilogram',kg],['Gram tambahan',gram]],'Massa beras') if visual else None;source='massa pada gambar' if visual else f'{kg} kg {gram} g'
        if level=='easy':return make(f'Nyatakan {source} dalam gram.','1000*k+g',{'k':kg,'g':gram},f'1 kg=1000 g. Massa = {kg}×1000+{gram}={1000*kg+gram} g.',f'sd3_berat_konversi_{code.lower()}',level,scene)
        if level=='medium':return make(f'Beras bermassa {source}. Dipakai {pack} gram. Berapa gram yang tersisa?','1000*k+g-p',{'k':kg,'g':gram,'p':pack},f'Massa awal {1000*kg+gram} g. Setelah dipakai tersisa {1000*kg+gram-pack} g.',f'sd3_berat_konversi_pakai_{code.lower()}',level,scene)
        second=r.randint(2,7)*100;bags=r.choice([2,4,5]);usable=1000*kg+gram+second-pack
        return make(f'Beras awal bermassa {source}. Ditambah {second} g, kemudian {pack} g disisihkan. Sisa dimasukkan sama banyak ke {bags} kantong. Berapa gram dalam satu kantong?','(1000*k+g+added-reserved)/bags',{'k':kg,'g':gram,'added':second,'reserved':pack,'bags':bags},f'Konversi awal menjadi {1000*kg+gram} g. Setelah tambahan dan penyisihan sisa {usable} g; bagi {bags}, tiap kantong {s.Rational(usable,bags)} g.',f'sd3_berat_gabungan_bagi_{code.lower()}',level,scene)
    if grade==3 and bab==4:
        shape_pool=['triangle','square','rectangle','pentagon','hexagon']
        shapes=r.sample(shape_pool,3);scene={'kind':'shapes','items':[{'label':label,'shape':shape} for label,shape in zip(['P','Q','R'],shapes)]} if visual else None
        translated={'triangle':'segitiga','square':'persegi','rectangle':'persegi panjang','pentagon':'segi lima','hexagon':'segi enam','right_triangle':'segitiga siku-siku'}
        if code in 'AB':
            if code=='B':shapes=r.choices(['square','rectangle','right_triangle'],k=3);scene={'kind':'shapes','items':[{'label':label,'shape':shape} for label,shape in zip(['P','Q','R'],shapes)]} if visual else None
            prop=0 if code=='A' else 1
            if level=='easy':
                selected=shapes[:1];source='bangun P pada gambar' if visual else translated[shapes[0]];cert={'type':'sd_high_shapes','shapes':selected,'property':prop,'query':'sum'}
                return make(f'Berapa banyak '+('sisi' if code=='A' else 'sudut siku-siku')+f' pada {source}?','',{},'Kenali bangun, lalu hitung '+('segmen pembentuk batasnya.' if code=='A' else 'sudut yang membentuk seperempat putaran.'),f'sd3_bangun_{code.lower()}_langsung',level,scene,certificate=cert)
            source='bangun P,Q,R pada gambar' if visual else ', '.join(translated[t] for t in shapes)
            query='sum' if level=='medium' else 'filtered_sum' if code=='A' else 'difference';cert={'type':'sd_high_shapes','shapes':shapes,'property':prop,'query':query};answer=solve_certificate(cert)
            question=(f'Pada {source}, berapa jumlah seluruh '+('sisi?' if code=='A' else 'sudut siku-siku?')) if level=='medium' else (f'Periksa {source}. Pilih hanya bangun yang memiliki sudut siku-siku. Berapa jumlah sisi dari bangun yang dipilih?' if code=='A' else f'Untuk {source}, jumlahkan semua sisi, kemudian kurangi dengan jumlah seluruh sudut siku-siku. Berapa hasilnya?')
            return make(question,'',{},f'Identifikasi sifat tiap bangun sebelum menjumlahkan. Setelah '+('penyaringan bangun' if query=='filtered_sum' else 'penghitungan tiap sifat')+f', hasil {answer}.',f'sd3_bangun_{code.lower()}_gabung_sifat',level,scene,certificate=cert)
        # A horizontal, vertical, and oblique family, scaled without changing relations.
        scale=r.randint(2,5);segments=[[[0,0],[scale*3,0]],[[0,scale],[scale*3,scale]],[[scale, -1],[scale,2*scale+1]],[[0,2*scale],[3*scale,2*scale]]];r.shuffle(segments)
        scene={'kind':'lines','segments':segments,'labels':['1','2','3','4']} if visual else None;source='garis bernomor pada gambar' if visual else '; '.join('garis '+str(i+1)+(' mendatar' if p[0][1]==p[1][1] else ' tegak') for i,p in enumerate(segments))
        removed=[] if level!='hard' else [r.randrange(4)];query='parallel' if level=='easy' else 'right' if level=='medium' else 'both';cert={'type':'sd_high_lines','segments':segments,'removed':removed,'query':query}
        q=f'Perhatikan {source}. '+('Berapa pasangan garis sejajar?' if level=='easy' else 'Berapa pasangan garis tegak lurus?' if level=='medium' else f'Garis nomor {removed[0]+1} dihapus. Pada garis yang tersisa, hitung pasangan sejajar dan pasangan tegak lurus secara terpisah, lalu jumlahkan. Berapa hasilnya?')
        return make(q,'',{},f'Bandingkan arah tiap pasangan; pasangan dihitung sekali. '+(f'Hapus dulu garis {removed[0]+1}. ' if removed else '')+f'Hasil yang diminta {solve_certificate(cert)}.',f'sd3_relasi_garis_{level}',level,scene,certificate=cert)
    # Grade3 data interpretation / tallying raw observations.
    if grade==3 and bab==5:
        vals=r.sample(range(5,30),4);labels=['Apel','Jeruk','Pisang','Mangga'];scene={'kind':'bars','labels':labels,'values':vals} if visual else None;source='data buah pada diagram' if visual else '; '.join(f'{k} {v}' for k,v in zip(labels,vals))
        if code=='A':
            inputs=dict(zip(['a','b','c','d'],vals))
            if level=='easy':return make(f'Perhatikan {source}. Berapa frekuensi terbesar?','Max(a,b,c,d)',inputs,f'Bandingkan keempat frekuensi; terbesar {max(vals)}.','sd3_data_terbesar',level,scene)
            if level=='medium':return make(f'Perhatikan {source}. Berapa selisih frekuensi terbesar dan terkecil?','Max(a,b,c,d)-Min(a,b,c,d)',inputs,f'Frekuensi terbesar {max(vals)}, terkecil {min(vals)}. Selisih {max(vals)-min(vals)}.','sd3_data_banding_dua_ujung',level,scene)
            added=r.randint(2,8);expr='Abs((a+b+added)-(c+d))'
            return make(f'Perhatikan {source}. Kelompok I terdiri dari apel dan jeruk, kelompok II pisang dan mangga. Ada tambahan {added} pemilih untuk kelompok I. Berapa selisih mutlak jumlah kedua kelompok sesudah tambahan?',expr,{**inputs,'added':added},f'Awal kelompok I {vals[0]+vals[1]}, II {vals[2]+vals[3]}; tambahan membuat I={vals[0]+vals[1]+added}. Selisih mutlak {abs(vals[0]+vals[1]+added-vals[2]-vals[3])}.','sd3_data_kelompok_perubahan',level,scene)
        data=[6]+[r.choice([5,6,7,8]) for _ in range(r.randint(11,19))];r.shuffle(data);target=r.choice(data);counts=Counter(data)
        scene=table(['Nomor','Nilai'],[[i+1,v] for i,v in enumerate(data)],'Catatan nilai siswa') if visual else None;source='catatan nilai pada gambar' if visual else ', '.join(map(str,data))
        if level=='easy':return make(f'Dari {source}, berapa frekuensi nilai {target}?','',{},f'Buat turus untuk setiap kemunculan nilai {target}; ada {counts[target]}.','sd3_tabel_frekuensi_langsung',level,scene,certificate={'type':'sd_high_frequency','data':data,'target':target})
        scene=table(['Nilai','Frekuensi'],[[k,counts[k]] for k in [5,6,7,8]],'Tabel nilai siswa') if visual else None;source='tabel frekuensi pada gambar' if visual else '; '.join(f'nilai {k}: {counts[k]} siswa' for k in [5,6,7,8]);inputs={'a':counts[5],'b':counts[6],'c':counts[7],'d':counts[8]}
        if level=='medium':return make(f'Perhatikan {source}. Berapa siswa yang mendapat nilai sekurang-kurangnya 7?','c+d',inputs,f'Nilai yang memenuhi 7 dan 8. Frekuensi gabungan {counts[7]}+{counts[8]}={counts[7]+counts[8]}.','sd3_tabel_gabung_kategori',level,scene)
        transfer=r.randint(1,max(1,counts[6]));extra=r.randint(1,4);value=counts[7]+counts[8]+transfer+extra
        return make(f'Perhatikan {source}. Setelah koreksi, {transfer} siswa yang semula bernilai 6 berubah menjadi 7. Lalu ditambahkan catatan {extra} siswa baru bernilai 8. Berapa siswa bernilai sekurang-kurangnya 7 pada tabel akhir?','c+d+transfer+extra',{**inputs,'transfer':transfer,'extra':extra},f'Awal yang mencapai 7 ada {counts[7]+counts[8]}; koreksi menambah {transfer} tanpa menambah jumlah seluruh siswa. Data baru menambah {extra}; hasil {value}.','sd3_tabel_koreksi_tambah',level,scene)
    # Grade4 fractions and decimal/percent representations.
    if grade==4 and bab==2:
        den=r.choice([3,4,5,6,7,8,9,10,12]);num=r.randint(1,den-1);scene={'kind':'fraction_grid','rows':1,'cols':den,'shaded':num} if visual else None
        source='arsiran pada gambar' if visual else f'{num} dari {den} bagian sama besar'
        if code=='A':
            scene={'kind':'fraction_grid','rows':1,'cols':den,'shaded':1} if visual else None;source='satu bagian berarsir pada gambar' if visual else f'satu dari {den} bagian sama besar'
            if level=='easy':return make(f'Nyatakan {source} sebagai pecahan.','1/d',{'d':den},f'Satu bagian dari {den} bagian adalah 1/{den}.','sd4_pecahan_pembilang_satu',level,scene)
            pieces=r.randint(2,den-1)
            if level=='medium':return make(f'Ukuran satu bagian sesuai {source}. Jika {pieces} bagian seperti itu diambil, berapa bagian dari seluruh benda?','k/d',{'k':pieces,'d':den},f'Tiap bagian 1/{den}; {pieces} bagian menjadi {pieces}/{den}.','sd4_pecahan_satuan_beberapa',level,scene)
            taken=r.randint(1,pieces-1);more=1
            return make(f'Ukuran tiap bagian sesuai {source}. Mula-mula dipilih {pieces} bagian. Kemudian {taken} bagian dikembalikan dan satu bagian lain diambil lagi. Berapa bagian dari seluruh benda yang akhirnya dipilih?','(k-t+1)/d',{'k':pieces,'t':taken,'d':den},f'Banyak bagian terpilih {pieces}-{taken}+1={pieces-taken+1}. Karena setiap bagian 1/{den}, pecahan akhirnya {pieces-taken+1}/{den}.','sd4_pecahan_satuan_perubahan',level,scene)
        if code=='B':
            second=r.choice([v for v in range(1,den) if v!=num]);scene=table(['Bagian','Pembilang'],[['P',num],['Q',second],['Penyebut sama',den]]) if visual else None;source='pecahan P dan Q pada gambar' if visual else f'P={num}/{den}, Q={second}/{den}'
            if level=='easy':return make(f'Perhatikan {source}. Berapa nilai pecahan yang lebih besar?','Max(p,q)/d',{'p':num,'q':second,'d':den},f'Penyebut sama, pembilang lebih besar menentukan pecahan lebih besar. Nilainya {max(num,second)}/{den}.','sd4_pecahan_penyebut_banding',level,scene)
            if level=='medium':return make(f'Perhatikan {source}. Berapa selisih pecahan yang lebih besar dan lebih kecil?','Abs(p-q)/d',{'p':num,'q':second,'d':den},f'Penyebut tetap {den}, kurangi pembilang. Selisih {abs(num-second)}/{den}.','sd4_pecahan_penyebut_selisih',level,scene)
            # Choosing a portion to equalize two pieces, in units of the common denominator.
            den=r.choice([5,6,7,8,9,10,12]);p=r.randint(2,den-2);q=r.randint(1,p-1);added=r.randint(1,den-p-1);scene=table(['Pecahan','Pembilang'],[['P',p],['Q',q],['Penyebut sama',den]]) if visual else None;source='pecahan P dan Q pada gambar' if visual else f'P={p}/{den}, Q={q}/{den}'
            return make(f'Perhatikan {source if not visual else "pecahan P,Q pada gambar"}. Dari P dipindahkan bagian sebesar selisih P dan Q ke Q. Kemudian Q ditambah lagi {added}/{den}. Berapa pecahan Q terakhir?','(q+(p-q)+added)/d',{'p':p,'q':q,'added':added,'d':den},f'Selisih P-Q={p-q}/{den}. Q sesudah menerima selisih menjadi {p}/{den}; tambahan terakhir memberi {p+added}/{den}.','sd4_pecahan_penyebut_transfer',level,scene)
        if code=='C':
            factor=r.randint(2,5);newden=den*factor
            if level=='easy':return make(f'Pecahan pada {source} disederhanakan. Berapa nilainya?','n/d',{'n':num,'d':den},f'Bagian berarsir {num}/{den}; bentuk sederhana {s.Rational(num,den)}.','sd4_pecahan_senilai_sederhana',level,scene)
            if level=='medium':return make(f'Pecahan yang ditunjukkan oleh {source} ditulis dengan penyebut {newden}. Berapa pembilangnya?','n*newden/d',{'n':num,'d':den,'newden':newden},f'Penyebut dikali {factor}; pembilang juga dikali {factor}, sehingga {num*factor}.','sd4_pecahan_senilai_pembilang',level,scene)
            secondfactor=r.randint(2,4);targetden=den*factor*secondfactor
            return make(f'Pecahan dari {source} mula-mula ditulis dengan penyebut {newden}, kemudian ditulis lagi dengan penyebut {targetden}. Berapa selisih pembilang bentuk terakhir dan bentuk pertama yang berpenyebut {newden}?','n*(last-first)/d',{'n':num,'d':den,'last':targetden,'first':newden},f'Pembilang pada penyebut {newden}: {num*factor}. Pada penyebut {targetden}: {num*factor*secondfactor}. Selisih {num*factor*(secondfactor-1)}.','sd4_pecahan_senilai_dua_bentuk',level,scene)
        den=100;num=r.randint(5,85);scene={'kind':'fraction_grid','rows':10,'cols':10,'shaded':num} if visual else None;source='petak berarsir pada grid 100 petak' if visual else f'{num} dari 100 petak'
        if code=='D':
            if level=='easy':return make(f'Nyatakan bagian {source} sebagai bilangan desimal.','n/100',{'n':num},f'{num}/100={num/100:.2f}; nilainya {s.Rational(num,100)}.','sd4_desimal_perseratusan',level,scene)
            more=r.randint(1,9)
            if level=='medium':return make(f'Bagian awal sesuai {source}. Setelah {more} petak lagi diarsir, berapa bagian berarsir dalam bentuk desimal?','(n+more)/100',{'n':num,'more':more},f'Petak berarsir kini {num+more} dari 100, yaitu {(num+more)/100:.2f}.','sd4_desimal_tambah_petak',level,scene)
            erase=r.randint(2,min(8,num));add=r.randint(1,9)
            return make(f'Bagian awal sesuai {source}. {erase} petak dihapus arsirannya, kemudian {add} petak kosong diarsir. Berapa selisih mutlak bagian berarsir akhir terhadap 0,50?','Abs((n-erase+add)/100-1/2)',{'n':num,'erase':erase,'add':add},f'Jumlah akhir {num-erase+add} petak, desimal {(num-erase+add)/100:.2f}. Bandingkan dengan 0,50: selisih mutlak {s.Rational(abs(num-erase+add-50),100)}.','sd4_desimal_perubahan_banding',level,scene)
        if level=='easy':return make(f'Berapa persen bagian {source}?','n',{'n':num},f'Persen berarti per seratus; {num} dari 100 sama dengan {num}%.','sd4_persen_grid',level,scene)
        added=r.randint(1,9)
        if level=='medium':return make(f'Data awal sesuai {source}. Sesudah {added} petak kosong diarsir, berapa persen petak berarsir?','n+added',{'n':num,'added':added},f'Jumlah arsir {num+added} dari 100, jadi {num+added}%.','sd4_persen_perubahan',level,scene)
        goal=r.randint(90,99);removed=r.randint(1,4)
        return make(f'Awal arsiran sesuai {source}. {removed} petak berarsir dihapus. Setelah itu, berapa petak kosong perlu diarsir agar tepat {goal}% dari seluruh petak berarsir?','goal-(n-removed)',{'goal':goal,'n':num,'removed':removed},f'Setelah dihapus tersisa {num-removed} petak berarsir. Target {goal}% berarti {goal} petak. Tambahan {goal}-{num-removed}={goal-num+removed}.','sd4_persen_target_setelah_hapus',level,scene)
    if grade==4 and bab==3:
        if code=='A':
            unit=r.choice([['circle','square'],['triangle','square','circle'],['circle','triangle','triangle']]);target=r.choice(unit);symbols={'circle':'lingkaran','square':'persegi','triangle':'segitiga'};visible=list(unit);scene={'kind':'pattern','items':visible} if visual else None;source='satu unit pola pada gambar' if visual else 'satu unit pola '+', '.join(symbols[z] for z in unit)
            if level=='easy':
                positions=r.randint(7,12);skip=0
            elif level=='medium':positions=r.randint(13,20);skip=r.randint(1,3)
            else:positions=r.randint(21,35);skip=r.randint(4,8)
            cert={'type':'sd_high_pattern','unit':unit,'target':target,'length':positions,'skip':skip}
            q=f'Perhatikan {source}. Pola berulang terus. '+(f'Dari {positions} bentuk pertama, berapa {symbols[target]}?' if skip==0 else f'Sebanyak {skip} bentuk pertama dilepas. Dari {positions} bentuk berikutnya, berapa yang berupa {symbols[target]}?')
            return make(q,'',{},f'Satu unit pola {list(map(symbols.get,unit))}. Mulai hitung setelah melewati {skip} bentuk, gunakan kelompok pola utuh dan sisa. Jumlah {symbols[target]} yang diminta {solve_certificate(cert)}.','sd4_pola_gambar_posisi_hitung',level,scene,certificate=cert)
        first=r.randint(3,20);step=r.randint(2,9);vals=[first+i*step for i in range(4)];scene=cards(['1','2','3','4'],vals) if visual else None;source='empat bilangan pada gambar' if visual else ', '.join(map(str,vals))
        if level=='easy':return make(f'Perhatikan {source}. Polanya bertambah tetap. Berapa bilangan berikutnya?','d+(d-c)',{'c':vals[2],'d':vals[3]},f'Beda tetap {step}; setelah {vals[3]} adalah {vals[3]+step}.','sd4_pola_bilangan_lanjut',level,scene)
        n=r.randint(7,12)
        if level=='medium':return make(f'Perhatikan {source}. Pola bertambah tetap. Berapa bilangan pada urutan ke-{n}?','a+(n-1)*(b-a)',{'a':first,'b':first+step,'n':n},f'Beda {step}. Dari suku pertama, lakukan {n-1} penambahan; hasil {first+(n-1)*step}.','sd4_pola_bilangan_urutan',level,scene)
        cutoff=first+n*step;extra=r.randint(1,step-1) if step>2 else 1
        return make(f'Perhatikan {source}. Pola bertambah tetap. Berapa nomor urutan bilangan pertama yang lebih besar dari {cutoff+extra}?','floor((cutoff-a)/(b-a))+2',{'a':first,'b':first+step,'cutoff':cutoff+extra},f'Beda {step}; nilai pada urutan {n+1} adalah {cutoff}, masih belum melewati batas {cutoff+extra}. Urutan berikutnya {n+2} bernilai {cutoff+step}, sudah lebih besar.','sd4_pola_bilangan_batas_urutan',level,scene)
    if grade==4 and bab==4:
        length=r.randint(4,9);width=r.randint(3,7);height=r.randint(2,5)
        if code=='A':
            cut=r.randint(1,width-1);scene={'kind':'area_grid','rows':width,'cols':length,'shaded':length*width,'cell_label':'1 cm2'} if visual else None;source='persegi satuan pada gambar' if visual else f'{width} baris dengan {length} persegi satuan per baris';total=length*width
            if level=='easy':return make(f'Bangun tersusun dari {source}; tiap petak luasnya 1 cm². Berapa luas seluruh bangun?','l*w',{'l':length,'w':width},f'Ada {width}×{length}={total} petak, jadi {total} cm².','sd4_luas_petak_satuan',level,scene)
            if level=='medium':return make(f'Bangun awal tersusun dari {source}; tiap petak 1 cm². {cut} baris penuh dipotong. Berapa luas tersisa?','l*(w-cut)',{'l':length,'w':width,'cut':cut},f'Sisa baris {width-cut}, tiap baris {length} petak. Luas {length*(width-cut)} cm².','sd4_luas_potong_baris',level,scene)
            attached=r.randint(2,5);overlap=r.randint(1,min(attached,length)-1)
            return make(f'Bangun awal terdiri dari {source}, tiap petak 1 cm². Ditempel bangun kedua seluas {attached*width} cm². Keduanya bertumpang tindih seluas {overlap*width} cm², lalu {cut} petak dari batas luar dipotong. Berapa luas gabungan akhir?','l*w+attached-overlap-cut',{'l':length,'w':width,'attached':attached*width,'overlap':overlap*width,'cut':cut},f'Luas awal {total}. Tambah luas kedua {attached*width}, kurangi tumpang tindih {overlap*width} sekali agar tidak ganda, lalu potongan {cut}. Luas akhir {total+attached*width-overlap*width-cut} cm².','sd4_luas_gabungan_tumpang_potong',level,scene)
        scene={'kind':'volume_blocks','length':length,'width':width,'height':height} if visual else None;source='susunan kubus pada gambar' if visual else f'{length} kubus sepanjang baris, {width} baris tiap lapisan, {height} lapisan';total=length*width*height
        if level=='easy':return make(f'Perhatikan {source}. Semua lapisan terisi penuh tanpa rongga. Berapa kubus satuan penyusunnya?','l*w*h',{'l':length,'w':width,'h':height},f'Tiap lapisan {length*width} kubus, ada {height} lapisan; total {total}.','sd4_volume_susunan_penuh',level,scene)
        if level=='medium':return make(f'Dari {source} yang penuh tanpa rongga, satu lapisan paling atas diambil. Berapa kubus tersisa?','l*w*(h-1)',{'l':length,'w':width,'h':height},f'Satu lapisan {length*width} kubus; lapisan tersisa {height-1}, total {length*width*(height-1)}.','sd4_volume_ambil_lapisan',level,scene)
        extra=r.randint(2,7);remove=r.randint(1,min(length,width)-1)
        return make(f'Dari {source} yang penuh tanpa rongga, satu lapisan paling atas diambil. Setelah itu diambil lagi satu tiang tegak setinggi seluruh sisa susunan. Lalu ditambah {extra} kubus satuan di luar susunan. Berapa jumlah kubus akhir?','l*w*(h-1)-(h-1)+extra',{'l':length,'w':width,'h':height,'extra':extra},f'Sesudah lapisan atas diambil sisa {length*width*(height-1)} kubus. Tiang berikutnya hanya setinggi {height-1} karena lapisan atas sudah hilang. Kurangi sekali, tambah {extra}; hasil {length*width*(height-1)-(height-1)+extra}.','sd4_volume_lapisan_tiang_bertahap',level,scene)
    if grade==4 and bab==5:
        if code=='A':
            shapes=r.sample(['square','rectangle','triangle','pentagon','hexagon'],3);scene={'kind':'shapes','items':[{'label':label,'shape':sh} for label,sh in zip(['P','Q','R'],shapes)]} if visual else None;namesh={'square':'persegi','rectangle':'persegi panjang','triangle':'segitiga','pentagon':'segi lima','hexagon':'segi enam'}
            source='bangun P,Q,R pada gambar' if visual else ', '.join(namesh[t] for t in shapes)
            if level=='easy':cert={'type':'sd_high_shapes','shapes':shapes[:1],'query':'sum','property':0};q=f'Berapa banyak sisi bangun P pada gambar?' if visual else f'Berapa banyak sisi {namesh[shapes[0]]}?'
            elif level=='medium':cert={'type':'sd_high_shapes','shapes':shapes,'query':'filtered_sum','property':0};q=f'Perhatikan {source}. Berapa jumlah sisi bangun-bangun yang memiliki sudut siku-siku?'
            else:cert={'type':'sd_high_shapes','shapes':shapes,'query':'difference','property':0};q=f'Perhatikan {source}. Jumlahkan seluruh sisi dari ketiga bangun, lalu kurangi jumlah seluruh sudut siku-sikunya. Berapa hasilnya?'
            return make(q,'',{},f'Kenali ciri setiap bangun dari sisi dan sudutnya. Hasil perhitungan sifat yang diminta {solve_certificate(cert)}.','sd4_ciri_bangun_klasifikasi_hitung',level,scene,certificate=cert)
        length=r.randint(5,10);width=r.randint(3,7);removed=r.randint(1,width-1);scene={'kind':'area_grid','rows':width,'cols':length,'shaded':length*width,'cell_label':'1 petak'} if visual else None;source='susunan petak persegi pada gambar' if visual else f'persegi panjang {width} baris, masing-masing {length} petak'
        if level=='easy':return make(f'Perhatikan {source}. Bangun diurai menjadi semua petak persegi satuan. Berapa petak penyusunnya?','l*w',{'l':length,'w':width},f'Tiap baris {length} petak dan ada {width} baris; jumlah {length*width}.','sd4_dekomposisi_petakan',level,scene)
        if level=='medium':return make(f'Perhatikan {source}. Bangun dipotong sejajar baris menjadi bagian {removed} baris dan sisanya. Berapa banyak petak pada bagian yang lebih besar?','l*Max(cut,w-cut)',{'l':length,'w':width,'cut':removed},f'Dua bagian mempunyai {removed} dan {width-removed} baris. Pilih jumlah baris lebih besar lalu kali {length}; hasil {length*max(removed,width-removed)}.','sd4_dekomposisi_banding_bagian',level,scene)
        extra=r.randint(2,6);overlap=r.randint(1,min(extra,length)-1)
        return make(f'Perhatikan {source}. Bangun dipotong sebanyak {removed} baris penuh. Bagian yang tersisa disusun bersama {extra} petak baru; {overlap} petak baru menutupi petak lama, bukan memperluas bangun. Berapa petak pada bangun gabungan akhir?','l*(w-cut)+extra-overlap',{'l':length,'w':width,'cut':removed,'extra':extra,'overlap':overlap},f'Sisa setelah penguraian {length*(width-removed)} petak. Tambahan efektif hanya {extra}-{overlap}={extra-overlap}; total {length*(width-removed)+extra-overlap}.','sd4_komposisi_setelah_urai',level,scene)
    if grade==4 and bab==6:
        unit=r.choice([2,3,4,5]);counts=r.sample(range(3,10),3);labels=['Kelas A','Kelas B','Kelas C'];values=[u*unit for u in counts];scene={'kind':'pictogram' if code=='A' else 'bars','labels':labels,'values':values,'unit':unit} if visual else None;source='diagram pada gambar' if visual else '; '.join(f'{label}={v}' for label,v in zip(labels,values));inputs=dict(zip(['a','b','c'],values))
        if level=='easy':return make(f'Perhatikan {source}. Berapa jumlah pada kelas A?','a',inputs,f'Baca kelas A dengan memperhatikan skala/keterangan simbol: jumlahnya {values[0]}.',f'sd4_diagram_{code.lower()}_baca',level,scene)
        if level=='medium':return make(f'Perhatikan {source}. Berapa selisih jumlah terbesar dan terkecil?','Max(a,b,c)-Min(a,b,c)',inputs,f'Terbesar {max(values)}, terkecil {min(values)}; selisih {max(values)-min(values)}.',f'sd4_diagram_{code.lower()}_banding',level,scene)
        transfer=r.randint(1,min(values[0],values[1])-1);extra=r.randint(2,7);expr='Abs((a-transfer)+(b+transfer)-(c+extra))'
        return make(f'Perhatikan {source}. {transfer} siswa pindah dari A ke B, lalu C mendapat {extra} siswa baru. Berapa selisih mutlak gabungan A dan B dengan C sesudah perubahan?',expr,{**inputs,'transfer':transfer,'extra':extra},f'A menjadi {values[0]-transfer}, B {values[1]+transfer}; gabungan A+B tetap {values[0]+values[1]}. C menjadi {values[2]+extra}. Selisih mutlak {abs(values[0]+values[1]-values[2]-extra)}.',f'sd4_diagram_{code.lower()}_transfer_gabung',level,scene)
    raise ValueError((grade,bab,code,level))
