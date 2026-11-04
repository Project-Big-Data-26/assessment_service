"""Grade-11 advanced variations requiring genuine reconstruction and constraints."""
import sympy as s
from .targeted_math import checked,constant,system,finite,m,pair


def generate(bab,code,level,r):
    a,b,c,x=s.symbols('a b c x',real=True)
    A=r.randint(2,7);B=r.randint(2,8);C=r.randint(1,7);T=r.randint(3,7)
    U=r.randint(3,8);V=r.randint(1,U-1)
    if bab==1:
        if code=='A':
            p=U*U;q=V*V;k=U*V
            return checked(rf'Matriks simetris $M=\begin{{pmatrix}}x&{k}\\{k}&y\end{{pmatrix}}$ mempunyai determinan nol dan jumlah elemen diagonal {p+q}. Jika $x>y>0$, tentukan $x-y$.',p-q,
                rf'Determinan nol memberi xy={k*k}; jumlah diagonal memberi x+y={p+q}. Akar t²-{p+q}t+{k*k}=0 adalah {p} dan {q}. Syarat x>y memilih x={p}, y={q}, sehingga selisihnya {p-q}.',
                'v2_matriks_singular_rekonstruksi','hard',system(['a','b'],[a*b-k*k,a+b-p-q],a-b,[a-b,b]))
        if code=='B':
            if level=='easy':
                return constant(rf'Matriks $\begin{{pmatrix}}x+{A}&{B}\\0&1\end{{pmatrix}}=\begin{{pmatrix}}{U+A}&{B}\\0&1\end{{pmatrix}}$. Tentukan x.',U,
                    f'Elemen baris pertama kolom pertama sama: x+{A}={U+A}, jadi x={U}.','v2_kesamaan_matriks_langsung','easy')
            P=U*V;S=U+V
            return checked(rf'Dua matriks $\begin{{pmatrix}}x^2+y^2&x+y\\xy&1\end{{pmatrix}}$ dan $\begin{{pmatrix}}{U*U+V*V}&{S}\\{P}&1\end{{pmatrix}}$ sama. Jika $x>y$, tentukan $x^3-y^3$.',U**3-V**3,
                f'Kesamaan elemen memberi x+y={S}, xy={P}. Bilangan x,y berakar pada t²-{S}t+{P}=0, yaitu {U},{V}. Syarat x>y menentukan urutan. Selisih kubiknya {U**3-V**3}.',
                'v2_kesamaan_matriks_akar','hard',system(['a','b'],[a+b-S,a*b-P],a**3-b**3,[a-b]))
        if level=='easy':
            return constant(rf'Matriks $P=\begin{{pmatrix}}{A}&{U}\\{V}&1\end{{pmatrix}}$ dan $Q=\begin{{pmatrix}}1&{B}\\0&{C}\end{{pmatrix}}$. Berapa elemen baris pertama kolom kedua dari $P+Q$?',U+B,
                f'Jumlahkan elemen yang bersesuaian: {U}+{B}={U+B}.','v2_jumlah_matriks_elemen','easy')
        P=s.Matrix([[A,a],[2*a+b,B]]);Q=s.Matrix([[C,b-U-V],[-2*U-V,T]])
        query=(P-Q).det();value=query.subs({a:U,b:V})
        return checked(rf'Matriks $P={s.latex(P)}$ dan $Q={s.latex(Q)}$ memenuhi syarat bahwa $P+Q$ diagonal. Tentukan $\det(P-Q)$.',value,
            f'Kedua elemen di luar diagonal P+Q harus nol: a+b={U+V} dan 2a+b={2*U+V}. Maka a={U}, b={V}. Bentuk P-Q, lalu gunakan determinan 2×2; hasil {value}.',
            'v2_penjumlahan_diagonal_determinan','hard',system(['a','b'],[a+b-U-V,2*a+b-2*U-V],query))
    if bab==2:
        if code=='A':
            if level=='medium':
                target=A*T*T+B*T+C
                return constant(rf'Polinomial $P(x)={A}x^2+bx+{C}$ memenuhi $P(1)={A+B+C}$. Tentukan $P({T})$.',target,
                    f'Dari P(1) diperoleh b={B}. Substitusi ke polinomial pada x={T}, hasil {target}.','v2_polinomial_parameter_rutin','medium')
            f=a*x*x+b*x+c;vals=[A*j*j-2*A*U*j+C for j in [0,1,3]];query=c-b*b/(4*a)
            return checked(rf'Polinomial kuadrat $P(x)=ax^2+bx+c$ memenuhi $P(0)={vals[0]}$, $P(1)={vals[1]}$, dan $P(3)={vals[2]}$. Tentukan nilai minimum P pada bilangan real.',C-A*U*U,
                f'Tiga nilai menentukan c={C}, a={A}, b={-2*A*U}. Lengkapi kuadrat: P(x)={A}(x-{U})²+({C-A*U*U}). Karena a>0, nilai minimum {C-A*U*U}.',
                'v2_polinomial_rekonstruksi_minimum','hard',system(['a','b','c'],[f.subs(x,j)-v for j,v in zip([0,1,3],vals)],query,[a]))
        if code=='B':
            P=x*x+a*x+b;Q=x+b;product=s.expand(P*Q);coef=U+V;linear=V*(U+1);query=s.expand(P*P-Q*Q).coeff(x,2)
            return checked(rf'Diketahui $P(x)=x^2+ax+b$ dan $Q(x)=x+b$ dengan a>b>0. Koefisien $x^2$ pada PQ adalah {coef}, sedangkan koefisien x pada PQ adalah {linear}. Tentukan koefisien $x^2$ pada $P^2-Q^2$.',query.subs({a:U,b:V}),
                f'Pada PQ kedua koefisien memberi a+b={coef} dan b(a+1)={linear}. Eliminasi membentuk persamaan kuadrat; syarat a>b>0 memilih a={U}, b={V}. Koefisien x² dari P²-Q² adalah a²+2b-1={U*U+2*V-1}.',
                'v2_operasi_polinomial_koefisien_balik','hard',system(['a','b'],[product.coeff(x,2)-coef,product.coeff(x,1)-linear],query,[a-b,b]))
        if code=='C':
            value=U*U+A*U+B
            return constant(rf'Tentukan sisa pembagian $P(x)=x^2+{A}x+{B}$ oleh $x-{U}$.',value,
                f'Teorema sisa memberi P({U})={U*U}+{A*U}+{B}={value}.','v2_sisa_polinomial_langsung','easy')
        if code=='D':
            return constant(rf'Polinomial $P(x)=(x-{U})(x+{V})$. Berapa akar positif P?',U,
                f'Faktor nol memberi x={U} atau x=-{V}. Akar positif adalah {U}.','v2_akar_polinomial_langsung','easy')
        n=r.randint(4,7)
        if level=='easy':
            return constant(rf'Dalam $(x+{A})^{n}$, berapa koefisien $x^{n-1}$?',n*A,
                f'Pilih satu faktor konstanta dari {n} faktor: koefisien {n}×{A}={n*A}.','v2_identitas_koefisien_awal','easy')
        coef1=n*(U+V);coef2=s.binomial(n,2)*(U*U+V*V)
        return checked(rf'Pada identitas $(x+a)^{n}+(x+b)^{n}$, koefisien $x^{n-1}$ adalah {coef1} dan koefisien $x^{n-2}$ adalah {coef2}. Jika $a>b>0$, tentukan $a^3-b^3$.',U**3-V**3,
            f'Koefisien pertama memberi a+b={U+V}. Koefisien berikutnya memberi a²+b²={U*U+V*V}; maka ab={U*V}. Selesaikan pasangan akar dan gunakan a>b: a={U}, b={V}. Selisih kubik {U**3-V**3}.',
            'v2_identitas_binomial_parameter','hard',system(['a','b'],[a+b-U-V,a*a+b*b-U*U-V*V],a**3-b**3,[a-b,b]))
    if bab==3:
        u=r.randint(2,7);v=r.randint(1,u-1);den=u*u+v*v;sin=s.Rational(2*u*v,den);cos=s.Rational(u*u-v*v,den)
        if code=='A':
            if level=='medium':
                return constant(rf'Sisi akhir sudut θ di kuadran I melalui titik {pair(u*u-v*v,2*u*v)}. Tentukan $\sin\theta$.',sin,
                    f'Jarak ke pusat adalah {den}. Sinus sama dengan ordinat dibagi jarak: {sin}.','v2_lingkaran_satuan_koordinat','medium')
            S=sin-cos;K=r.randint(2,7)
            return checked(rf'θ berada di kuadran II dan $\sin\theta+\cos\theta={s.latex(S)}$. Tentukan $\sin\theta-{K}\cos\theta$.',sin+K*cos,
                f'Tulis u=sin θ, v=cos θ. Syarat u+v={S}, u²+v²=1, u>0, v<0 memberi u={sin}, v={-cos}. Substitusi menghasilkan {sin+K*cos}.',
                'v2_unit_circle_cabang_kuadran','hard',system(['a','b'],[a+b-S,a*a+b*b-1],a-K*b,[a,-b]))
        if code=='B':
            freq=r.randint(2,7);shift=r.randint(-5,5);amp=r.randint(2,8);period=2*s.pi/freq
            if level=='medium':
                return constant(rf'Fungsi $f(x)={amp}\sin(bx)+({shift})$ dengan b>0 mempunyai periode {s.latex(period)}. Tentukan $f({s.latex(s.pi/(2*freq))})$.',amp+shift,
                    f'Periode 2π/b memberi b={freq}. Sudut pada nilai x yang diminta π/2, sehingga f={amp}+({shift})={amp+shift}.','v2_periode_evaluasi','medium')
            value=(s.Rational(amp,2)+shift)*(amp*s.sqrt(3)/2+shift)
            return checked(rf'Fungsi $f(x)=a\sin(bx)+c$ dengan a,b>0 mempunyai nilai maksimum {amp+shift}, minimum {shift-amp}, dan maksimum pertama pada $x={s.latex(s.pi/(2*freq))}$. Tentukan $f({s.latex(s.pi/(6*freq))})f({s.latex(s.pi/(3*freq))})$.',value,
                f'Ekstrem memberi a={amp}, c={shift}; maksimum pertama memberi b={freq}. Kedua argumen sinus menjadi π/6 dan π/3. Kalikan ({amp}/2+{shift}) dan ({amp}√3/2+{shift}), hasil {s.latex(value)}.',
                'v2_grafik_trigonometri_rekonstruksi','hard',system(['a','b','c'],[a+c-amp-shift,c-a-shift+amp,b-freq],(a/2+c)*(a*s.sqrt(3)/2+c),[a,b]))
        if code=='C':
            if level=='medium':
                val=2*sin*cos
                return constant(rf'Untuk sudut lancip θ diketahui $\tan\theta={s.latex(sin/cos)}$. Tentukan $\sin 2\theta$.',val,
                    f'Gunakan sin 2θ=2tan θ/(1+tan²θ); substitusi menghasilkan {val}.','v2_identitas_sudut_ganda','medium')
            S=sin+cos;K=r.randint(2,7);sign=1 if sin>cos else -1
            return checked(rf'θ lancip, $\sin\theta+\cos\theta={s.latex(S)}$, dan $\sin\theta'+('>' if sign>0 else '<')+rf'\cos\theta$. Tentukan $\sec\theta+{K}\tan\theta$.',(1+K*sin)/cos,
                f'Dari jumlah serta identitas kuadrat diperoleh pasangan sin={sin}, cos={cos}, dengan urutan dipilih oleh ketaksamaan. Nilai sec+{K}tan=(1+{K}sin)/cos={s.latex((1+K*sin)/cos)}.',
                'v2_identitas_pemilihan_cabang','hard',system(['a','b'],[a+b-S,a*a+b*b-1],(1+K*a)/b,[a,b,sign*(a-b)]))
        if code=='D':
            if level=='easy':
                side=r.randint(3,25);angle=r.choice([15,20,25,30,35,40,45,50,55,60,65,70,75])
                return constant(rf'Segitiga ABC mempunyai A={angle}° dan B={angle}°. Jika sisi di depan A {side} cm, berapa sisi di depan B?',side,
                    'Sudut yang sama mempunyai sisi di hadapannya sama panjang.','v2_sinus_sudut_sama','easy')
            k=r.randint(3,8);side_a=k+r.randint(1,k-1);side_b=2*k;val=side_b**2+2*side_a**2
            return checked(rf'Dalam segitiga ABC, A=30°, sisi di depan A adalah {side_a} cm dan sisi di depan B adalah {side_b} cm. Ada dua segitiga yang memenuhi data. Jika dua kemungkinan panjang sisi di depan C adalah c₁ dan c₂, tentukan $c_1^2+c_2^2$.',val,
                f'Aturan kosinus terhadap A memberi c²-{side_b}√3 c+({side_b**2-side_a**2})=0. Jumlah akar {side_b}√3 dan hasil kali {side_b**2-side_a**2}. Maka jumlah kuadrat akar =3×{side_b**2}-2×({side_b**2-side_a**2})={val}. Kedua akar positif karena b/2<a<b.',
                'v2_sinus_ambigu_dua_segitiga','hard',system(['a','b'],[a+b-side_b*s.sqrt(3),a*b-side_b**2+side_a**2],a*a+b*b,[a,b]))
        return constant(rf'Dua sisi segitiga panjangnya {A} cm dan {B} cm dengan sudut apit 90°. Tentukan kuadrat sisi di depan sudut itu.',A*A+B*B,
            f'Aturan kosinus: c²={A}²+{B}²-2×{A}×{B} cos90°={A*A+B*B}.','v2_kosinus_sudut_siku','easy')
    if bab==4:
        if code=='A':
            return checked(rf'Vektor v=(x,y) mempunyai jumlah komponen {U+V} dan kuadrat panjang {U*U+V*V}. Jika x>y, tentukan kuadrat panjang $v+{pair(A,B)}$.',(U+A)**2+(V+B)**2,
                f'Dari x+y={U+V} dan x²+y²={U*U+V*V}, diperoleh xy={U*V}. Pilih x={U}, y={V} sesuai syarat. Kuadrat panjang v+w=({U+A})²+({V+B})²={(U+A)**2+(V+B)**2}.',
                'v2_vektor_rekonstruksi_norma','hard',system(['a','b'],[a+b-U-V,a*a+b*b-U*U-V*V],(a+A)**2+(b+B)**2,[a-b]))
        if code=='B':
            p=r.randint(1,4);q=r.randint(10,16);aa=r.randint(2,5);bb=r.randint(1,3);dot=aa*p+bb*q;norm=p*p+q*q
            if C*bb==T*aa:C+=1
            return checked(rf'Vektor u={pair(aa,bb)} dan v=(x,y) memenuhi $u\cdot v={dot}$, $|v|^2={norm}$, serta ${aa}y-{bb}x>0$. Tentukan $v\cdot{pair(C,T)}$.',C*p+T*q,
                f'Selesaikan {aa}x+{bb}y={dot} bersama x²+y²={norm}. Ketaksamaan memilih x={p}, y={q}; hasil kali titik berikutnya {C}×{p}+{T}×{q}={C*p+T*q}.',
                'v2_dot_norma_orientasi','hard',system(['a','b'],[aa*a+bb*b-dot,a*a+b*b-norm],C*a+T*b,[aa*b-bb*a]))
        if U*B==A*V:B+=1
        return constant(rf'Pada segitiga A{pair(A,B)}, B{pair(U,V)}, C{pair(U+A,V+B)}, titik M dan N adalah titik tengah AB dan AC. Dengan vektor, tentukan kuadrat panjang MN.',s.Rational(A*A+B*B,4),
            f'Vektor MN=(AC-AB)/2=BC/2=({A}/2,{B}/2). Kuadrat panjangnya ({A}²+{B}²)/4={s.Rational(A*A+B*B,4)}.','v2_geometri_garis_tengah','medium')
    if bab==5:
        px=r.randint(2,8);py=r.randint(2,8);sx=r.randint(-8,8);sy=r.randint(-8,8)
        if code=='A':
            Q=(-py-B,px+A);query=(sy-a)+(-sx-b)
            return checked(rf'Transformasi F berupa translasi (a,b), lalu rotasi 90° berlawanan arah jarum jam terhadap O. Diketahui F({pair(px,py)})={pair(*Q)}. Jika F(R)={pair(sx,sy)}, tentukan jumlah koordinat R.',sy-A-sx-B,
                f'Aturan F(x,y)=(-y-b,x+a). Data titik memberi a={A}, b={B}. Invers memberi R=({sy-A},{-sx-B}), sehingga jumlah koordinat {sy-A-sx-B}.',
                'v2_transformasi_inverse_berantai','hard',system(['a','b'],[-py-b-Q[0],px+a-Q[1]],query))
        # F = upper-triangular matrix after a quarter-turn.
        query=(-a*sx+a*sy*0+sy)/(a*b) # replaced with directly derived inverse below
        query=(sy/b)+(sy/b-sx)/a
        return checked(rf'Transformasi T bermatriks $\begin{{pmatrix}}a&1\\0&b\end{{pmatrix}}$ dengan a,b>0. R adalah rotasi 90° berlawanan arah jarum jam. Komposisi $T\circ R$ memetakan titik {pair(px,py)} ke {pair(px-A*py,B*px)}. Jika komposisi tersebut memetakan P ke {pair(sx,sy)}, tentukan jumlah koordinat P.',query.subs({a:A,b:B}),
            f'Matriks komposisi adalah [[1,-a],[b,0]]. Titik yang diketahui menentukan a={A}, b={B}. Dari Y=bx dan X=x-ay diperoleh x=Y/b, y=(Y/b-X)/a. Jumlahnya {query.subs({a:A,b:B})}.',
            'v2_matriks_transformasi_inverse','hard',system(['a','b'],[px-a*py-(px-A*py),b*px-B*px],query,[a,b]))
    if bab==6:
        if code=='A':
            base=r.randint(2,5);power=r.randint(2,5)
            if level=='medium':
                return constant(rf'Diketahui $\log_{base}({A}x+{B})={power}$. Tentukan x.',s.Rational(base**power-B,A),
                    f'Bentuk eksponensial memberi {A}x+{B}={base**power}; isolasi x={s.Rational(base**power-B,A)}.','v2_logaritma_linear_inverse','medium')
            return checked(rf'Bilangan a>1 memenuhi $\log_a X=1$, $\log_a Y=2$, dan $X+Y={base+base*base}$. Tentukan $\log_a {base**power}$.',power,
                f'Dari definisi log, X=a dan Y=a². Maka a²+a={base+base*base}, dengan akar yang memenuhi a>1 ialah {base}. Jadi log_a({base**power})={power}.',
                'v2_logaritma_basis_tersembunyi','hard',system(['a','b','c'],[b-a,c-a*a,b+c-base-base*base],s.log(base**power)/s.log(a),[a-1]))
        if code=='B':
            if level=='easy':
                return constant(rf'Fungsi $f(x)=(x+{A})/(x-{B})$ untuk $x\ne {B}$. Tentukan $f({B+1})$.',A+B+1,
                    f'Substitusi menghasilkan ({B+1}+{A})/1={A+B+1}.','v2_fungsi_rasional_langsung','easy')
            H=r.randint(1,3);K=H*r.randint(2,5);shift=r.randint(1,5);lo=shift-3;hi=shift+2*K
            guards=[s.Piecewise((0,s.Ne(x,shift)),(1,True)),s.Piecewise((0,s.Ne(K/(x-shift),H)),(1,True)),s.Piecewise((0,K/(x-shift)>s.Rational(1,2)),(1,True))]
            vals=[z for z in range(lo,hi+1) if z!=shift and s.Rational(K,z-shift)!=H and s.Rational(K,z-shift)>s.Rational(1,2)]
            return checked(rf'$f(t)=(t^2-{H*H})/(t-{H})$ dengan $t\ne {H}$, dan $g(x)={K}/(x-{shift})$. Tentukan jumlah seluruh x bilangan bulat pada [{lo},{hi}] yang membuat $(f\circ g)(x)>{H}+1/2$.',sum(vals),
                f'f(t)=t+{H} tetap mengecualikan t={H}. Jadi syaratnya x≠{shift}, {K}/(x-{shift})≠{H}, dan {K}/(x-{shift})>1/2. Nilai yang memenuhi {vals}; jumlah {sum(vals)}.',
                'v2_domain_komposisi_berlubang','hard',finite(['x'],[[lo,hi]],guards,x,'sum'))
        initial=r.randint(2,10)*100;growth=r.choice([2,3]);offset=r.randint(2,30)
        data=[initial*growth**j-offset for j in range(3)]
        return checked(rf'Model populasi $N(t)=ab^t-c$ memiliki a>0, b>1, c>0. Hasil pengamatan menunjukkan N(0)={data[0]}, N(1)={data[1]}, N(2)={data[2]}. Tentukan N({T}).',initial*growth**T-offset,
            f'Selisih berturut-turut berasio b={growth}; maka a={initial} dan c={offset}. Substitusi t={T} memberi {initial*growth**T-offset}.',
            'v2_eksponensial_tiga_parameter','hard',system(['a','b','c'],[a*b**j-c-v for j,v in enumerate(data)],a*b**T-c,[a,b-1,c]))
    raise ValueError((bab,code,level))
