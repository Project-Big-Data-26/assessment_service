"""Locally authored upper-secondary problems with explicit inverse models."""
from itertools import permutations
import sympy as s
from .targeted_math import checked,constant,system,finite,m,pair,rp

a,b,c,x=s.symbols('a b c x',real=True)

def interest(r,rate=False):
    P=r.randint(10,60)*100000;I=P*s.Rational(r.randint(1,3),100);u=r.randint(2,5);v=u+r.randint(2,5);T=v+r.randint(2,6);D=r.randint(2,9)*100000
    cert=system(['a','b'],[a+u*b-P-u*I,a+v*b-P-v*I],1200*b/a if rate else a+T*b+D*(1+(T-v)*b/a),[a,b])
    value=1200*I/P if rate else P+T*I+D*(1+(T-v)*I/P)
    q=f'Tabungan menggunakan bunga tunggal bulanan dengan modal dan suku bunga tetap. Saldo akhir bulan {u} adalah {rp(P+u*I)}, dan akhir bulan {v} adalah {rp(P+v*I)}; tidak ada transaksi atau biaya sebelum saat itu. '
    q+=('Berapa persentase suku bunga per tahun?' if rate else f'Tepat sesudah pencatatan saldo bulan {v}, ditambahkan {rp(D)} dengan suku bunga yang sama. Berapa saldo akhir bulan {T}, dalam rupiah?')
    return checked(q,value,f'Selisih saldo dibagi selisih waktu memberi bunga awal per bulan {rp(I)}. Modal awal {rp(P)}, suku bunga bulanan {m(I/P)}. '+(f'Persentase tahunan =12 × 100 × {I/P}={value}.' if rate else f'Modal awal berbunga selama {T} bulan; tambahan hanya {T-v} bulan. Jumlah {P}+{T}×{I}+{D}(1+{T-v}×{I/P})={value}.'),'v2_bunga_tunggal_rekonstruksi','hard',cert)

def arithmetic(r,series=False):
    A=r.randint(2,20);D=r.randint(2,8);N=r.randint(8,20)
    if not series:
        query=s.floor((A+(N-1)*D-a)/b)+2
        return checked(rf'Barisan aritmetika mempunyai beda positif, $U_2+U_7={2*A+7*D}$ dan $U_3={A+2*D}$. Berapa indeks terkecil n sehingga $U_n>{A+(N-1)*D}$?',N+1,
            f'Tulis U_n=a+(n-1)d. Data memberi 2a+7d={2*A+7*D}, a+2d={A+2*D}, sehingga a={A}, d={D}. Ketaksamaan menjadi n>{N}; indeks bulat terkecil {N+1}.','v2_barisan_kendala_indeks','hard',system(['a','b'],[2*a+7*b-2*A-7*D,a+2*b-A-2*D],query,[b]))
    S3=3*(A+D);S5=5*(A+2*D);bound=s.Rational(N,2)*(2*A+(N-1)*D)
    query=s.floor((-(2*a-b)+s.sqrt((2*a-b)**2+8*b*bound))/(2*b))+1
    return checked(rf'Deret aritmetika bersuku pertama dan beda positif memenuhi $S_3={S3}$ dan $S_5={S5}$. Berapa n terkecil dengan $S_n>{bound}$?',N+1,
        f'Rumus jumlah memberi a+d={A+D}, a+2d={A+2*D}, jadi a={A}, d={D}. Selesaikan n(2a+(n-1)d)/2>{bound}. Batas positif n={N}, sehingga n terkecil {N+1}.','v2_deret_inverse_batas','hard',system(['a','b'],[3*(a+b)-S3,5*(a+2*b)-S5],query,[a,b]))

def generate(grade,bab,code,level,r):
    A=r.randint(2,8);B=r.randint(2,9);C=r.randint(1,8);U=r.randint(3,12);V=r.randint(2,8);T=r.randint(3,7)
    if grade==10:
        if bab==1:
            base=r.randint(2,4)
            if code=='A':
                if level=='medium':
                    return constant(rf'Jika ${base}^n\cdot {base}^{A}={base**(U+A)}$, tentukan $2n+{B}$.',2*U+B,f'Kesamaan pangkat memberi n+{A}={U+A}, sehingga n={U}; hasil 2n+{B}={2*U+B}.','v2_pangkat_inverse_rutin',level)
                return checked(rf'Bilangan a,b memenuhi ${base}^{{a+b}}={base**(U+V)}$ dan ${base}^{{a-2b}}={s.latex(s.Rational(base)**(U-2*V))}$. Tentukan ${base}^{{ab}}$.',base**(U*V),f'Basis sama memberi a+b={U+V}, a-2b={U-2*V}. Eliminasi menentukan b={V}, a={U}. Maka ab={U*V} dan nilai pangkat {base**(U*V)}.','v2_eksponen_dua_parameter',level,system(['a','b'],[a+b-U-V,a-2*b-U+2*V],base**(a*b)))
            if code=='B':
                p=A*A;q=B*B
                return checked(rf'Bilangan positif a,b memenuhi $ab={p*q}$ dan $a^2/b={s.latex(s.Rational(p*p,q))}$. Tentukan $\sqrt a+1/\sqrt b$.',A+s.Rational(1,B),f'Kalikan kedua persamaan: a³={p**3}, jadi a={p}. Dari ab diketahui b={q}. Akar positifnya {A} dan {B}, sehingga hasil {A}+1/{B}.','v2_sifat_pangkat_inverse',level,system(['a','b'],[a*b-p*q,a*a-s.Rational(p*p,q)*b],s.sqrt(a)+1/s.sqrt(b),[a,b]))
            if code=='C':
                initial=U*10;growth=r.choice([2,3]);take=r.choice([2,4]);val=initial*growth**(5+T)*s.Rational(take-1,take)-initial
                return checked(rf'Populasi dimodelkan $N(t)=ab^t$, a>0,b>1. Diketahui N(2)={initial*growth**2} dan N(5)={initial*growth**5}. Tepat setelah pengamatan t=5, sebanyak 1/{take} populasi dipindahkan. Sisanya tetap bertumbuh dengan faktor b setiap satuan waktu. Berapa selisih populasi pada t={5+T} terhadap N(0)?',val,f'Rasio N(5)/N(2)=b³={growth**3}, jadi b={growth} dan a={initial}. Setelah pemindahan tersisa ({take}-1)/{take} N(5); tumbuhkan {T} kali lalu kurangi a, hasil {val}.','v2_eksponensial_intervensi',level,system(['a','b'],[a*b*b-initial*growth**2,a*b**5-initial*growth**5],a*b**(5+T)*s.Rational(take-1,take)-a,[a,b-1]))
            d=r.choice([2,3,5,6,7]);return constant(rf'Sederhanakan $\sqrt{{{A*A*d}}}$ dalam bentuk akar paling sederhana.',A*s.sqrt(d),f'Pisahkan faktor kuadrat: √({A}²×{d})={A}√{d}.','v2_radikal_faktor_kuadrat',level)
        if bab==2:return arithmetic(r,code=='B') if code in 'AB' else interest(r)
        if bab==3:
            k=r.randint(3,20);eye=s.Rational(r.randint(12,18),10);H=k*s.sqrt(3)+eye;value=s.sqrt(H*H+9*k*k)
            return checked(rf'Seorang pengamat dengan tinggi mata {m(eye)} m melihat puncak menara dengan sudut elevasi 30°. Setelah berjalan {2*k} m menuju menara di tanah datar, sudutnya 60°. Kabel dipasang dari puncak menara ke titik tanah tempat pengamat semula berdiri. Berapa panjang kabel dalam meter?',value,
                f'Misalkan jarak dekat x dan tinggi menara di atas mata h. Maka h=x√3=(x+{2*k})/√3, sehingga x={k}, h={k}√3. Tinggi menara H=h+{eye}; jarak titik jauh {3*k}. Kabel =√(H²+{3*k}²)={s.latex(value)}.','v2_trigonometri_dua_posisi_kabel',level,system(['a','b'],[b-a*s.sqrt(3),b-(a+2*k)/s.sqrt(3)],s.sqrt((b+eye)**2+(a+2*k)**2),[a,b]))
        if bab==4:
            if level=='easy':
                if code=='B':return constant(rf'Daerah memenuhi $x,y\ge0$ dan $x+y\le {U*B}$. Pada x=0, berapa y terbesar?',U*B,f'Substitusi x=0 memberi y≤{U*B}; batasnya tercapai.','v2_ptldv_potong_sumbu',level)
                return constant(rf'Diketahui x+y={A+B}, y+z={B+C}, x+z={A+C}. Jumlahkan ketiga persamaan untuk menentukan x+y+z.',A+B+C,f'Jumlah ruas kiri 2(x+y+z), ruas kanan {2*(A+B+C)}. Bagi dua memberi {A+B+C}.','v2_spltv_jumlah_terpandu',level)
            prices=[A*1000,B*1000,C*1000];matrix=s.Matrix([[1,1,1],[2,1,3],[1,3,2]]);tot=matrix*s.Matrix(prices);fee=U*1000;budget=r.randint(30,80)*10000;pack=2*a+3*b+c;val=(budget-fee)//(2*prices[0]+3*prices[1]+prices[2])
            return checked(f'Harga buku, pena, dan penggaris tetap. Pembelian (1 buku,1 pena,1 penggaris), (2 buku,1 pena,3 penggaris), dan (1 buku,3 pena,2 penggaris) berturut-turut berbiaya {list(map(int,tot))} rupiah. Sebuah paket berisi 2 buku,3 pena,1 penggaris. Dengan anggaran {budget} rupiah dan biaya kirim tetap {fee} rupiah per pesanan, berapa paket utuh terbanyak yang bisa dibeli?',val,
                f'Selesaikan SPLTV dari ketiga pembelian: harga {prices} rupiah. Harga paket {2*prices[0]+3*prices[1]+prices[2]}. Sisa dana setelah kirim {budget-fee}; bagi harga paket dan bulatkan ke bawah, hasil {val}.','v2_spltv_paket_anggaran',level,system(['a','b','c'],list(matrix*s.Matrix([a,b,c])-tot),s.floor((budget-fee)/pack),[a,b,c]))
        if bab==5:
            if code=='A':return constant(rf'Akar persamaan $x^2-{U+V}x+{U*V}=0$ adalah p,q. Tentukan $(p-q)^2$ tanpa mencari akar satu per satu.',(U-V)**2,f'Vieta memberi p+q={U+V}, pq={U*V}; (p-q)²=(p+q)²-4pq={(U-V)**2}.','v2_vieta_selisih_akar',level)
            H=r.randint(-5,8);L=r.randint(-4,0);R=r.randint(2,6);F=lambda t:A*(t-H)**2+C;query=s.Piecewise((c-b*b/(4*a),s.And(-b/(2*a)>=L,-b/(2*a)<=R)),(s.Min(a*L*L+b*L+c,a*R*R+b*R+c),True));value=F(max(L,min(H,R)))
            return checked(rf'Fungsi kuadrat f memenuhi f(0)={F(0)}, f(1)={F(1)}, f(2)={F(2)}. Tentukan nilai minimum f pada interval tertutup [{L},{R}].',value,f'Tiga data memberi f(x)={A}(x-({H}))²+{C}. Titik puncak x={H}; periksa apakah ada dalam interval. Titik terdekat pada interval adalah {max(L,min(H,R))}, sehingga minimum {value}.','v2_kuadrat_rekonstruksi_interval',level,system(['a','b','c'],[a*t*t+b*t+c-F(t) for t in [0,1,2]],query,[a]))
        if bab==6:
            if code=='A':
                widths=[r.randint(2,4),r.randint(5,7),r.randint(8,10)];start=r.randint(0,10);bounds=[start,start+widths[0],start+sum(widths[:2]),start+sum(widths)];mid=[s.Rational(bounds[i]+bounds[i+1],2) for i in range(3)];freq3=U*2
                if level=='medium':
                    f1=A*widths[0];f2=B*widths[1];return constant(f'Histogram kepadatan memiliki dua kelas [{bounds[0]},{bounds[1]}) dan [{bounds[1]},{bounds[2]}), dengan tinggi {A} dan {B}. Frekuensi adalah luas batang. Berapa proporsi data di kelas kedua?',s.Rational(f2,f1+f2),f'Luas batang pertama {f1}, kedua {f2}. Proporsi kedua {f2}/({f1}+{f2})={s.Rational(f2,f1+f2)}.','v2_histogram_luas_proporsi',level)
                N=A*widths[0]+B*widths[1]+freq3;mean=(A*widths[0]*mid[0]+B*widths[1]*mid[1]+freq3*mid[2])/N
                return checked(f'Histogram kepadatan terdiri dari kelas [{bounds[0]},{bounds[1]}), [{bounds[1]},{bounds[2]}), [{bounds[2]},{bounds[3]}]. Frekuensi kelas terakhir {freq3}, jumlah seluruh data {N}, dan rata-rata berdasarkan titik tengah {m(mean)}. Berapa rasio tinggi batang pertama terhadap kedua?',s.Rational(A,B),f'Misalkan tinggi pertama a dan kedua b. Frekuensi = lebar×tinggi. Jumlah memberi {widths[0]}a+{widths[1]}b={N-freq3}; persamaan rata-rata memakai titik tengah {mid}. Penyelesaian a={A}, b={B}; rasio {s.Rational(A,B)}.','v2_histogram_rekonstruksi_kepadatan',level,system(['a','b'],[widths[0]*a+widths[1]*b+freq3-N,widths[0]*mid[0]*a+widths[1]*mid[1]*b+freq3*mid[2]-N*mean],a/b,[a,b]))
            if code=='B':
                n=r.randint(12,30);mean=r.randint(50,75);delta=r.randint(1,3);old=r.randint(20,40);new=old+n*delta;p=r.randint(30,60);q=r.randint(60,90);val=s.Rational(n*mean-p-q,n-2)
                return checked(f'Rata-rata n data semula {mean}. Mengganti nilai {old} dengan {new} menaikkan rata-rata sebesar {delta}. Data lalu dikembalikan persis ke keadaan semula. Jika dua data bernilai {p} dan {q} dihapus, berapa rata-rata sisanya?',val,f'Kenaikan jumlah {new-old}=n×{delta}, jadi n={n}. Jumlah asli {n*mean}. Hapus kedua nilai dan dua anggota: rata-rata ({n*mean}-{p}-{q})/({n}-2)={val}.','v2_statistika_koreksi_penghapusan',level,system(['a'],[delta*a-new+old],(a*mean-p-q)/(a-2),[a-2]))
            if level=='medium':
                q1=U;med=U+B;q3=med+C;k=r.randint(2,5);shift=r.randint(30,60);val=shift-k*med+k*(q3-q1)
                return constant(f'Suatu data mempunyai Q1={q1}, median={med}, Q3={q3}. Setiap nilai x diubah menjadi y={shift}-{k}x. Tentukan median baru ditambah jangkauan antarkuartil baru.',val,f'Transformasi menurun membalik urutan. Median baru {shift-k*med}; IQR baru {k}({q3}-{q1})={k*(q3-q1)}. Jumlah {val}.','v2_transformasi_kuartil',level)
            n=r.choice([15,17,19,21,23]);d=r.randint(1,3);v1=A;v2=A+B;v3=A+B+C+(B==2*C);mid=(n+1)//2;bexpr=n-3*a-d;cexpr=2*a+d;query=(v1*a+v2*bexpr+v3*cexpr)/n
            guards=[s.Piecewise((0,bexpr>0),(1,True)),s.Piecewise((0,a<mid),(1,True)),s.Piecewise((0,a+bexpr>=mid),(1,True))];feasible=[j for j in range(1,n) if n-3*j-d>0 and j<mid<=n-2*j-d];val=max(query.subs(a,j) for j in feasible)
            return checked(f'Data berjumlah {n}, hanya bernilai {v1}, {v2}, atau {v3}, masing-masing frekuensinya a,b,c positif. Diketahui c=2a+{d} dan median data adalah {v2}. Berapa rata-rata terbesar yang mungkin?',val,f'Dari jumlah diperoleh b={n}-3a-{d}, c=2a+{d}. Posisi median {mid} mensyaratkan a<{mid}≤a+b. Kandidat a={feasible}; hitung rata-rata tiap kandidat dengan semua frekuensi positif. Nilai terbesar {val}.','v2_frekuensi_median_optimasi',level,finite(['a'],[[1,n-1]],guards,query,'max'))
        if code=='A':
            n=r.randint(4,9);bound=r.randint(n+1,2*n-1);cert={'type':'finite_probability','variables':['a','b'],'ranges':[[1,n],[1,n]],'event':f'a+b>={bound}','condition':'Eq(Mod(a+b,2),0)'};from .targeted_math import solve_certificate
            val=solve_certificate(cert);return checked(f'Dua dadu adil masing-masing bernomor 1 sampai {n} dilempar. Diketahui jumlah kedua angka genap. Berapa peluang jumlahnya paling sedikit {bound}?',val,f'Ruang sampel bersyarat memuat pasangan (i,j) dengan jumlah genap. Pilih lagi pasangan berjumlah ≥{bound}. Menghitung pasangan terurut dari {n*n} kemungkinan memberi perbandingan {val}.','v2_distribusi_dadu_bersyarat',level,cert)
        if code=='B':
            bb=r.randint(12,30);ratio=r.randint(2,4);aa=ratio*bb;both=r.randint(2,bb-2);union=aa+bb-both;N=aa+bb+r.randint(5,15);val=s.Rational(N-union,N-bb)
            return checked(f'Dari {N} siswa, {union} mengikuti setidaknya satu klub A atau B, dan {both} mengikuti keduanya. Banyak anggota A adalah {ratio} kali anggota B. Di antara siswa yang tidak mengikuti B, berapa proporsi yang juga tidak mengikuti A?',val,f'Inklusi-eksklusi memberi |A|+|B|={union+both}; rasio menentukan |B|={bb}. Siswa di luar kedua klub {N-union}, sedangkan yang tidak B {N-bb}. Proporsi {val}.','v2_venn_inverse_ruang_bersyarat',level,system(['a','b'],[a+b-union-both,a-ratio*b],(N-union)/(N-b),[a,b]))
        p=s.Rational(r.randint(2,7),10);s1=s.Rational(9,10);s2=s.Rational(7,10);tot=p*s1+(1-p)*s2
        return checked(f'Pabrik A dan B menyuplai barang; proporsi dari A belum diketahui. Peluang lolos uji barang A adalah {m(s1)}, barang B {m(s2)}. Peluang lolos uji seluruh barang {m(tot)}. Jika sebuah barang ternyata lolos, berapa peluang berasal dari A?',p*s1/tot,f'Tulis proporsi A=p. Persamaan {s1}p+{s2}(1-p)={tot} memberi p={p}. Bagian yang sekaligus A dan lolos {p*s1}; bagi peluang lolos {tot}, hasil {p*s1/tot}.','v2_campuran_inverse_peluang',level,system(['a'],[s1*a+s2*(1-a)-tot],a*s1/tot,[a,1-a]))
    if grade==11:
        if bab==1:
            if code=='A':
                u=r.randint(0,4);v=u+r.randint(12,20);k=u+2;scale=r.choice([2,3]);shift=r.randint(-4,4);hole=scale*r.randint(3,4)+shift;lo=-3;hi=15;g=scale*x+shift
                guards=[s.Piecewise((0,g>=u),(1,True)),s.Piecewise((0,g<=v),(1,True)),s.Piecewise((0,g>k),(1,True)),s.Piecewise((0,s.Ne(g,hole)),(1,True))];vals=[j for j in range(lo,hi+1) if u<=scale*j+shift<=v and scale*j+shift>k and scale*j+shift!=hole]
                if level=='medium':return constant(rf'Tentukan banyak x bilangan bulat dalam [{lo},{hi}] agar $\sqrt{{{scale}x+({shift-k})}}$ terdefinisi pada bilangan real.',sum(scale*j+shift-k>=0 for j in range(lo,hi+1)),f'Syarat {scale}x+({shift-k})≥0; hitung bilangan bulat dalam interval yang memenuhi.','v2_domain_akar_interval',level)
                return checked(rf'Diketahui $f(t)=\sqrt{{(t-{u})({v}-t)}}/((t-{hole})\sqrt{{t-{k}}})$ dan $g(x)={scale}x+({shift})$. Tentukan jumlah seluruh x bilangan bulat pada [{lo},{hi}] yang berada dalam domain real $f\circ g$.',sum(vals),f'Akar pembilang mensyaratkan {u}≤g≤{v}; akar penyebut mengharuskan g>{k}; faktor penyebut lain mengecualikan g={hole}. Iris semua kendala, diperoleh x={vals}; jumlah {sum(vals)}.','v2_domain_komposisi_irisan',level,finite(['x'],[[lo,hi]],guards,x,'sum'))
            if code=='B':
                aa=A;bb=B;cc=C;d0=aa*cc+bb;d1=aa*(1+cc)+bb;e0=bb*bb+cc;query=(a*T+b)**2+c
                return checked(rf'Fungsi $f(x)=ax+b$, $g(x)=x^2+c$ dengan a,b,c>0 memenuhi $(f\circ g)(0)={d0}$, $(f\circ g)(1)={d1}$, dan $(g\circ f)(0)={e0}$. Tentukan $(g\circ f)({T})$.',query.subs({a:aa,b:bb,c:cc}),f'Selisih dua data pertama memberi a={aa}. Kemudian ac+b={d0}, b²+c={e0}. Eliminasi dan syarat positif memberi b={bb}, c={cc}. Hitung (a×{T}+b)²+c, hasil {query.subs({a:aa,b:bb,c:cc})}.','v2_komposisi_tiga_parameter',level,system(['a','b','c'],[a*c+b-d0,a*(1+c)+b-d1,b*b+c-e0],query,[a,b,c]))
            if A*C==B:B+=1
            K=A+r.choice([1,2,3]);vals=[s.Rational(A*j+B,j+C) for j in [0,1,2]];query=(b-K*c)/(K-a)
            return checked(rf'Fungsi invertibel $f(x)=(ax+b)/(x+c)$ memenuhi f(0)={m(vals[0])}, f(1)={m(vals[1])}, f(2)={m(vals[2])}. Tentukan $f^{{-1}}({K})$.',s.Rational(B-K*C,K-A),f'Kalikan penyebut di tiga data untuk memperoleh SPL tiga parameter. Hasil a={A}, b={B}, c={C}. Dari y=(ax+b)/(x+c), invers x=(b-yc)/(y-a). Masukkan y={K}, hasil {s.Rational(B-K*C,K-A)}.','v2_invers_mobius_rekonstruksi',level,system(['a','b','c'],[a*j+b-vals[j]*(j+c) for j in range(3)],query))
        if bab==2:
            if code=='A':
                theta=r.choice([s.pi/3,s.pi/2,2*s.pi/3]);inner=U;diff=A;area=((inner+diff)**2-inner**2)*theta/2
                if level=='medium':return constant(rf'Busur lingkaran berjari-jari r dengan sudut pusat 60° panjangnya {m(inner*s.pi/3)} cm. Tentukan panjang busur 150° pada lingkaran itu.',inner*5*s.pi/6,f'L=rπ/3 memberi r={inner}. Busur 150°=5rπ/6={s.latex(inner*5*s.pi/6)}.','v2_busur_radius_inverse',level)
                return checked(rf'Dua juring sepusat mempunyai sudut pusat sama kurang dari satu putaran. Selisih jari-jari {diff} cm, selisih panjang busur {m(diff*theta)} cm, dan selisih luas {m(area)} cm². Tentukan keliling juring luar.',(inner+diff)*(theta+2),f'Jika radius dalam r dan sudut θ radian, beda busur {diff}θ menentukan θ={theta}. Selisih luas ((r+{diff})²-r²)θ/2={area} memberi r={inner}. Keliling luar (r+{diff})θ+2(r+{diff})={s.latex((inner+diff)*(theta+2))}.','v2_juring_sepusat_inverse',level,system(['a','b'],[diff*b-diff*theta,((a+diff)**2-a*a)*b/2-area],(a+diff)*(b+2),[a,b]))
            if code=='B':
                small=r.randint(2,6);large=small+r.randint(2,7);dist=large+small+r.randint(2,7);le=s.sqrt(dist*dist-(large-small)**2);li=s.sqrt(dist*dist-(large+small)**2)
                return checked(rf'Dua lingkaran berpusat berjarak {dist} cm. Garis singgung persekutuan luar panjangnya {m(le)} cm dan dalam {m(li)} cm. Tentukan selisih jari-jari terbesar dan setengah jari-jari terkecil.',large-s.Rational(small,2),f'Pythagoras memberi (R-r)²={dist**2}-{s.latex(le**2)} dan (R+r)²={dist**2}-{s.latex(li**2)}. Karena R>r>0, akar positif menentukan R={large}, r={small}. Hasil R-r/2={large-s.Rational(small,2)}.','v2_dua_singgung_rekonstruksi',level,system(['a','b'],[(a-b)**2-dist*dist+le**2,(a+b)**2-dist*dist+li**2],a-b/2,[a-b,b]))
            u=r.randint(2,6);v=u+r.randint(2,6);k=s.Rational(u+v,2);d=s.Rational(u*v,k);S=2*(u+v)
            return checked(rf'Tali busur AB dan CD berpotongan di X. Diketahui AX=x, XB={S}-x, CX=2x+{m(d)}, dan DX={m(k)}, semua panjang dalam cm. Jika AX<DX, tentukan panjang CD.',2*u+d+k,f'Teorema dua tali busur: x({S}-x)={k}(2x+{d}). Akar persamaan x={u} atau {v}. Syarat x<{k} memilih {u}. Jadi CD=2x+{d}+{k}={2*u+d+k}.','v2_tali_busur_cabang_akar',level,system(['a'],[a*(S-a)-k*(2*a+d)],2*a+d+k,[k-a,2*a+d,a]))
        # Statistics: exact reconstruction from summary constraints.
        xs=[0,1,2,4];ys=[r.randint(2,8),r.randint(8,14),r.randint(12,18),r.randint(19,27)];mx=s.Rational(sum(xs),4);ssx=sum((j-mx)**2 for j in xs);my=s.Rational(sum(ys),4);cov=sum((j-mx)*(v-my) for j,v in zip(xs,ys));slope=cov/ssx
        if code=='A':
            if level=='medium':return constant(f'Diagram pencar memperlihatkan titik ({U},{A}) dan ({U+B},{A+2*B}); taksiran linear memakai garis melalui dua titik ini. Berapa taksiran y pada x={U+B+C}?',A+2*(B+C),f'Gradien selisih y/selisih x=2. Dari titik pertama, y={A}+2(x-{U}); substitusi memberi {A+2*(B+C)}.','v2_pencar_interpolasi',level)
            left=[(j,A+2*j) for j in range(3)];right=[(j+U+5,A-10+2*j) for j in range(3)];allpts=left+right
            def covariance(pts):return sum((s.Rational(p[0])-s.Rational(sum(t[0] for t in pts),len(pts)))*(s.Rational(p[1])-s.Rational(sum(t[1] for t in pts),len(pts))) for p in pts)
            signs=[covariance(left)>0,covariance(right)>0,covariance(allpts)<0,False];flips=[r.choice([True,False]) for _ in range(4)];truths=[v if f else not v for v,f in zip(signs,flips)];claims=[f'kovarians kelompok I {">0" if flips[0] else "<0"}',f'kovarians kelompok II {">0" if flips[1] else "<0"}',f'kovarians gabungan {"<0" if flips[2] else ">0"}',('korelasi saja membuktikan sebab-akibat' if flips[3] else 'korelasi saja belum membuktikan sebab-akibat')];value=sum(bool(v) for v in truths)
            cert=system(['a','b','c'],[a-covariance(left),b-covariance(right),c-covariance(allpts)],s.Piecewise((1,a>0 if flips[0] else a<0),(0,True))+s.Piecewise((1,b>0 if flips[1] else b<0),(0,True))+s.Piecewise((1,c<0 if flips[2] else c>0),(0,True))+(0 if flips[3] else 1))
            return checked(f'Data pencar kelompok I: {left}; kelompok II: {right}. Periksa empat pernyataan berikut: '+ '; '.join(claims)+'. Berapa pernyataan yang benar?',value,f'Jumlah hasil kali simpangan pada dua kelompok dan gabungan berturut-turut {covariance(left)}, {covariance(right)}, {covariance(allpts)}. Tandanya harus dihitung per kelompok dan gabungan; korelasi tidak cukup membuktikan kausalitas. Kebenaran pernyataan {list(map(bool,truths))}; jumlah {value}.','v2_pencar_efek_penggabungan',level,cert)
        if code=='B':
            variable_y=[ys[0],ys[1],ys[2],a];mean_y=sum(variable_y)/4;cov_expr=sum((j-mx)*(v-mean_y) for j,v in zip(xs,variable_y));at=r.randint(5,10);query=mean_y-slope*mx+slope*at
            return checked(f'Empat titik data adalah {list(zip(xs[:3],ys[:3]))} dan (4,t). Regresi kuadrat terkecil y atas x mempunyai gradien {m(slope)}. Tentukan taksiran y saat x={at}.',my+slope*(at-mx),f'Rata-rata x={mx}, jumlah kuadrat simpangan x={ssx}. Syarat gradien menentukan t={ys[3]}. Rata-rata y={my}; intersep ȳ-mx̄={my-slope*mx}. Taksiran pada x={at} adalah {my+slope*(at-mx)}.','v2_regresi_data_hilang',level,system(['a'],[cov_expr-slope*ssx],query))
        if level=='medium':
            p=r.randint(3,6);q=r.randint(7,9);return constant(f'Dua studi memiliki koefisien korelasi {m(s.Rational(p,10))} dan {m(s.Rational(q,10))}. Berapa selisih koefisien determinasi studi kedua dan pertama dalam poin persentase?',q*q-p*p,f'Koefisien determinasi 100r². Selisih {q*q}-{p*p}={q*q-p*p} poin persentase.','v2_determinasi_perbandingan',level)
        variable_y=[ys[0],ys[1],ys[2],a];mean_y=sum(variable_y)/4;cx=sum((j-mx)*(v-mean_y) for j,v in zip(xs,variable_y));sy=sum((v-mean_y)**2 for v in variable_y);r2=s.factor(cov**2/(ssx*sum((v-my)**2 for v in ys)));guard=s.Piecewise((0,cx>0),(1,True));equation=s.factor(cx**2-r2*ssx*sy);values=[j for j in range(31) if equation.subs(a,j)==0 and cx.subs(a,j)>0]
        return checked(f'Empat pasangan data adalah {list(zip(xs[:3],ys[:3]))} dan (4,t), dengan t bilangan bulat dari 0 sampai 30. Korelasi Pearson positif dan kuadratnya {m(r2)}. Tentukan jumlah semua nilai t yang mungkin.',sum(values),f'Hitung Sxx={ssx}, Sxy(t), dan Syy(t) menggunakan rata-rata yang juga bergantung t. Persamaan Sxy²={r2} Sxx Syy disertai Sxy>0 memberi kandidat {values}. Jumlahnya {sum(values)}.','v2_korelasi_inverse_cabang',level,finite(['a'],[[0,30]],[equation,guard],a,'sum'))
    if grade==12:
        if bab==1:return arithmetic(r) if code=='A' else interest(r)
        if bab==2:
            if code=='A':return interest(r,True)
            if code=='B':
                factor=s.Rational(r.randint(11,14),10);P=r.randint(10,50)*100000;D=r.randint(2,8)*100000;M2=P*factor**2;M4=P*factor**4+D*factor
                if level=='medium':return constant(f'Deposito berbunga majemuk {m(100*(factor-1))}% per tahun. Awal tahun 0 disetor {rp(P)} dan tepat akhir tahun 1 ditambah {rp(D)}. Berapa saldo akhir tahun 3 dalam rupiah?',P*factor**3+D*factor**2,f'Setoran awal bertumbuh 3 tahun, tambahan 2 tahun: {P}×({factor})³+{D}×({factor})²={P*factor**3+D*factor**2}.','v2_majemuk_dua_setoran',level)
                return checked(f'Rekening majemuk memiliki faktor tahunan f>1 dan modal awal P. Saldo akhir tahun 2 adalah {m(M2)} rupiah. Tepat akhir tahun 3 ditambah {rp(D)}, lalu saldo akhir tahun 4 menjadi {m(M4)} rupiah. Tidak ada transaksi lain. Tentukan modal awal P dalam rupiah.',P,f'Gunakan saldo tahun 2 sebagai dasar: {M4}={M2}f²+{D}f. Akar f>1 adalah {factor}. Kemudian P={M2}/f²={P}.','v2_majemuk_modal_faktor_inverse',level,system(['a','b'],[a*b*b-M2,M2*b*b+D*b-M4],a,[a,b-1]))
            rate=s.Rational(r.randint(1,4),20);P=U*100000;D=A*10000;n=r.randint(2,4)
            if code=='C':return constant(rf'Setoran {rp(D)} dilakukan tiap akhir tahun selama {n} tahun, bunga {m(rate*100)}% per tahun. Gunakan langsung rumus $S=D((1+i)^n-1)/i$. Tentukan S dalam rupiah.',D*((1+rate)**n-1)/rate,f'Substitusi D={D}, i={rate}, n={n} memberi S={D*((1+rate)**n-1)/rate}.','v2_anuitas_rumus_terpandu',level)
            if code=='D':return constant(f'Utang {rp(P)} berbunga majemuk {m(rate*100)}% per tahun. Tepat akhir tahun 1 dibayar {rp(D)}. Tanpa pembayaran lain, berapa sisa utang akhir tahun 3?',(P*(1+rate)-D)*(1+rate)**2,f'Akhir tahun pertama utang {P*(1+rate)}, setelah bayar {P*(1+rate)-D}. Majemukkan sisa dua tahun: {(P*(1+rate)-D)*(1+rate)**2}.','v2_utang_majemuk_pembayaran',level)
            S=P*(1+2*rate);M=P*(1+rate)**2;query=a*((1+b)**3-(1+3*b))
            return checked(f'Modal sama P ditawarkan dalam dua skema dengan suku bunga tahunan sama r>0. Skema bunga tunggal bernilai {m(S)} rupiah setelah 2 tahun, sedangkan majemuk tahunan {m(M)} rupiah. Tentukan selisih saldo majemuk dan tunggal setelah 3 tahun, dalam rupiah.',P*((1+rate)**3-(1+3*rate)),f'Susun P(1+2r)={S}, P(1+r)²={M}. Selesaikan dengan P>0,r>0: P={P}, r={rate}. Selisih tahun ketiga P[(1+r)³-(1+3r)]={P*((1+rate)**3-(1+3*rate))}.','v2_parameter_dua_skema_bunga',level,system(['a','b'],[a*(1+2*b)-S,a*(1+b)**2-M],query,[a,b]))
        if bab==3:
            if code=='A':
                digits=[0,*sorted(r.sample(range(1,10),5))];threshold=r.randint(2,7)*1000
                if level=='medium':return constant(f'Dari angka {digits}, dibentuk bilangan tiga angka tanpa pengulangan. Berapa banyak bilangan yang dapat dibuat?',5*5*4,'Digit pertama ada 5 pilihan bukan nol, kedua 5 pilihan tersisa termasuk nol, ketiga 4 pilihan. Hasil 100.','v2_aturan_tempat_nol',level)
                valid=[v for v in permutations(digits,4) if v[0]!=0 and v[-1]%2==0 and int(''.join(map(str,v)))>threshold];counts={j:sum(v[-1]==j for v in valid) for j in digits if j%2==0};cert={'type':'digit_arrangements','digits':digits,'length':4,'threshold':threshold}
                return checked(f'Dari angka {digits}, dibentuk bilangan genap empat angka tanpa pengulangan yang lebih besar dari {threshold}. Berapa banyak bilangan yang memenuhi?',len(valid),f'Pisahkan berdasarkan angka terakhir yang genap. Larang nol di depan, larang pengulangan, dan periksa batas ribuan. Jumlah menurut digit terakhir: {counts}. Total {len(valid)}.','v2_aturan_tempat_batas_genap',level,cert)
            men=r.randint(4,7);women=r.randint(4,7);k=r.randint(4,6)
            if level=='easy':
                if code=='C':return constant(f'Dari {men+women} peserta berbeda dipilih dua anggota tim tanpa jabatan. Berapa cara memilih?',s.binomial(men+women,2),f'Tanpa urutan gunakan C({men+women},2)={s.binomial(men+women,2)}.','v2_kombinasi_pasangan',level)
                n=r.randint(15,50)
                return constant(f'Dari {n} siswa dipilih seorang ketua dan seorang wakil yang berbeda. Berapa susunan jabatan?',n*(n-1),f'Pilihan ketua {n}, wakil {n-1}. Hasil {n*(n-1)}.','v2_permutasi_dua_jabatan',level)
            cert={'type':'committee','men':men,'women':women,'size':k,'mode':'restricted' if code=='C' else 'two_female_officers'}
            if code=='C':
                value=sum(s.binomial(women,j)*(s.binomial(men,k-j)-(s.binomial(men-2,k-j-2) if k-j>=2 else 0)) for j in range(2,min(k,women)+1) if 0<=k-j<=men)
                return checked(f'Tim {k} orang dipilih dari {men} laki-laki dan {women} perempuan. Tim harus memuat sedikitnya dua perempuan; dua laki-laki tertentu A dan B tidak boleh bersama dalam tim. Berapa tim yang memenuhi?',value,'Pisahkan menurut jumlah perempuan j≥2. Untuk tiap j, hitung C(perempuan,j)×C(laki-laki,k-j), lalu kurangi tim yang memuat A dan B sekaligus dengan memilih anggota laki-laki sisanya dari selain A,B. Jumlah seluruh kasus memberi '+str(value)+'.','v2_kombinasi_batas_larangan',level,cert)
            value=women*(women-1)*(s.binomial(men+women-2,k-2)-s.binomial(women-2,k-2))
            return checked(f'Sebuah tim {k} orang dari {men} laki-laki dan {women} perempuan memiliki ketua dan wakil. Keduanya harus perempuan dan tim harus memiliki setidaknya seorang laki-laki. Berapa susunan tim beserta jabatannya?',value,f'Pilih dua pejabat perempuan berurutan: {women}×{women-1}. Dari sisa pilih {k-2} anggota; kurangi pilihan yang semuanya perempuan. Hasil {women}×{women-1}[C({men+women-2},{k-2})-C({women-2},{k-2})]={value}.','v2_kombinasi_jabatan_komplemen',level,cert)
        red=r.randint(3,8);blue=r.randint(3,8)
        if code=='B':
            p=s.Rational(A,10);q=s.Rational(B,10);return constant(f'Kejadian A dan B saling bebas, dengan P(A)={m(p)} dan P(B)={m(q)}. Tentukan peluang keduanya terjadi.',p*q,f'Karena bebas, P(A∩B)=P(A)P(B)={p*q}.','v2_kejadian_bebas_langsung',level)
        value=s.binomial(red,2)*blue/(s.binomial(red+blue,3)-s.binomial(blue,3));cert={'type':'conditional_urn','red':red,'blue':blue}
        return checked(f'Dari {red} bola merah dan {blue} biru, tiga bola diambil sekaligus secara acak. Diketahui sedikitnya satu bola merah terambil. Berapa peluang tepat dua bola merah terambil?',value,f'Banyak pilihan bersyarat C({red+blue},3)-C({blue},3). Pilihan tepat dua merah C({red},2)×{blue}. Rasio keduanya {value}.','v2_peluang_kombinasi_bersyarat',level,cert)
    raise ValueError((grade,bab,code,level))
