"""Replacement capacity for deficits revealed by the second local content review."""
from copy import deepcopy
from itertools import product
import sympy as s

from .sd_difficulty_review import assess


def solve_certificate(cert):
    kind=cert['type']
    if kind=='sd_review_shape_budget':
        properties={'square':(4,4),'rectangle':(4,4),'right_triangle':(3,1),'triangle':(3,0),'pentagon':(5,0)}
        total=sum(properties[sh][cert['property']] for sh in cert['shapes'] if properties[sh][1]>0)
        return s.Integer(max(0,total*cert['cost']-cert['stock']))
    p=cert['inputs']
    if kind=='sd_review_pattern_minimum':
        unit=p['unit'];skip=p['skip'];symbol=p['symbol'];goal=p['goal'];last=p['last']
        for length in range(1,101):
            seq=[unit[(skip+i)%len(unit)] for i in range(length)]
            if seq.count(symbol)>=goal and seq[-1]==last:return s.Integer(length)
        raise ValueError('Pattern constraints impossible')
    if kind=='sd_review_grid_route':
        grid=p['grid'];start=tuple(p['start']);blocked=tuple(p['blocked']);length=p['length'];candidates=[]
        def visit(pos,n,visited):
            if n==0:candidates.append(grid[pos[0]][pos[1]]);return
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                q=(pos[0]+dr,pos[1]+dc)
                if q==blocked or q in visited or not 0<=q[0]<3 or not 0<=q[1]<3:continue
                visit(q,n-1,visited|{q})
        visit(start,length,{start});assert candidates
        return s.Integer(max(candidates))
    if kind=='sd_review_fraction_minimum':
        n=p['denominator'];already=p['shaded'];feasible=[k for k in range(already,n+1) if 2*k>n and k%2==0]
        assert feasible;return s.Rational(min(feasible)-already,n)
    raise ValueError(kind)


def fmt(value):return '$'+s.latex(s.sympify(value))+'$'


def make(question,expression,inputs,solution,family,scene,bindings=(),cert=None):
    from .sd_bank_low import solve_certificate as solve_low
    cert=cert or {'type':'sd_low_expression','expression':expression,'inputs':inputs}
    value=solve_certificate(cert) if cert['type'].startswith('sd_review') else solve_low(cert)
    if bindings:cert['visual_bindings']=[{'input':name,'path':path} for name,path in bindings]
    proposal=([1-value,value/2,(value+1)/2,value**2,s.Rational(1,3),s.Rational(2,3)] if 0<value<1 else [value+1,value-1,value+2,value+3,value/2])
    wrong=[]
    for v in proposal:
        v=s.sympify(v)
        if v<0 or v==value or v in wrong:continue
        wrong.append(v)
        if len(wrong)==3:break
    assert len(wrong)==3
    decision=assess(question,cert,family,0,scene);assert decision['assessedLevel'] is not None
    return {'question':question,'answer':fmt(value),'wrong':list(map(fmt,wrong)),'explanation':solution+' Hasil akhirnya '+fmt(value)+'.',
            'kind':family,'steps':decision['steps'],'rationale':decision['reason'],'scene':scene,'certificate':cert}


def generate(grade,bab,code,level,r,visual,index):
    from .sd_bank_low import generate as low
    from .sd_bank_high import generate as high
    original=low if grade<=2 else high
    # Most slots already have appropriate variants; reject accidental shortcuts.
    if not ((grade<=2 and ((level=='medium' and ((grade==1 and (bab==1 and code=='A' or bab==5 and code=='A' or bab==8)) or (grade==2 and (bab in (1,7) and code=='A' or bab==8 or bab==6 and code=='B')))) or (level=='hard' and ((grade==1 and bab==5 and code=='C') or (grade==2 and (bab==1 and code=='B' or bab==4)))) or (grade==2 and bab==4 and code=='B' and level=='easy')))
            or (grade==3 and bab==4) or (grade==4 and ((bab==2 and code in 'ABE') or (bab==3 and code=='A') or (bab==5 and code=='A') or (bab==6 and level=='hard')))):
        model=original(grade,bab,code,level,r,visual,index)
        d=assess(model['question'],model['certificate'],model['kind'],grade,model['scene'])
        if d['assessedLevel']==level:return model
        return None
    if grade<=2:
        if level=='medium' and (bab==8 or grade==1 and bab==8):
            a,b,c=[r.randint(2,9) for _ in range(3)];extra=r.randint(1,3)
            scene={'kind':'pictogram' if code=='B' or grade==1 else 'tally','labels':['Apel','Jeruk','Pisang'],'values':[a,b,c],'unit':1} if visual else None
            intro='Banyak pemilih tiap buah tercatat pada gambar.' if visual else f'Pemilih apel {a}, jeruk {b}, pisang {c} anak.'
            return make(intro+f' Sebanyak {extra} anak baru memilih jeruk. Berapa jumlah pemilih jeruk dan pisang sekarang?','b+c+extra',{'a':a,'b':b,'c':c,'extra':extra},f'Jeruk menjadi {b+extra}; tambahkan {c} pemilih pisang.','sd_review_data_update',scene,[('b',['values',1]),('c',['values',2])] if visual else [])
        if level=='medium' and bab==6 and code=='B':
            hour=r.randint(6,10);minute=r.choice([0,30]);duration=r.choice([10,15,20]);target=hour+1;scene={'kind':'clock','hour':hour,'minute':minute} if visual else None
            intro='Jam pada gambar menunjukkan awal kegiatan.' if visual else f'Kegiatan dimulai pukul {hour:02d}.{minute:02d}.'
            return make(intro+f' Setelah belajar {duration} menit, berapa menit lagi sampai pukul {target:02d}.00?','60-minute-duration',{'minute':minute,'duration':duration},f'Selisih awal ke jam berikutnya {60-minute} menit; kurangi {duration} menit kegiatan.','sd_review_clock_interval',scene,[('minute',['minute'])] if visual else [])
        if level=='medium':
            cap=10 if grade==1 and bab==1 else 20 if grade==1 else 50 if bab==1 else 100
            a=r.randint(2,cap//2);b=r.randint(1,cap-a);take=r.randint(1,min(a,3));scene={'kind':'groups','groups':[{'label':'A','count':a,'shape':'circle'},{'label':'B','count':b,'shape':'circle'}]} if visual else None
            intro='Lihat banyak benda di A dan B pada gambar.' if visual else f'A berisi {a} benda, B berisi {b} benda.'
            return make(intro+f' Dari A diambil {take} benda. Sisanya digabung dengan B. Berapa jumlah gabungannya?','a-t+b',{'a':a,'b':b,'t':take},f'A tersisa {a-take}, lalu gabungkan dengan {b} benda di B.','sd_review_count_update',scene,[('a',['groups',0,'count']),('b',['groups',1,'count'])] if visual else [])
        if (grade==1 and bab==5 and code=='C') or (grade==2 and bab==1 and code=='B'):
            tens=r.randint(1,1 if grade==1 else 4);units=r.randint(1,8);n=10*tens+units;need=r.randint(units+1,min(n,units+15))
            scene={'kind':'cards','cards':[{'label':'Banyak lidi','value':n}]} if visual else None
            intro='Jumlah lidi diperlihatkan pada kartu.' if visual else f'Ada {n} lidi.'
            return make(intro+f' Lidi dibuat menjadi ikatan berisi 10 dan sisanya satuan lepas. Sebanyak {need} lidi harus diberikan dalam bentuk satuan lepas. Buka ikatan sesedikit mungkin. Berapa lidi lepas tersisa setelah pemberian?','Mod(n,10)+10*ceiling((need-Mod(n,10))/10)-need',{'n':n,'need':need},f'Awalnya ada {units} satuan lepas, belum cukup untuk {need}. Buka {(need-units+9)//10} ikatan; jumlah lepas bertambah kelipatan 10. Setelah memberikan {need}, hitung sisanya.','sd_review_place_minimum_open',scene,[('n',['cards',0,'value'])] if visual else [])
        if bab==4 and code=='A':
            cells=r.sample(range(1,10),9);grid=[cells[i:i+3] for i in (0,3,6)];blocked=r.choice([[0,0],[0,2],[2,0],[2,2]]);start=[1,1]
            scene={'kind':'table','headers':['Kiri','Tengah','Kanan'],'rows':grid} if visual else None
            intro='Susunan kartu terlihat pada gambar.' if visual else f'Kartu tiga baris dari atas adalah {grid[0]}, {grid[1]}, {grid[2]}.'
            cert={'type':'sd_review_grid_route','inputs':{'grid':grid,'start':start,'blocked':blocked,'length':2}}
            rr,cc=blocked;labels=['kiri','tengah','kanan']
            question=intro+f' Mulai di tengah. Bergerak tepat dua langkah ke kotak yang bersisian, tidak boleh kembali ke kotak yang sudah dilewati. Kotak baris {rr+1} kolom {labels[cc]} ditutup. Berapa bilangan terbesar yang mungkin menjadi tujuan?'
            if visual:
                cert['visual_bindings']=[]
                for y in range(3):
                    for z in range(3):
                        cert['visual_bindings'].append({'input':'grid','input_path':[y,z],'path':['rows',y,z]})
            return make(question,None,{},'Periksa tujuan yang bisa dicapai dengan dua langkah, singkirkan kotak tertutup dan langkah yang kembali, lalu bandingkan bilangan pada tujuan sah.','sd_review_grid_route',scene,cert=cert)
        if bab==4 and code=='B':return pattern(r,visual,level,grade)
    if grade==3 and bab==4 and code=='C':
        k=r.randint(2,5);segments=[[[0,0],[3*k,0]],[[0,k],[3*k,k]],[[0,2*k],[3*k,2*k]],[[k,-1],[k,2*k+1]]]
        if level=='hard':segments.append([[0,-1],[3*k,3*k-1]])
        r.shuffle(segments);removed=r.randrange(len(segments));scene={'kind':'lines','segments':segments,'labels':[str(i+1) for i in range(len(segments))]} if visual else None
        directions=['mendatar' if p[0][1]==p[1][1] else 'tegak' if p[0][0]==p[1][0] else 'miring naik' for p in segments]
        intro='Perhatikan garis-garis pada gambar.' if visual else 'Arah garis bernomor adalah '+', '.join(str(i+1)+' '+v for i,v in enumerate(directions))+'. Garis miring naik membentuk sudut 45 derajat terhadap garis mendatar.'
        cert={'type':'sd_high_lines','segments':segments,'removed':[removed],'query':'right' if level=='medium' else 'both'}
        if visual:
            cert['visual_bindings']=[]
            for i,p in enumerate(segments):
                cert['visual_bindings'].append({'input':'segments','input_path':[i,1,1],'path':['segments',i,1,1]})
        from .sd_bank_high import solve_certificate as high_solve
        value=high_solve(cert)
        if level=='medium':family='sd_review_lines_after_removal';ask='berapa pasangan garis tegak lurus yang masih ada?'
        else:family='sd_review_lines_mixed';ask='hitung pasangan sejajar dan pasangan tegak lurus pada garis yang tersisa. Berapa jumlah kedua hitungan itu?'
        q=intro+f' Garis nomor {removed+1} dihapus. '+ask[0].upper()+ask[1:]
        # Keep the same exact geometry certificate but use the reviewed family.
        from .sd_bank_high import make as high_make
        model=high_make(q,'',{},f'Keluarkan garis {removed+1}, lalu periksa tiap pasangan yang tersisa sekali. Garis miring tidak otomatis sejajar atau tegak lurus dengan semua garis lain. Hasil {value}.',family,level,scene,certificate=cert)
        return model
    if (grade==3 and bab==4 and code in 'AB') or (grade==4 and bab==5 and code=='A'):
        shapes=r.sample(['square','rectangle','right_triangle','triangle','pentagon'],3)
        if not any(sh in ('square','rectangle','right_triangle') for sh in shapes):return None
        scene={'kind':'shapes','items':[{'label':label,'shape':sh} for label,sh in zip('PQR',shapes)]} if visual else None
        names={'square':'persegi','rectangle':'persegi panjang','right_triangle':'segitiga siku-siku','triangle':'segitiga sama sisi','pentagon':'segi lima beraturan'}
        intro='Tiga bangun ditunjukkan oleh gambar.' if visual else 'Bangunnya adalah '+', '.join(names[sh] for sh in shapes)+'.'
        prop=1 if grade==3 and code=='B' else 0;quantity=sum(({'square':4,'rectangle':4,'right_triangle':1}[sh] if prop==1 else {'square':4,'rectangle':4,'right_triangle':3}[sh]) for sh in shapes if sh in ('square','rectangle','right_triangle'));cost=r.choice([2,3]);stock=r.randint(1,max(2,quantity*cost-1))
        cert={'type':'sd_review_shape_budget','shapes':shapes,'property':prop,'cost':cost,'stock':stock}
        if visual:cert['visual_bindings']=[{'input':'shapes','input_path':[i],'path':['items',i,'shape'],'alternatives':['triangle','square','right_triangle','pentagon']} for i in range(3)]
        noun='sudut siku-siku' if prop==1 else 'sisi'
        q=intro+f' Pilih hanya bangun yang mempunyai sudut siku-siku. Pada setiap {noun} dari bangun terpilih dipasang {cost} stiker. Sudah tersedia {stock} stiker. Berapa stiker tambahan paling sedikit yang dibutuhkan?'
        return make(q,None,{},f'Bangun yang dipilih {[names[sh] for sh in shapes if sh in ("square","rectangle","right_triangle")]}. Jumlah {noun} yang dihias {quantity}; perlu {quantity*cost} stiker. Kurangi stok {stock}.','sd_review_shape_budget',scene,cert=cert)
    if grade==4:
        if bab==2 and code=='A':
            den=r.randint(4,12);scene={'kind':'fraction_grid','rows':1,'cols':den,'shaded':1} if visual else None
            intro='Gambar menunjukkan satu bagian satuan dari sebuah benda utuh.' if visual else f'Sebuah benda utuh terbagi menjadi {den} bagian sama besar; satu bagian sudah diwarnai.'
            if level=='medium':
                take=r.randint(3,den);back=r.randint(1,take-1)
                return make(intro+f' Sebanyak {take} bagian dipilih, lalu {back} bagian dikembalikan. Berapa pecahan benda yang masih dipilih?','(a-b)/d',{'a':take,'b':back,'d':den},f'Bagian terpilih tinggal {take-back}. Tiap bagian bernilai 1/{den}.','sd_review_fraction_update',scene,[('d',['cols'])] if visual else [])
            cert={'type':'sd_review_fraction_minimum','inputs':{'denominator':den,'shaded':1},'visual_bindings':[{'input':'denominator','path':['cols']}] if visual else []}
            return make(intro+' Bagian yang diwarnai harus lebih banyak daripada bagian putih dan jumlah bagian berwarna harus genap. Berapa pecahan tambahan paling sedikit yang harus diwarnai?',None,{},f'Cari bilangan genap terkecil yang lebih besar dari setengah {den}. Kurangi satu bagian yang sudah berwarna, kemudian tulis sebagai pecahan berpenyebut {den}.','sd_review_fraction_minimum',scene,cert=cert)
        if bab==2 and code=='B':
            den=r.randint(7,12);p=r.randint(4,den-1);q=r.randint(1,p-3);added=r.randint(1,p-q-1);transfer=(p-q-added+1)//2
            scene={'kind':'table','headers':['Bagian','Pembilang'], 'rows':[['P',p],['Q',q],['Penyebut sama',den]]} if visual else None
            intro='Pecahan P dan Q ditunjukkan dalam tabel.' if visual else f'P={p}/{den}, Q={q}/{den}.'
            return make(intro+f' Q ditambah {added}/{den}. Sesudah itu, beberapa bagian satuan 1/{den} dipindahkan dari P ke Q agar Q paling sedikit sama besar dengan P. Pemindahan dilakukan sesedikit mungkin. Berapa pecahan P sesudah pemindahan?','(p-ceiling((p-q-added)/2))/d',{'p':p,'q':q,'added':added,'d':den},f'Q mula-mula menjadi {q+added}/{den}. Tiap satu bagian dipindah, selisih pembilang mengecil 2. Perlu minimal {transfer} bagian; P tersisa {p-transfer}/{den}.','sd_review_fraction_balance',scene,[('p',['rows',0,1]),('q',['rows',1,1]),('d',['rows',2,1])] if visual else [])
        if bab==2 and code=='E':
            n=r.randint(15,65);removed=r.randint(1,10);package=r.choice([4,5,10]);goal=r.randint(n+1,90);packs=(goal-(n-removed)+package-1)//package;value=n-removed+package*packs
            if value>100:return None
            scene={'kind':'fraction_grid','rows':10,'cols':10,'shaded':n} if visual else None;intro='Persentase awal terlihat pada grid 100 petak.' if visual else f'Pada grid 100 petak, {n} petak berarsir.'
            return make(intro+f' Mula-mula {removed} arsiran dihapus. Setelah itu arsiran hanya boleh ditambah dalam paket {package} petak. Targetnya sedikitnya {goal}% berarsir. Dengan paket sesedikit mungkin, berapa persen petak akhirnya berarsir?','n-removed+package*ceiling((goal-n+removed)/package)',{'n':n,'removed':removed,'package':package,'goal':goal},f'Awal sesudah hapus {n-removed} petak. Kekurangan ke target {goal-n+removed}; dibutuhkan {packs} paket utuh. Akhir {value} petak dari 100.','sd_review_percent_packages',scene,[('n',['shaded'])] if visual else [])
        if bab==3 and code=='A':return pattern(r,visual,level,grade)
        if bab==6:
            a,b,c=r.sample(range(8,35),3);transfer=r.randint(1,min(a,b)-1);new=r.randint(2,7);unit=1 if code=='B' else r.choice([1,2]);a*=unit;b*=unit;c*=unit
            scene={'kind':'bars' if code=='B' else 'pictogram','labels':['Kelas A','Kelas B','Kelas C'],'values':[a,b,c],'unit':unit} if visual else None;intro='Jumlah siswa pada tiga kelas ditunjukkan oleh diagram.' if visual else f'Jumlah siswa A={a}, B={b}, C={c}.'
            # Comparing each updated class prevents the old transfer cancellation.
            return make(intro+f' Sebanyak {transfer} siswa pindah dari A ke B, lalu C mendapat {new} siswa baru. Berapa selisih antara kelas terbanyak dan tersedikit sesudah perubahan?','Max(a-t,b+t,c+n)-Min(a-t,b+t,c+n)',{'a':a,'b':b,'c':c,'t':transfer,'n':new},f'Perbarui ketiga kelas menjadi {a-transfer}, {b+transfer}, {c+new}; tentukan maksimum dan minimum baru lalu kurangkan.','sd_review_diagram_reorder',scene,[('a',['values',0]),('b',['values',1]),('c',['values',2])] if visual else [])
    return None


def pattern(r,visual,level,grade):
    unit=r.sample(['circle','square','triangle'],r.choice([2,3]));words={'circle':'lingkaran','square':'persegi','triangle':'segitiga'};target=r.choice(unit)
    scene={'kind':'pattern','items':unit} if visual else None;intro='Satu unit pola tampak pada gambar.' if visual else 'Satu unit pola adalah '+', '.join(words[v] for v in unit)+'.'
    if level=='easy':
        cert={'type':'sd_high_pattern','unit':unit,'length':len(unit),'skip':0,'target':target}
        if visual:cert['visual_bindings']=[{'input':'unit','input_path':[i],'path':['items',i],'alternatives':['circle','square','triangle']} for i in range(len(unit))]
        from .sd_bank_high import make as high_make
        return high_make(intro+f' Pada satu unit itu saja, berapa banyak {words[target]}?','',{},f'Hitung hanya dalam satu unit yang tertulis/terlihat: {unit.count(target)}.','sd_review_pattern_read','easy',scene,certificate=cert)
    skip=r.randint(1,3 if grade==2 else 7);goal=r.randint(3,5 if grade==2 else 9);last=r.choice(unit);cert={'type':'sd_review_pattern_minimum','inputs':{'unit':unit,'skip':skip,'symbol':target,'goal':goal,'last':last}}
    if visual:
        cert['visual_bindings']=[{'input':'unit','input_path':[i],'path':['items',i],'alternatives':['circle','square','triangle']} for i in range(len(unit))]
        cert['visual_bindings'].append({'input':'unit','path':['items'],'alternatives':[unit[i:]+unit[:i] for i in range(1,len(unit))]})
    return make(intro+f' Pola diulang terus dan {skip} bentuk pertama dibuang. Dari awal sisa, akan diambil potongan yang memuat sedikitnya {goal} {words[target]} dan berakhir dengan {words[last]}. Berapa bentuk paling sedikit dalam potongan itu?',None,{},f'Lanjutkan pola sesudah membuang {skip} bentuk. Periksa jumlah {words[target]} dan bentuk terakhir bersama-sama; pilih potongan terpendek yang memenuhi kedua syarat.','sd_review_pattern_minimum',scene,cert=cert)
