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
TARGETED_HARD_FAMILIES=frozenset("""
v2_acak_skor_bertingkat
v2_akar_rekonstruksi_panjang
v2_aturan_tempat_batas_genap
v2_balok_tiga_kendala
v2_barisan_kendala_indeks
v2_bijeksi_larangan_beririsan
v2_binomial_parameter_balik
v2_bunga_tunggal_rekonstruksi
v2_campuran_inverse_peluang
v2_cincin_rekonstruksi_tepi
v2_ciri_segiempat_diagonal_inverse
v2_ciri_segitiga_rekonstruksi
v2_densitas_parameter_ganda
v2_deret_inverse_batas
v2_desimal_basis_berubah_inverse
v2_dilatasi_pusat_inverse
v2_diskret_parameter_momen
v2_distribusi_dadu_bersyarat
v2_domain_komposisi_berlubang
v2_domain_komposisi_irisan
v2_dot_norma_orientasi
v2_dua_gradien_singgung
v2_dua_singgung_rekonstruksi
v2_eksponen_dua_parameter
v2_eksponensial_intervensi
v2_eksponensial_tiga_parameter
v2_ekstrem_rekonstruksi
v2_elips_fokus_irisan
v2_empiris_gabungan_inverse
v2_faktor_batas_kantong
v2_frekuensi_median_optimasi
v2_garis_rekonstruksi_perpotongan
v2_grafik_trigonometri_rekonstruksi
v2_harapan_roda_inverse
v2_histogram_rekonstruksi_kepadatan
v2_identitas_binomial_parameter
v2_identitas_pemilihan_cabang
v2_integer_jarak_cabang
v2_integral_kondisi_ganda
v2_integral_momen_balik
v2_invers_mobius_rekonstruksi
v2_investigasi_respons_kelompok
v2_jaring_prisma_limas_gabungan
v2_jenis_data_audit_salah_label
v2_juring_sepusat_inverse
v2_keliling_pagar_lapis_inverse
v2_keliling_poligon_inverse
v2_keliling_segitiga_inverse
v2_kelipatan_jadwal_pengecualian
v2_kerucut_luas_inverse
v2_kesamaan_matriks_akar
v2_kesamaan_rasio_penambahan
v2_kombinasi_batas_larangan
v2_kombinasi_jabatan_komplemen
v2_komposisi_tiga_parameter
v2_kongruen_dimensi_tersembunyi
v2_konstruksi_tiga_terowongan
v2_kontinu_campuran_balik
v2_korelasi_inverse_cabang
v2_kuadrat_rekonstruksi_interval
v2_limit_turunan_parameter
v2_lingkaran_kelompok_inverse
v2_lingkaran_rekonstruksi
v2_logaritma_basis_tersembunyi
v2_lokasi_balik_jalur
v2_luas_berganti_posisi
v2_luas_dimensi_potongan_inverse
v2_majemuk_modal_faktor_inverse
v2_matriks_singular_rekonstruksi
v2_matriks_transformasi_inverse
v2_nilai_tempat_digit_inverse
v2_operasi_aljabar_rekonstruksi
v2_operasi_polinomial_koefisien_balik
v2_optimasi_pagar_biaya
v2_pangkat_sistem_eksponen
v2_parameter_dua_skema_bunga
v2_pecahan_basis_berubah_inverse
v2_pecahan_urut_potong_sambung
v2_peluang_kombinasi_bersyarat
v2_peluang_komposisi_inverse
v2_peluang_rekonstruksi_sektor
v2_pembagian_pecahan_stok
v2_pemusatan_koreksi_inverse
v2_pencar_efek_penggabungan
v2_pengumpulan_data_duplikat_hilang
v2_penjumlahan_diagonal_determinan
v2_plsv_dua_regim_biaya
v2_pmf_normalisasi_momen
v2_polinomial_rekonstruksi_minimum
v2_ptlsv_model_perbandingan
v2_pythagoras_dimensi_pita
v2_rasio_bagian_tersembunyi
v2_rasio_pesanan_biaya
v2_rasio_transfer_inverse
v2_rasional_batas_penyaringan
v2_rasional_operasi_pengurutan
v2_refleksi_dua_sumbu_inverse
v2_regresi_data_hilang
v2_relasi_tiga_kendala
v2_rotasi_pusat_inverse
v2_sampel_strata_cadangan
v2_sebangun_selisih_keliling
v2_segitiga_sebangun_dimensi
v2_sekan_parameter_bulat
v2_sifat_pangkat_inverse
v2_sinus_ambigu_dua_segitiga
v2_skala_dimensi_inverse
v2_spasial_minimum_multitampak
v2_spldv_paket_batas
v2_spltv_paket_anggaran
v2_statistika_koreksi_penghapusan
v2_sudut_garis_bagi_luar
v2_sudut_tumpang_tindih_alat
v2_tali_busur_cabang_akar
v2_transformasi_inverse_berantai
v2_translasi_dua_vektor_inverse
v2_trigonometri_dua_posisi_kabel
v2_turunan_hasil_kali_balik
v2_unit_circle_cabang_kuadran
v2_unsur_aljabar_parameter
v2_urut_bilangan_digit_tersembunyi
v2_vektor_rekonstruksi_norma
v2_venn_inverse_ruang_bersyarat
v2_volume_perpindahan_inverse
""".split())


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
    if kind=='session_chart_choice':
        p=cert['inputs'];diagram='Diagram batang' if p['mode']=='categories' else 'Diagram garis'
        if cert['task']=='read':return diagram+'; frekuensi kedua '+m(p['b'])+'.'
        if cert['task']=='update':return diagram+'; selisih akhir '+m(abs(p['a']+p['added_a']-p['b']-p['added_b']))+'.'
        ratio=s.Rational(p['origin']+p['b'],p['origin']+p['a']);return diagram+'; rasio frekuensi kedua terhadap pertama '+m(ratio)+'.'
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
        assert pairs;return s.Integer(min(a+b for a,b in pairs))
    if kind=='session_common_bags':
        p=cert['inputs'];ks=[n for n in range(1,p['cap']+1) if p['fruit_a']%n==p['fruit_b']%n==0]
        return s.Rational(p['fruit_a']+p['fruit_b'],max(ks))
    if kind=='session_bar_reallocate':
        p=cert['inputs'];values=[p['a']-p['move'],p['b']+p['move'],p['c']+p['extra']]
        return s.Integer(max(values)-min(values))
    if kind=='session_data_audit':
        p=cert['inputs'];correct_total=p['reported']-p['duplicate']+p['missing'];return s.Integer(correct_total-p['other'])
    if kind=='session_scientific_inverse':
        p=cert['inputs'];ratio=s.Rational(p['ratio_num'],p['ratio_den']);difference=s.log(ratio*p['coefficient_b']/p['coefficient_a'],10);exponent_a=(p['sum_exponents']+difference)/2;exponent_b=(p['sum_exponents']-difference)/2
        return s.simplify(p['coefficient_a']*10**exponent_a-p['coefficient_b']*10**exponent_b)
    if kind=='session_geometry_shared':
        p=cert['inputs'];width=s.Rational(p['outer'],2)-p['length_a']-p['length_b'];return s.simplify(p['laps_a']*2*(p['length_a']+width)+p['laps_b']*2*(p['length_b']+width-2))
    if kind=='session_45_pythagoras':
        p=cert['inputs'];a=s.sympify(p['perimeter'])/(2+s.sqrt(2));return s.simplify(a*a/2-p['removed'])
    if kind=='session_distance_ratio':
        p=cert['inputs'];distance=s.sqrt(p['dx']**2+p['dy']**2);return s.simplify(distance*(p['ratio_a']+p['ratio_b'])/p['ratio_a'])
    if kind=='session_distance_equal':
        p=cert['inputs'];t=s.Rational(p['dx']**2+p['yb']**2-p['ya']**2,2*p['dx']);return s.simplify(s.sqrt(t*t+p['ya']**2))
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
    if kind=='session_triangle_repair':
        p=cert['inputs'];leg=s.Rational(p['perimeter']+p['difference'],3);base=leg-p['difference']+p['added_base'];new_leg=s.floor(base/2)+1
        return s.simplify(base+2*new_leg)
    if kind=='session_polyhedron_group':
        p=cert['inputs'];n=s.Rational(p['faces']-2*p['prisms']-p['pyramids'],p['prisms']+p['pyramids']);return s.simplify(n*(3*p['prisms']+2*p['pyramids']))
    if kind=='session_congruence_parameters':
        p=cert['inputs'];det=p['a']*p['d']-p['b']*p['c'];x=s.Rational(p['P']*p['d']-p['b']*p['Q'],det);y=s.Rational(p['a']*p['Q']-p['P']*p['c'],det)
        return s.simplify(x*x+y*y)
    if kind=='session_circle_two_boundaries':
        p=cert['inputs'];inner=s.Rational(p['area_over_pi']-p['width']**2,2*p['width']);outer=inner+p['width']
        return s.simplify(2*s.pi*(p['outer_laps']*outer+p['inner_laps']*inner))
    return s.sympify(solve_targeted(cert))


def assess(model,grade):
    cert=model['certificate'];kind=cert['type']
    if kind=='session_chart_choice':
        level={'read':'easy','update':'medium','axis_audit':'hard'}[cert['task']]
        return {'assessedLevel':level,'reason':{'easy':'Memilih representasi sesuai tujuan dan membaca satu frekuensi langsung.','medium':'Memilih jenis diagram untuk tujuan penyajian, memperbarui dua frekuensi lalu membandingkannya.','hard':'Mengevaluasi jenis diagram dan pengaruh awal sumbu yang dipotong, merekonstruksi frekuensi lalu menguji klaim perbandingan batang.'}[level],'steps':{'easy':1,'medium':3,'hard':4}[level],'flags':[],'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,'apiCalls':0}
    if kind.startswith('session_basic'):return basic.assess(model,grade)
    if kind.startswith('session_sma'):
        from .session_high_sma import assess as sma_assess
        return sma_assess(model,grade)
    if kind in {'session_targeted_visual','session_parameter_visual'}:return assess({**model,'certificate':cert['base']},grade)
    if kind=='session_data_audit' and cert['inputs']['duplicate']==cert['inputs']['missing']:
        return {'assessedLevel':'easy','reason':'Data ganda dan data hilang bernilai sama sehingga koreksinya saling membatalkan; tersisa satu pengurangan langsung.','steps':1,'flags':['numerical_shortcut'],'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,'apiCalls':0}
    if kind in {'session_finite_factor_pairs','session_common_bags','session_bar_reallocate','session_data_audit','session_scientific_inverse','session_geometry_shared','session_45_pythagoras','session_distance_ratio','session_distance_equal','session_place_order_inverse','session_cube_tunnels','session_spatial_minimum','session_urn_inverse','session_triangle_repair','session_polyhedron_group','session_congruence_parameters','session_circle_two_boundaries'}:
        reason='Menggabungkan kendala, menilai kemungkinan atau membalik informasi sebelum menentukan kuantitas akhir.'
    elif kind in {'symbolic_constraints','finite_constraints','restricted_bijection','digit_arrangements','committee','conditional_urn','finite_probability'}:
        if model['kind'] not in TARGETED_HARD_FAMILIES and model['kind']!='v2_model_aljabar_dua_tarif':raise ValueError('Unreviewed constraint template')
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
    if 0<=value<=1 and any(word in stem.lower() for word in ('peluang','proporsi')):
        wrong=[]
        for t in [1-value,value/2,(value+1)/2,value**2,s.Rational(1,3),s.Rational(2,3),s.Integer(0),s.Integer(1)]:
            if 0<=t<=1 and t!=value and t not in wrong:wrong.append(t)
            if len(wrong)==3:break
        draft.distractors=[m(v) for v in wrong]
    model={'question':draft.question,'answer':draft.answer,'wrong':draft.distractors,'explanation':draft.explanation,'kind':family,'steps':4,'rationale':'Menggabungkan beberapa kendala dan membalik hubungan yang diberikan.','scene':None,'certificate':cert}
    model['assessment']=assess(model,0);return model


def hard_special(grade,bab,code,r):
    if grade==9 and bab==2 and code=='D':
        inner=r.randint(3,25);width=r.randint(1,9);area=(inner+width)**2-inner**2;la=r.randint(2,5);lb=r.choice([n for n in range(1,5) if n!=la])
        return _make(f'Dua lingkaran sepusat membentuk cincin selebar {width} cm dan luas '+m(area*s.pi)+f' cm². Pita melingkari seluruh batas luar {la} kali dan seluruh batas dalam {lb} kali. Berapa panjang pita seluruhnya dalam bentuk eksak?',{'type':'session_circle_two_boundaries','inputs':{'width':width,'area_over_pi':area,'outer_laps':la,'inner_laps':lb}},'session_lingkaran_dua_batas_balik','Selisih kuadrat jari-jari menentukan jumlah jari-jari setelah dibagi lebar cincin. Gabungkan jumlah dan selisih untuk mendapatkan kedua jari-jari, lalu hitung panjang pita pada dua batas dengan banyak lilitan berbeda')
    if grade==5 and bab==7 and code=='A':
        leg=r.randint(10,28);difference=r.randint(1,leg-3);base=leg-difference;perimeter=2*leg+base;added=r.randint(leg+difference+1,leg+difference+15)
        return _make(f'Segitiga sama kaki mempunyai keliling {perimeter} cm. Alasnya {difference} cm lebih pendek daripada setiap kaki. Alas kemudian diperpanjang {added} cm. Dua kaki dibuat ulang dengan panjang bilangan bulat yang sama dan sesingkat mungkin, dengan syarat jumlah kedua kaki lebih panjang daripada alas. Berapa keliling segitiga baru?',{'type':'session_triangle_repair','inputs':{'perimeter':perimeter,'difference':difference,'added_base':added}},'session_ciri_segitiga_perbaikan','Gunakan keliling dan selisih sisi untuk menemukan alas semula. Perbarui alas, kemudian pilih panjang kaki bulat terkecil yang memenuhi syarat segitiga dan hitung keliling baru')
    if grade==9 and bab==2 and code=='A':
        n=r.randint(3,12);prisms=r.randint(2,9);pyramids=r.randint(1,7);faces=prisms*(n+2)+pyramids*(n+1)
        return _make(f'Sebuah kelompok mempunyai {prisms} prisma dan {pyramids} limas. Semua alasnya segi-n dengan n yang sama. Jumlah seluruh bidang sisi bangun-bangun tersebut {faces}. Berapa jumlah seluruh rusuknya? Bangun dihitung terpisah, tidak saling ditempel.',{'type':'session_polyhedron_group','inputs':{'prisms':prisms,'pyramids':pyramids,'faces':faces}},'session_klasifikasi_jaring_balik','Prisma segi-n memiliki n+2 bidang sisi dan 3n rusuk; limas segi-n memiliki n+1 bidang sisi dan 2n rusuk. Gunakan jumlah sisi untuk menentukan n, lalu jumlahkan rusuk seluruh bangun')
    if grade==9 and bab==3 and code=='D':
        while True:
            a,b,c,d=[r.randint(1,5) for _ in range(4)];x,y=r.randint(2,7),r.randint(2,7);p=a*x+b*y;q=c*x+d*y
            if a*d!=b*c and p+q<170:break
        return _make(f'Dua segitiga kongruen memiliki sudut-sudut bersesuaian. Pada segitiga pertama dua sudut dinyatakan ({a}x+{b}y)° dan ({c}x+{d}y)°. Pada segitiga kedua sudut bersesuaiannya {p}° dan {q}°. Tentukan x²+y².',{'type':'session_congruence_parameters','inputs':{'a':a,'b':b,'c':c,'d':d,'P':p,'Q':q}},'session_kongruen_dua_parameter','Kekongruenan menyamakan kedua pasang sudut. Bentuk dan selesaikan dua persamaan untuk x,y, lalu hitung jumlah kuadratnya')
    if grade==5 and bab==9 and code=='B':
        a=r.randint(4,9);b=r.randint(1,a-1);tail=r.randint(100,999);prefix=r.randint(1,8);difference=9000*(a-b);first=prefix*100000+10000*a+1000*b+tail;second=prefix*100000+10000*b+1000*a+tail;other=r.randint(max(100000,second-12000),min(999999,first+12000))
        return _make(f'Dua bilangan enam angka ditulis {prefix}AB{tail} dan {prefix}BA{tail}. A,B digit bukan nol, A>B, dan A+B={a+b}. Bilangan pertama lebih besar {difference} daripada kedua. Jika keduanya diurutkan bersama {other}, berapa bilangan di posisi tengah?',{'type':'session_place_order_inverse','inputs':{'prefix':prefix,'sum':a+b,'difference':difference,'tail':tail,'other':other}},'session_urut_enam_digit_balik','Selisih bilangan menentukan 9000(A−B). Gabungkan dengan jumlah digit untuk mendapatkan A dan B, susun kedua bilangan enam angka lalu urutkan bersama bilangan ketiga')
    if grade==5 and bab==2 and code in 'DE':
        if code=='E':
            g=r.randint(2,16);u,v=r.choice([(2,3),(3,5),(4,5),(5,7),(3,8),(7,9)]);limit=g*u*v;product=g*g*u*v;valid=[a for a in s.divisors(product) if a<=product//a and s.gcd(a,product//a)==g];cap=r.randint(valid[0],valid[-1]-1)
            cert={'type':'session_finite_factor_pairs','inputs':{'gcd':g,'lcm':limit,'cap':cap,'limit':limit}}
            return _make(f'Dua bilangan positif A dan B memenuhi A≤B. FPB-nya {g} dan KPK-nya {limit}. A tidak lebih dari {cap}. Berapa nilai A+B terkecil yang mungkin?',cert,'session_fpb_kpk_inverse','Daftar pasangan faktor dari FPB×KPK, periksa FPB dan KPK tiap pasangan serta batas A, kemudian pilih jumlah terkecil yang masih memenuhi batas')
        a,b=r.choice([(3,4),(4,5),(5,6),(5,7),(7,8)]);g=r.choice([6,8,9,10,12,14,15,16,18,20]);cap=r.randint(min(s.factorint(g)),g-1)
        return _make(f'Ada {a*g} apel dan {b*g} jeruk yang seluruhnya dibagi ke kantong tanpa sisa. Isi apel antar kantong sama, demikian pula jeruk. Tersedia paling banyak {cap} kantong. Jika kantong dipakai sebanyak mungkin, berapa banyak buah tiap kantong?',{'type':'session_common_bags','inputs':{'fruit_a':a*g,'fruit_b':b*g,'cap':cap}},'session_faktor_persekutuan_batas','Cari faktor persekutuan yang tidak melebihi batas jumlah kantong. Pilih yang terbesar lalu bagi kedua jenis buah dengannya')
    if grade==5 and bab==4 and code=='E':
        a,b=r.randint(10,35),r.randint(10,35);w=r.randint(5,18);outer=2*(a+b+w);la,lb=r.randint(2,4),r.randint(1,3)
        return _make(f'Dua persegi panjang panjangnya {a} cm dan {b} cm. Lebar pertama x cm dan lebar kedua x−2 cm. Keduanya ditempel tanpa tumpang tindih pada seluruh sisi lebar kedua. Keliling gabungannya {outer} cm. Setelah dipisah, pita mengelilingi bangun pertama {la} kali dan bangun kedua {lb} kali. Berapa panjang pita seluruhnya?',{'type':'session_geometry_shared','inputs':{'length_a':a,'length_b':b,'outer':outer,'laps_a':la,'laps_b':lb}},'session_keliling_gabungan_balik','Keliling gabungan 2(a+x)+2(b+x−2)−2(x−2)=2(a+b+x). Tentukan x, hitung kedua keliling terpisah, lalu kalikan masing-masing dengan banyak lilitan dan jumlahkan')
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
        a,b=r.choice([(3,4),(4,5),(5,6),(5,7),(7,8)]);g=r.choice([6,8,9,10,12,14,15,16,18]);cap=r.randint(min(s.factorint(g)),g-1)
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
        a,b=r.randint(2,9),r.randint(2,9);pa=r.randint(2,6);pb=r.choice([n for n in range(1,7) if n!=pa]);ratio=s.Rational(a,b)*s.Integer(10)**(pa-pb)
        return _make(f'Dua besaran ditulis dalam bentuk baku P={a}×10^m dan Q={b}×10^n, dengan m,n bilangan bulat positif. Diketahui m+n={pa+pb} dan P/Q={m(ratio)}. Tentukan P−Q.',{'type':'session_scientific_inverse','inputs':{'coefficient_a':a,'coefficient_b':b,'sum_exponents':pa+pb,'ratio_num':int(ratio.p),'ratio_den':int(ratio.q)}},'session_bentuk_baku_operasi_bertingkat','Perbandingan P/Q menentukan 10^(m−n). Gabungkan selisih pangkat dengan jumlah pangkat untuk menemukan m dan n, baru hitung kedua besaran serta selisihnya')
    if grade==8 and bab==2 and code=='C':
        a=r.randint(6,30);removed=r.randint(1,a*a//3);perimeter=a*(2+s.sqrt(2))
        return _make('Segitiga siku-siku sama kaki mempunyai keliling '+m(perimeter)+' cm. Dari daerah itu dipotong bagian seluas '+str(removed)+' cm². Berapa luas daerah yang tersisa?',{'type':'session_45_pythagoras','inputs':{'perimeter':str(perimeter),'removed':removed}},'session_segitiga_istimewa_balik','Dengan kaki a, keliling a(2+√2). Tentukan a, hitung luas a²/2, lalu kurangi bagian yang dipotong')
    if grade==8 and bab==2 and code=='E':
        dx=r.randint(12,30);ya=r.randint(3,10);yb=r.randint(3,12)
        return _make(f'Titik A=(0,{ya}) dan B=({dx},{yb}). Titik C berada pada sumbu x positif dan berjarak sama dari A dan B. Berapa panjang AC dalam bentuk eksak?',{'type':'session_distance_equal','inputs':{'dx':dx,'ya':ya,'yb':yb}},'session_jarak_koordinat_balik','Misalkan C=(t,0). Samakan kuadrat jarak AC dan BC agar t² saling menghapus, tentukan t positif, lalu gunakan rumus jarak untuk AC')
    return None


def bijection_model(r,visual):
    size=r.randint(4,7);count=r.randint(2,min(5,size));forbidden=r.sample([(i,j) for i in range(size) for j in range(size)],count)
    cert={'type':'restricted_bijection','size':size,'forbidden':[list(v) for v in forbidden]}
    stem=f'Ada {size} siswa bernomor 1 sampai {size} dan {size} loker bernomor sama. Setiap siswa mendapat tepat satu loker berbeda. '
    if visual:stem+='Pasangan siswa dan loker yang dilarang ditunjukkan pada tabel gambar. '
    else:stem+='Larangan penempatan adalah '+', '.join(f'siswa {i+1} tidak boleh loker {j+1}' for i,j in forbidden)+'. '
    model=_make(stem+'Berapa korespondensi satu-satu yang diperbolehkan?',cert,'v2_bijeksi_larangan_beririsan','Periksa penempatan satu-satu dengan mengeluarkan semua susunan yang melanggar setidaknya satu larangan; tumpang tindih larangan harus diperhitungkan')
    if visual:
        model['scene']={'kind':'table','headers':['Siswa','Loker yang dilarang'],'rows':[[i+1,j+1] for i,j in forbidden]};model['visual_kind']='math_scene'
        cert['visual_bindings']=[{'certificate_path':['forbidden',i,k],'path':['rows',i,k],'offset':1,'alternatives':list(range(size))} for i in range(count) for k in (0,1)]
    return model


def chart_scene(cert):
    p=cert['inputs'];origin=p.get('origin',0);a=origin+p['a'];b=origin+p['b'];labels=['Kategori A','Kategori B'] if p['mode']=='categories' else ['Hari 1','Hari 2']
    return {'kind':'coordinate_graph','x_range':[0,3],'y_range':[origin,max(a,b)+5],'tick_step':[1,5],
            'polylines':[[[0.6,origin],[1.4,origin],[1.4,a],[0.6,a],[0.6,origin]],[[1.6,origin],[2.4,origin],[2.4,b],[1.6,b],[1.6,origin]]],
            'points':[{'x':1,'y':a+2,'label':labels[0]},{'x':2,'y':b+2,'label':labels[1]}],'title':'Frekuensi; perhatikan awal sumbu tegak'}


def diagram_choice(level,r,visual):
    task={'easy':'read','medium':'update','hard':'axis_audit'}[level];a=r.randint(5,40);b=r.randint(5,45);mode=r.choice(['categories','time']);p={'a':a,'b':b,'mode':mode}
    if task=='update':p.update(added_a=r.randint(2,12),added_b=r.randint(2,12))
    if task=='axis_audit':p.update(b=2*a,origin=r.randint(3,25))
    cert={'type':'session_chart_choice','task':task,'inputs':p}
    purpose='membandingkan frekuensi dua kategori yang tidak berurutan' if mode=='categories' else 'menunjukkan perubahan frekuensi dari hari pertama ke hari kedua dengan selang waktu sama'
    intro='Data awal terlihat pada gambar. ' if visual else f"Frekuensi pertama {p.get('origin',0)+p['a']} dan kedua {p.get('origin',0)+p['b']}. "
    if task=='read':question=intro+'Tujuan penyajian adalah '+purpose+'. Pasangan jenis diagram yang sesuai dan frekuensi kedua adalah ....';number=s.Integer(p['b']);suffix='frekuensi kedua '
    elif task=='update':question=intro+f"Frekuensi pertama bertambah {p['added_a']} dan kedua bertambah {p['added_b']}. Tujuan penyajian adalah "+purpose+'. Pasangan diagram yang sesuai dan selisih frekuensi setelah perubahan adalah ....';number=s.Integer(abs(p['a']+p['added_a']-p['b']-p['added_b']));suffix='selisih akhir '
    else:
        if not visual:intro+=f"Diagram awal menggunakan sumbu tegak dari {p['origin']}, sehingga panjang batang kedua dua kali pertama. "
        question=intro+'Seorang siswa menyimpulkan frekuensi kedua dua kali pertama karena batangnya dua kali lebih panjang. Tujuan penyajian adalah '+purpose+'. Pilih jenis diagram yang sesuai dan rasio frekuensi sebenarnya untuk mengevaluasi kesimpulan itu.';number=s.Rational(p['origin']+p['b'],p['origin']+p['a']);suffix='rasio frekuensi kedua terhadap pertama '
    diagram='Diagram batang' if mode=='categories' else 'Diagram garis';other='Diagram garis' if mode=='categories' else 'Diagram lingkaran';answer=solve(cert)
    wrong=[other+'; '+suffix+m(number)+'.',diagram+'; '+suffix+m(2 if task=='axis_audit' else number+1)+'.',other+'; '+suffix+m(2 if task=='axis_audit' else number+2)+'.']
    explanation=('Diagram batang membandingkan kategori terpisah.' if mode=='categories' else 'Diagram garis sesuai untuk menampilkan perubahan dengan urutan waktu yang bermakna.')+' '
    if task=='axis_audit':explanation+=f"Frekuensi sebenarnya diperoleh dengan menambahkan awal sumbu {p['origin']} pada panjang masing-masing batang. Rasio frekuensi "+m(number)+', sehingga rasio panjang batang tidak langsung sama dengan rasio frekuensi.'
    elif task=='update':explanation+='Perbarui kedua frekuensi sebelum mencari selisihnya, yaitu '+m(number)+'.'
    else:explanation+='Frekuensi kedua dibaca langsung, yaitu '+m(number)+'.'
    result={'question':question,'answer':answer,'wrong':wrong,'wrong_reasons':['Jenis diagram tidak sesuai tujuan penyajian pada soal.','Jenis diagram sesuai, tetapi nilai yang menyertainya tidak memenuhi data dan perhitungan.','Jenis diagram dan nilai yang menyertainya tidak sesuai tujuan serta data.'],'explanation':explanation,'kind':'session_memilih_diagram_'+task,'steps':{'easy':1,'medium':3,'hard':4}[level],'rationale':'Menilai representasi berdasarkan tujuan serta data yang relevan.','scene':chart_scene(cert) if visual else None,'visual_kind':'math_scene','certificate':cert}
    result['assessment']=assess(result,7);return result


def essential_visual(model):
    """Move one pivotal observed datum into a factual table, preserving its recipe."""
    if model.get('scene'):return model
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
        model['scene']={'kind':'table','headers':['Data','Nilai'],'rows':[['T1',old]]};model['visual_kind']='math_scene';model['certificate']=wrapped;wrapped['visual_bindings']=[{'input':'visible','path':['rows',0,1],'alternatives':[change]}]
        return model
    return None


def check_visual(model):
    scene=model.get('scene')
    if not scene:return {'status':'text_question'}
    if model['certificate']['type'].startswith('session_sma'):
        from .session_high_sma import check_visual as sma_check
        return sma_check(model)
    from .math_scene_visuals import validate_scene
    validate_scene(scene);cert=model['certificate'];initial=solve(cert);passed=[]
    if cert['type']=='session_chart_choice':
        assert scene==chart_scene(cert),'Chart and source frequencies differ'
        for key in ('a','b'):
            altered=deepcopy(cert);altered['inputs'][key]+=5;validate_scene(chart_scene(altered))
            if solve(altered)!=initial:passed.append(key)
        assert passed;return {'status':'verified_locally','pivotalFacts':passed,'independentVisionValidation':False}
    if cert['type']=='session_basic_linked':
        for binding in cert['visual_bindings']:
            path=binding['certificate_path'];value=_at(cert,path)
            assert s.sympify(_at(scene,binding['path']))==s.sympify(value),'Scene and retained input differ'
            alternatives=binding.get('alternatives',[s.sympify(value)+1,s.sympify(value)+2,s.sympify(value)-1])
            for change in alternatives:
                altered=deepcopy(cert);_put(altered,path,str(change) if isinstance(value,str) else int(change))
                changed_scene=deepcopy(scene);_put(changed_scene,binding['path'],str(change));validate_scene(changed_scene)
                try:
                    if s.simplify(solve(altered)-initial)!=0:passed.append([path[0],path[-1]]);break
                except (ValueError,TypeError,ZeroDivisionError):continue
    else:
        for binding in cert.get('visual_bindings',[]):
            if 'certificate_path' in binding:
                value=_at(cert,binding['certificate_path']);assert _at(scene,binding['path'])==value+binding.get('offset',0)
                for change in binding['alternatives']:
                    altered=deepcopy(cert);_put(altered,binding['certificate_path'],change)
                    # Duplicate restrictions do not represent two distinct facts.
                    if len({tuple(v) for v in altered.get('forbidden',[])})!=len(altered.get('forbidden',[])):continue
                    if solve(altered)!=initial:passed.append(binding['certificate_path']);break
                continue
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
    if grade==7 and bab==6 and code=='F':return diagram_choice(level,r,visual)
    if grade>=10:
        from .session_high_sma import generate as sma_generate
        candidate=sma_generate(name,bab,code,level,r,visual,index)
        if candidate is not None:return candidate
    elif level in ('easy','medium'):
        return basic.generate(grade,bab,code,level,r,visual,index)
    special=bijection_model(r,visual) if grade==8 and bab==4 and code=='C' else hard_special(grade,bab,code,r) if grade<10 else None
    if special is not None:model=special
    else:
        from scripts.generate_targeted_replenishment import factory
        try:authored=factory(name,bab,code,'hard',r)
        except (AssertionError,ValueError,ZeroDivisionError):return None
        d=authored.draft;model={'question':d.question,'answer':d.answer,'wrong':d.distractors,'explanation':d.explanation,'kind':d.kind,'steps':authored.steps,'rationale':authored.rationale,'scene':None,'certificate':authored.certificate}
        value=solve(authored.certificate)
        if 0<=value<=1 and any(word in d.question.lower() for word in ('peluang','proporsi')):
            wrong=[]
            for t in [1-value,value/2,(value+1)/2,value**2,s.Rational(1,3),s.Rational(2,3),s.Integer(0),s.Integer(1)]:
                if 0<=t<=1 and t!=value and t not in wrong:wrong.append(t)
                if len(wrong)==3:break
            model['wrong']=[m(t) for t in wrong]
        try:model['assessment']=assess(model,grade)
        except (AssertionError,ValueError):return None
    if model['assessment']['assessedLevel']!=level:return None
    if visual:
        model=essential_visual(model)
        if model is None:return None
    return model
