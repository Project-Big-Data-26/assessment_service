"""Regular SMA templates: algebra, geometry, statistics, finance and probability."""
import math
import sympy as s
from .replenishment_math import numeric,text,m,rp,pair,statistics,linear,probability,sequences


def finance(r,level,mode):
    principal=r.randint(3,30)*1200000;rate=r.choice([2,3,4,5,6,8,10,12]);years=r.randint(2,5)
    i=s.Rational(rate,100)
    if mode=='simple':
        months=r.randint(3,24);interest=s.Rational(principal*rate*months,1200)
        if level=='hard':
            desired=interest+principal
            return numeric(f'Simpanan berbunga tunggal {rate}% per tahun menjadi {rp(desired)} setelah {months} bulan. Berapa modal awalnya?',principal,
                           f'Nilai akhir M=P(1+{rate}/100×{months}/12). Maka P={desired}/({1+i*s.Rational(months,12)})={principal} rupiah.','bunga_tunggal_balik')
        return numeric(f'Modal {rp(principal)} disimpan dengan bunga tunggal {rate}% per tahun selama {months} bulan. Berapa bunga yang diperoleh?',interest,
                       f'Bunga=P×r×t={principal}×{rate}/100×{months}/12={interest} rupiah.','bunga_tunggal')
    if mode=='compound':
        value=principal*(1+i)**years
        return numeric(f'Modal {rp(principal)} mendapat bunga majemuk {rate}% per tahun. Tanpa pembulatan antara dan tanpa transaksi lain, berapa nilai akhir setelah {years} tahun?',value,
                       f'M=P(1+i)^n={principal}(1+{rate}/100)^{years}={value} rupiah.','investasi_majemuk',wrong=[principal*(1+i*years),principal*(1+i)**(years-1),principal*i*years])
    if mode=='annuity_investment':
        payment=r.randint(1,9)*100000;periods=r.randint(3,8)
        value=payment*sum((1+i)**j for j in range(periods))
        return numeric(f'Pada akhir setiap tahun disetor {rp(payment)} selama {periods} tahun. Bunga majemuk {rate}% per tahun. Berapa nilai akumulasi tepat setelah setoran terakhir, tanpa pembulatan?',value,
                       f'Setoran terakhir belum berbunga. Jumlah akhirnya {payment}×[1+(1+{i})+...+(1+{i})^{periods-1}]={value}.','anuitas_investasi')
    if mode=='loan_compound':
        value=principal*(1+i)**years
        return numeric(f'Pinjaman awal {rp(principal)} dikenai bunga majemuk {rate}% per tahun dan belum dibayar selama {years} tahun. Berapa sisa utangnya tepat setelah {years} tahun, tanpa biaya lain dan tanpa pembulatan?',value,
                       f'Utang berkembang dengan faktor (1+i) tiap tahun. Nilai akhirnya={principal}(1+{i})^{years}={value}.','pinjaman_majemuk')
    if mode=='loan_annuity':
        payment=r.randint(5,12)*1000000;interest=principal*i
        if payment<=interest:payment=int(interest)+1000000
        value=payment-interest
        return numeric(f'Pinjaman {rp(principal)} berbunga {rate}% pada periode pertama. Anuitas akhir periode sebesar {rp(payment)} terdiri atas bunga dan angsuran pokok. Berapa angsuran pokok periode pertama?',value,
                       f'Bunga={principal}×{i}={interest}. Angsuran pokok=anuitas-bunga={payment}-{interest}={value} rupiah.','pinjaman_anuitas')
    value=s.Rational(rate*years,100)
    return numeric(f'Modal {rp(principal)} menghasilkan bunga tunggal selama {years} tahun sebesar {rp(principal*value)}. Berapa suku bunga tahunannya dalam persen?',rate,
                   f'r=I/(P×t)×100%={principal*value}/({principal}×{years})×100%={rate}%.','parameter_keuangan')


def generate(book,bab,code,level,r):
    grade=int(book[5:]);a=r.randint(2,9);b=r.randint(2,10);k=r.randint(2,7)
    if grade==12:
        if bab==1:
            if code=='A':return sequences(r,level)
            if code=='B':return sequences(r,level,'sum')
            return finance(r,level,'simple')
        if bab==2:
            return finance(r,level,{'A':'simple','B':'compound','C':'annuity_investment',
                                    'D':'loan_compound','E':'loan_annuity','F':'parameter'}[code])
        if bab==3:
            if code=='A':
                digits=r.randint(5,8);length=r.randint(3,min(5,digits));available=sorted(r.sample(range(1,10),digits))
                value=math.factorial(digits)//math.factorial(digits-length)
                return numeric(f'Dari digit {", ".join(map(str,available))} dibuat bilangan {length} angka tanpa pengulangan digit. Berapa banyak bilangan yang dapat dibuat?',value,
                               f'Aturan pengisian tempat memberi {digits}×{digits-1}×... sebanyak {length} faktor, yaitu {value}.','aturan_pengisian_tempat')
            if code=='B':
                n=r.randint(5,10);value=math.factorial(n-1)*2
                return numeric(f'Sebanyak {n} orang berbeda berbaris. Dua orang tertentu harus berdampingan. Berapa susunan barisan yang mungkin?',value,
                               f'Gabungkan dua orang menjadi satu blok. Ada ({n}-1)! susunan blok dan 2 urutan internal. Total={value}.','permutasi_bersyarat')
            if code=='C':
                men=r.randint(5,12);women=r.randint(3,8);size=r.randint(3,min(5,men));value=s.binomial(men+women,size)-s.binomial(men,size)
                return numeric(f'Dari {men} siswa putra dan {women} siswa putri dipilih tim {size} orang. Berapa tim yang memuat sedikitnya satu putri?',value,
                               f'Jumlah semua tim C({men+women},{size}) dikurangi tim seluruhnya putra C({men},{size}), diperoleh {value}.','kombinasi_bersyarat')
            n=r.randint(4,9);success=r.randint(1,n-1);p=s.Rational(r.randint(2,7),10)
            value=s.binomial(n,success)*p**success*(1-p)**(n-success)
            return numeric(f'Sebuah tim menjalani {n} pertandingan independen dengan peluang menang tetap {m(p)} per pertandingan. Berapa peluang tim menang tepat {success} pertandingan?',value,
                           f'P=C({n},{success})({p})^{success}(1-{p})^{n-success}={value}.','kombinasi_dalam_peluang')
        if bab==4:
            return probability(r,level,'two' if (code=='B' or level=='hard') else 'single')
    if grade==10 and bab==1:
        if code in 'AB':
            base=r.randint(2,7);p=r.randint(2,5);q=r.randint(2,5);sub=r.randint(1,4)
            return numeric(f'Diketahui $({base}^{p})^{q}/{base}^{sub}={base}^n$. Tentukan $n$.',p*q-sub,
                           f'Gunakan (a^p)^q=a^(pq), lalu bagi dengan a^{sub}: n={p*q}-{sub}={p*q-sub}.','sifat_eksponen')
        if code=='C':
            initial=r.randint(2,15)*100;ratio=r.choice([2,3]);period=r.randint(2,6)
            return numeric(f'Populasi awal {initial}. Setiap periode populasi menjadi {ratio} kali sebelumnya. Jika pola tetap, berapa populasi setelah {period} periode?',initial*ratio**period,
                           f'Fungsi pertumbuhan P(t)={initial}×{ratio}^t. Pada t={period}, P={initial*ratio**period}.','fungsi_eksponensial')
        d=r.choice([2,3,5,6,7]);u=r.randint(2,10);v=r.randint(2,10)
        return numeric(f'Sederhanakan $\\sqrt{{{u*u*d}}}-\\sqrt{{{v*v*d}}}$.',(u-v)*s.sqrt(d),
                       f'Keluarkan faktor kuadrat: {u}√{d}-{v}√{d}=({u-v})√{d}.','bentuk_akar')
    if grade==10 and bab==2:
        if code=='A':return sequences(r,level)
        if code=='B':return sequences(r,level,'sum')
        return finance(r,level,'simple')
    if grade==10 and bab==3:
        if code=='A':
            u,v,h=r.choice([(3,4,5),(5,12,13),(8,15,17),(7,24,25)]);scale=r.randint(1,6)
            return numeric(f'Pada segitiga siku-siku, sisi di depan sudut $\\theta$ panjangnya {u*scale} cm, sisi sampingnya {v*scale} cm, dan sisi miringnya {h*scale} cm. Tentukan $\\sin\\theta+\\cos\\theta$.',s.Rational(u+v,h),
                           f'sin θ={u}/{h} dan cos θ={v}/{h}; jumlahnya {s.Rational(u+v,h)}.','perbandingan_trigonometri')
        height=r.randint(5,30);eye=r.randint(1,3);angle=r.choice([30,45,60]);tan={30:s.sqrt(3)/3,45:s.Integer(1),60:s.sqrt(3)}[angle]
        distance=height/tan
        return numeric(f'Sudut elevasi puncak menara dari mata pengamat adalah {angle}°. Tinggi puncak di atas mata pengamat {height} m. Berapa jarak mendatar pengamat ke kaki menara?',distance,
                       f'tan {angle}° = tinggi/jarak = {height}/d, sehingga d={height}/({tan})={distance} m.','aplikasi_trigonometri')
    if grade==10 and bab==4:
        if code=='A':
            u=r.randint(2,12);v=r.randint(2,12);w=r.randint(2,12)
            return numeric(f'Selesaikan sistem $x+y={u+v}$, $y+z={v+w}$, dan $x+z={u+w}$. Berapa nilai $x+y+z$?',u+v+w,
                           f'Jumlahkan ketiga persamaan: 2(x+y+z)={2*(u+v+w)}. Jadi x+y+z={u+v+w}.','sistem_linear_tiga_variabel')
        limit=r.randint(6,15);cx=r.randint(2,8);cy=r.randint(2,8);unit=10000
        # Enumerate integer feasible points instead of assuming a vertex is feasible.
        feasible=[(u,v) for u in range(limit+1) for v in range(limit+1) if u+v<=limit and 2*u+v<=limit+a]
        value=max((cx*u+cy*v)*unit for u,v in feasible)
        return numeric(f'Produksi kursi $x$ dan meja $y$ harus memenuhi $x+y\\le {limit}$, $2x+y\\le {limit+a}$, dan $x,y$ bilangan cacah. Keuntungan per kursi {rp(cx*unit)} dan per meja {rp(cy*unit)}. Berapa keuntungan maksimum?',value,
                       f'Evaluasi titik bilangan cacah yang memenuhi kedua batas. Nilai maksimum {cx*unit}x+{cy*unit}y adalah {value} rupiah.','optimasi_pertidaksamaan_linear')
    if grade==10 and bab==5:
        u=r.randint(-8,8);v=r.randint(-8,8)
        if code=='A':
            x=s.Symbol('x');expr=s.expand((x-u)*(x-v));value=u+v
            return numeric(f'Akar persamaan {m(expr)} $=0$ adalah $p$ dan $q$. Tentukan $p+q$.',value,
                           f'Persamaan dapat difaktorkan menjadi (x-({u}))(x-({v}))=0. Jumlah akar={u}+({v})={value}.','persamaan_kuadrat')
        h=r.randint(-6,6);c=r.randint(-10,10);coef=r.randint(1,5)
        return numeric(f'Fungsi $f(x)={coef}(x-({h}))^2+({c})$ memiliki nilai minimum ....',c,
                       f'Karena {coef}>0 dan kuadrat selalu nonnegatif, minimum terjadi saat x={h}; nilainya {c}.','fungsi_kuadrat_minimum')
    if grade==10 and bab==6:
        if code=='A':
            width=r.randint(2,6);f1=r.randint(5,20);f2=r.randint(5,20)
            return numeric(f'Dua kelas histogram yang berdampingan sama-sama memiliki lebar {width}. Frekuensinya {f1} dan {f2}. Jika digabung menjadi satu kelas, berapa densitas frekuensi kelas gabungan?',s.Rational(f1+f2,2*width),
                           f'Frekuensi gabungan={f1+f2}, lebar gabungan={2*width}; densitas=(frekuensi/lebar)={s.Rational(f1+f2,2*width)}.','representasi_histogram')
        return statistics(r,level,'range' if code=='C' else 'mean')
    if grade==10 and bab==7:
        if code=='A':
            threshold=r.randint(4,10);count=sum(i+j>=threshold for i in range(1,7) for j in range(1,7))
            return numeric(f'Dua dadu adil bersisi enam dilempar bersama. Berapa peluang jumlah mata dadu paling sedikit {threshold}?',s.Rational(count,36),
                           f'Dari 36 pasangan berurutan, ada {count} yang jumlahnya minimal {threshold}. Peluangnya {s.Rational(count,36)}.','distribusi_peluang_dadu')
        if code=='B':
            total=r.randint(30,70);one=r.randint(10,total//2);two=r.randint(10,total//2);both=r.randint(2,min(one,two)-1)
            return numeric(f'Dari {total} siswa, {one} menyukai matematika, {two} menyukai IPA, dan {both} menyukai keduanya. Jika dipilih satu siswa acak, berapa peluang ia menyukai matematika atau IPA?',s.Rational(one+two-both,total),
                           f'Gunakan aturan penjumlahan: n(M∪I)={one}+{two}-{both}={one+two-both}. Peluangnya {s.Rational(one+two-both,total)}.','aturan_penjumlahan_peluang')
        return probability(r,level,'two')
    if grade==11:
        x=s.Symbol('x',real=True)
        if bab==1:
            if code=='A':
                endpoint=r.randint(3,15);shift=r.randint(2,9);value=endpoint-shift
                return numeric(f'Fungsi $f(x)=\\sqrt{{{endpoint}-x}}$ terdefinisi pada bilangan real. Berapa nilai $x$ terbesar dalam domainnya?',endpoint,
                               f'Syarat akar real: {endpoint}-x≥0, sehingga x≤{endpoint}. Nilai terbesar {endpoint}.','domain_fungsi')
            if code=='B':
                c=r.randint(2,9);d=r.randint(1,9);t=r.randint(-5,8)
                value=a*(c*t+d)+b
                return numeric(f'Diketahui $f(x)={a}x+{b}$ dan $g(x)={c}x+{d}$. Tentukan $(f\\circ g)({t})$.',value,
                               f'g({t})={c*t+d}, kemudian f(g({t}))={a}×({c*t+d})+{b}={value}.','komposisi_fungsi')
            t=r.randint(2,15);v=a*t+b
            return numeric(f'Fungsi $f(x)={a}x+{b}$ memiliki invers. Tentukan $f^{{-1}}({v})$.',t,
                           f'Balikkan y={a}x+{b} menjadi x=(y-{b})/{a}. Maka f⁻¹({v})={t}.','fungsi_invers')
        if bab==2:
            radius=r.randint(5,20)
            if code=='A':
                angle=r.choice([30,45,60,90,120,150]);value=s.Rational(angle,360)*2*s.pi*radius
                return numeric(f'Lingkaran berjari-jari {radius} cm memiliki busur bersudut pusat {angle}°. Berapa panjang busurnya dalam bentuk $\\pi$?',value,
                               f'Panjang busur=(θ/360°)×2πr=({angle}/360)×2π×{radius}={value} cm.','panjang_busur')
            if code=='B':
                u,v,h=r.choice([(3,4,5),(5,12,13),(8,15,17)]);scale=r.randint(1,5);rad=u*scale;distance=h*scale;value=v*scale
                return numeric(f'Titik P berjarak {distance} cm dari pusat lingkaran berjari-jari {rad} cm. Garis PT menyinggung lingkaran di T. Berapa panjang PT?',value,
                               f'OT tegak lurus PT. PT=√(OP²-r²)=√({distance}²-{rad}²)={value} cm.','garis_singgung_lingkaran')
            u=r.randint(2,10);v=r.randint(2,10);w=r.randint(2,10);value=s.Rational(u*v,w)
            return numeric(f'Tali busur AB dan CD berpotongan di X. Diketahui AX={u} cm, XB={v} cm, dan CX={w} cm. Tentukan XD.',value,
                           f'Teorema tali busur: AX×XB=CX×XD. XD={u}×{v}/{w}={value} cm.','perpotongan_tali_busur')
        if bab==3:
            slope=r.choice([-4,-3,-2,2,3,4]);intercept=r.randint(5,30);xs=[r.randint(1,10)+j*10 for j in range(4)];ys=[slope*v+intercept for v in xs]
            if code=='A':
                direction='positif' if slope>0 else 'negatif';other='negatif' if slope>0 else 'positif'
                return text(f'Pasangan data $(x,y)$ adalah {", ".join(pair(u,v) for u,v in zip(xs,ys))}. Arah pola pada diagram pencarnya adalah ....',f'Korelasi linear {direction}.',
                            [f'Korelasi linear {other}.','Tidak memiliki pola hubungan.','Pola berbentuk lingkaran.'],
                            f'Setiap kenaikan x diikuti perubahan y dengan gradien {slope}, sehingga arah hubungannya {direction}.','diagram_pencar')
            if code=='B':
                t=r.randint(5,25);value=slope*t+intercept
                return numeric(f'Garis regresi suatu data adalah $\\hat y={slope}x+({intercept})$. Berapa prediksi $y$ ketika $x={t}$?',value,
                               f'Substitusi x={t}: ŷ={slope}×{t}+({intercept})={value}.','prediksi_regresi')
            coefficient=s.Rational(r.randint(10,95),100);value=100*coefficient**2
            return numeric(f'Koefisien korelasi dua variabel adalah {m(coefficient)}. Berapa koefisien determinasinya dalam persen?',value,
                           f'Koefisien determinasi=r²×100%={coefficient}²×100%={value}%.','koefisien_determinasi')
    raise ValueError(f'Unsupported regular SMA topic {book}/{bab}/{code}')
