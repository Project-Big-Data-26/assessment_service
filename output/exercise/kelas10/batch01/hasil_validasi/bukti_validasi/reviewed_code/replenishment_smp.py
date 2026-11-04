"""SMP mathematics variation families with exact arithmetic and explicit assumptions."""
import math
import sympy as s
from .replenishment_math import numeric,text,m,rp,pair,statistics,linear,probability,factors


def generate(book,bab,code,level,r):
    grade=int(book[5:]);a=r.randint(2,12);b=r.randint(2,10);k=r.randint(2,8)
    if grade==7:
        if bab==1:
            if code=='A':
                v=-r.randint(8,25);n=r.randint(3,6)
                return numeric(f'Terdapat {n} bilangan bulat negatif berbeda yang semuanya lebih besar daripada {v}. Berapakah nilai terkecil yang mungkin untuk bilangan terbesar di antara bilangan-bilangan itu?',v+n,
                               f'Agar nilai terbesarnya minimum, pilih {n} bilangan bulat berurutan mulai {v+1}. Yang terbesar adalah {v+n}.','urutan_bilangan_bulat')
            if code=='B':return numeric(f'Suhu mula-mula $-{a}$°C, naik {b}°C, lalu turun {k}°C. Berapa suhu akhirnya?',-a+b-k,f'Suhu akhir = -{a}+{b}-{k}={-a+b-k}°C.','operasi_bilangan_bulat')
            return numeric(f'Tiga bel berbunyi setiap {a}, {b}, dan {k} menit. Ketiganya berbunyi bersama sekarang. Setelah berapa menit ketiganya berbunyi bersama lagi?',s.ilcm(a,b,k),f'Cari KPK dari {a}, {b}, dan {k}: {s.ilcm(a,b,k)} menit.','faktor_dan_kpk')
        if bab==2:
            p=s.Rational(a,a+b);q=s.Rational(b,b+k)
            if code=='A':
                n=r.randint(-8,8);fraction=s.Rational(r.randint(1,8),10)
                return numeric(f'Bilangan {m(n+fraction)} terletak di antara dua bilangan bulat berurutan. Berapa jumlah kedua bilangan bulat tersebut?',2*n+1,
                               f'Karena 0<{fraction}<1, batasnya {n} dan {n+1}. Jumlah keduanya {2*n+1}.','letak_bilangan_rasional')
            if code=='B':
                return numeric(f'Diketahui bilangan {m(-p)} dan {m(-q)}. Berapa selisih bilangan yang lebih besar dengan yang lebih kecil?',abs(p-q),
                               f'Bandingkan nilai pecahan negatif, lalu hitung nilai mutlak selisihnya: |(-{p})-(-{q})|={abs(p-q)}.','membandingkan_rasional')
            return numeric(f'Hitung nilai {m(p)} + {m(q)} × {k}.',p+q*k,f'Kerjakan perkalian dahulu, lalu jumlahkan: {p}+({q}×{k})={p+q*k}.','operasi_rasional',wrong=[(p+q)*k,p+q/k,p*q*k])
        if bab==3:
            if code=='A':return numeric(f'Rasio banyak buku fiksi terhadap nonfiksi adalah {a}:{b}. Jumlahnya {k*(a+b)} buku. Berapa buku nonfiksi?',b*k,f'Satu bagian rasio bernilai {k}. Buku nonfiksi={b}×{k}={b*k}.','rasio_bagian_total')
            if code=='B':
                scale=r.choice([100,200,250,500,1000]);length=r.randint(3,25)
                return numeric(f'Panjang jalan pada denah {length} cm dengan skala 1:{scale}. Berapa panjang sebenarnya dalam meter?',s.Rational(length*scale,100),
                               f'Panjang sebenarnya={length}×{scale} cm={s.Rational(length*scale,100)} meter.','skala_peta')
            return numeric(f'Sebuah mesin menghasilkan {a*b} barang dalam {a} menit dengan laju tetap. Berapa barang yang dihasilkan dalam {a+k} menit?',b*(a+k),
                           f'Laju mesin={a*b}/{a}={b} barang/menit. Dalam {a+k} menit dihasilkan {b*(a+k)} barang.','laju_satuan')
        if bab==4:
            if code=='A':return numeric(f'Pada bentuk aljabar {m(a*s.Symbol("x")-b*s.Symbol("y")+k)}, berapa jumlah koefisien $x$ dan $y$?',a-b,
                                       f'Koefisien x adalah {a}; koefisien y adalah -{b}. Jumlahnya {a-b}.','unsur_aljabar')
            if code=='B':
                x=s.Symbol('x');expr=s.expand((x+a)*(x+b));v=expr.subs(x,k)
                return numeric(f'Diketahui $P(x)=(x+{a})(x+{b})$. Setelah dikembangkan, tentukan $P({k})$.',v,
                               f'Polinomialnya {m(expr)}. Substitusi x={k} menghasilkan {v}.','operasi_aljabar')
            total=a*k+b
            return numeric(f'Biaya sewa alat terdiri atas biaya tetap {rp(b*1000)} dan biaya {rp(a*1000)} per jam. Jika total biaya {rp(total*1000)}, berapa lama sewanya?',k,
                           f'Model biaya: {b}+{a}t={total} dalam ribu rupiah. Jadi t=({total}-{b})/{a}={k} jam.','pemodelan_aljabar')
        if bab==5:
            if code=='A':
                c=r.randint(25,75);d=r.randint(25,75);v=180-c-d
                return numeric(f'Dua sudut sebuah segitiga masing-masing {c}° dan {d}°. Tentukan sudut ketiganya.',v,f'Jumlah sudut segitiga 180°. Sudut ketiga=180-{c}-{d}={v}°.','hubungan_sudut')
            ratio=r.randint(2,6);small=r.randint(3,20)
            if code=='B':return numeric(f'Dua persegi panjang sebangun. Panjang sisi bersesuaian pada bangun kecil dan besar adalah {a} cm dan {a*ratio} cm. Jika sisi lain pada bangun kecil {small} cm, berapa sisi bersesuaiannya pada bangun besar?',small*ratio,
                                       f'Faktor skala={a*ratio}/{a}={ratio}. Sisi lainnya={small}×{ratio}={small*ratio} cm.','arti_kesebangunan')
            return numeric(f'Segitiga ABC sebangun dengan DEF dengan korespondensi A-D, B-E, C-F. Jika AB={a} cm, DE={a*ratio} cm, dan BC={small} cm, tentukan EF.',small*ratio,
                           f'EF/BC=DE/AB={ratio}, sehingga EF={ratio}×{small}={small*ratio} cm.','kesebangunan_segitiga')
        if bab==6:
            if code=='A':return statistics(r,level)
            if code=='B':
                count=r.randint(12,40)
                return text(f'Peneliti mencatat banyak saudara kandung dari {count} siswa. Jenis data banyak saudara kandung adalah ....','Data kuantitatif diskret.',
                            ['Data kuantitatif kontinu.','Data kualitatif nominal.','Data kualitatif ordinal.'],
                            'Banyak saudara dihitung dalam bilangan bulat, sehingga merupakan data kuantitatif diskret.','jenis_data')
            if code=='C':
                vals=r.sample(range(10,50),3);idx=vals.index(max(vals))
                return text(f'Data penjualan produk A, B, C berturut-turut {vals[0]}, {vals[1]}, dan {vals[2]}. Jika digambar pada diagram batang dengan skala sama mulai nol, batang tertinggi mewakili ....',
                            f'Produk {"ABC"[idx]}.',[f'Produk {"ABC"[(idx+1)%3]}.',f'Produk {"ABC"[(idx+2)%3]}.','Ketiganya sama tinggi.'],
                            f'Frekuensi terbesar {max(vals)} milik produk {"ABC"[idx]}, sehingga batangnya tertinggi.','membaca_diagram')
            if code=='D':
                v1=r.randint(12,40);v2=r.randint(12,40);v3=r.randint(12,40)
                return numeric(f'Diagram batang mencatat penjualan hari Senin {v1} unit, Selasa {v2} unit, dan Rabu {v3} unit. Berapa selisih penjualan tertinggi dan terendah?',max(v1,v2,v3)-min(v1,v2,v3),
                               f'Tertinggi {max(v1,v2,v3)}, terendah {min(v1,v2,v3)}. Selisih={max(v1,v2,v3)-min(v1,v2,v3)} unit.','interpretasi_diagram_batang')
            if code=='E':
                total=12*r.randint(4,12);part=r.randint(1,10);value=30*part
                return numeric(f'Dalam diagram lingkaran yang memuat {total} siswa, suatu kategori beranggotakan {total*part//12} siswa. Berapa sudut pusat kategori itu?',value,
                               f'Sudut pusat=({total*part//12}/{total})×360°={value}°.','diagram_lingkaran')
            survey=r.randint(4,60)
            if level=='easy':
                return text(f'Sekolah ingin membandingkan jumlah anggota {survey} ekstrakurikuler yang berbeda. Diagram yang paling tepat untuk membandingkan besar tiap kategori adalah ....','Diagram batang.',
                            ['Diagram garis untuk urutan waktu.','Diagram pencar untuk dua variabel numerik.','Gambar dekorasi tanpa skala.'],
                            'Data berupa kategori dan jumlah, sehingga diagram batang memudahkan perbandingan antar kategori.','memilih_diagram_kategori')
            if level=='medium':
                return text(f'Data suhu diukur setiap jam selama {survey} jam untuk melihat perubahannya. Diagram yang paling sesuai adalah ....','Diagram garis.',
                            ['Diagram lingkaran.','Piktogram tanpa urutan waktu.','Diagram batang bertumpuk tanpa keterangan waktu.'],
                            'Diagram garis menampilkan perubahan nilai secara berurutan terhadap waktu.','memilih_diagram_waktu')
            return text(f'Peneliti mengukur durasi belajar dan nilai tes dari {survey*5} siswa. Ia ingin memeriksa pola hubungan kedua variabel, bukan proporsi kategori atau perubahan waktu. Diagram yang paling tepat adalah ....','Diagram pencar.',
                        ['Diagram lingkaran nilai tes.','Diagram garis dengan siswa diurutkan sembarang.','Piktogram jumlah siswa saja.'],
                        'Setiap siswa menghasilkan pasangan dua variabel numerik. Diagram pencar memperlihatkan arah dan pola hubungannya.','evaluasi_pemilihan_diagram')
    if grade==8:
        if bab==1:
            if code=='A':
                base=r.randint(2,5);p=r.randint(2,5);q=r.randint(2,4);t=r.randint(1,4);v=p*q-t
                return numeric(f'Bentuk $({base}^{p})^{q} : {base}^{t}$ ditulis sebagai ${base}^n$. Tentukan $n$.',v,
                               f'Pangkat pada pangkat dikalikan, lalu pada pembagian dikurangi: n={p}×{q}-{t}={v}.','aturan_pangkat')
            if code=='B':
                d=r.choice([2,3,5,6,7]);u=r.randint(2,9);v=r.randint(2,9)
                return numeric(f'Sederhanakan $\\sqrt{{{u*u*d}}}+\\sqrt{{{v*v*d}}}$.',(u+v)*s.sqrt(d),
                               f'Keluarkan faktor kuadrat: {u}√{d}+{v}√{d}=({u+v})√{d}.','operasi_bentuk_akar',wrong=[s.sqrt((u*u+v*v)*d),(u+v)*d,(u*v)*s.sqrt(d)])
            exponent=r.randint(3,8);coefficient=r.randint(11,99)
            return numeric(f'Bilangan {coefficient*10**exponent} ditulis sebagai $a\\times10^n$ dengan $1\\le a<10$. Berapakah nilai $n$?',exponent+1,
                           f'{coefficient*10**exponent}=({coefficient}/10)×10^{exponent+1}. Koefisien berada pada [1,10), sehingga n={exponent+1}.','bentuk_baku')
        if bab==2:
            triple=r.choice([(3,4,5),(5,12,13),(8,15,17),(7,24,25)]);scale=r.randint(1,5);u,v,h=[z*scale for z in triple]
            if code=='B':return numeric(f'Dua sisi terpendek suatu tripel Pythagoras adalah {u} dan {v}. Berapa sisi terpanjangnya?',h,f'√({u}²+{v}²)=√{h*h}={h}.','tripel_pythagoras')
            if code=='C':
                side=r.randint(3,20)
                return numeric(f'Segitiga siku-siku sama kaki mempunyai kedua sisi siku-siku {side} cm. Berapa panjang sisi miringnya?',side*s.sqrt(2),
                               f'Dengan Pythagoras: c=√({side}²+{side}²)={side}√2 cm.','segitiga_istimewa')
            if code=='E':
                x1=r.randint(-10,10);y1=r.randint(-10,10)
                return numeric(f'Tentukan jarak antara titik {pair(x1,y1)} dan {pair(x1+u,y1+v)}.',h,
                               f'Selisih koordinat mendatar {u}, tegak {v}. Jarak=√({u}²+{v}²)={h}.','rumus_jarak')
            context='Sebuah tangga bersandar pada tembok tegak' if code=='D' else 'Sebuah segitiga siku-siku memiliki dua sisi yang saling tegak lurus'
            question=(f'{context}. Jarak kaki tangga ke tembok {u} m dan tinggi ujung tangga {v} m. Berapa panjang tangga?' if code=='D'
                      else f'{context} dengan panjang {u} cm dan {v} cm. Berapa panjang sisi miringnya?')
            return numeric(question,h,f'Pythagoras memberi c²={u}²+{v}²={h*h}; jadi c={h}.','penerapan_pythagoras')
        if bab==3:
            if code=='A':return linear(r,level)
            if code=='B':return linear(r,level)
            return linear(r,level,'inequality')
        if bab==4:
            if code=='A':
                A=[r.randint(1,4),r.randint(5,8),r.randint(9,12)];B=[a*b,a*(b+1),a*(b+2)]
                pairs=[(u,v) for u in A for v in B if v%u==0]
                return numeric(f'Diketahui A={A} dan B={B}. Relasi dari A ke B adalah "faktor dari". Berapa banyak pasangan berurutan dalam relasi tersebut?',len(pairs),
                               f'Pasangan yang memenuhi adalah {pairs}; jumlahnya {len(pairs)}.','relasi_faktor')
            if code=='B':
                value=a*k+b
                return numeric(f'Fungsi $f(x)={a}x+{b}$. Jika $f(t)={value}$, tentukan $t$.',k,
                               f'{a}t+{b}={value}, sehingga t=({value}-{b})/{a}={k}.','fungsi_linear')
            n=r.randint(3,8)
            return numeric(f'Himpunan A dan B masing-masing memiliki {n} anggota. Berapa banyak korespondensi satu-satu dari A ke B?',math.factorial(n),
                           f'Pilihan pasangan berturut-turut {n}, {n-1}, ..., 1. Jumlahnya {n}!={math.factorial(n)}.','korespondensi_satu_satu')
        if bab==5:
            slope=r.choice([-4,-3,-2,2,3,4]);intercept=r.randint(-9,9);x0=r.randint(-5,8)
            if code=='A':return numeric(f'Garis mempunyai persamaan $y={slope}x+({intercept})$. Berapa ordinat titik pada garis yang absisnya {x0}?',slope*x0+intercept,
                                       f'Substitusi x={x0}: y={slope}×({x0})+({intercept})={slope*x0+intercept}.','grafik_garis_lurus')
            x1=r.randint(-5,5);y1=r.randint(-8,8);dx=r.randint(2,7)
            return numeric(f'Garis melalui {pair(x1,y1)} dan {pair(x1+dx,y1+slope*dx)}. Tentukan gradiennya.',slope,
                           f'm=({y1+slope*dx}-({y1}))/({x1+dx}-({x1}))={slope*dx}/{dx}={slope}.','gradien')
        if bab==6:return statistics(r,level,'range' if code=='B' else ('median' if level=='medium' else 'mean'))
    if grade==9:
        if bab==1:
            u=r.randint(2,15);v=r.randint(2,15);p=r.randint(2,7);q=r.randint(2,7)
            if code=='A':return numeric(f'Titik $(x,{v})$ memenuhi persamaan ${p}x+{q}y={p*u+q*v}$. Tentukan $x$.',u,
                                       f'{p}x+{q}×{v}={p*u+q*v}; jadi {p}x={p*u}, sehingga x={u}.','persamaan_dua_variabel')
            return numeric(f'Diketahui $x+y={u+v}$ dan ${p}x+{p+1}y={p*u+(p+1)*v}$. Tentukan $x$.',u,
                           f'Kurangi persamaan kedua dengan {p} kali persamaan pertama: y={v}. Maka x={u+v}-{v}={u}.','sistem_linear_dua_variabel')
        if bab==2:
            u=r.randint(4,18);v=r.randint(3,15);h=r.randint(3,16)
            if code=='A':
                n=r.randint(3,10)
                return numeric(f'Sebuah prisma tegak memiliki alas segi-{n}. Berapa banyak rusuk prisma tersebut?',3*n,
                               f'Alas dan tutup masing-masing {n} rusuk, ditambah {n} rusuk tegak: total 3×{n}={3*n}.','ciri_prisma')
            if code=='B':return numeric(f'Balok mempunyai panjang {u} cm, lebar {v} cm, dan tinggi {h} cm. Berapa luas permukaannya?',2*(u*v+u*h+v*h),
                                       f'L=2(pl+pt+lt)=2({u*v}+{u*h}+{v*h})={2*(u*v+u*h+v*h)} cm².','luas_permukaan_balok')
            if code=='C':return numeric(f'Balok berukuran {u} cm × {v} cm × {h} cm. Berapa volumenya?',u*v*h,
                                       f'V=p×l×t={u}×{v}×{h}={u*v*h} cm³.','volume_balok')
            if code=='D':return numeric(f'Lingkaran mempunyai jari-jari {u} cm. Dengan $\\pi$ tetap sebagai simbol, berapa luasnya?',u*u*s.pi,
                                       f'L=πr²=π×{u}²={u*u}π cm².','luas_lingkaran')
            if code=='E':return numeric(f'Tabung tertutup memiliki jari-jari {u} cm dan tinggi {h} cm. Berapa luas seluruh permukaannya dalam bentuk $\\pi$?',2*u*(u+h)*s.pi,
                                       f'L=2πr(r+t)=2π×{u}×({u}+{h})={2*u*(u+h)}π cm².','luas_permukaan_tabung')
            return numeric(f'Kerucut memiliki jari-jari {u} cm dan tinggi {h} cm. Berapa volumenya dalam bentuk $\\pi$?',s.Rational(u*u*h,3)*s.pi,
                           f'V=πr²t/3=π×{u}²×{h}/3={s.Rational(u*u*h,3)}π cm³.','volume_kerucut')
        if bab==3:
            px=r.randint(-12,12);py=r.randint(-12,12);dx=r.randint(2,9);dy=r.randint(2,9)
            if code=='A':tx,ty=px+dx,py+dy;desc=f'ditranslasi oleh vektor {pair(dx,dy)}'
            elif code=='B':tx,ty=-px,py;desc='dicerminkan terhadap sumbu-$y$'
            elif code=='C':tx,ty=-py,px;desc='dirotasi 90° berlawanan arah jarum jam terhadap O(0,0)'
            elif code=='E':tx,ty=k*px,k*py;desc=f'didilatasi berpusat di O(0,0) dengan faktor {k}'
            else:
                u=r.randint(4,20);v=r.randint(4,20);w=r.randint(max(u,v),u+v-1)
                return numeric(f'Segitiga ABC kongruen dengan DEF, dengan A-D, B-E, C-F. Jika AB={u} cm, BC={v} cm, AC={w} cm, berapa keliling DEF?',u+v+w,
                               f'Bangun kongruen mempunyai sisi bersesuaian sama panjang. Keliling DEF={u}+{v}+{w}={u+v+w} cm.','kekongruenan')
            choices=[pair(tx+1,ty),pair(tx,ty+1),pair(tx-1,ty-1)]
            return text(f'Titik P{pair(px,py)} {desc}. Koordinat bayangannya adalah ....',pair(tx,ty),choices,
                        f'Gunakan aturan transformasi tersebut pada koordinat ({px},{py}), diperoleh ({tx},{ty}).','transformasi_koordinat')
        if bab==4:
            if code=='A':return probability(r,level,'two' if level=='hard' else 'single')
            if code=='B':
                total=r.randint(30,90);hit=r.randint(5,total-5)
                return numeric(f'Dalam {total} percobaan, suatu kejadian muncul {hit} kali. Berapa peluang empirisnya?',s.Rational(hit,total),
                               f'Peluang empiris=frekuensi kejadian/banyak percobaan={hit}/{total}={s.Rational(hit,total)}.','peluang_empiris')
            if code=='C':return probability(r,level,'expected')
            n=r.randint(5,15);groups=r.randint(3,8);pop=n*groups;sample=r.randint(2,n)
            return numeric(f'Populasi terdiri atas {groups} kelompok dengan anggota sama banyak, total {pop} orang. Sampel diambil proporsional, {sample} orang per kelompok. Berapa jumlah seluruh sampel?',sample*groups,
                           f'Ada {groups} kelompok, masing-masing menyumbang {sample} orang, sehingga sampelnya {sample*groups} orang.','sampling_proporsional')
    raise ValueError(f'Unsupported SMP topic {book}/{bab}/{code}')
