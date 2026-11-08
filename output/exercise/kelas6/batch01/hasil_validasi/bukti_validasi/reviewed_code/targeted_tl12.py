"""Locally authored advanced grade-12 problems with recomputable constraints."""
import sympy as s
from .targeted_math import checked, constant, system, finite, m, pair


def generate(bab, code, level, r):
    a,b,c,x,t=s.symbols('a b c x t',real=True)
    A=r.randint(2,6);B=r.randint(2,7);C=r.randint(1,8);T=r.randint(3,6)
    if bab==1:
        h=r.randint(-7,7);k=r.randint(-7,7);R=r.randint(3,9)
        circle=s.expand((x-h)**2+(s.Symbol('y')-k)**2-R**2)
        if code=='A':
            p=(h+R,k);q=(h,k+R);offset=k-2*h
            eq=[p[0]**2+p[1]**2+a*p[0]+b*p[1]+c,
                q[0]**2+q[1]**2+a*q[0]+b*q[1]+c, a-b/2-offset]
            query=(a*a+b*b)/4-c
            return checked(rf'Sebuah lingkaran melalui P{pair(*p)} dan Q{pair(*q)}. Pusatnya terletak pada garis $y=2x+({offset})$. Tentukan kuadrat jari-jari lingkaran tersebut.',R**2,
                rf'Tulis x²+y²+Dx+Ey+F=0. Substitusi kedua titik dan syarat pusat (-D/2,-E/2) pada garis menghasilkan pusat ({h},{k}). Jarak kuadrat pusat ke P adalah {R**2}.',
                'v2_lingkaran_rekonstruksi','hard',system(['a','b','c'],eq,query))
        if code=='B':
            b0=r.randint(3,8);f=r.randint(2,7);aa=b0*b0+f*f;y0=s.Rational(2*k+b0,2)
            query=a+s.sqrt(c*(1-(y0-b)**2/(c-f*f)))
            val=h+s.sqrt(3*aa)/2
            return checked(rf'Elips berfokus F₁{pair(h-f,k)} dan F₂{pair(h+f,k)}, serta melalui titik {pair(h,k+b0)}. Berapa koordinat $x$ yang lebih besar dari dua titik elips pada garis $y={s.latex(y0)}$?',val,
                rf'Pusat adalah ({h},{k}); c={f}, b={b0}, dan a²=b²+c²={aa}. Substitusi y={y0} memberi (x-{h})²=3a²/4. Cabang kanan adalah {s.latex(val)}.',
                'v2_elips_fokus_irisan','hard',system(['a','b','c'],[a-h,b-k,c-aa],query))
        if code=='C':
            slope=r.randint(1,4);lo=-r.randint(12,25);hi=r.randint(12,25)
            valid=[v for v in range(lo,hi+1) if (slope*h-k-v)**2<R*R*(slope*slope+1)]
            # Finite equality indicator is evaluated exactly for every parameter.
            return checked(rf'Lingkaran ${s.latex(circle)}=0$ dan keluarga garis ${slope}x-y=t$ diberikan. Parameter $t$ bilangan bulat pada interval [{lo},{hi}]. Berapa jumlah semua nilai $t$ yang membuat garis memotong lingkaran di dua titik berbeda?',sum(valid),
                rf'Pusat ({h},{k}), r²={R**2}. Dua perpotongan memerlukan ({slope*h-k}-t)² < {R**2*(slope*slope+1)}. Nilai bulat yang memenuhi: {valid}; jumlahnya {sum(valid)}.',
                'v2_sekan_parameter_bulat','hard',finite(['t'],[[lo,hi]],[s.Piecewise((0,(slope*h-k-t)**2<R*R*(slope*slope+1)),(1,True))],t,'sum'))
        d=R+r.randint(2,7);e=r.randint(2,8);prod=s.Rational(e*e-R*R,d*d-R*R)
        return checked(rf'Dari titik P{pair(h+d,k+e)} ditarik dua garis singgung ke lingkaran ${s.latex(circle)}=0$. Jika gradiennya $m_1$ dan $m_2$, tentukan $m_1m_2$.',prod,
            rf'Pusat ({h},{k}). Garis melalui P bergradien m menyinggung jika ({d}m-{e})²={R**2}(m²+1). Persamaan gradien memiliki koefisien utama {d*d-R*R} dan konstanta {e*e-R*R}; hasil kali akar {prod}.',
            'v2_dua_gradien_singgung','hard',system(['a'],[(d*d-R*R)*a-(e*e-R*R)],a))
    if bab==2:
        if code=='A':
            p=r.randint(2,4);q=2*p+1;der=2*A*p+B;fv=A*q*q+B*q+C
            return checked(rf'Fungsi $f(x)=ax^2+bx+{C}$ memenuhi $f({q})={fv}$ dan $f^\prime({p})={der}$. Gunakan definisi turunan sebagai limit hasil bagi selisih untuk menentukan $f^\prime({T})$.',2*A*T+B,
                rf'Dari definisi limit, f′(x)=2ax+b. Dua data memberi {q*q}a+{q}b={fv-C} dan {2*p}a+b={der}; diperoleh a={A}, b={B}. Jadi f′({T})={2*A*T+B}.',
                'v2_limit_turunan_parameter','hard',system(['a','b'],[a*q*q+b*q+C-fv,2*a*p+b-der],2*a*T+b))
        if code=='B':
            f=(a*x*x+b*x)*(x+C);df=s.diff(f,x);d0=df.subs({x:0,a:A,b:B});d1=df.subs({x:1,a:A,b:B});query=s.diff(f,x,2).subs(x,T)
            val=query.subs({a:A,b:B})
            return checked(rf'Untuk $f(x)=(ax^2+bx)(x+{C})$ diketahui $f^\prime(0)={d0}$ dan $f^\prime(1)={d1}$. Tentukan $f^{{\prime\prime}}({T})$.',val,
                rf'Aturan hasil kali memberi f′={s.latex(df)}. Kedua nilai turunannya menentukan a={A}, b={B}. Turunkan sekali lagi lalu substitusi x={T}; hasilnya {val}.',
                'v2_turunan_hasil_kali_balik','hard',system(['a','b'],[df.subs(x,0)-d0,df.subs(x,1)-d1],query))
        if code=='C':
            u=r.randint(1,4);v=u+r.randint(2,5);f=x**3+a*x*x+b*x+C;df=s.diff(f,x);aa=-s.Rational(3,2)*(u+v);bb=3*u*v
            val=s.simplify(f.subs({x:u,a:aa,b:bb})-f.subs({x:v,a:aa,b:bb}))
            return checked(rf'Fungsi $f(x)=x^3+ax^2+bx+{C}$ mempunyai titik stasioner pada $x={u}$ dan $x={v}$. Tentukan selisih nilai maksimum lokal dan minimum lokalnya.',val,
                rf'Syarat f′({u})=f′({v})=0 menghasilkan a={aa}, b={bb}. Turunan kedua negatif di {u} dan positif di {v}. Hitung f({u})-f({v})={val}.',
                'v2_ekstrem_rekonstruksi','hard',system(['a','b'],[df.subs(x,u),df.subs(x,v)],f.subs(x,u)-f.subs(x,v)))
        p=r.randint(2,6)*10000;q=r.randint(1,5)*10000;budget=r.randint(12,30)*120000;val=s.Rational(budget**2,12*p*q)
        return checked(rf'Kebun persegi panjang berbatasan dengan sungai pada salah satu sisinya. Sisi sejajar sungai yang lain berpagar dengan biaya Rp{p:,} per meter; dua sisi tegak dan dua pagar pembagi yang tegak lurus sungai masing-masing berbiaya Rp{q:,} per meter. Anggaran tepat Rp{budget:,}. Berapa luas maksimum kebun?'.replace(',','.'),s.Rational(budget**2,16*p*q),
            rf'Jika sisi sejajar sungai x dan kedalaman y, terdapat empat ruas pagar sepanjang y. Kendala biaya {p}x+{4*q}y={budget}. Luas xy maksimum saat x={s.Rational(budget,2*p)}, y={s.Rational(budget,8*q)}; hasil kali {s.Rational(budget**2,16*p*q)} m².',
            'v2_optimasi_pagar_biaya','hard',system(['a','b'],[p*a+4*q*b-budget,p*a-4*q*b],a*b,[a,b]))
    if bab==3:
        if code=='A':
            f=a*x*x+b*x;F=s.integrate(f,x);u=F.subs({x:1,a:A,b:B});v=F.subs({x:2,a:A,b:B});query=F.subs(x,T)
            return checked(rf'Fungsi $F$ memenuhi $F^\prime(x)=ax^2+bx$, $F(0)=0$, $F(1)={s.latex(u)}$, dan $F(2)={s.latex(v)}$. Tentukan $F({T})$.',query.subs({a:A,b:B}),
                rf'Integralkan: F(x)=ax³/3+bx²/2+C; F(0)=0 memberi C=0. Dua nilai F menentukan a={A}, b={B}. Substitusi {T} memberi {query.subs({a:A,b:B})}.',
                'v2_integral_kondisi_ganda','hard',system(['a','b'],[F.subs(x,1)-u,F.subs(x,2)-v],query))
        if code=='B':
            f=a*x+b;p=s.integrate(f,(x,0,1)).subs({a:A,b:B});q=s.integrate(x*f,(x,0,1)).subs({a:A,b:B});query=s.integrate(x*x*f,(x,0,T))
            return checked(rf'Diketahui $f(x)=ax+b$, $\int_0^1 f(x)\,dx={s.latex(p)}$, dan $\int_0^1 xf(x)\,dx={s.latex(q)}$. Hitung $\int_0^{T}x^2f(x)\,dx$.',query.subs({a:A,b:B}),
                rf'Integral data memberi a/2+b={p} dan a/3+b/2={q}; maka a={A}, b={B}. Integralkan x²({A}x+{B}) pada batas 0 hingga {T}.',
                'v2_integral_momen_balik','hard',system(['a','b'],[a/2+b-p,a/3+b/2-q],query))
        L=r.randint(5,9);root=r.randint(1,(L-1)//2);height=A*root*(L-root);area=s.Rational(A*L**3,6);f=a*x*(L-x)
        query=2*s.integrate(height-f,(x,0,b))+s.integrate(f-height,(x,b,L-b))
        value=query.subs({a:A,b:root})
        return checked(rf'Kurva $y=ax({L}-x)$ dengan $a>0$ membatasi luas {s.latex(area)} dengan sumbu x pada interval $[0,{L}]$. Tentukan luas seluruh daerah antara kurva tersebut dan garis $y={height}$ pada interval yang sama.',value,
            rf'Dari integral terhadap sumbu x diperoleh a={A}. Persamaan kurva dengan y={height} berakar {root} dan {L-root}. Pada dua interval luar garis berada di atas kurva; pada interval tengah kurva di atas garis. Jumlahkan ketiga integral selisih positif; luas {value}.',
            'v2_luas_berganti_posisi','hard',system(['a','b'],[a*L**3/6-area,a*b*(L-b)-height],query,[a,b,L/2-b]))
    if bab==4:
        if code=='A':
            if level=='medium':
                vals=[A,A+B,A+B+C];weights=[r.randint(1,4) for _ in vals];z=sum(weights);val=sum(s.Rational(v*w,z) for v,w in zip(vals,weights))
                return constant(rf'Variabel acak X bernilai {vals[0]}, {vals[1]}, {vals[2]} dengan peluang $k$, ${weights[1]}/{weights[0]}k$, dan ${weights[2]}/{weights[0]}k$. Tentukan $E(X)$.',val,
                    rf'Jumlah peluang harus 1, sehingga k={s.Rational(weights[0],z)}. Kalikan setiap nilai X dengan peluangnya dan jumlahkan: {val}.','v2_acak_normalisasi_harapan','medium')
            n=r.randint(4,8);same=r.randint(5,12);near=r.randint(2,6);loss=r.randint(1,5)
            scores=[same if i==j else near if abs(i-j)==1 else -loss for i in range(1,n+1) for j in range(1,n+1)];val=s.Rational(sum(scores),n*n)
            reward=s.Piecewise((same,a-b==0),(near,s.Abs(a-b)==1),(-loss,True))
            # Equality must be symbolic rather than Python's structural equality.
            reward=s.Piecewise((same,s.Eq(a,b)),(near,s.Eq(s.Abs(a-b),1)),(-loss,True))
            return checked(rf'Dua dadu adil masing-masing bernomor 1 sampai {n} dilempar. Pemain memperoleh {same} poin jika hasil sama, {near} poin jika selisih hasil tepat 1, dan kehilangan {loss} poin untuk hasil lainnya. Berapa nilai harapan skor satu permainan?',val,
                rf'Ada {n*n} pasangan berurutan. Hasil sama ada {n}, selisih 1 ada {2*(n-1)}, dan sisanya {n*n-n-2*(n-1)}. Harapan=({same}×{n}+{near}×{2*(n-1)}-{loss}×{n*n-n-2*(n-1)})/{n*n}={val}.',
                'v2_acak_skor_bertingkat','hard',finite(['a','b'],[[1,n],[1,n]],[],reward/(n*n),'sum'))
        if code=='B':
            xs=[A,A+B,A+B+C];p=s.Rational(r.randint(1,3),10);q=s.Rational(r.randint(2,4),10);tail=1-p-q;mean=p*xs[0]+q*xs[1]+tail*xs[2];cut=xs[1]+r.randint(1,3)
            query=a*(xs[0]-cut)**2+b*(xs[1]-cut)**2+(1-a-b)*(xs[2]-cut)**2
            return checked(rf'X hanya bernilai {xs[0]}, {xs[1]}, dan {xs[2]}. Diketahui $P(X\le {xs[1]})={s.latex(p+q)}$ dan $E(X)={s.latex(mean)}$. Tentukan $E[(X-{cut})^2]$.',query.subs({a:p,b:q}),
                rf'Misalkan dua peluang pertama p dan q. Data memberi p+q={p+q} dan {xs[0]}p+{xs[1]}q+{xs[2]}(1-p-q)={mean}. Diperoleh p={p}, q={q}. Jumlahkan (x-{cut})²P(X=x), hasil {query.subs({a:p,b:q})}.',
                'v2_diskret_parameter_momen','hard',system(['a','b'],[a+b-p-q,a*xs[0]+b*xs[1]+(1-a-b)*xs[2]-mean],query,[a,b,1-a-b]))
        if code=='C':
            L=r.randint(4,10)
            if level=='medium':
                width=12*r.randint(2,6);lo=r.randint(1,8);cut=lo+width//4;threshold=lo+r.choice([width//3,width//2,2*width//3]);value=s.Rational(lo+width-threshold,width)
                return constant(rf'X seragam kontinu pada $[{lo},b]$. Diketahui $P(X<{cut})=1/4$. Tentukan $P(X>{threshold})$.',value,
                    rf'Perbandingan panjang interval memberi ({cut}-{lo})/(b-{lo})=1/4, sehingga b={lo+width}. Panjang bagian di atas {threshold} adalah {lo+width-threshold} dari total {width}; peluang {value}.','v2_kontinu_batas_balik','medium')
            p=s.Rational(r.randint(1,3),10);q=s.Rational(r.randint(2,4),10);cdf1=p+q/2;cdf2=p+q+(1-p-q)/3;val=p/2+3*q/4
            return checked(rf'Suatu sumber memilih distribusi seragam $[0,{L}]$, $[{L},{3*L}]$, atau $[{3*L},{6*L}]$ dengan peluang $p$, $q$, dan $1-p-q$. Diketahui $P(X<{2*L})={s.latex(cdf1)}$ serta $P(X<{4*L})={s.latex(cdf2)}$. Tentukan $P({s.latex(s.Rational(L,2))}<X<{s.latex(s.Rational(5*L,2))})$.',val,
                rf'Data distribusi campuran memberi p+q/2={cdf1} dan p+q+(1-p-q)/3={cdf2}. Maka p={p}, q={q}. Interval pertanyaan mencakup separuh interval pertama dan 3/4 interval kedua, sehingga peluang p/2+3q/4={val}.',
                'v2_kontinu_campuran_balik','hard',system(['a','b'],[a+b/2-cdf1,a+b+(1-a-b)/3-cdf2],a/2+3*b/4,[a,b,1-a-b]))
        if code=='D':
            n=r.randint(5,9);Z=A*n*(n+1)//2+B*n;pa=s.Rational(A,Z);pb=s.Rational(B,Z);mean=sum(j*(pa*j+pb) for j in range(1,n+1));cut=r.randint(2,n-1);query=sum(a*j+b for j in range(cut,n+1) if j%2==0)
            return checked(rf'Fungsi peluang X adalah $P(X=j)=aj+b$ untuk $j=1,2,\ldots,{n}$, dan nol di luar nilai itu. Diketahui $E(X)={s.latex(mean)}$. Tentukan peluang bahwa X genap dan $X\ge {cut}$.',query.subs({a:pa,b:pb}),
                rf'Normalisasi memberi {n*(n+1)//2}a+{n}b=1; rumus harapan memberi {sum(j*j for j in range(1,n+1))}a+{n*(n+1)//2}b={mean}. Maka a={pa}, b={pb}; jumlahkan peluang nilai genap minimal {cut}.',
                'v2_pmf_normalisasi_momen','hard',system(['a','b'],[sum(a*j+b for j in range(1,n+1))-1,sum(j*(a*j+b) for j in range(1,n+1))-mean],query))
        if code=='E':
            L=r.randint(4,10);Z=s.Rational(A*L*L,2)+B*L;pa=A/Z;pb=B/Z;mean=pa*L**3/3+pb*L*L/2;u=r.randint(1,L-2);v=r.randint(u+1,L-1);query=a*(v*v-u*u)/2+b*(v-u)
            return checked(rf'Densitas X berbentuk $f(x)=ax+b$ pada $0\le x\le {L}$ dan nol di luar interval. Diketahui $E(X)={s.latex(mean)}$. Tentukan $P({u}<X<{v})$.',query.subs({a:pa,b:pb}),
                rf'Integral densitas memberi {L*L}/2 a+{L}b=1. Integral x f(x) memberi {L**3}/3 a+{L*L}/2 b={mean}. Diperoleh a={pa}, b={pb}; integralkan ax+b antara {u} dan {v}.',
                'v2_densitas_parameter_ganda','hard',system(['a','b'],[a*L*L/2+b*L-1,a*L**3/3+b*L*L/2-mean],query,[a,b]))
        n=r.randint(5,10);p=r.choice([s.Rational(1,3),s.Rational(2,3),s.Rational(2,5),s.Rational(3,5)]);mu=n*p;var=n*p*(1-p);val=p**n+n*(1-p)*p**(n-1)
        return checked(rf'X berdistribusi binomial dengan parameter n dan p yang belum diketahui. Diberikan $E(X)={s.latex(mu)}$ dan $\operatorname{{Var}}(X)={s.latex(var)}$. Tentukan peluang bahwa banyak kegagalan paling banyak satu.',val,
            rf'Dari np={mu} dan np(1-p)={var}, p=1-Var/E={p} dan n={n}. Paling banyak satu gagal berarti X=n atau n-1. Peluangnya p^n+n(1-p)p^(n-1)={val}.',
            'v2_binomial_parameter_balik','hard',system(['a','b'],[a*b-mu,a*b*(1-b)-var],b**a+a*(1-b)*b**(a-1),[a,b,1-b]))
    raise ValueError((bab,code,level))
