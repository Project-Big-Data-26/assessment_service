"""Tingkat Lanjut reference variants with symbolic calculus and exact probability."""
import math
import sympy as s
from .replenishment_math import numeric,text,m,pair,x


def generate(book,bab,code,level,r):
    grade=int(book.split('_')[0][5:]);a=r.randint(2,9);b=r.randint(2,9);c=r.randint(2,9);k=r.randint(2,7)
    if grade==11:
        if bab==1:
            if code=='A':
                n=r.randint(2,5);choices=r.randint(2,7);value=choices**n
                return numeric(f'Setiap elemen matriks diagonal berordo {n}×{n} dipilih dari {choices} nilai berbeda yang memuat nol. Elemen di luar diagonal wajib nol. Berapa banyak matriks diagonal yang mungkin?',value,
                               f'Ada {n} elemen diagonal yang bebas, masing-masing {choices} pilihan. Jadi ada {choices}^{n}={value} matriks.','jenis_matriks_diagonal')
            if code=='B':
                u=r.randint(-5,8);v=r.randint(-5,8);value=u+v
                return numeric(f'Dua matriks $A=\\begin{{pmatrix}}{a}x+{b}&{c}\\\\{k}&y-{b}\\end{{pmatrix}}$ dan $B=\\begin{{pmatrix}}{a*u+b}&{c}\\\\{k}&{v-b}\\end{{pmatrix}}$ sama. Tentukan $x+y$.',value,
                               f'Elemen bersesuaian harus sama: {a}x+{b}={a*u+b}, sehingga x={u}; y-{b}={v-b}, sehingga y={v}. Jumlahnya {value}.','kesamaan_matriks')
            if code=='C':
                u=r.randint(2,15);v=r.randint(2,15);value=u-v
                return numeric(f'Matriks $A=\\begin{{pmatrix}}{a}&{u}\\\\{v}&{b}\\end{{pmatrix}}$ dan $B=\\begin{{pmatrix}}{c}&{k}\\\\{a}&{c}\\end{{pmatrix}}$. Berapa selisih elemen baris 1 kolom 2 dan baris 2 kolom 1 dari $A+B$?',u+k-v-a,
                               f'Elemen (1,2)={u}+{k}={u+k}; elemen (2,1)={v}+{a}={v+a}. Selisihnya {u+k-v-a}.','penjumlahan_matriks')
            if code=='D':
                A=s.Matrix([[a,b],[c,k]]);B=s.Matrix([[k,c],[b,a]]);P=A*B
                return numeric(f'Diketahui $A={s.latex(A)}$ dan $B={s.latex(B)}$. Tentukan elemen baris 1 kolom 2 dari $AB$.',P[0,1],
                               f'Kalikan baris pertama A dengan kolom kedua B: {a}×{c}+{b}×{a}={P[0,1]}.','perkalian_matriks')
            A=s.Matrix([[a,b],[c,k]]);det=A.det()
            if det==0:return generate(book,bab,code,level,r)
            if level=='easy':return numeric(f'Tentukan determinan matriks $A={s.latex(A)}$.',det,f'det(A)={a}×{k}-{b}×{c}={det}.','determinan_matriks')
            return numeric(f'Matriks $A={s.latex(A)}$ memiliki invers. Tentukan elemen baris 1 kolom 1 dari $A^{{-1}}$.',s.Rational(k,det),
                           f'det(A)={det}. Invers 2×2 mempunyai elemen (1,1)=d/det(A)={k}/{det}.','invers_matriks')
        if bab==2:
            degree=r.randint(3,6);u=r.randint(-5,6);v=r.randint(-5,6)
            if code=='A':
                expr=a*x**degree+b*x**(degree-1)+c
                return numeric(f'Polinomial $P(x)={s.latex(expr)}$. Tentukan $P({u})$.',expr.subs(x,u),
                               f'Substitusi x={u}: P({u})={s.latex(expr.subs(x,u))}.','evaluasi_polinomial')
            if code=='B':
                P=a*x*x+b*x+c;Q=b*x*x-c*x+k;product=s.expand(P*Q);power=r.choice([1,2,3])
                return numeric(f'Jika $P(x)={s.latex(P)}$ dan $Q(x)={s.latex(Q)}$, berapa koefisien $x^{power}$ dalam $P(x)Q(x)$?',product.coeff(x,power),
                               f'Kalikan dan kelompokkan pangkat sama: P(x)Q(x)={m(product)}. Koefisien yang diminta {product.coeff(x,power)}.','operasi_polinomial')
            if code=='C':
                expr=a*x**3-b*x**2+c*x-k
                return numeric(f'Tentukan sisa pembagian $P(x)={s.latex(expr)}$ oleh $(x-({u}))$.',expr.subs(x,u),
                               f'Teorema sisa: sisanya P({u})={expr.subs(x,u)}.','sisa_pembagian_polinomial')
            if code=='D':
                if len({u,v,k})!=3:return generate(book,bab,code,level,r)
                expr=s.expand((x-u)*(x-v)*(x-k));coefficient=expr.coeff(x,1)
                return numeric(f'Polinomial $P(x)={s.latex(expr)}$ mempunyai faktor $(x-({u}))$. Berapa hasil kali dua akar lainnya?',v*k,
                               f'Faktorisasi lengkap (x-({u}))(x-({v}))(x-{k}). Dua akar lainnya {v} dan {k}, hasil kali {v*k}.','faktor_polinomial')
            power=r.randint(3,6);p=s.expand((x+a)**power);coefficient=p.coeff(x,power-2)
            return numeric(f'Dalam identitas $(x+{a})^{power}$, tentukan koefisien $x^{power-2}$.',coefficient,
                           f'Teorema binomial memberi C({power},2)×{a}²={coefficient}.','identitas_polinomial')
        if bab==3:
            if code=='A':
                angle=r.choice([30,45,60,120,135,150,210,225,240,300,315,330]);turns=r.randint(1,4);theta=s.pi*s.Rational(angle+360*turns,180);value=s.sin(theta)
                return numeric(f'Tentukan $\\sin({angle+360*turns}^\\circ)$.',value,
                               f'Kurangi {turns} putaran penuh: sin({angle+360*turns}°)=sin({angle}°)={m(value)}.','lingkaran_satuan')
            if code=='B':
                amplitude=r.randint(2,10);frequency=r.randint(2,8);shift=r.randint(-5,5)
                if level=='hard':
                    return numeric(f'Gerak benda mengikuti $y={amplitude}\\sin({frequency}t)+({shift})$, dengan sudut dalam radian. Berapa selisih nilai maksimum dan minimumnya?',2*amplitude,
                                   f'Nilai maksimum {shift+amplitude}, minimum {shift-amplitude}. Selisihnya 2×amplitudo={2*amplitude}.','grafik_trigonometri_rentang')
                return numeric(f'Fungsi $y={amplitude}\\cos({frequency}x)+({shift})$ menggunakan radian. Berapa periodenya?',2*s.pi/frequency,
                               f'Periode cos(bx) adalah 2π/|b|={m(2*s.pi/frequency)}.','periode_trigonometri')
            if code=='C':
                angle=r.choice([30,45,60]);value=(s.sin(s.pi*angle/180)**2+s.cos(s.pi*angle/180)**2)*a+b
                return numeric(f'Sederhanakan ${a}(\\sin^2 {angle}^\\circ+\\cos^2 {angle}^\\circ)+{b}$.',value,
                               f'Identitas sin²θ+cos²θ=1 memberi {a}×1+{b}={a+b}.','identitas_trigonometri')
            if code=='D':
                A=r.choice([30,45,60]);B=r.choice([30,45,60]);side=r.randint(3,15)
                value=side*s.sin(s.pi*A/180)/s.sin(s.pi*B/180)
                return numeric(f'Pada segitiga ABC, $A={A}^\\circ$, $B={B}^\\circ$, dan sisi di depan B adalah {side} cm. Berapa sisi di depan A?',value,
                               f'Aturan sinus: a/sin A=b/sin B. Jadi a={side} sin {A}°/sin {B}°={m(s.simplify(value))} cm.','aturan_sinus')
            angle=r.choice([60,90,120]);side1=r.randint(3,15);side2=r.randint(3,15);square=side1**2+side2**2-2*side1*side2*s.cos(s.pi*angle/180)
            return numeric(f'Dua sisi segitiga panjangnya {side1} cm dan {side2} cm, dengan sudut apit {angle}°. Berapa panjang sisi di depan sudut tersebut?',s.sqrt(square),
                           f'Aturan kosinus: c²={side1}²+{side2}²-2×{side1}×{side2} cos {angle}°={m(square)}; c={m(s.sqrt(square))}.','aturan_kosinus')
        if bab==4:
            ux=r.randint(-8,8);uy=r.randint(-8,8);vx=r.randint(-8,8);vy=r.randint(-8,8)
            if code=='A':
                return numeric(f'Diketahui vektor u={pair(ux,uy)} dan v={pair(vx,vy)}. Tentukan kuadrat panjang $u+v$.',(ux+vx)**2+(uy+vy)**2,
                               f'u+v=({ux+vx},{uy+vy}); kuadrat panjangnya=({ux+vx})²+({uy+vy})²={(ux+vx)**2+(uy+vy)**2}.','vektor_pada_bidang')
            if code=='B':return numeric(f'Diketahui vektor u={pair(ux,uy)} dan v={pair(vx,vy)}. Tentukan $u\\cdot v$.',ux*vx+uy*vy,
                                       f'Hasil kali titik = {ux}×({vx})+({uy})×({vy})={ux*vx+uy*vy}.','hasil_kali_titik')
            ax=r.randint(-8,8);ay=r.randint(-8,8);bx=r.randint(-8,8);by=r.randint(-8,8)
            mx=s.Rational(ax+bx,2);my=s.Rational(ay+by,2)
            return text(f'Titik A{pair(ax,ay)} dan B{pair(bx,by)}. Dengan rumus vektor posisi titik tengah, koordinat titik tengah AB adalah ....',pair(mx,my),
                        [pair(mx+1,my),pair(mx,my+1),pair(mx-1,my-1)],
                        f'Vektor posisi titik tengah=(OA+OB)/2=({mx},{my}).','pembuktian_vektor_titik_tengah')
        if bab==5:
            px=r.randint(-12,12);py=r.randint(-12,12)
            if code=='A':tx,ty=px+a,py+b;desc=f'translasi dengan vektor {pair(a,b)}'
            elif code=='B':tx,ty=-py,px;desc='transformasi bermatriks $\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$'
            else:tx,ty=-(py+b),px+a;desc=f'translasi {pair(a,b)} dilanjutkan rotasi 90° berlawanan arah jarum jam terhadap O'
            return text(f'Titik P{pair(px,py)} dikenai {desc}. Koordinat bayangannya adalah ....',pair(tx,ty),
                        [pair(tx+1,ty),pair(tx,ty+1),pair(tx-1,ty-1)],
                        f'Terapkan transformasi sesuai urutannya pada ({px},{py}); hasil akhirnya ({tx},{ty}).','transformasi_matriks')
        if bab==6:
            if code=='A':
                base=r.randint(2,6);power=r.randint(2,6)
                return numeric(f'Jika $\\log_{{{base}}} x={power}$, tentukan nilai $x/{base}$.',base**(power-1),
                               f'Definisi logaritma memberi x={base}^{power}. Maka x/{base}={base}^{power-1}={base**(power-1)}.','fungsi_logaritma')
            if code=='B':
                u=r.randint(2,12);shift=r.randint(2,10);value=a*u+b
                return numeric(f'Fungsi $f(x)=\\frac{{({a}x+{b})(x-{shift})}}{{x-{shift}}}$ didefinisikan untuk $x\\ne {shift}$. Tentukan $f({u+shift})$.',a*(u+shift)+b,
                               f'Untuk x≠{shift}, faktor (x-{shift}) dapat dicoret. Jadi f(x)={a}x+{b}; f({u+shift})={a*(u+shift)+b}.','fungsi_aljabar_rasional')
            initial=r.randint(2,20)*100;growth=r.choice([2,3]);periods=r.randint(2,7)
            if level=='easy':
                return numeric(f'Suatu populasi mula-mula {initial} dan menjadi {growth} kali setiap jam. Menurut model eksponensial ini, berapa populasi setelah {periods} jam?',initial*growth**periods,
                               f'N(t)={initial}×{growth}^t; N({periods})={initial*growth**periods}.','pemodelan_eksponensial')
            if level=='medium':
                return numeric(f'Model pertumbuhan $N(t)={initial}\\cdot {growth}^t$ menggunakan t dalam jam. Setelah berapa jam populasinya menjadi {initial*growth**periods}?',periods,
                               f'Bagi dengan {initial}: {growth}^t={growth}^{periods}, sehingga t={periods}.','fungsi_non_aljabar_balik')
            rate=r.randint(2,6);duration=periods*rate
            return numeric(f'Populasi {initial} organisme berlipat {growth} setiap {rate} jam. Tidak ada kematian dan model berlaku terus. Berapa pertambahan populasi selama {duration} jam?',initial*(growth**periods-1),
                           f'Terjadi {duration}/{rate}={periods} periode. Populasi akhir {initial*growth**periods}; pertambahannya {initial*(growth**periods-1)}.','pemodelan_non_aljabar_bertahap')
    if grade==12:
        if bab==1:
            h=r.randint(-8,8);v=r.randint(-8,8);radius=r.randint(3,12)
            if code=='A':
                if level=='hard':
                    expr=s.expand((x-h)**2+(s.Symbol('y')-v)**2-radius**2)
                    return numeric(f'Lingkaran mempunyai persamaan ${s.latex(expr)}=0$. Tentukan kuadrat jari-jarinya.',radius**2,
                                   f'Lengkapi kuadrat sehingga (x-({h}))²+(y-({v}))²={radius**2}. Jadi r²={radius**2}.','persamaan_lingkaran')
                return numeric(f'Lingkaran berpusat di {pair(h,v)} melalui {pair(h+radius,v)}. Berapa jari-jarinya?',radius,
                               f'Jarak pusat ke titik tersebut = √(({h+radius}-{h})²+({v}-{v})²)={radius}.','unsur_lingkaran')
            if code=='B':
                major=r.randint(5,15);minor=r.randint(2,major-1);focus2=major**2-minor**2
                return numeric(f'Elips $\\frac{{(x-({h}))^2}}{{{major**2}}}+\\frac{{(y-({v}))^2}}{{{minor**2}}}=1$ memiliki fokus sejajar sumbu x. Berapa jarak antara kedua fokus?',2*s.sqrt(focus2),
                               f'c²=a²-b²={major**2}-{minor**2}={focus2}. Jarak fokus=2c={m(2*s.sqrt(focus2))}.','fokus_elips')
            if code=='C':
                coeff=r.randint(1,5);n=r.randint(2,7);constant=coeff*h+v+radius*s.sqrt(coeff**2+1)
                return numeric(f'Garis ${coeff}x+y=p$ menyinggung lingkaran $(x-({h}))^2+(y-({v}))^2={radius**2}$. Tentukan nilai $p$ yang lebih besar.',constant,
                               f'Jarak pusat ke garis = |{coeff}×({h})+({v})-p|/√{coeff**2+1}={radius}. Jadi p={coeff*h+v}±{radius}√{coeff**2+1}; pilih nilai lebih besar.','kedudukan_garis_lingkaran')
            value=h+radius
            return numeric(f'Lingkaran berpusat di {pair(h,v)} berjari-jari {radius}. Garis singgung di titik paling kanan berbentuk $x=c$. Tentukan $c$.',value,
                           f'Titik paling kanan adalah ({h}+{radius},{v})=({value},{v}); jari-jari mendatar, sehingga garis singgungnya x={value}.','garis_singgung_lingkaran')
        if bab==2:
            t=r.randint(-5,7);p=a*x**3+b*x**2+c*x+k
            if code=='A':
                # Definition is evaluated using an independent symbolic limit.
                h=s.Symbol('h');f=a*x*x+b*x+c;value=s.limit((f.subs(x,t+h)-f.subs(x,t))/h,h,0)
                return numeric(f'Untuk $f(x)={s.latex(f)}$, hitung $\\lim_{{h\\to0}}\\frac{{f({t}+h)-f({t})}}{{h}}$.',value,
                               f'Kembangkan pembilang, bagi dengan h, lalu ambil limit h→0. Hasilnya f′({t})={value}.','definisi_turunan_limit')
            if code=='B':
                derivative=s.diff(p,x);value=derivative.subs(x,t)
                return numeric(f'Diketahui $f(x)={s.latex(p)}$. Tentukan $f^\\prime({t})$.',value,
                               f'Aturan pangkat memberi f′(x)={m(derivative)}. Pada x={t}, nilainya {value}.','sifat_turunan')
            if code=='C':
                center=r.randint(2,12);height=r.randint(-8,8);f=a*(x-center)**2+height
                return numeric(f'Fungsi $f(x)={s.latex(s.expand(f))}$ mempunyai titik minimum. Berapa absis titik minimumnya?',center,
                               f'f′(x)={m(s.diff(f,x))}=0 memberi x={center}. Karena f″(x)={2*a}>0, titik tersebut minimum.','titik_stasioner_minimum')
            total=r.randint(20,80)*2;value=s.Rational(total,4)
            return numeric(f'Tersedia pagar sepanjang {total} meter untuk kebun persegi panjang tertutup. Dengan fungsi luas dan turunan, tentukan panjang salah satu sisi agar luas maksimum.',value,
                           f'Jika sisi x dan {total}/2-x, luas L=x({total}/2-x). L′={total}/2-2x=0 memberi x={value}. L″=-2<0, sehingga maksimum.','optimasi_turunan')
        if bab==3:
            power=r.randint(2,5);lo=r.randint(0,4);hi=lo+r.randint(2,6);integrand=a*x**power+b*x+c
            if code=='A':
                antiderivative=s.integrate(integrand,x);point=r.randint(1,5);value=antiderivative.subs(x,point)
                return numeric(f'Fungsi $F$ memenuhi $F^\\prime(x)={s.latex(integrand)}$ dan $F(0)=0$. Tentukan $F({point})$.',value,
                               f'Integralnya F(x)={m(antiderivative)}+C. Dari F(0)=0 diperoleh C=0. Maka F({point})={value}.','integral_tak_tentu_dengan_syarat')
            if code=='B':
                value=s.integrate(integrand,(x,lo,hi));anti=s.integrate(integrand,x)
                return numeric(f'Hitung $\\int_{{{lo}}}^{{{hi}}}({s.latex(integrand)})\\,dx$.',value,
                               f'Antiturunannya {m(anti)}. Substitusi batas atas dikurangi batas bawah menghasilkan {value}.','integral_tentu')
            width=r.randint(2,8);coef=r.randint(1,5);upper=coef*x*(width-x);value=s.integrate(upper,(x,0,width))
            return numeric(f'Tentukan luas daerah antara kurva $y={s.latex(s.expand(upper))}$ dan sumbu x pada $0\\le x\\le {width}$.',value,
                           f'Kurva nonnegatif pada interval tersebut. Integralkan {m(s.expand(upper))} dari 0 sampai {width}; hasilnya {value}.','luas_daerah_integral')
        if bab==4:
            n=r.randint(4,10);p=s.Rational(r.randint(2,7),10)
            if code=='A':
                value=n*p
                return numeric(f'Dalam {n} percobaan Bernoulli independen, peluang sukses tiap percobaan {m(p)}. Variabel acak X menyatakan jumlah sukses. Berapa $E(X)$?',value,
                               f'X adalah jumlah {n} indikator sukses. E(X)=n×p={n}×{p}={value}.','variabel_acak_harapan')
            if code=='B':
                values=[r.randint(1,5),r.randint(6,10),r.randint(11,15)];weights=[r.randint(1,5) for _ in range(3)];total=sum(weights);value=sum(v*s.Rational(w,total) for v,w in zip(values,weights))
                return numeric(f'X bernilai {values[0]}, {values[1]}, {values[2]} dengan peluang berturut-turut {m(s.Rational(weights[0],total))}, {m(s.Rational(weights[1],total))}, {m(s.Rational(weights[2],total))}. Tentukan $E(X)$.',value,
                               f'E(X)=ΣxP(X=x)={value}; jumlah peluangnya 1.','harapan_variabel_diskret')
            if code=='C':
                lo=r.randint(10,40);width=r.randint(6,20);cut=r.randint(1,width-1);value=s.Rational(cut,width)
                return numeric(f'Waktu tunggu X berdistribusi seragam kontinu pada interval [{lo},{lo+width}] menit. Berapa $P(X<{lo+cut})$?',value,
                               f'Peluang seragam kontinu = panjang subinterval/panjang seluruh interval = {cut}/{width}={value}.','variabel_kontinu_seragam')
            if code=='D':
                top=r.randint(3,8);denom=top*(top+1)//2;threshold=r.randint(2,top);value=s.Rational(sum(range(threshold,top+1)),denom)
                return numeric(f'Fungsi peluang diskret $P(X=j)=j/{denom}$ untuk $j=1,2,\\ldots,{top}$. Tentukan $P(X\\ge {threshold})$.',value,
                               f'Jumlah peluang=({"+".join(map(str,range(threshold,top+1)))})/{denom}={value}. Normalisasi sah karena Σj={denom}.','fungsi_peluang_diskret')
            if code=='E':
                L=r.randint(3,12);cut=r.randint(1,L-1);value=s.Rational(cut**2,L**2)
                return numeric(f'Densitas X adalah $f(x)=2x/{L**2}$ untuk $0\\le x\\le {L}$ dan nol di luar interval. Tentukan $P(X<{cut})$.',value,
                               f'Integral seluruh densitas =1. P(X<{cut})=∫₀^{cut} 2x/{L**2} dx={cut**2}/{L**2}={value}.','fungsi_densitas')
            if code=='F':
                successes=r.randint(1,n-1)
                if level=='easy':
                    return numeric(f'X berdistribusi binomial dengan $n={n}$ dan $p={s.latex(p)}$. Berapa nilai harapan X?',n*p,
                                   f'Untuk distribusi binomial, E(X)=np={n}×{p}={n*p}.','binomial_harapan')
                if level=='hard':
                    value=sum(s.binomial(n,j)*p**j*(1-p)**(n-j) for j in range(successes,n+1))
                    return numeric(f'Dari {n} percobaan independen dengan peluang sukses {m(p)}, berapa peluang terdapat paling sedikit {successes} sukses?',value,
                                   f'Jumlahkan peluang binomial untuk j={successes},...,{n}: ΣC({n},j)({p})^j(1-{p})^({n}-j)={value}.','binomial_kumulatif')
                value=s.binomial(n,successes)*p**successes*(1-p)**(n-successes)
                return numeric(f'X berdistribusi binomial dengan $n={n}$ dan $p={s.latex(p)}$. Tentukan $P(X={successes})$.',value,
                               f'P=C({n},{successes})p^{successes}(1-p)^{n-successes}={value}.','binomial_tepat_k')
            mean=r.randint(40,90);sd=r.randint(3,12);z=r.choice([-2,-1,1,2]);score=mean+z*sd
            phi={-2:s.Rational(228,10000),-1:s.Rational(1587,10000),1:s.Rational(8413,10000),2:s.Rational(9772,10000)}
            if level=='easy':return numeric(f'Nilai tes X berdistribusi normal dengan rata-rata {mean} dan simpangan baku {sd}. Berapa skor baku Z untuk nilai {score}?',z,
                                           f'Z=(X-μ)/σ=({score}-{mean})/{sd}={z}.','normal_skor_baku')
            if level=='medium':return numeric(f'X normal dengan rata-rata {mean} dan simpangan baku {sd}. Gunakan $\\Phi({z})={s.latex(phi[z])}$. Tentukan $P(X<{score})$ menurut nilai tabel tersebut.',phi[z],
                                             f'Standardisasi memberi Z=({score}-{mean})/{sd}={z}. Maka peluangnya Φ({z})={phi[z]}.','normal_peluang_tabel')
            low=mean-sd;high=mean+2*sd;value=1-phi[z]
            return numeric(f'Pada distribusi normal, nilai {low} mempunyai skor baku -1 dan nilai {high} mempunyai skor baku 2. Gunakan $\\Phi({z})={s.latex(phi[z])}$. Berapa $P(X>{score})$?',value,
                           f'Dari selisih skor, 3σ={high-low}, sehingga σ={sd}. Lalu μ={low}+{sd}={mean}. Nilai {score} mempunyai Z={z}; peluang di kanannya 1-Φ({z})={value}.','normal_parameter_dan_peluang')
    raise ValueError(f'Unsupported TL topic {book}/{bab}/{code}')
