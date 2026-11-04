"""Primary-school variations using diagrams described unambiguously in words."""
from collections import Counter
from decimal import Decimal
import sympy as s
from .targeted_math import checked,constant,system,finite,m,pair,rp

a,b,c,x=s.symbols('a b c x',real=True)

def guard(condition):return s.Piecewise((0,condition),(1,True))

def decimal(value):
    value=s.Rational(value)
    return format(Decimal(int(value.p))/Decimal(int(value.q)),'f').replace('.',',')

def place_value(r,million=False,ordering=False,level='hard'):
    p=r.randint(5,9);q=r.randint(1,p-1);tail=r.randint(100,999);prefix=r.randint(1,8)*100000 if million else 0;number=prefix+10000*p+1000*q+tail;swapped=prefix+10000*q+1000*p+tail;digit=r.randint(1,9)
    if level=='medium':
        return constant(f'Bilangan {number} ditambah {digit} ribuan lalu dikurangi {q} ratusan. Berapa bilangan akhirnya?',number+digit*1000-q*100,f'Nilai {digit} ribuan={digit*1000} dan {q} ratusan={q*100}. Hasil {number+digit*1000-q*100}.','v2_nilai_tempat_perubahan',level)
    eq=[a+b-p-q,9000*(a-b)-(number-swapped)];base=prefix+10000*a+1000*b+tail;other=prefix+10000*q+1000*a+tail
    if ordering:
        known=r.randint(swapped+1,number-1);query=base+other+known-s.Max(base,other,known)-s.Min(base,other,known)
        return checked(f'Dua bilangan lima angka adalah AB{tail} dan BA{tail}. A dan B digit bukan nol, A>B, A+B={p+q}. Bilangan pertama lebih besar {number-swapped} daripada kedua. Jika keduanya diurutkan bersama {known}, berapa bilangan di posisi tengah?',known,f'Pertukaran digit puluh ribuan dan ribuan memberi 9000(A-B)={number-swapped}, maka A-B={p-q}. Bersama jumlah digit diperoleh A={p},B={q}. Bilangan {number},{swapped}; urutkan bersama {known}, posisi tengah {known}.','v2_urut_bilangan_digit_tersembunyi',level,system(['a','b'],eq,query,[a-b,b]))
    described=(str(prefix//100000)+'AB'+str(tail) if million else 'AB'+str(tail));query=base-digit*100
    return checked(f'Sebuah bilangan ditulis {described}, dengan A dan B digit bukan nol, A>B, A+B={p+q}. Menukar posisi A dan B memperkecil bilangan sebesar {number-swapped}. Berapa bilangan semula setelah dikurangi {digit} ratusan?',number-digit*100,f'Nilai pertukaran adalah (10000-1000)(A-B), sehingga A-B={p-q}. Dari jumlah digit didapat A={p},B={q}. Bilangan semula {number}; kurangi {digit*100} menjadi {number-digit*100}.','v2_nilai_tempat_digit_inverse',level,system(['a','b'],eq,query,[a-b,b]))

def ratio(r,mode):
    u=r.randint(2,5);v=u+r.randint(1,4);unit=r.randint(4,12);p=u*unit;q=v*unit;move=r.randint(1,unit);after=s.Rational(p+move,q-move)
    if mode=='A':
        val=q-p+move
        return checked(f'Rasio pensil kotak A:B semula {u}:{v}. Setelah {move} pensil dari B dipindahkan ke A, rasionya menjadi {m(after)}:1. Berapa selisih jumlah pensil B semula dengan A semula yang ditambah {move}?',q-p-move,f'Tulis jumlah awal u bagian dan v bagian. Rasio sesudah pemindahan menentukan satu bagian {unit}. Maka awal A={p}, B={q}; selisih B-(A+{move})={q-p-move}.','v2_rasio_bagian_tersembunyi','hard',system(['a','b'],[v*a-u*b,a+move-after*(b-move)],b-a-move,[a,b-move]))
    if mode=='B':
        add=r.randint(1,unit);after=s.Rational(p+add,q+add)
        return checked(f'Dua kelompok memiliki rasio banyak anggota {u}:{v}. Setelah masing-masing menerima {add} anggota baru, rasionya menjadi {m(after)}:1. Berapa jumlah anggota kedua kelompok semula?',p+q,f'Tulis banyak awal {u}k dan {v}k. Kesamaan rasio ({u}k+{add})/({v}k+{add})={after} memberi k={unit}. Jumlah awal ({u}+{v})×{unit}={p+q}.','v2_kesamaan_rasio_penambahan','hard',system(['a','b'],[v*a-u*b,a+add-after*(b+add)],a+b,[a,b]))
    extra=r.randint(2,6);total=p+q;costA=r.randint(2,6)*1000;costB=r.randint(7,10)*1000
    return checked(f'Peserta A dan B memiliki rasio {u}:{v}; kelompok B lebih banyak {q-p} orang. Biaya makan per orang A {costA} rupiah dan B {costB} rupiah. Jika {extra} orang A berhalangan dan tidak dipesankan makan, berapa total biaya?',(p-extra)*costA+q*costB,f'Selisih {v-u} bagian={q-p}, jadi satu bagian {unit}. Peserta awal A={p}, B={q}. Pesanan A tinggal {p-extra}; biaya ({p}-{extra})×{costA}+{q}×{costB}={(p-extra)*costA+q*costB}.','v2_rasio_pesanan_biaya','hard',system(['a','b'],[v*a-u*b,b-a-q+p],(a-extra)*costA+b*costB,[a-extra,b]))

def generate(grade,bab,code,level,r):
    A=r.randint(2,8);B=r.randint(2,9);C=r.randint(1,7);U=r.randint(4,14);V=r.randint(3,9);T=r.randint(3,7)
    if grade==1:
        if bab==1:
            u=r.randint(2,6);v=r.randint(2,5)
            return constant(f'Perhatikan gambar apel. Di piring ada ${u}$ apel, lalu ditambah lagi ${v}$ apel. Berapa jumlah apel seluruhnya? ${u} + {v} = \\dots$',u+v,f'Hitung penjumlahan konkret: ${u} + {v} = {u+v}$.','v2_sd1_penjumlahan_konkret',level)
        if bab==2:
            total=r.randint(6,12);taken=r.randint(2,total-2)
            return constant(f'Ada ${total}$ kelereng di toples. Sebanyak ${taken}$ butir diambil. Berapa sisa kelereng di toples? ${total} - {taken} = \\dots$',total-taken,f'Hitung pengurangan konkret: ${total} - {taken} = {total-taken}$.','v2_sd1_pengurangan_konkret',level)
        return constant(f'Kotak A berisi ${A}$ bola dan Kotak B berisi ${A+B}$ bola. Berapa selisih banyak bola? ${A+B} - {A} = \\dots$',B,f'Selisih adalah ${A+B} - {A} = {B}$.','v2_sd1_selisih_objek',level)
    if grade==2:
        if bab==1:
            u=r.randint(15,45);v=r.randint(10,35)
            return constant(f'Koleksi stiker Ani ada ${u}$ lembar. Ia diberi paman ${v}$ lembar lagi. Berapa total stiker Ani sekarang? ${u} + {v} = \\dots$',u+v,f'${u} + {v} = {u+v}$.','v2_sd2_penjumlahan_puluhan',level)
        if bab==2:
            piring=r.randint(3,5);kue=r.randint(2,4)
            return constant(f'Ada ${piring}$ piring, tiap piring berisi ${kue}$ kue donat. Berapa banyak donat seluruhnya? ${piring} \\times {kue} = \\dots$',piring*kue,f'Perkalian berulang: ${piring} \\times {kue} = {piring*kue}$.','v2_sd2_perkalian_dasar',level)
        h=r.randint(1,11)
        return constant(f'Jarum pendek jam dinding menunjuk angka ${h}$ dan jarum panjang menunjuk angka $12$. Jam tersebut menunjukkan pukul ....',h,f'Pukul ${h:02d}.00$.','v2_sd2_jam_analog',level)
    if grade==3:
        if bab==1:
            divisor=r.randint(2,5);quotient=r.randint(15,40);total=divisor*quotient
            return constant(f'Sebanyak ${total}$ permen dibagikan sama banyak kepada ${divisor}$ anak. Berapa permen untuk tiap anak? ${total} \\div {divisor} = \\dots$',quotient,f'${total} \\div {divisor} = {quotient}$.','v2_sd3_pembagian_ratusan',level)
        if bab==2:
            denom=r.choice([3,4,6]);num=r.randint(1,denom-1)
            return constant(f'Sebuah kue bolu dipotong menjadi ${denom}$ bagian sama besar. Budi memakan ${num}$ bagian. Nilai pecahan bagian yang dimakan adalah ....',s.Rational(num,denom),f'Pecahan bagian kue adalah $\\frac{{{num}}}{{{denom}}}$.','v2_sd3_pecahan_sederhana',level)
        p=r.randint(6,12);l=r.randint(3,p-1)
        return constant(f'Persegi panjang memiliki panjang ${p}\\text{{ cm}}$ dan lebar ${l}\\text{{ cm}}$. Kelilingnya adalah $K = 2 \\times (p + l) = \\dots\\text{{ cm}}$.',2*(p+l),f'$K = 2 \\times ({p} + {l}) = {2*(p+l)}$.','v2_sd3_keliling_persegi_panjang',level)
    if grade==4:
        if bab==1:
            k=r.choice([2,3,4])
            return constant(f'Pecahan yang senilai dengan $\\frac{{1}}{{2}}$ jika pembilang dan penyebut dikalikan ${k}$ adalah ....',s.Rational(k,2*k),f'$\\frac{{1 \\times {k}}}{{2 \\times {k}}} = \\frac{{{k}}}{{{2*k}}}$.','v2_sd4_pecahan_senilai',level)
        if bab==2:
            s_val=r.randint(4,12)
            return constant(f'Sebuah persegi memiliki sisi ${s_val}\\text{{ cm}}$. Luasnya adalah $L = s \\times s = \\dots\\text{{ cm}}^2$.',s_val*s_val,f'$L = {s_val} \\times {s_val} = {s_val*s_val}\\text{{ cm}}^2$.','v2_sd4_luas_persegi',level)
        val=r.randint(10,30)
        return constant(f'Diagram batang menunjukkan siswa yang suka apel ada ${val}$ anak dan jeruk ada ${val+5}$ anak. Berapa selisih banyak siswa? ${val+5} - {val} = \\dots$',5,f'${val+5} - {val} = 5$.','v2_sd4_diagram_batang',level)
    if grade==5:
        if bab in [1,9]:return place_value(r,bab==9,code=='B',level)
        if bab==2:
            if code=='E':
                u=r.randint(2,8);v=r.randint(2,8);return constant(f'Tentukan FPB dari {u*6} dan {v*6}.',s.igcd(u*6,v*6),f'Faktorkan kedua bilangan atau daftar faktornya; faktor persekutuan terbesar {s.igcd(u*6,v*6)}.','v2_fpb_langsung',level)
            if level=='medium':
                start=U*A;end=start+A*(B+1);return constant(f'Berapa jumlah kelipatan {A} yang lebih besar dari {start} dan lebih kecil dari {end}?',B,f'Kelipatan yang dihitung mulai {start+A} hingga {end-A}; ada {B} bilangan.','v2_kelipatan_batas_rutin',level)
            if code=='C':
                u=A*U;v=B*U;cap=r.randint(2,U);vals=[j for j in range(1,cap+1) if u%j==v%j==0];best=max(vals)
                return checked(f'Ada {u} jeruk dan {v} apel. Semua dibagi ke kantong dengan isi jeruk sama dan isi apel sama, tanpa sisa. Tersedia paling banyak {cap} kantong. Berapa banyak buah dalam satu kantong jika kantong yang dipakai sebanyak mungkin?',s.Rational(u+v,best),f'Banyak kantong harus faktor kedua jumlah dan tidak lebih dari {cap}. Kandidat {vals}; terbesar {best}. Isi per kantong {u}/{best}+{v}/{best}={s.Rational(u+v,best)}.','v2_faktor_batas_kantong',level,finite(['x'],[[1,cap]],[s.Mod(u,x),s.Mod(v,x)],s.Rational(u+v,1)/x,'min'))
            p=r.randint(3,8);q=r.randint(4,10);period=s.ilcm(p,q);start=r.randint(1,3)*period;end=start+r.randint(3,6)*period;maintenance=period*r.randint(2,3);vals=[j for j in range(start+1,end) if j%p==j%q==0 and j%maintenance!=0]
            return checked(f'Dua lampu menyala tiap {p} dan {q} menit, bersama pada menit 0. Pada menit kelipatan {maintenance}, listrik padam sehingga keduanya tidak menyala. Berapa kali keduanya benar-benar menyala bersama setelah menit {start} dan sebelum menit {end}?',len(vals),f'Kelipatan persekutuan muncul setiap KPK({p},{q})={period} menit. Periksa batas terbuka dan keluarkan jadwal padam. Menit tersisa {vals}; jumlah kejadian {len(vals)}.','v2_kelipatan_jadwal_pengecualian',level,finite(['x'],[[start+1,end-1]],[s.Mod(x,p),s.Mod(x,q),guard(s.Ne(s.Mod(x,maintenance),0))],s.Integer(1),'count'))
        if bab==3:
            den=r.choice([12,18,24,30]);p=r.randint(2,den//3);q=r.randint(p+1,den//2);z=r.randint(q+1,den-1);f=[s.Rational(p,den),s.Rational(q,den),s.Rational(z,den)];r.shuffle(f);left=1-max(f);gap=max(f)-min(f)
            return checked(f'Tiga pita memiliki panjang {m(f[0])}, {m(f[1])}, dan {m(f[2])} meter. Pita terpanjang dipotong hingga panjangnya sama dengan pita terpendek; potongannya disambungkan ke pita yang panjangnya di tengah. Berapa panjang pita tengah setelah disambung?',sorted(f)[1]+gap,f'Urutan panjang {sorted(f)}. Potongan dari terpanjang adalah {max(f)}-{min(f)}={gap}; tambahkan pada pita tengah {sorted(f)[1]}, menjadi {sorted(f)[1]+gap}.','v2_pecahan_urut_potong_sambung',level,system(['a','b','c'],[a-f[0],b-f[1],c-f[2]],a+b+c-2*s.Min(a,b,c)))
        if bab==4:
            if code=='E':
                p=U;q=V;h=A;w=B;C=min(q,h)
                if level=='easy':return constant(f'Dua persegi panjang {p}×{q} cm dan {w}×{h} cm ditempel tanpa tumpang tindih, dengan satu ruas batas sepanjang {C} cm berimpit. Dengan rumus K gabungan=K1+K2-2×ruas berimpit, tentukan keliling gabungan.',2*(p+q+h+w-C),f'Keliling {2*(p+q)}+{2*(h+w)}-2×{C}={2*(p+q+h+w-C)} cm.','v2_keliling_gabungan_terpandu',level)
                shared=min(q,h);return constant(f'Persegi panjang {p}×{q} cm ditempel pada persegi panjang {w}×{h} cm tanpa tumpang tindih. Keduanya memiliki satu ruas batas berimpit sepanjang {shared} cm. Berapa keliling gabungan?',2*(p+q+w+h-shared),f'Jumlah keliling {2*(p+q+w+h)}; ruas bersama dihitung dua kali tetapi bukan batas luar. Kurangi 2×{shared}, hasil {2*(p+q+w+h-shared)}.','v2_keliling_gabungan_ruas',level)
            if code=='B':
                small=U;diff=r.randint(2,5);base=small+diff;per=2*small+base;gap=r.randint(1,3)
                if base>=2*small:base=small+1;diff=1;per=3*small+1
                return checked(f'Segitiga sama kaki berkeliling {per} cm. Alasnya {diff} cm lebih panjang daripada tiap kaki. Pita menutup seluruh alas dan satu kaki, dengan tambahan {gap} cm untuk simpul. Berapa panjang pita?',small+base+gap,f'Tiga sisi terdiri dari dua kaki sama dan alas kaki+{diff}. Kurangi kelebihan alas dari keliling, bagi 3: kaki={small}. Alas={base}. Pita={small}+{base}+{gap}={small+base+gap}.','v2_keliling_segitiga_inverse',level,system(['a','b'],[2*a+b-per,b-a-diff],a+b+gap,[a,b,2*a-b]))
            if code=='D' and level=='medium':
                return constant(f'Segi enam memiliki empat sisi sepanjang {U} cm dan dua sisi sepanjang {V} cm. Berapa kelilingnya?',4*U+2*V,f'Jumlahkan panjang keenam sisi: 4×{U}+2×{V}={4*U+2*V}.','v2_keliling_poligon_kelompok',level)
            if code=='D':
                p=U;q=p+r.randint(2,5);total=3*p+3*q;diff=q-p
                return checked(f'Segi enam memiliki tiga sisi pendek sama panjang dan tiga sisi panjang sama panjang. Tiap sisi panjang {diff} cm lebih panjang daripada sisi pendek. Kelilingnya {total} cm. Dua sisi panjang ditempel ke pita secara terpisah dengan tambahan simpul {C} cm per sisi. Berapa seluruh pita yang diperlukan?',2*(q+C),f'Keliling setelah dikurangi tiga kelebihan panjang {3*diff} menyisakan enam sisi dasar. Sisi pendek {p}, sisi panjang {q}; pita dua sisi plus dua simpul =2({q}+{C})={2*(q+C)}.','v2_keliling_poligon_inverse',level,system(['a','b'],[3*a+3*b-total,b-a-diff],2*(b+C),[a,b]))
            length=U+V;width=U;diff=V;per=2*(length+width);door=C
            return checked(f'Kebun persegi panjang memiliki keliling {per} m; panjangnya {diff} m lebih dari lebarnya. Pagar sepanjang satu sisi panjang dibagi menjadi dua bagian oleh pintu selebar {door} m. Tiga sisi lain memakai dua lapis kawat, sedangkan sisi yang berpintu hanya satu lapis. Berapa total panjang kawat?',2*(length+2*width)+length-door,f'Dari setengah keliling p+l={length+width} dan p-l={diff}, diperoleh p={length},l={width}. Tiga sisi lain total {length+2*width}, dua lapis {2*(length+2*width)}. Sisi berpintu {length-door}; total {2*(length+2*width)+length-door}.','v2_keliling_pagar_lapis_inverse',level,system(['a','b'],[2*(a+b)-per,a-b-diff],2*(a+2*b)+a-door,[a,b,a-door]))
        if bab==5:
            p=U+V;q=U;cutw=r.randint(1,q-1);cuth=r.randint(1,q-1)
            if level=='easy':
                if code=='D':return constant(f'Persegi bersisi {U} cm. Dengan rumus L=s×s, tentukan luasnya.',U*U,f'L={U}×{U}={U*U} cm².','v2_keliling_luas_persegi_dasar',level)
                return constant(f'Bangun gabungan terdiri dari persegi panjang {p}×{q} cm dan persegi {A}×{A} cm tanpa tumpang tindih. Tentukan luas total.',p*q+A*A,f'Jumlah luas {p*q}+{A*A}={p*q+A*A} cm².','v2_luas_gabungan_langsung',level)
            border=r.randint(1,3);total=2*(p+q);query=a*b-cutw*cuth
            return checked(f'Persegi panjang berkeliling {total} cm; panjangnya {V} cm lebih dari lebar. Sebuah persegi panjang kecil {cutw}×{cuth} cm dipotong dari satu sudut. Sisa bangun ditutup ubin seluas 1 cm² per ubin tanpa celah. Berapa ubin yang dibutuhkan?',p*q-cutw*cuth,f'Setengah keliling p+l={p+q}, selisih p-l={V}. Jadi p={p},l={q}. Luas awal {p*q}, luas potongan {cutw*cuth}. Sisa dan jumlah ubin {p*q-cutw*cuth}.','v2_luas_dimensi_potongan_inverse',level,system(['a','b'],[a+b-p-q,a-b-V],query,[a,b,a-cutw,b-cuth]))
        if bab==6:
            alpha=r.randint(10,35);beta=r.randint(10,35);gamma=90-alpha-beta;d=r.randint(2,8)
            if level=='medium':return constant(f'Sudut siku-siku dibagi menjadi tiga sudut berurutan. Dua sudutnya {alpha}° dan {beta}°. Berapa sudut ketiga?',gamma,f'Jumlah 90°. Sudut ketiga 90-{alpha}-{beta}={gamma}°.','v2_sudut_siku_tiga_bagian',level)
            # Three adjacent rays with two overlapping measured angles.
            return checked(f'Dari titik O terdapat empat sinar OA,OB,OC,OD berurutan di dalam sudut siku-siku AOD. Diketahui AOC={alpha+beta}° dan BOD={beta+gamma}°. Jika busur derajat diputar sehingga OA terbaca {d}°, berapa bacaan untuk OB pada arah putar yang sama?',alpha+d,f'Tulis AOB=u, BOC=v, COD=w. Ketiganya berjumlah 90°, u+v={alpha+beta}, v+w={beta+gamma}. Jumlah dua pengukuran dikurangi 90 memberi v={beta}. Maka u={alpha}; setelah nol alat bergeser {d}°, OB terbaca {alpha+d}°.','v2_sudut_tumpang_tindih_alat',level,system(['a','b','c'],[a+b+c-90,a+b-alpha-beta,b+c-beta-gamma],a+d,[a,b,c]))
        if bab==7:
            if code=='A':
                U=max(U,5)
                leg=U+3;base=2*U-1;per=2*leg+base;diff=leg-base
                return checked(f'Segitiga mempunyai tepat dua sisi sama panjang. Kelilingnya {per} cm. Sisi yang tidak sama {abs(diff)} cm '+('lebih pendek' if diff>0 else 'lebih panjang')+f' daripada masing-masing sisi sama. Tentukan panjang sisi tidak sama.',base,f'Sifat segitiga sama kaki memberi dua kaki sama. Jika kaki x, alas x-({diff}); maka 3x-({diff})={per}, x={leg}. Alas {base}. Periksa 2×{leg}>{base}.','v2_ciri_segitiga_rekonstruksi',level,system(['a','b'],[2*a+b-per,a-b-diff],b,[a,b,2*a-b]))
            diag1=U+V;diag2=U;diff=V;area=s.Rational(diag1*diag2,2)
            return checked(f'Sebuah segi empat mempunyai empat sisi sama panjang, dan kedua diagonal saling tegak lurus serta membagi dua. Jumlah panjang diagonal {diag1+diag2} cm, selisihnya {diff} cm. Berapa luasnya? Gunakan L=1/2×d1×d2 setelah mengenali sifat bangun.',area,f'Sifat menunjukkan belah ketupat. Dari jumlah dan selisih, diagonal {diag1} dan {diag2}. Luas setengah hasil kali={area} cm².','v2_ciri_segiempat_diagonal_inverse',level,system(['a','b'],[a+b-diag1-diag2,a-b-diff],a*b/2,[a,b]))
        if bab==8:
            if code=='C':
                vals=[r.randint(5,20) for _ in range(4)];value=abs(max(vals)-sum(vals[:2]))
                return constant(f'Diagram batang menunjukkan penjualan Senin–Kamis berturut-turut {vals} unit, semua batang memakai skala sama mulai nol. Berapa selisih mutlak antara penjualan tertinggi sehari dengan jumlah penjualan dua hari pertama?',value,f'Tertinggi sehari {max(vals)}, jumlah dua hari pertama {sum(vals[:2])}. Kurangi nilai yang lebih kecil dari yang lebih besar, selisih {value}.','v2_batang_gabungan_perbandingan',level)
            counts=[r.randint(3,9) for _ in range(4)];duplicated=r.randint(1,min(counts));missing=r.randint(1,3);raw=sum(counts)+duplicated;value=counts[2]+missing
            return checked(f'Survei pilihan buah memiliki {raw} lembar masuk, termasuk {duplicated} lembar duplikat yang harus dihapus. Setelah dihapus, kategori apel,mangga,jeruk,pisang berjumlah {counts[0]}, {counts[1]}, x, {counts[3]}. Ternyata {missing} siswa lain belum dicatat dan semuanya memilih jeruk. Berapa frekuensi jeruk setelah audit lengkap?',value,f'Lembar sah awal {raw}-{duplicated}={sum(counts)}. Kurangi kategori selain jeruk {counts[0]+counts[1]+counts[3]} memberi jeruk {counts[2]}. Tambah {missing} data tertinggal menjadi {value}.','v2_pengumpulan_data_duplikat_hilang',level,system(['a'],[a+counts[0]+counts[1]+counts[3]-raw+duplicated],a+missing,[a]))
    if grade==6:
        if bab==1:
            denom=r.choice([4,5,8,10]);used=r.randint(1,denom-2);fraction=s.Rational(used,denom);initial=denom*r.randint(3,9);extra=r.randint(2,8);portion=s.Rational(r.randint(1,3),4)
            if level=='medium':
                if code=='A':return constant(f'Sebanyak {initial} kg tepung tersedia. {m(fraction)} bagiannya dipakai. Dari tepung yang dipakai, {m(portion)} bagian untuk kue A. Berapa kg tepung untuk kue A?',initial*fraction*portion,f'Tepung terpakai {initial*fraction} kg; bagian kue A {initial*fraction*portion} kg.','v2_perkalian_pecahan_bertahap',level)
                weight=s.Rational(r.randint(12,45),10);price=r.randint(3,9)*1000;paid=price*10
                return constant(f'Harga buah {price} rupiah per kg. Membeli {decimal(weight)} kg dan membayar {paid} rupiah. Berapa kembaliannya?',paid-price*weight,f'Harga pembelian {price}×{decimal(weight)}={price*weight}; kembali {paid-price*weight}.','v2_desimal_harga_kembalian',level)
            remain=initial*(1-fraction);final=(remain+extra)*(1-portion);packet=s.Rational(r.randint(1,3),4)
            if code=='B':
                val=s.floor(final/packet)
                return checked(f'Tersedia tepung sejumlah belum diketahui. {m(fraction)} bagiannya dipakai, dan sisanya {m(remain)} kg. Kemudian ditambah {extra} kg dan {m(portion)} dari stok baru dipakai lagi. Tepung tersisa dikemas masing-masing {m(packet)} kg. Berapa kemasan penuh yang dapat dibuat?',val,f'Sisa awal menunjukkan stok awal {initial} kg. Stok setelah tambahan {remain+extra}; sesudah pemakaian kedua tersisa {final}. Bagi berat tiap kemasan dan ambil bagian bulat: {val}.','v2_pembagian_pecahan_stok',level,system(['a'],[(1-fraction)*a-remain],s.floor(((1-fraction)*a+extra)*(1-portion)/packet),[a]))
            # Reverse first allocation, then a second allocation with a changed base.
            value=initial*fraction+portion*(remain+extra)
            if code=='C':
                return checked(f'Persediaan bahan mula-mula belum diketahui. Setelah {decimal(fraction)} dari seluruh bahan dipakai, tersisa {decimal(remain)} kg. Stok ditambah {extra} kg; lalu {decimal(portion)} dari stok sesudah tambahan dipakai. Berapa total bahan yang dipakai dalam kedua tahap, dalam kg?',value,f'Sisa awal adalah {decimal(1-fraction)} kali stok awal, jadi stok awal {initial} kg. Pemakaian pertama {decimal(initial*fraction)} kg. Stok baru {decimal(remain+extra)} kg; pemakaian kedua {decimal(portion*(remain+extra))} kg. Total {decimal(value)} kg.','v2_desimal_basis_berubah_inverse',level,system(['a'],[(1-fraction)*a-remain],fraction*a+portion*((1-fraction)*a+extra),[a]))
            return checked(f'Persediaan bahan mula-mula belum diketahui. Setelah {m(fraction)} bagiannya dipakai, tersisa {m(remain)} kg. Stok lalu ditambah {extra} kg; {m(portion)} dari stok sesudah tambahan dipakai. Berapa total bahan yang dipakai pada kedua tahap?',value,f'Sisa awal adalah {1-fraction} bagian, sehingga stok awal {initial} kg. Pemakaian pertama {initial*fraction}. Dasar pecahan tahap kedua berubah menjadi {remain+extra}; pemakaian kedua {portion*(remain+extra)}. Jumlah {value}.','v2_pecahan_basis_berubah_inverse',level,system(['a'],[(1-fraction)*a-remain],fraction*a+portion*((1-fraction)*a+extra),[a]))
        if bab==2:return ratio(r,code)
        if bab==3:
            if code=='A':
                n=r.randint(6,16);k=r.choice([j for j in range(1,n//2+1) if (n-j)%2==0]);removed=3*n*k*k-2*k**3;val=n**3-removed
                if level=='medium':return constant(f'Kubus besar disusun dari {n}×{n}×{n} kubus satuan. Satu lapisan atas dan satu lapisan bawah diambil. Berapa kubus satuan tersisa?',n*n*(n-2),f'Lapisan tersisa {n-2}, tiap lapisan {n*n} kubus. Total {n*n*(n-2)}.','v2_kubus_lapisan',level)
                # Three centered, mutually perpendicular through-tunnels share one cube.
                return checked(f'Kubus {n}×{n}×{n} tersusun dari kubus satuan. Dibuat tiga terowongan lurus saling tegak lurus, masing-masing penampang {k}×{k} dan menembus sepanjang {n}. Ketiga terowongan berpotongan pada blok pusat {k}×{k}×{k}; setiap perpotongan dua terowongan tepat blok pusat yang sama. Berapa kubus satuan yang tidak dibuang?',val,f'Setiap terowongan membuang {n*k*k}. Menjumlahkan tiga terowongan menghitung blok pusat tiga kali. Agar blok pusat dihitung sekali, kurangi dua kali volume pusat. Kubus dibuang {removed}, sisa {n**3}-{removed}={val}.','v2_konstruksi_tiga_terowongan',level,system(['a','b'],[a-n*k*k,b-k**3],n**3-(3*a-2*b)))
            if code=='B':
                top=r.randint(3,5);h11=top;h12=r.randint(1,top);h21=r.randint(1,top);h22=top;front=[max(h11,h21),max(h12,h22)];side=[max(h11,h12),max(h21,h22)]
                if level=='medium':return constant(f'Tumpukan kubus pada kisi 2×2 memiliki tinggi baris pertama ({h11},{h12}) dan kedua ({h21},{h22}). Tampak depan menunjukkan maksimum tiap kolom. Berapa jumlah dua tinggi pada tampak depan?',sum(front),f'Maksimum kolom pertama {front[0]}, kedua {front[1]}; jumlah {sum(front)}.','v2_spasial_tampak_depan',level)
                # Break full symmetry with one specified height and a column maximum.
                f1=top;f2=r.randint(2,top);s1=top;s2=r.randint(1,top);fixed=r.randint(1,min(f2,s1));ranges=[[1,top]]*4;aa,bb,cc,dd=s.symbols('a b c d',real=True);eq=[s.Max(aa,cc)-f1,s.Max(bb,dd)-f2,s.Max(aa,bb)-s1,s.Max(cc,dd)-s2,bb-fixed];cert=finite(['a','b','c','d'],ranges,eq,aa+bb+cc+dd,'min')
                # Some randomly drawn views are inconsistent; construct a guaranteed witness.
                f1=top;f2=h12;s1=top;s2=h21;fixed=h12;eq=[s.Max(aa,cc)-f1,s.Max(bb,dd)-f2,s.Max(aa,bb)-s1,s.Max(cc,dd)-s2,bb-fixed];cert=finite(['a','b','c','d'],ranges,eq,aa+bb+cc+dd,'min');val=top+fixed+h21+1
                return checked(f'Empat sel kisi 2×2 semuanya berisi tumpukan kubus tegak tanpa celah. Tingginya a,b pada baris depan, c,d pada baris belakang. Tampak depan memberi maksimum tiap kolom ({f1},{f2}); tampak samping memberi maksimum tiap baris ({s1},{s2}). Diketahui b={fixed}. Berapa jumlah kubus paling sedikit yang mungkin?',val,f'Karena b={fixed}<{top}, maksimum baris depan menentukan a={top}. Maksimum baris belakang {h21}, sehingga c atau d harus {h21}; untuk minimum, pilih satu sel setinggi {h21}, yang lain 1, selama batas kolom dipenuhi. Total minimum {val}.','v2_spasial_minimum_multitampak',level,cert) if fixed<top else generate(grade,bab,code,level,r)
            sx=r.randint(1,5);sy=r.randint(1,5);right=r.randint(4,9);up=r.randint(3,8);left=r.randint(1,right-1);down=r.randint(1,up-1);dx=right-left;dy=up-down;end=(sx+dx,sy+dy);query=a+b
            return checked(f'Pada kisi, setiap langkah ke kanan menambah x dan ke atas menambah y. Dari titik awal yang belum diketahui, Rani bergerak {right} langkah kanan, {up} atas, {left} kiri, {down} bawah, lalu tiba di ({end[0]},{end[1]}). Dari titik awal yang sama ia harus mencapai ({end[0]+C},{end[1]+B}) dengan hanya langkah kanan dan atas. Berapa jumlah langkah paling sedikit?',dx+dy+C+B,f'Gerak bersih perjalanan awal ({dx},{dy}), jadi titik awal ({sx},{sy}). Selisih koordinat menuju tujuan baru ({dx+C},{dy+B}); semua positif, total minimum {dx+dy+C+B}.','v2_lokasi_balik_jalur',level,system(['a','b'],[a+dx-end[0],b+dy-end[1]],end[0]+C-a+end[1]+B-b))
        red=r.randint(3,8);blue=r.randint(4,10);add=r.randint(1,4);total=red+blue;after=s.Rational(red+add,total+add)
        if level=='medium':return constant(f'Pemutar adil memiliki {red} sektor merah dan {blue} biru sama luas. Sebanyak {add} sektor merah ditambahkan. Berapa peluang berhenti pada merah sesudah perubahan?',after,f'Sektor merah kini {red+add}, total {total+add}; peluang {after}.','v2_skala_peluang_perubahan',level)
        # Equal-probability condition reconstructs counts using an integer difference.
        red=r.randint(3,8);blue=red+add;after_remove=r.randint(1,red-1);value=s.Rational(red-after_remove,2*red+add-after_remove)
        return checked(f'Pemutar memiliki sektor merah dan biru sama luas. Sektor biru {add} lebih banyak daripada merah. Jika {add} sektor merah baru ditambahkan, kedua warna menjadi sama mungkin dan jumlah sektor menjadi {2*(red+add)}. Pemutar dikembalikan ke keadaan semula, lalu {after_remove} sektor merah dihapus. Berapa peluang merah pada pemutar terakhir?',value,f'Sesudah penambahan tiap warna memiliki {red+add} sektor. Maka merah semula {red}, biru {red+add}. Setelah penghapusan merah tinggal {red-after_remove}, total {2*red+add-after_remove}. Peluang {value}.','v2_peluang_rekonstruksi_sektor',level,system(['a','b'],[b-a-add,a+b+add-2*(red+add)],(a-after_remove)/(a+b-after_remove),[a-after_remove,b]))
    raise ValueError((grade,bab,code,level))
