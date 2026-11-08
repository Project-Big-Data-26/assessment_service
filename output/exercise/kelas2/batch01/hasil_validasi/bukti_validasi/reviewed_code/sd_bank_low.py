"""Reference-adaptable primary 1--2 exercises, authored offline.

The certificate stores the model and its inputs rather than a claimed answer.
Visual bindings name facts read from the diagram; prose does not repeat them.
"""
from collections import Counter
import sympy as s

NAMES = ['Nina','Damar','Siti','Beni','Lani','Raka','Mira','Tomi']
OBJECTS = ['kancing','manik-manik','kelereng','stiker','keping mainan','kartu']
SIDES = {'circle':0,'triangle':3,'square':4,'rectangle':4}


def solve_certificate(cert):
    inputs = cert['inputs']
    kind = cert['type']
    if kind == 'sd_low_grid':
        row,col=inputs['start'];grid=inputs['grid']
        for dr,dc in inputs['moves']:
            row+=dr;col+=dc
            assert 0<=row<len(grid) and 0<=col<len(grid[0])
        return s.Integer(grid[row][col])
    if kind == 'sd_low_pattern':
        period=inputs['period'];target=inputs['target'];start=inputs.get('start',0);end=inputs['end']
        return s.Integer(sum(period[i%len(period)]==target for i in range(start,end)))
    if kind != 'sd_low_expression':raise ValueError(kind)
    local={key:s.Rational(str(value)) for key,value in inputs.items()}
    local.update(Abs=s.Abs,Max=s.Max,Min=s.Min,Mod=s.Mod,floor=s.floor)
    value=s.simplify(s.sympify(cert['expression'],locals=local))
    assert not value.free_symbols and value.is_real and value.is_finite
    return value


def _fmt(value):return '$'+s.latex(s.sympify(value))+'$'


def _item(question,explanation,family,level,expr,inputs,scene=None,bindings=(),*,steps=None,cert_type='sd_low_expression'):
    cert={'type':cert_type,'inputs':inputs}
    if expr is not None:cert['expression']=str(expr)
    if bindings:cert['visual_bindings']=[{'input':name,'path':path} for name,path in bindings]
    value=solve_certificate(cert)
    wrong=[]
    candidates=([1-value,value/2,(1+value)/2,s.Rational(1,4),s.Rational(3,4),1,0]
                if 0<value<1 else [value+1,value-1,value+2,value-2,value+3,value+4])
    for v in candidates:
        v=s.simplify(v)
        if v<0 or v==value or any(v==w for w in wrong):continue
        wrong.append(v)
        if len(wrong)==3:break
    assert len(wrong)==3
    return {'question':question,'answer':_fmt(value),'wrong':[_fmt(v) for v in wrong],
            'explanation':explanation,'kind':family,'steps':steps or {'easy':1,'medium':2,'hard':4}[level],
            'rationale':{'easy':'Membaca satu informasi atau melakukan satu prosedur langsung sesuai lingkup kelas.',
             'medium':'Menghubungkan dua informasi melalui dua langkah yang saling bergantung.',
             'hard':'Memilih informasi yang relevan, memperbarui atau mengelompokkan keadaan, lalu membandingkan atau menentukan hasil akhir.'}[level],
            'scene':scene,'certificate':cert}


def _cards(values,labels=None,title='Kartu bilangan'):
    return {'kind':'cards','title':title,'cards':[{'label':lab,'value':int(v)} for lab,v in zip(labels or list('ABCDEFG'),values)]}


def _groups(values,shapes=None):
    return {'kind':'groups','groups':[{'label':lab,'count':int(v),'shape':shape} for lab,v,shape in zip('ABC',values,shapes or ['circle']*len(values))]}


def _bind_cards(names):return [(name,['cards',i,'value']) for i,name in enumerate(names)]
def _bind_groups(names):return [(name,['groups',i,'count']) for i,name in enumerate(names)]


def _counts(grade,bab,code,level,r,visual,cap):
    name=r.choice(NAMES);obj=r.choice(OBJECTS)
    if grade==1:
        u=r.randint(11,18) if cap==20 else r.randint(2,min(5,cap-3))
        v=r.randint(1,cap-u) if cap==20 else r.randint(1,min(4,cap-u))
    else:
        u=r.randint(11,max(12,cap//2));v=r.randint(5,min(cap-u,cap//2))
    take=r.randint(1,min(2,u))
    scene=_groups([u,v]) if visual else None
    intro=f'Perhatikan dua kelompok {obj}, A dan B, pada gambar. ' if visual else f'{name} mempunyai {u} {obj} di wadah A dan {v} di wadah B. '
    binding=_bind_groups(['a','b']) if visual else []
    if level=='easy':
        return _item(intro+'Berapa banyak benda pada kelompok A?',f'Hitung satu per satu benda kelompok A. Ada {u} benda.','sd_low_membilang_langsung',level,'a',{'a':u,'b':v},scene,binding)
    if level=='medium':
        return _item(intro+'Semua benda kedua kelompok disatukan. Berapa banyak bendanya?',f'Kelompok A berisi {u}, B berisi {v}. Gabungkan dan hitung: {u}+{v}={u+v}.','sd_low_membilang_gabungan',level,'a+b',{'a':u,'b':v},scene,binding)
    # Counting visible groups after a physical move is within concrete numbers.
    return _item(intro+f'{take} benda dari A dipindahkan ke B. Berapa selisih banyak benda kedua kelompok sesudah dipindahkan?',
        f'Mula-mula A={u}, B={v}. Sesudah dipindahkan A={u-take}, B={v+take}. Bandingkan jumlah baru; selisihnya {abs(u-take-v-take)}.',
        'sd_low_membilang_pindah_banding',level,'Abs((a-t)-(b+t))',{'a':u,'b':v,'t':take},scene,binding)


def _compare(grade,level,r,visual,cap,objects=False):
    low=r.randint(1,cap-4);high=low+r.randint(2,min(6,cap-low));extra=r.randint(1,min(3,cap-high)) if high<cap else 1
    scene=_groups([low,high]) if visual and objects else _cards([low,high]) if visual else None
    intro=('Amati kelompok A dan B pada gambar. ' if objects else 'Kartu A dan B menyatakan banyak benda pada masing-masing kelompok. Baca bilangan pada kedua kartu. ') if visual else f'Kartu A dan B menyatakan banyak benda pada masing-masing kelompok. Bilangan pada kartu A adalah {low}, pada kartu B {high}. '
    binding=(_bind_groups(['a','b']) if objects else _bind_cards(['a','b'])) if visual else []
    if level=='easy':return _item(intro+'Berapa selisih bilangan yang lebih besar dan lebih kecil?',f'Bilangan lebih besar {high}, lebih kecil {low}; selisih {high-low}.','sd_low_banding_selisih',level,'b-a',{'a':low,'b':high},scene,binding)
    if level=='medium':
        return _item(intro+f'Jumlah A ditambah {extra}. Berapa selisih A dan B sekarang?',f'A baru {low+extra}. Bandingkan dengan B={high}; selisih {abs(low+extra-high)}.','sd_low_banding_setelah_tambah',level,'Abs(a+t-b)',{'a':low,'b':high,'t':extra},scene,binding)
    move=r.randint(1,min(2,high));give=r.randint(1,min(2,low))
    return _item(intro+f'{move} benda dari B dipindahkan ke A, lalu {give} benda dari A diberikan kepada teman. Berapa selisih jumlah A dan B pada akhir kegiatan?',
        f'Sesudah pindah, A={low+move} dan B={high-move}. Setelah memberi, A={low+move-give}. Selisih akhir {abs(low+move-give-high+move)}.',
        'sd_low_banding_dua_perubahan',level,'Abs((a+t-g)-(b-t))',{'a':low,'b':high,'t':move,'g':give},scene,binding)


def _walk(level,r,visual,cap):
    start=r.randint(2,cap-4);forward=r.randint(1,min(4,cap-start));back=r.randint(1,min(2,start));again=r.randint(1,min(2,cap-(start+forward-back)))
    scene=_cards([start],['Mulai']) if visual else None;binding=[('a',['cards',0,'value'])] if visual else []
    intro='Mulailah dari bilangan pada kartu. ' if visual else f'Mulailah dari bilangan {start}. '
    if level=='easy':return _item(intro+f'Hitung maju {forward} langkah, satu bilangan tiap langkah. Bilangan berapakah yang dicapai?',f'Dari {start}, hitung maju {forward}: sampai {start+forward}.','sd_low_hitung_maju',level,'a+p',{'a':start,'p':forward},scene,binding)
    if level=='medium':return _item(intro+f'Hitung maju {forward} langkah lalu mundur {back} langkah. Bilangan berapakah yang dicapai?',f'Sesudah maju sampai {start+forward}. Mundur {back}, sampai {start+forward-back}.','sd_low_maju_mundur',level,'a+p-q',{'a':start,'p':forward,'q':back},scene,binding)
    return _item(intro+f'Hitung maju {forward} langkah, mundur {back} langkah, lalu maju lagi {again} langkah. Bilangan berapakah yang dicapai pada akhir seluruh gerakan?',
        f'Tahap pertama sampai {start+forward}; tahap kedua {start+forward-back}; terakhir {start+forward-back+again}. Jadi bilangan akhirnya {start+forward-back+again}.',
        'sd_low_urutan_tiga_gerak',level,'a+p-q+t',{'a':start,'p':forward,'q':back,'t':again},scene,binding)


def _pairs(level,r,visual):
    total=r.randint(6,10);shown=r.randint(1,total-2);gain=r.randint(1,min(2,total-shown));
    scene=_cards([total,shown],['Jumlah semua','Kelompok A']) if visual else None;binding=_bind_cards(['n','a']) if visual else []
    intro='Kartu menunjukkan jumlah semua benda dan banyak benda kelompok A. Sisanya berada di B. ' if visual else f'Ada {total} benda di kelompok A dan B. Kelompok A memiliki {shown} benda. '
    if level=='easy':return _item(intro+'Berapa benda di B?',f'Pasangan untuk melengkapi {total} dari {shown} adalah {total-shown}; B berisi {total-shown}.','sd_low_pasangan_pelengkap',level,'n-a',{'n':total,'a':shown},scene,binding)
    if level=='medium':return _item(intro+f'{gain} benda dari B dipindahkan ke A. Berapa benda di B sekarang?',f'Semula B={total}-{shown}={total-shown}. Setelah pindah {gain}, B tinggal {total-shown-gain}.','sd_low_pasangan_setelah_pindah',level,'n-a-t',{'n':total,'a':shown,'t':gain},scene,binding)
    return _item(intro+f'{gain} benda dari B dipindahkan ke A. Sesudah itu, berapa selisih banyak benda A dan B?',f'Cari B semula: {total-shown}. Sesudah pindah A={shown+gain}, B={total-shown-gain}; selisih {abs(shown+gain-(total-shown-gain))}.','sd_low_pasangan_ubah_banding',level,'Abs((a+t)-(n-a-t))',{'n':total,'a':shown,'t':gain},scene,binding)


def _operations(grade,bab,code,level,r,visual,cap,subtract=False):
    obj=r.choice(OBJECTS);name=r.choice(NAMES)
    if subtract:
        start=r.randint(max(6,cap//2),cap);first=r.randint(1,min(3,start-3));back=r.randint(1,min(3,cap-start+first));second=r.randint(1,min(2,start-first+back))
        scene=_groups([start]) if visual else None;binding=[('a',['groups',0,'count'])] if visual else []
        intro=f'{name} memiliki {obj} sebanyak yang tampak pada gambar. ' if visual else f'{name} mempunyai {start} {obj}. '
        if level=='easy':return _item(intro+f'Ia memberikan {first} benda. Berapa sisanya?',f'Sisa {start}-{first}={start-first}.','sd_low_pengurangan_konkret',level,'a-p',{'a':start,'p':first},scene,binding)
        if level=='medium':return _item(intro+f'Ia memberi {first} benda lalu mendapat {back} benda lagi. Berapa miliknya sekarang?',f'Sesudah memberi tinggal {start-first}. Tambah {back}, menjadi {start-first+back}.','sd_low_pengurangan_pemulihan',level,'a-p+q',{'a':start,'p':first,'q':back},scene,binding)
        return _item(intro+f'Ia memberi {first} benda, mendapat kembali {back} benda, kemudian memberi lagi {second} benda. Berapa benda yang dimilikinya setelah seluruh kegiatan?',
            f'Urutan jumlahnya {start-first}, {start-first+back}, lalu {start-first+back-second}. Jadi jumlah akhirnya {start-first+back-second}.',
            'sd_low_pengurangan_tiga_perubahan',level,'a-p+q-t',{'a':start,'p':first,'q':back,'t':second},scene,binding)
    first=r.randint(1,max(2,cap//3));second=r.randint(1,min(max(2,cap//3),cap-first-2));third=r.randint(1,min(3,cap-first-second));remove=r.randint(1,min(2,first+second))
    scene=_groups([first,second]) if visual else None;binding=_bind_groups(['a','b']) if visual else []
    intro=f'{name} memiliki {obj} pada kelompok A dan B di gambar. ' if visual else f'{name} mempunyai {first} {obj} di A dan {second} di B. '
    if level=='easy':return _item(intro+'Keduanya digabung. Berapa jumlahnya?',f'Jumlah {first}+{second}={first+second}.','sd_low_penjumlahan_gabung',level,'a+b',{'a':first,'b':second},scene,binding)
    if level=='medium':return _item(intro+f'Setelah digabung, ia mendapat {third} benda lagi. Berapa jumlah akhirnya?',f'Jumlah dua kelompok {first+second}. Tambahkan {third}; hasil {first+second+third}.','sd_low_penjumlahan_tiga_bagian',level,'a+b+c',{'a':first,'b':second,'c':third},scene,binding)
    return _item(intro+f'Kedua kelompok digabung, ditambah {third} benda dari teman, lalu {remove} benda diberikan kepada adik. Berapa jumlah akhirnya?',
        f'Gabungkan {first}+{second}={first+second}. Tambah {third} menjadi {first+second+third}; kurangi {remove}, tersisa {first+second+third-remove}.',
        'sd_low_penjumlahan_konteks_berubah',level,'a+b+c-d',{'a':first,'b':second,'c':third,'d':remove},scene,binding)


def _place(grade,level,r,visual,cap):
    tens=r.randint(1,cap//10-1 if cap>=50 else 1);units=r.randint(1,9 if cap>=50 else min(9,cap-10));number=tens*10+units;give=r.randint(1,units);extra=r.randint(1,3)
    scene=_cards([number],['Bilangan']) if visual else None;binding=[('a',['cards',0,'value'])] if visual else []
    intro='Perhatikan bilangan pada kartu. ' if visual else f'Perhatikan bilangan {number}. '
    if level=='easy':return _item(intro+'Berapa angka pada tempat satuannya?',f'{number} terdiri dari {tens} puluhan dan {units} satuan; angka satuan {units}.','sd_low_tempat_satuan',level,'Mod(a,10)',{'a':number},scene,binding)
    if level=='medium':return _item(intro+f'Bilangan itu dikurangi {give} satuan. Berapa angka satuan pada hasilnya?',f'{number}-{give}={number-give}. Angka satuannya {units-give}.','sd_low_tempat_ubah_satuan',level,'Mod(a-t,10)',{'a':number,'t':give},scene,binding)
    return _item(intro+f'Bilangan itu dibuat dengan ikatan sepuluh lidi dan lidi satuan. Satu ikatan dibuka menjadi lidi satuan; lalu {give} lidi satuan diberikan kepada teman. Berapa lidi satuan yang tidak terikat sekarang?',
        f'Awalnya ada {units} lidi satuan dan {tens} ikatan. Membuka satu ikatan menambah 10 satuan, menjadi {10+units}. Sesudah memberi {give}, satuan tidak terikat {10+units-give}.','sd_low_tempat_tukar_ikatan',level,'Mod(a,10)+10-t',{'a':number,'t':give},scene,binding)


def _shapes(grade,code,level,r,visual):
    tri=r.randint(2,5);square=r.randint(1,4);circle=r.randint(2,5);remove=r.randint(1,min(2,tri));add=r.randint(1,2)
    scene=_groups([tri,square,circle],['triangle','square','circle']) if visual else None;binding=_bind_groups(['a','b','c']) if visual else []
    intro='Perhatikan kelompok bangun A, B, dan C pada gambar. ' if visual else f'Ada {tri} segitiga, {square} persegi, dan {circle} lingkaran. '
    if code=='C':
        return _composition(level,r,visual)
    if level=='easy':return _item(intro+'Berapa banyak bangun berbentuk segitiga?',f'Bangun dengan tiga sisi lurus adalah segitiga; jumlahnya {tri}.','sd_low_ciri_bentuk',level,'a',{'a':tri,'b':square,'c':circle},scene,binding)
    if level=='medium':return _item(intro+'Bangun yang memiliki sudut dimasukkan ke satu kotak. Berapa jumlah bangun dalam kotak itu?',f'Segitiga dan persegi mempunyai sudut; lingkaran tidak. Jumlah {tri}+{square}={tri+square}.','sd_low_kelompok_berdasarkan_sudut',level,'a+b',{'a':tri,'b':square,'c':circle},scene,binding)
    return _item(intro+f'{remove} segitiga diambil dan {add} lingkaran ditambahkan. Berapa selisih banyak bangun yang memiliki sudut dengan yang tidak memiliki sudut sekarang?',
        f'Yang bersudut semula {tri+square}; sesudah diambil menjadi {tri+square-remove}. Lingkaran menjadi {circle+add}. Selisih kedua kelompok {abs(tri+square-remove-circle-add)}.',
        'sd_low_ciri_klasifikasi_perubahan',level,'Abs((a+b-t)-(c+g))',{'a':tri,'b':square,'c':circle,'t':remove,'g':add},scene,binding)


def _composition(level,r,visual):
    tri=r.randint(4,10);square=r.randint(1,4)
    scene=_groups([tri,square],['right_triangle','square']) if visual else None;binding=_bind_groups(['a','b']) if visual else []
    intro='Gambar menunjukkan keping segitiga siku-siku sama kaki yang identik pada A dan keping persegi pada B. ' if visual else f'Ada {tri} keping segitiga siku-siku sama kaki identik dan {square} keping persegi. '
    rule='Setiap dua keping segitiga dapat disatukan menjadi satu persegi yang sama besar dengan keping persegi yang ada. '
    if level=='easy':return _item(intro+rule+'Berapa persegi utuh yang dapat dibuat dari kelompok segitiga saja?',f'Pasangkan segitiga berdua-dua. Ada {tri//2} pasangan lengkap; {tri%2} segitiga tersisa.','sd_low_susun_dua_segitiga',level,'floor(a/2)',{'a':tri,'b':square},scene,binding)
    if level=='medium':return _item(intro+rule+'Berapa persegi seluruhnya setelah semua pasangan segitiga disusun dan digabung dengan persegi yang sudah ada?',f'Segitiga menghasilkan {tri//2} persegi. Tambahkan {square} persegi yang ada; total {tri//2+square}.','sd_low_susun_gabung_persegi',level,'floor(a/2)+b',{'a':tri,'b':square},scene,binding)
    return _item(intro+rule+'Setelah semua persegi dikumpulkan, dua persegi digabung berdampingan untuk membuat satu persegi panjang. Berapa persegi panjang utuh yang dapat dibuat?',
        f'Segitiga membentuk {tri//2} persegi; dengan yang sudah ada menjadi {tri//2+square}. Pasangkan persegi berdua-dua. Diperoleh {(tri//2+square)//2} persegi panjang utuh; sisa persegi {(tri//2+square)%2}.','sd_low_susun_dua_tahap',level,'floor((floor(a/2)+b)/2)',{'a':tri,'b':square},scene,binding)


def _length(level,r,visual,measure=False):
    start=r.randint(0,4);length=r.randint(4,10);second=r.randint(2,7);cut=r.randint(1,min(3,length-1));add=r.randint(1,3)
    scene={'kind':'ruler','start':0,'end':max(16,start+length+2),'step':1,'unit':'satuan','object_start':start,'object_end':start+length} if visual and measure else _cards([length,second],['Pita A (satuan)','Pita B (satuan)']) if visual else None
    binding=([('u',['object_start']),('v',['object_end'])] if measure else _bind_cards(['a','b'])) if visual else []
    inputs={'u':start,'v':start+length,'a':length,'b':second,'t':cut,'g':add}
    # For a ruler, all calculations use its endpoints, never an unbound copied length.
    base='v-u' if measure else 'a';exprbase='('+base+')'
    intro='Panjang pita diukur pada deretan petak satuan dalam gambar; ujung kiri tidak selalu di nol. ' if visual and measure else 'Baca panjang pita A dan B pada kartu gambar. ' if visual else f'Pita A panjangnya {length} satuan, pita B {second} satuan. '
    if level=='easy':return _item(intro+('Berapa panjang pita yang ditunjukkan?' if measure else 'Berapa selisih panjang kedua pita?'),f'Panjang A={length} satuan. '+(f'Kurangi posisi akhir {start+length} dengan awal {start}.' if measure else f'Panjang B={second}; selisih {abs(length-second)} satuan.'),'sd_low_panjang_langsung',level,base if measure else 'Abs(a-b)',inputs,scene,binding)
    if level=='medium':return _item(intro+f'Pita A dipotong {cut} satuan. Berapa selisih panjang pita A yang tersisa dengan pita sepanjang {second} satuan?',f'Panjang awal A={length}; sesudah dipotong {cut} tersisa {length-cut} satuan. Bandingkan dengan {second}, selisih {abs(length-cut-second)} satuan.','sd_low_panjang_potong_banding',level,'Abs('+exprbase+'-t-b)',inputs,scene,binding)
    return _item(intro+f'Pita A dipotong {cut} satuan, lalu disambung dengan pita baru sepanjang {add} satuan tanpa tumpang tindih. Berapa selisih panjang pita A terakhir dengan pita sepanjang {second} satuan?',
        f'Panjang A mula-mula {length}; setelah potong {length-cut}; setelah sambung {length-cut+add}. Bandingkan dengan {second}; selisih {abs(length-cut+add-second)} satuan.','sd_low_panjang_perubahan_banding',level,'Abs('+exprbase+'-t+g-b)',inputs,scene,binding)


def _data(grade,code,level,r,visual):
    vals=[r.randint(2,9) for _ in range(3)];a,b,c=vals;move=r.randint(1,min(2,a));add=r.randint(1,3);labels=['Apel','Jeruk','Pisang'];kind='pictogram' if code=='B' else 'tally' if grade==2 else 'groups'
    scene=({'kind':kind,'labels':labels,'values':vals,'unit':1} if kind!='groups' else _groups(vals,['circle','square','triangle'])) if visual else None
    binding=([(name,['values',i]) for i,name in enumerate(['a','b','c'])] if kind!='groups' else _bind_groups(['a','b','c'])) if visual else []
    intro='Perhatikan data pada gambar. ' if visual else f'Data pilihan buah: apel {a}, jeruk {b}, pisang {c} anak. '
    if visual and kind=='groups':intro+='Kelompok A adalah pilihan apel, B jeruk, C pisang. '
    if level=='easy':return _item(intro+'Berapa anak yang memilih apel?',f'Baca kategori apel (A): {a} anak.','sd_low_data_frekuensi',level,'a',{'a':a,'b':b,'c':c},scene,binding)
    if level=='medium':return _item(intro+'Berapa jumlah anak yang memilih jeruk atau pisang?',f'Jeruk {b}, pisang {c}. Jumlah {b}+{c}={b+c}.','sd_low_data_gabung_kategori',level,'b+c',{'a':a,'b':b,'c':c},scene,binding)
    return _item(intro+f'{move} anak yang tercatat memilih apel ternyata memilih jeruk; perbaiki catatannya. Kemudian {add} anak baru memilih pisang. Berapa selisih banyak pemilih jeruk dan pisang setelah perbaikan?',
        f'Koreksi kategori membuat jeruk menjadi {b+move}; apel turun menjadi {a-move}. Pisang bertambah menjadi {c+add}. Selisih jeruk dan pisang {abs(b+move-c-add)}.','sd_low_data_koreksi_kategori',level,'Abs((b+t)-(c+g))',{'a':a,'b':b,'c':c,'t':move,'g':add},scene,binding)


def _fractions(code,level,r,visual):
    divisor=4 if code=='C' else 2
    if code=='B':
        a=2*r.randint(2,6);b=2*r.randint(2,5);take=2*r.randint(1,min(2,(a+b)//2-1));scene=_groups([a,b]) if visual else None;binding=_bind_groups(['a','b']) if visual else []
        intro='Gambar menunjukkan kelompok benda A dan B. ' if visual else f'Kelompok A berisi {a} benda, B {b} benda. '
        if level=='easy':return _item(intro+'Setengah dari kelompok A diberikan kepada teman. Berapa benda yang diberikan?',f'Bagi A menjadi dua kelompok sama banyak: {a}/2={a//2}.','sd_low_setengah_kumpulan',level,'a/2',{'a':a,'b':b},scene,binding)
        if level=='medium':return _item(intro+'Setengah dari A dan setengah dari B disatukan. Berapa jumlah benda yang disatukan?',f'Setengah A={a//2}, setengah B={b//2}; jumlah {(a+b)//2}.','sd_low_setengah_dua_kumpulan',level,'a/2+b/2',{'a':a,'b':b},scene,binding)
        return _item(intro+f'Kedua kelompok digabung. Sebanyak {take} benda diambil, lalu sisanya dibagi kepada dua anak sama banyak. Berapa benda yang diterima setiap anak?',
            f'Jumlah awal {a+b}; sesudah diambil tersisa {a+b-take}. Setengah sisa={(a+b-take)//2}; masing-masing menerima sebanyak itu.','sd_low_setengah_setelah_perubahan',level,'(a+b-t)/2',{'a':a,'b':b,'t':take},scene,binding)
    denominator=divisor*r.randint(2,4);half=denominator//divisor
    shade1=half if level=='easy' else r.randint(0,max(0,half-1));shade2=r.randint(half+1,denominator)
    panel=lambda n,lab:{'kind':'fraction_grid','rows':divisor,'cols':denominator//divisor,'shaded':n,'title':lab}
    scene={'kind':'panels','panels':[panel(shade1,'Kue A'),panel(shade2,'Kue B')]} if visual else None
    binding=[('n',['panels',0,'rows']),('k',['panels',0,'cols']),('a',['panels',0,'shaded']),('b',['panels',1,'shaded'])] if visual else []
    inputs={'n':divisor,'k':denominator//divisor,'a':shade1,'b':shade2,'d':divisor}
    word='seperempat' if divisor==4 else 'setengah'
    intro='Kedua kue pada gambar sama besar, dipotong menjadi petak-petak sama luas. ' if visual else f'Dua kue sama besar masing-masing dibagi {denominator} petak sama luas. A memiliki {shade1} petak berwarna, B {shade2}. '
    if level=='easy':return _item(intro+'Berapa bagian kue A yang berwarna?',f'A mempunyai {shade1} dari {denominator} petak; pecahannya {shade1}/{denominator}={s.Rational(shade1,denominator)}.','sd_low_bagian_kue_'+word,level,'a/(n*k)',inputs,scene,binding)
    if level=='medium':return _item(intro+f'Berapa petak lagi pada A yang harus diwarnai agar tepat {word} kue A berwarna?',f'{word.capitalize()} dari {denominator} petak adalah {half}. A sudah berwarna {shade1}; perlu {half-shade1} petak lagi.','sd_low_lengkapi_'+word,level,'n*k/d-a',inputs,scene,binding)
    return _item(intro+f'Agar A dan B masing-masing tepat {word} berwarna, beberapa petak perlu diubah warnanya: petak putih menjadi berwarna atau sebaliknya. Berapa jumlah petak paling sedikit yang harus diubah pada kedua kue?',
        f'Target tiap kue {half} petak berwarna. Pada A tambahkan {half-shade1} petak; pada B hapus warna {shade2-half} petak. Total perubahan {abs(half-shade1)+abs(shade2-half)}.',
        'sd_low_perbaiki_dua_pecahan_'+word,level,'Abs(n*k/d-a)+Abs(b-n*k/d)',inputs,scene,binding)


def _grid_position(level,r,visual):
    data=r.sample(range(1,10),9);grid=[data[i:i+3] for i in [0,3,6]];start=[1,1]
    moves=([(-1,0)] if level=='easy' else [(-1,0),(0,1)] if level=='medium' else [(0,-1),(-1,0),(0,1)])
    paths={'easy':'satu kotak ke atas','medium':'satu kotak ke atas lalu satu kotak ke kanan','hard':'satu kotak ke kiri, satu kotak ke atas, lalu satu kotak ke kanan'}
    scene={'kind':'table','headers':['Kiri','Tengah','Kanan'],'rows':grid} if visual else None
    intro='Perhatikan susunan kartu tiga baris pada gambar. ' if visual else f'Kartu disusun tiga baris dari atas ke bawah: {grid[0]}, {grid[1]}, {grid[2]}. '
    row,col=start
    for dr,dc in moves:row+=dr;col+=dc
    item=_item(intro+f'Mulai dari kotak tepat di tengah. Bergerak {paths[level]}. Berapa bilangan pada kotak tujuan?',
        f'Mulai baris kedua kolom kedua. Ikuti gerak berurutan tanpa melompati kotak. Tujuan baris {row+1}, kolom {col+1}, berisi {grid[row][col]}.','sd_low_posisi_berurutan',level,None,{'grid':grid,'start':start,'moves':moves},scene,[('grid',['rows'])] if visual else [],cert_type='sd_low_grid')
    if visual:
        alternative=[list(v) for v in grid];alternative[row][col]=grid[row][col]+1 if grid[row][col]<9 else 8
        item['certificate']['visual_bindings'][0]['alternatives']=[alternative]
    return item


def _pattern(level,r,visual):
    period=r.sample(['circle','triangle','square'],r.choice([2,3]));visible=period*2;target=r.choice(period);words={'circle':'lingkaran','triangle':'segitiga','square':'persegi'};end=len(visible) if level=='easy' else len(visible)+r.randint(2,5) if level=='medium' else len(visible)+r.randint(6,10);start=0 if level!='hard' else r.randint(1,3)
    scene={'kind':'pattern','items':visible} if visual else None
    intro='Perhatikan pola bangun pada gambar; susunan yang sama terus berulang. ' if visual else 'Pola bangun berulang dengan urutan '+', '.join(words[j] for j in period)+'. '
    if level=='easy':question=intro+f'Pada {end} tempat pertama, berapa banyak {words[target]}?'
    elif level=='medium':question=intro+f'Pola dilanjutkan sampai {end} bangun. Berapa banyak {words[target]} pada seluruh urutan?'
    else:question=intro+f'Pola dilanjutkan sampai {end} bangun, kemudian {start} bangun pertama ditutup. Berapa banyak {words[target]} yang tidak ditutup?'
    count=sum(period[i%len(period)]==target for i in range(start,end))
    item=_item(question,f'Unit berulang adalah '+', '.join(words[j] for j in period)+f'. Lanjutkan hingga tempat {end}. '+(f'Keluarkan tempat 1 sampai {start}. ' if start else '')+f'Hitung {words[target]} di tempat yang diminta: {count}.','sd_low_pola_lanjut_hitung',level,None,{'period':visible,'target':target,'start':start,'end':end},scene,[('period',['items'])] if visual else [],cert_type='sd_low_pattern')
    if visual:
        other=next(shape for shape in period if shape!=target)
        item['certificate']['visual_bindings'][0]['alternatives']=[[other if shape==target else shape for shape in visible]]
    return item


def _weight(level,r,visual):
    a=r.randint(3,12);b=r.randint(2,10);give=r.randint(1,min(2,a));extra=r.randint(1,3)
    scene=_cards([a,b],['Karung A (kg)','Karung B (kg)']) if visual else None;binding=_bind_cards(['a','b']) if visual else []
    intro='Baca berat kedua karung pada kartu gambar. ' if visual else f'Karung A beratnya {a} kg, karung B {b} kg. '
    if level=='easy':return _item(intro+'Berapa selisih berat kedua karung dalam kg?',f'Berat A={a} kg, B={b} kg; selisih {abs(a-b)} kg.','sd_low_berat_banding',level,'Abs(a-b)',{'a':a,'b':b},scene,binding)
    if level=='medium':return _item(intro+f'Dari A diambil {give} kg. Berapa selisih berat kedua karung setelah itu?',f'A kini {a-give} kg; bandingkan dengan B={b}. Selisih {abs(a-give-b)} kg.','sd_low_berat_perubahan',level,'Abs(a-t-b)',{'a':a,'b':b,'t':give},scene,binding)
    return _item(intro+f'Dari A dipindahkan {give} kg ke B. Setelah itu {extra} kg bahan baru ditambahkan ke A. Berapa selisih berat kedua karung terakhir?',
        f'Sesudah pindah A={a-give}, B={b+give}. Tambah ke A menjadi {a-give+extra}. Selisih akhir {abs(a-give+extra-b-give)} kg.','sd_low_berat_pindah_tambah',level,'Abs((a-t+g)-(b+t))',{'a':a,'b':b,'t':give,'g':extra},scene,binding)


def _time(level,r,visual):
    hour=r.randint(1,12) if level=='easy' else r.randint(6,10);minute=0 if level=='easy' else r.choice([0,30]);duration=r.choice([15,20,25]);rest=r.choice([5,10,15]);again=r.choice([10,15,20]);target=hour+2
    scene={'kind':'clock','hour':hour,'minute':minute} if visual else None;binding=[('h',['hour']),('m',['minute'])] if visual else []
    intro='Perhatikan jam pada gambar. ' if visual else f'Jam menunjukkan pukul {hour:02d}.{minute:02d}. '
    if level=='easy':return _item(intro+'Jam itu menunjukkan pukul berapa tepat? Pilih angka jamnya.',f'Jarum menit pada 12 dan jarum jam di {hour}, sehingga pukul {hour:02d}.00.','sd_low_baca_jam_tepat',level,'h',{'h':hour,'m':minute},scene,binding)
    if level=='medium':return _item(intro+f'Berapa menit lagi sampai pukul {hour+1:02d}.00?',f'Jam berikutnya pada menit 00. Waktu yang diperlukan 60-{minute}={60-minute} menit.','sd_low_waktu_sampai_jam',level,'60-m',{'h':hour,'m':minute},scene,binding)
    return _item(intro+f'Siti mulai belajar saat itu selama {duration} menit, istirahat {rest} menit, lalu belajar lagi {again} menit. Berapa menit waktu tersisa dari akhir kegiatan sampai pukul {target:02d}.00?',
        f'Waktu awal {hour:02d}.{minute:02d}. Lama kegiatan {duration}+{rest}+{again}={duration+rest+again} menit. Jarak awal ke pukul {target:02d}.00 adalah {120-minute} menit; sisa {120-minute-duration-rest-again} menit.','sd_low_waktu_tiga_kegiatan',level,'t*60-(h*60+m)-(a+b+c)',{'h':hour,'m':minute,'t':target,'a':duration,'b':rest,'c':again},scene,binding)


def _solids(level,r,visual):
    a=r.randint(2,6);b=r.randint(2,5);c=r.randint(1,4);remove=r.randint(1,min(2,a));add=r.randint(1,3)
    scene={'kind':'panels','panels':[{'kind':'shapes','items':[{'label':'A','shape':'cube'},{'label':'B','shape':'sphere'},{'label':'C','shape':'cylinder'}]},{'kind':'table','headers':['Kelompok','Banyak benda'],'rows':[['A',a],['B',b],['C',c]]}]} if visual else None
    binding=[('a',['panels',1,'rows',0,1]),('b',['panels',1,'rows',1,1]),('c',['panels',1,'rows',2,1])] if visual else []
    intro='Gambar menunjukkan jenis bangun ruang A,B,C dan banyak benda tiap kelompok. ' if visual else f'Ada {a} kubus, {b} bola, dan {c} tabung. '
    if level=='easy':return _item(intro+'Berapa benda yang seluruh permukaannya datar?',f'Kubus memiliki permukaan datar saja. Jumlah kubus {a}; bola dan tabung memiliki permukaan lengkung.','sd_low_ruang_permukaan_datar',level,'a',{'a':a,'b':b,'c':c},scene,binding)
    if level=='medium':return _item(intro+'Berapa benda yang memiliki setidaknya satu permukaan lengkung?',f'Bola dan tabung memiliki permukaan lengkung. Jumlah {b}+{c}={b+c}.','sd_low_ruang_kelompok_lengkung',level,'b+c',{'a':a,'b':b,'c':c},scene,binding)
    return _item(intro+f'{remove} kubus dikeluarkan dan {add} bola ditambahkan. Berapa selisih banyak benda yang memiliki permukaan lengkung dengan benda yang seluruh permukaannya datar sekarang?',
        f'Kubus tersisa {a-remove}. Benda berpermukaan lengkung menjadi bola {b+add} ditambah tabung {c}, total {b+add+c}. Selisih {abs(b+add+c-(a-remove))}.','sd_low_ruang_klasifikasi_perubahan',level,'Abs((b+g+c)-(a-t))',{'a':a,'b':b,'c':c,'t':remove,'g':add},scene,binding)


def generate(grade,bab,code,level,r,visual,index):
    if grade==1:
        if bab==1:
            if code=='A':return _counts(grade,bab,code,level,r,visual,10)
            if code=='B':return _compare(grade,level,r,visual,10,True)
            if code=='C':return _walk(level,r,visual,10)
            if code=='D':return _pairs(level,r,visual)
        if bab==2:return _operations(grade,bab,code,level,r,visual,10)
        if bab==3:return _operations(grade,bab,code,level,r,visual,10,True)
        if bab==4:return _shapes(grade,code,level,r,visual)
        if bab==5:
            if code=='A':return _counts(grade,bab,code,level,r,visual,20)
            if code=='B':return _walk(level,r,visual,20)
            if code=='C':return _place(grade,level,r,visual,20)
            if code=='D':return _compare(grade,level,r,visual,20)
        if bab==6:
            if code=='A':return _compare(grade,level,r,visual,19,True)
            return _operations(grade,bab,code,level,r,visual,19,code=='C')
        if bab==7:return _length(level,r,visual,code=='B')
        if bab==8:return _data(grade,code,level,r,visual)
    if grade==2:
        if bab==1:
            if code=='A':return _counts(grade,bab,code,level,r,visual,50)
            if code=='B':return _place(grade,level,r,visual,50)
            if code=='C':return _compare(grade,level,r,visual,50)
        if bab==2:return _operations(grade,bab,code,level,r,visual,50,code=='B')
        if bab==3:
            if code=='A':return _shapes(grade,'A',level,r,visual)
            if code=='B':return _composition(level,r,visual)
            return _solids(level,r,visual)
        if bab==4:return _grid_position(level,r,visual) if code=='A' else _pattern(level,r,visual)
        if bab==5:return _fractions(code,level,r,visual)
        if bab==6:return _weight(level,r,visual) if code=='A' else _time(level,r,visual)
        if bab==7:return _counts(grade,bab,code,level,r,visual,100) if code=='A' else _compare(grade,level,r,visual,100)
        if bab==8:return _data(grade,code,level,r,visual)
    raise ValueError((grade,bab,code,level))
