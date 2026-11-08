"""Reviewed direct and linked SMA/TL exercises for the three-session round.

Each operation is an authored content family. Requested stock and target labels
are never inputs to assessment. Certificates preserve all visible parameters and
the mathematical expression, rather than storing a claimed answer as a constant.
"""
from copy import deepcopy
import sympy as s

from .replenishment_math import m

POLICY = 'codex-session-sma-content-v1'
BASES = set('''exponent_definition exponent_rules exponential_model radicals
arithmetic_term arithmetic_sum interest trig_ratio trig_application linear_system
linear_inequality quadratic_equation quadratic_function histogram mean spread
distribution probability_union probability_product function composition inverse
arc tangent chord scatter regression correlation compound annuity compound_loan
loan_annuity financial_parameter counting permutation combination mixed_counting
single_probability joint_probability matrix_types matrix_equal matrix_sum
matrix_product matrix_inverse polynomial_value polynomial_product polynomial_remainder
polynomial_factor polynomial_identity unit_circle trig_graph trig_identity sine_rule
cosine_rule vector dot_product vector_proof cartesian_transform matrix_transform
composed_transform logarithm algebraic_function nonalgebraic_function circle ellipse
circle_position circle_tangent derivative_definition derivative_rules stationary
derivative_application indefinite_integral definite_integral integral_area random_variable
discrete_variable continuous_variable probability_function density binomial normal'''.split())


def solve(cert):
    if cert['type'] != 'session_sma_expression':
        raise ValueError('Unknown session SMA certificate')
    values={key:s.sympify(value) for key,value in cert['inputs'].items()}
    functions={'sqrt':s.sqrt,'pi':s.pi,'sin':s.sin,'cos':s.cos,'tan':s.tan,
               'log':s.log,'binomial':s.binomial,'factorial':s.factorial,
               'Max':s.Max,'Min':s.Min,'Abs':s.Abs,'Piecewise':s.Piecewise,'Eq':s.Eq}
    expression=s.sympify(cert['expression'],locals={**functions,**{key:s.Symbol(key) for key in values}})
    result=s.simplify(expression.subs({s.Symbol(key):value for key,value in values.items()}))
    if result.free_symbols or result.is_real is not True or result.is_finite is not True:
        raise ValueError('Mathematical query is not a finite real value')
    return result


def assess(model,grade):
    kind=model['kind'];prefix='session_sma_'
    if not kind.startswith(prefix):raise ValueError('Unreviewed SMA session family')
    operation=kind[len(prefix):];base,tier=operation.rsplit('_',1)
    if base not in BASES or tier not in {'direct','linked','reconstruct'}:
        raise ValueError('Unreviewed SMA operation')
    cert=model['certificate']
    if cert['operation'] != operation:raise ValueError('Content family and certificate disagree')
    value=solve(cert)
    level={'direct':'easy','linked':'medium','reconstruct':'hard'}[tier]
    flags=[]
    if tier=='linked' and base in {'radicals','exponential_model','probability_union'}:
        # Explicitly avoid degenerate subtraction instances with no real work.
        if value==0:
            level='easy';flags.append('cancelling_instance')
    return {'assessedLevel':level,'reason':
            ('Satu definisi atau prosedur langsung dalam materi kelas sasaran.' if level=='easy' else
             'Menghubungkan data dengan parameter, batas, atau hasil antara sebelum menghitung kuantitas yang diminta.' if level=='medium' else
             'Merekonstruksi parameter tersembunyi dari beberapa kendala, memilih cabang yang sah, lalu memakai model untuk besaran baru.'),
            'steps':{'easy':1,'medium':3,'hard':5}[level],'policyVersion':POLICY,'confidenceScore':0,
            'confidenceMeasured':False,'apiCalls':0,'flags':flags}


def _plain(value):
    value=s.sympify(value)
    return int(value) if value.is_Integer else str(value)


def _make(base,tier,question,inputs,expression,explanation,visual,labels=None,probability=False):
    data={key:_plain(value) for key,value in inputs.items()}
    operation=base+'_'+tier
    cert={'type':'session_sma_expression','operation':operation,'inputs':data,'expression':str(expression)}
    value=solve(cert)
    proposals=([1-value,value/2,(value+1)/2,value**2,s.Rational(1,3),s.Rational(2,3),s.Rational(1,4),s.Rational(3,4)]
               if probability else [value+1,value-1,value*2,value/2,value+2,-value,value+3])
    wrong=[]
    for candidate in proposals:
        candidate=s.simplify(candidate)
        if not candidate.is_real or not candidate.is_finite or candidate==value or candidate in wrong:continue
        if probability and not 0<=candidate<=1:continue
        wrong.append(candidate)
        if len(wrong)==3:break
    if len(wrong)!=3:raise ValueError('Not enough distinct admissible options')
    labels=labels or {}
    scene=None
    if visual:
        rows=[[labels.get(key,key),value] for key,value in data.items()]
        scene={'kind':'table','headers':['Besaran','Nilai'],'rows':rows,'title':'Data untuk soal'}
        cert['visual_bindings']=[{'input':key,'path':['rows',i,1]} for i,key in enumerate(data)]
        stem='Gunakan data pada tabel. '+question
    else:
        facts='; '.join((labels.get(key,key)+' = '+m(s.sympify(value))) for key,value in data.items())
        stem='Diketahui '+facts+'. '+question
    model={'question':stem,'answer':m(value),'wrong':list(map(m,wrong)),
           'explanation':explanation+' Hasilnya '+m(value)+'.',
           'kind':'session_sma_'+operation,'scene':scene,'visual_kind':'math_scene' if visual else None,
           'certificate':cert}
    decision=assess(model,10);model.update(assessment=decision,steps=decision['steps'],rationale=decision['reason'])
    return model


def check_visual(model):
    if not model.get('scene'):return {'status':'text_question'}
    from .math_scene_visuals import validate_scene
    validate_scene(model['scene']);cert=model['certificate'];original=solve(cert);passed=[]
    for binding in cert['visual_bindings']:
        key=binding['input'];i=binding['path'][1]
        if s.sympify(model['scene']['rows'][i][1])!=s.sympify(cert['inputs'][key]):
            raise ValueError('Visible data and arithmetic certificate disagree')
        for delta in (1,-1,2):
            changed=deepcopy(cert);changed['inputs'][key]=_plain(s.sympify(cert['inputs'][key])+delta)
            try:new=solve(changed)
            except (ValueError,ZeroDivisionError):continue
            if new!=original:
                scene=deepcopy(model['scene']);scene['rows'][i][1]=changed['inputs'][key];validate_scene(scene)
                passed.append(key);break
    if not passed:raise ValueError('Image supplies no pivotal facts')
    return {'status':'verified_locally','pivotalInputs':passed}


def generate(name,bab,code,level,r,visual,index):
    """Return an approved easy/medium recipe; higher-level hard routing is external."""
    if level=='hard':return _hard_missing(name,bab,code,r,visual)
    if level not in {'easy','medium'}:return None
    grade=int(name[5:].split('_')[0]);tl=name.endswith('_tl');tier='direct' if level=='easy' else 'linked'
    a=r.randint(2,12);b=r.randint(2,13);c=r.randint(1,11);d=r.randint(2,12);t=r.randint(2,9);n=r.randint(3,12)
    make=lambda base,q,data,expr,why,**kw:_make(base,tier,q,data,expr,why,visual,**kw)
    if not tl and grade in (10,12) and ((grade==10 and bab==2) or (grade==12 and bab==1)):
        if code=='A':
            if level=='easy':return make('arithmetic_term','Barisan aritmetika mempunyai suku pertama $a$ dan beda $d$. Tentukan suku ke-$n$.',{'a':a,'d':d,'n':n},'a+(n-1)*d','Gunakan rumus suku ke-n barisan aritmetika.')
            p=r.randint(2,5);q=p+r.randint(2,6);u=a+(p-1)*d;v=a+(q-1)*d
            return make('arithmetic_term','Barisan aritmetika memenuhi $U_p=u$ dan $U_q=v$. Tentukan $U_n$.',{'p':p,'q':q,'u':u,'v':v,'n':q+r.randint(2,7)},'u+(n-p)*(v-u)/(q-p)','Tentukan beda dari dua suku yang diketahui, kemudian lanjutkan ke indeks yang diminta.')
        if code=='B':
            if level=='easy':return make('arithmetic_sum','Barisan aritmetika mempunyai suku pertama $a$ dan beda $d$. Hitung jumlah $n$ suku pertamanya.',{'a':a,'d':d,'n':n},'n*(2*a+(n-1)*d)/2','Gunakan jumlah deret aritmetika.')
            p=r.randint(2,5);q=p+r.randint(2,6)
            return make('arithmetic_sum','Barisan aritmetika memenuhi $U_p=u$ dan $U_q=v$. Hitung jumlah $n$ suku pertama.',{'p':p,'q':q,'u':a+(p-1)*d,'v':a+(q-1)*d,'n':q+r.randint(2,7)},'n*(2*(u-(p-1)*(v-u)/(q-p))+(n-1)*(v-u)/(q-p))/2','Cari beda dan suku pertama dari dua data, lalu gunakan rumus jumlah deret.')
        return _finance('interest',tier,r,visual)
    if not tl and grade==12 and bab==2:
        return _finance({'A':'interest','B':'compound','C':'annuity','D':'compound_loan','E':'loan_annuity','F':'financial_parameter'}[code],tier,r,visual)
    if not tl and grade==10:
        if bab==1:
            if code=='A':
                if level=='easy':return make('exponent_definition','Menurut definisi eksponen, berapa nilai $a^n$?',{'a':a,'n':r.randint(2,7)},'a**n','Eksponen n berarti mengalikan a dengan dirinya sebanyak n faktor.')
                return make('exponent_definition','Gunakan definisi eksponen untuk menghitung $a^p+a^{p+q}$.',{'a':a,'p':r.randint(2,4),'q':r.randint(1,3)},'a**p+a**(p+q)','Nyatakan pangkat kedua dari hasil pangkat pertama, kemudian jumlahkan.')
            if code=='B':
                if level=='easy':return make('exponent_rules','Jika $a^p a^q=a^k$ dengan $a>1$, tentukan $k$.',{'a':a,'p':b,'q':c},'p+q','Perkalian bilangan berpangkat dengan basis sama menjumlahkan eksponennya.')
                return make('exponent_rules','Jika $(a^p)^q/a^r=a^k$ dengan $a>1$, tentukan $k$.',{'a':a,'p':b,'q':c,'r':d},'p*q-r','Gabungkan aturan pangkat dari pangkat dengan aturan pembagian.')
            if code=='C':
                if level=='easy':return make('exponential_model','Populasi mula-mula $P$ dan menjadi $a$ kali setiap periode. Berapa populasinya setelah $t$ periode?',{'P':a*100,'a':r.randint(2,4),'t':r.randint(2,5)},'P*a**t','Gunakan model pertumbuhan eksponensial.')
                return make('exponential_model','Dua kultur mula-mula berisi $P$ dan $Q$ organisme. Kultur pertama berlipat $a$ dan kedua berlipat $b$ setiap periode. Berapa selisih mutlak populasinya setelah $t$ periode?',{'P':a*100,'Q':b*100,'a':2,'b':3,'t':r.randint(2,5)},'Abs(P*a**t-Q*b**t)','Hitung perkembangan kedua kultur secara terpisah, lalu bandingkan hasilnya.')
            data={'a':a,'b':b,'c':c,'d':r.choice([2,3,5,6,7])}
            if level=='easy':return make('radicals',r'Sederhanakan $\sqrt{a^2d}$.',{'a':a,'d':data['d']},'a*sqrt(d)','Keluarkan faktor kuadrat sempurna dari akar.')
            return make('radicals',r'Sederhanakan $\sqrt{a^2d}-\sqrt{b^2d}+\sqrt{c^2d}$.',data,'(a-b+c)*sqrt(d)','Sederhanakan masing-masing akar menjadi suku sejenis, kemudian gabungkan koefisiennya.')
        if bab==3:
            if code=='A':
                u=r.randint(3,12);v=r.randint(1,u-1);legs={'p':u*u-v*v,'q':2*u*v,'h':u*u+v*v}
                return make('trig_ratio',r'Segitiga siku-siku mempunyai sisi depan sudut $\theta$ sebesar $p$, sisi samping $q$, dan sisi miring $h$. Tentukan '+(r'$\sin\theta$.' if level=='easy' else r'$\sin\theta+\cos\theta$.'),legs,'p/h' if level=='easy' else '(p+q)/h','Gunakan perbandingan sisi depan dan samping terhadap sisi miring.')
            angle=r.choice([30,45,60])
            if level=='easy':return make('trig_application',r'Pengamat di tanah melihat puncak menara dengan sudut elevasi $\theta$ derajat dan jarak mendatar $d$ meter. Berapa tinggi menara?',{'theta':angle,'d':a*3},'d*tan(pi*theta/180)','Perbandingan tangen menghubungkan tinggi dengan jarak mendatar.')
            return make('trig_application',r'Tinggi menara $h$ meter dan tinggi mata pengamat $e$ meter. Sudut elevasi dari mata ke puncak adalah $\theta$ derajat. Berapa jarak mendatar pengamat ke menara?',{'theta':angle,'h':a*4,'e':r.randint(1,3)},'(h-e)/tan(pi*theta/180)','Tentukan selisih tinggi terhadap mata, lalu gunakan perbandingan tangen.')
        if bab==4:
            if code=='A':
                if level=='easy':return make('linear_system','Sistem memenuhi $x+y=u$ dan $x-y=v$. Tentukan $x$.',{'u':a+b,'v':a-b},'(u+v)/2','Jumlahkan kedua persamaan lalu bagi dua.')
                return make('linear_system',r'Sistem memenuhi $x+ay=u$ dan $x+by=v$ dengan $a\ne b$. Tentukan $xy$.',{'a':a,'b':a+r.randint(1,6),'u':c+a*d,'v':c+(a+r.randint(7,9))*d},'((v-u)/(b-a))*(u-a*(v-u)/(b-a))','Eliminasi x untuk mencari y, substitusikan untuk mencari x, lalu hitung hasil kali.')
            if level=='easy':return make('linear_inequality',r'Daerah memenuhi $ax+by\le C$ dan $x,y\ge0$. Pada $y=0$, berapa $x$ terbesar?',{'a':a,'b':b,'C':a*c},'C/a','Pada sumbu x, substitusikan y=0 ke batas pertidaksamaan.')
            return make('linear_inequality',r'Untuk $x,y\ge0$ dan $ax+by\le C$, tentukan nilai maksimum $px+qy$.',{'a':a,'b':b,'C':a*b*c,'p':d,'q':r.randint(2,15)},'Max(p*C/a,q*C/b)','Daerah layak berbentuk segitiga; bandingkan fungsi tujuan pada kedua titik potong sumbu dan titik asal.')
        if bab==5:
            if code=='A':
                roots={'a':1,'b':-(a+b),'c':a*b}
                if level=='easy':return make('quadratic_equation','Akar $ax^2+bx+c=0$ adalah $p,q$. Tentukan $p+q$.',roots,'-b/a','Gunakan hubungan jumlah akar dengan koefisien.')
                return make('quadratic_equation','Akar $ax^2+bx+c=0$ adalah $p,q$. Tentukan $(p-q)^2$ tanpa mencari akar satu per satu.',roots,'(b*b-4*a*c)/(a*a)','Hubungkan jumlah dan hasil kali akar melalui identitas selisih kuadrat.')
            if level=='easy':return make('quadratic_function','Untuk $a>0$, tentukan nilai minimum $f(x)=a(x-h)^2+k$.',{'a':a,'h':b,'k':r.randint(-15,15)},'k','Kuadrat bernilai minimum nol pada titik puncak.')
            return make('quadratic_function','Untuk $a>0$, absis titik puncak $f(x)=ax^2+bx+c$ adalah $x_v$. Tentukan $f(x_v+t)$.',{'a':a,'b':-2*a*b,'c':c,'t':t},'c-b*b/(4*a)+a*t*t','Tentukan koordinat puncak, lalu gunakan bentuk kuadrat sempurna untuk mengevaluasi titik yang berjarak t dari puncak.')
        if bab==6:
            if code=='A':
                if level=='easy':return make('histogram','Sebuah kelas histogram berfrekuensi $f$ dan lebar $w$. Tentukan densitas frekuensinya.',{'f':a*b,'w':b},'f/w','Densitas frekuensi adalah frekuensi dibagi lebar kelas.')
                return make('histogram','Dua kelas histogram yang bersebelahan berfrekuensi $f,g$ dengan lebar $u,v$. Jika digabung, berapa densitas frekuensi kelas baru?',{'f':a*b,'g':c*d,'u':b,'v':d},'(f+g)/(u+v)','Gabungkan frekuensi dan lebar interval terlebih dahulu, kemudian hitung densitas baru.')
            if code=='B':
                if level=='easy':return make('mean','Tentukan rata-rata tiga data $a,b,c$.',{'a':a,'b':b,'c':c},'(a+b+c)/3','Rata-rata adalah jumlah data dibagi banyak data.')
                return make('mean','Sebanyak $n$ data mempunyai rata-rata $m$. Satu data baru ditambahkan sehingga rata-ratanya menjadi $q$. Berapa data baru itu?',{'n':n,'m':a,'q':a+r.randint(1,5)},'(n+1)*q-n*m','Ubah kedua rata-rata menjadi jumlah data; selisih jumlah tersebut adalah data tambahan.')
            if level=='easy':return make('spread','Data memiliki nilai minimum $a$ dan maksimum $b$. Berapa jangkauannya?',{'a':a,'b':a+b},'b-a','Jangkauan adalah nilai maksimum dikurangi nilai minimum.')
            return make('spread','Kuartil pertama $Q1$ dan kuartil ketiga $Q3$ diberikan. Menurut aturan $1,5$ kali jangkauan antarkuartil, berapa pagar atas pencilan?',{'Q1':a,'Q3':a+b},'Q3+3*(Q3-Q1)/2','Hitung jangkauan antarkuartil, kemudian tambahkan satu setengah kalinya pada kuartil ketiga.')
        if bab==7:
            if code=='A':
                if level=='easy':return make('distribution','Kotak berisi $r$ bola merah dan $b$ bola biru. Berapa peluang bola merah dalam satu pengambilan acak?',{'r':a,'b':b},'r/(r+b)','Semua bola sama mungkin terpilih; bagi jumlah hasil yang sesuai dengan seluruh hasil.',probability=True)
                sides=r.randint(5,15);total=r.randint(3,sides+1)
                return make('distribution',r'Dua dadu adil masing-masing bernomor 1 sampai $n$ dilempar. Berapa peluang jumlah hasilnya tepat $s$? Data memenuhi $2\le s\le n+1$.',{'n':sides,'s':total},'(s-1)/(n*n)','Ada s-1 pasangan berurutan dengan jumlah s, dari n kuadrat pasangan yang sama mungkin.',probability=True)
            if code=='B':
                if level=='easy':return make('probability_union','Dalam $N$ siswa, $a$ mengikuti klub A dan $b$ mengikuti klub B. Kedua klub tidak beririsan. Berapa peluang siswa acak mengikuti A atau B?',{'N':4*(a+b),'a':a,'b':b},'(a+b)/N','Untuk kejadian saling lepas, jumlahkan peluang masing-masing.',probability=True)
                overlap=r.randint(1,min(a,b)-1)
                return make('probability_union','Dari $N$ siswa, $a$ mengikuti A, $b$ mengikuti B, dan $k$ mengikuti keduanya. Berapa peluang siswa acak tidak mengikuti kedua klub itu?',{'N':4*(a+b),'a':a,'b':b,'k':overlap},'(N-a-b+k)/N','Gunakan inklusi-eksklusi untuk gabungan, lalu ambil komplemennya.',probability=True)
            if level=='easy':return make('probability_product','Tersedia $a$ pilihan baju dan $b$ pilihan celana. Berapa pasangan satu baju dan satu celana yang mungkin?',{'a':a,'b':b},'a*b','Gunakan aturan perkalian untuk dua tahap pilihan.')
            return make('probability_product','Kotak berisi $r$ bola merah dan $b$ bola biru. Dua bola diambil berturut-turut tanpa pengembalian. Berapa peluang keduanya merah?',{'r':a,'b':b},'r*(r-1)/((r+b)*(r+b-1))','Setelah bola merah pertama diambil, perbarui pembilang dan penyebut untuk pengambilan kedua.',probability=True)
    if not tl and grade==11:
        if bab==1:
            if code=='A':
                if level=='easy':return make('function','Untuk $f(x)=ax+b$, tentukan $f(t)$.',{'a':a,'b':b,'t':t},'a*t+b','Substitusikan argumen ke aturan fungsi.')
                lo=a;hi=a+b;k=r.randint(lo,hi)
                return make('function',r'Fungsi $f(x)=\sqrt{x-L}\sqrt{U-x}/(x-k)$ didefinisikan pada bilangan real. Berapa banyak bilangan bulat dalam domainnya?',{'L':lo,'U':hi,'k':k},'U-L','Kedua akar memberi interval tertutup L sampai U, sedangkan penyebut mengeluarkan satu bilangan bulat k di dalam interval.')
            if code=='B':
                if level=='easy':return make('composition',r'Untuk $f(x)=ax+b$ dan $g(x)=cx+d$, tentukan $(f\circ g)(t)$.',{'a':a,'b':b,'c':c,'d':d,'t':t},'a*(c*t+d)+b','Hitung g(t), kemudian gunakan hasil itu sebagai masukan f.')
                return make('composition',r'Untuk $f(x)=ax+b$, $g(x)=cx+d$, dan $h(x)=x^2+k$, tentukan $(f\circ g\circ h)(t)$.',{'a':a,'b':b,'c':c,'d':d,'k':r.randint(1,8),'t':t},'a*(c*(t*t+k)+d)+b','Terapkan fungsi paling kanan dahulu, kemudian g dan f secara berurutan.')
            if level=='easy':return make('inverse','Fungsi $f(x)=ax+b$ memiliki invers. Tentukan $f^{-1}(y)$.',{'a':a,'b':b,'y':a*t+b},'(y-b)/a','Balikkan operasi penambahan lalu perkalian pada fungsi linear.')
            return make('inverse',r'Untuk $f(x)=ax+b$ dan $g(x)=cx+d$, tentukan $(g\circ f)^{-1}(y)$.',{'a':a,'b':b,'c':c,'d':d,'y':c*(a*t+b)+d},'((y-d)/c-b)/a','Balikkan komposisi dengan invers fungsi paling luar lebih dahulu.')
        if bab==2:
            if code=='A':
                if level=='easy':return make('arc',r'Lingkaran berjari-jari $r$ mempunyai busur dengan sudut pusat $t$ derajat. Berapa panjang busurnya dalam bentuk $\pi$?',{'r':a,'t':r.choice([30,45,60,72,90,120,135,150])},'2*pi*r*t/360','Ambil bagian t/360 dari keliling lingkaran.')
                return make('arc','Sebuah juring mempunyai jari-jari $r$ dan panjang busur $s$. Berapa luas juring tersebut?',{'r':a,'s':b*c},'r*s/2','Hubungkan panjang busur dengan sudut pusat; substitusi ke luas juring memberi setengah hasil kali jari-jari dan busur.')
            if code=='B':
                if level=='easy':return make('tangent','Jarak titik P ke pusat lingkaran adalah $d$ dan jari-jari lingkaran $r$. Tentukan panjang garis singgung dari P.',{'d':a+b,'r':a},'sqrt(d*d-r*r)','Jari-jari tegak lurus garis singgung; gunakan teorema Pythagoras.')
                return make('tangent','Dua lingkaran berjari-jari $r,s$ mempunyai jarak pusat $d$ dengan $d>r+s$. Berapa panjang ruas garis singgung persekutuan luarnya?',{'r':a,'s':b,'d':a+b+c},'sqrt(d*d-(r-s)**2)','Bentuk segitiga siku-siku dengan sisi tegak selisih jari-jari dan sisi miring jarak pusat.')
            if level=='easy':return make('chord','Tali busur AB dan CD berpotongan di X. Diketahui $AX=a$, $XB=b$, dan $CX=c$. Tentukan $XD$.',{'a':a,'b':b,'c':c},'a*b/c','Gunakan hasil kali ruas tali busur yang berpotongan.')
            return make('chord','Dua tali busur berpotongan di X. Panjang dua ruas pada tali busur pertama adalah $x$ dan $x+a$. Pada tali busur kedua panjang ruasnya $u$ dan $v$. Berapa panjang seluruh tali busur pertama?',{'a':a,'u':b,'v':c},'sqrt(a*a+4*u*v)','Hasil kali ruas memberi persamaan kuadrat x(x+a)=uv. Pilih akar positif lalu hitung 2x+a.')
        if bab==3:
            if code=='A':
                data={'x1':a,'y1':b,'x2':a+c,'y2':b+c*d}
                if level=='easy':return make('scatter','Dua titik pada pola linear tepat diberikan sebagai $(x1,y1)$ dan $(x2,y2)$. Tentukan gradien pola tersebut.',data,'(y2-y1)/(x2-x1)','Bandingkan perubahan ordinat dengan perubahan absis.')
                return make('scatter','Seluruh titik data terletak tepat pada satu garis. Dua di antaranya $(x1,y1)$ dan $(x2,y2)$. Berapa nilai $y$ yang diperkirakan ketika $x=t$?',{**data,'t':a+c+r.randint(2,9)},'y1+(t-x1)*(y2-y1)/(x2-x1)','Tentukan gradien dari dua titik, susun garis, lalu evaluasi pada absis baru.')
            if code=='B':
                if level=='easy':return make('regression',r'Garis regresi adalah $\hat y=ax+b$. Berapa prediksi $y$ ketika $x=t$?',{'a':a,'b':b,'t':t},'a*t+b','Substitusikan nilai prediktor ke garis regresi.')
                return make('regression',r'Garis regresi adalah $\hat y=ax+b$ dengan $a>0$. Berapa nilai $x$ yang menghasilkan prediksi $y=q$?',{'a':a,'b':b,'q':a*t+b},'(q-b)/a','Gunakan prediksi yang diketahui untuk membentuk persamaan linear, lalu selesaikan terhadap prediktor.')
            if level=='easy':return make('correlation','Koefisien korelasi adalah $r$. Tentukan koefisien determinasi dalam persen.',{'r':s.Rational(r.choice([-1,1])*r.randint(1,99),100)},'100*r*r','Koefisien determinasi adalah kuadrat korelasi dikali seratus persen.')
            sx=r.randint(2,9);sy=r.randint(2,9);cov=sx*sy*s.Rational(r.randint(1,9),10)
            return make('correlation','Kovarians dua variabel adalah $c$, dengan simpangan baku $s,t$. Tentukan koefisien determinasinya dalam persen.',{'c':cov,'s':sx,'t':sy},'100*(c/(s*t))**2','Hitung korelasi dari kovarians dan dua simpangan baku, kemudian kuadratkan untuk memperoleh determinasi.')
    if not tl and grade==12:
        if bab==3:
            if code=='A':
                if level=='easy':return make('counting','Kode terdiri dari satu simbol A, satu simbol B, dan satu simbol C. Tersedia $a,b,c$ pilihan untuk masing-masing posisi. Berapa kode yang mungkin?',{'a':a,'b':b,'c':c},'a*b*c','Gunakan aturan perkalian untuk tiga posisi independen.')
                nn=r.randint(6,20);length=r.randint(3,min(6,nn));even=r.randint(1,nn-1)
                return make('counting','Terdapat $n$ digit berbeda yang semuanya bukan nol; tepat $e$ di antaranya genap. Berapa bilangan genap $k$ angka tanpa pengulangan yang dapat dibentuk?',{'n':nn,'e':even,'k':length},'e*factorial(n-1)/factorial(n-k)','Isi posisi terakhir dengan digit genap, kemudian susun posisi lain dari digit yang tersisa.')
            if code=='B':
                nn=r.randint(7,24);kk=r.randint(3,min(6,nn))
                if level=='easy':return make('permutation','Dari $n$ orang dipilih dan diurutkan $k$ orang untuk menempati jabatan berbeda. Berapa susunan yang mungkin?',{'n':nn,'k':kk},'factorial(n)/factorial(n-k)','Jabatan berbeda membuat urutan pemilihan diperhitungkan.')
                return make('permutation','Dari $n$ orang, sebanyak $k$ dipilih lalu disusun berjajar. Dua orang tertentu wajib terpilih dan berdampingan. Berapa susunan yang memenuhi?',{'n':nn,'k':kk},'2*binomial(n-2,k-2)*factorial(k-1)','Pilih anggota lain, gabungkan dua orang wajib sebagai satu blok, lalu perhitungkan dua urutan internal blok.')
            if code=='C':
                if level=='easy':return make('combination','Dari $n$ peserta dipilih $k$ anggota tim tanpa jabatan. Berapa tim yang mungkin?',{'n':r.randint(9,30),'k':r.randint(2,6)},'binomial(n,k)','Anggota tim tidak diurutkan, sehingga gunakan kombinasi.')
                return make('combination','Dari $a$ peserta putra dan $b$ peserta putri dipilih tim $k$ orang. Berapa tim yang memuat sedikitnya satu putri?',{'a':a+4,'b':b+2,'k':r.randint(2,5)},'binomial(a+b,k)-binomial(a,k)','Kurangkan tim yang seluruhnya putra dari seluruh kemungkinan tim.')
            if level=='easy':return make('mixed_counting','Ketua dipilih dari kelompok A berisi $a$ orang, dan sekretaris dari kelompok B berisi $b$ orang. Kedua kelompok terpisah. Berapa pasangan pengurus yang mungkin?',{'a':a,'b':b},'a*b','Gunakan aturan perkalian karena asal kedua jabatan terpisah.')
            return make('mixed_counting','Dari $n$ orang dipilih seorang ketua dan $k$ anggota tanpa jabatan. Ketua tidak boleh merangkap anggota. Berapa susunan kepengurusan yang mungkin?',{'n':r.randint(9,25),'k':r.randint(2,6)},'n*binomial(n-1,k)','Pilih ketua terlebih dahulu, kemudian pilih anggota sebagai kelompok tanpa urutan.')
        if bab==4:
            if code=='A':
                if level=='easy':return make('single_probability','Kotak berisi $r$ bola merah, $b$ biru, dan $g$ hijau. Berapa peluang memperoleh bola merah?',{'r':a,'b':b,'g':c},'r/(r+b+g)','Bagi jumlah bola merah dengan jumlah seluruh bola.',probability=True)
                return make('single_probability','Kotak berisi $r$ bola merah, $b$ biru, dan $g$ hijau. Diketahui bola terambil bukan biru. Berapa peluang bola itu merah?',{'r':a,'b':b,'g':c},'r/(r+g)','Kondisi bukan biru mengubah ruang sampel menjadi gabungan merah dan hijau.',probability=True)
            if level=='easy':return make('joint_probability','Dua percobaan independen mempunyai peluang sukses $p$ dan $q$. Berapa peluang keduanya sukses?',{'p':s.Rational(a,20),'q':s.Rational(b,20)},'p*q','Untuk kejadian independen, kalikan kedua peluang.',probability=True)
            return make('joint_probability','Kotak memuat $r$ bola merah dan $b$ bola biru. Dua bola diambil tanpa pengembalian. Berapa peluang bola pertama merah dan kedua biru?',{'r':a,'b':b},'r*b/((r+b)*(r+b-1))','Kalikan peluang tahap pertama dengan peluang tahap kedua pada jumlah bola yang sudah berkurang.',probability=True)
    if tl and grade==11:return _tl11(bab,code,tier,r,visual)
    if tl and grade==12:return _tl12(bab,code,tier,r,visual)
    return None


def _finance(base,tier,r,visual):
    P=r.randint(6,50)*100000;rate=r.choice([2,3,4,5,6,8,10,12]);n=r.randint(2,6);D=r.randint(1,8)*10000
    make=lambda q,data,expr,why:_make(base,tier,q,data,expr,why,visual)
    if base=='interest':
        if tier=='direct':return make('Modal $P$ mendapat bunga tunggal $r$ persen per tahun selama $t$ tahun. Berapa bunga yang diperoleh?',{'P':P,'r':rate,'t':n},'P*r*t/100','Bunga tunggal adalah modal dikali suku bunga per tahun dan waktu.')
        return make('Simpanan berbunga tunggal $r$ persen per tahun menjadi $M$ rupiah setelah $t$ tahun. Berapa modal awalnya?',{'M':s.Rational(P)*(1+s.Rational(rate*n,100)),'r':rate,'t':n},'M/(1+r*t/100)','Nyatakan nilai akhir sebagai modal ditambah bunga, kemudian selesaikan terhadap modal.')
    if base=='compound':
        if tier=='direct':return make('Modal $P$ mendapat bunga majemuk $r$ persen per tahun. Berapa nilai akhirnya setelah $n$ tahun, tanpa pembulatan?',{'P':P,'r':rate,'n':n},'P*(1+r/100)**n','Gunakan faktor pertumbuhan tahunan berulang.')
        return make('Modal $P$ mendapat bunga majemuk $r$ persen per tahun selama $n$ tahun. Pada akhir periode dikenai biaya $B$. Berapa keuntungan bersih terhadap modal awal, tanpa pembulatan?',{'P':P,'r':rate,'n':n,'B':D},'P*(1+r/100)**n-P-B','Hitung nilai akhir majemuk, lalu kurangkan modal dan biaya.')
    if base=='annuity':
        if tier=='direct':return make('Setoran $D$ dilakukan setiap akhir tahun selama $n$ tahun dengan bunga $r$ persen per tahun. Gunakan rumus anuitas biasa $S=D((1+i)^n-1)/i$. Tentukan $S$ tanpa pembulatan.',{'D':D,'r':rate,'n':n},'D*((1+r/100)**n-1)/(r/100)','Ubah persen menjadi i, kemudian gunakan rumus yang diberikan.')
        k=r.randint(1,n-1)
        return make('Setoran $D$ dilakukan setiap akhir tahun selama $n$ tahun dengan bunga $r$ persen. Tepat sesudah setoran tahun ke-$k$, ditarik $W$ rupiah. Berapa saldo setelah setoran terakhir, tanpa pembulatan?',{'D':D,'r':rate,'n':n,'k':k,'W':s.Rational(D,2)},'D*((1+r/100)**n-1)/(r/100)-W*(1+r/100)**(n-k)','Hitung saldo anuitas utuh, lalu kurangkan nilai akhir dari dana yang ditarik lebih awal.')
    if base=='compound_loan':
        if tier=='direct':return make('Pinjaman $P$ berbunga majemuk $r$ persen per tahun tanpa pembayaran. Berapa utang setelah $n$ tahun, tanpa pembulatan?',{'P':P,'r':rate,'n':n},'P*(1+r/100)**n','Majemukkan utang dengan faktor bunga tahunan.')
        return make('Utang awal $P$ berbunga majemuk $r$ persen per tahun. Pada akhir tahun pertama dibayar $D$. Tanpa pembayaran lain, berapa sisa utang akhir tahun ke-$n$, tanpa pembulatan?',{'P':P,'r':rate,'n':n,'D':D},'(P*(1+r/100)-D)*(1+r/100)**(n-1)','Perbarui saldo setelah bunga dan pembayaran pertama, lalu maj emukkan saldo sisa untuk tahun-tahun berikutnya.'.replace('maj emukkan','majemukkan'))
    if base=='loan_annuity':
        payment=P*s.Rational(rate,100)+D
        if tier=='direct':return make('Pinjaman $P$ berbunga $r$ persen per periode. Anuitas yang dibayar pada akhir periode pertama sebesar $A$. Berapa angsuran pokok pertama?',{'P':P,'r':rate,'A':payment},'A-P*r/100','Anuitas terdiri atas bunga periode berjalan dan pengurangan pokok.')
        return make('Pinjaman $P$ berbunga $r$ persen per periode dengan anuitas akhir periode tetap $A$. Berapa angsuran pokok pada pembayaran kedua?',{'P':P,'r':rate,'A':payment},'A-(P*(1+r/100)-A)*r/100','Hitung saldo setelah pembayaran pertama, bunga periode kedua, kemudian bagian pokok dari anuitas kedua.')
    if tier=='direct':return make('Modal $P$ menghasilkan bunga tunggal $I$ selama $t$ tahun. Berapa suku bunga tahunannya dalam persen?',{'P':P,'I':s.Rational(P*rate*n,100),'t':n},'100*I/(P*t)','Balikkan rumus bunga tunggal terhadap suku bunga.')
    return make('Modal $P$ menjadi $M$ setelah dua tahun dengan bunga majemuk tahunan tetap. Berapa suku bunga dalam persen?',{'P':P,'M':s.Rational(P)*(1+s.Rational(rate,100))**2},'100*(sqrt(M/P)-1)','Perbandingan nilai akhir dan modal adalah kuadrat faktor pertumbuhan tahunan.')


def _tl11(bab,code,tier,r,visual):
    easy=tier=='direct';a=r.randint(2,12);b=r.randint(2,13);c=r.randint(1,11);d=r.randint(2,12);t=r.randint(2,8);n=r.randint(3,8)
    make=lambda base,q,data,expr,why,**kw:_make(base,tier,q,data,expr,why,visual,**kw)
    if bab==1:
        if code=='A':
            if easy:return make('matrix_types','Matriks diagonal berordo $n$ mempunyai setiap elemen diagonal yang dipilih bebas dari $k$ nilai berbeda, termasuk nol. Ada berapa matriks yang mungkin?',{'n':n,'k':a},'k**n','Hanya n posisi diagonal yang bebas; gunakan aturan perkalian.')
            return make('matrix_types','Matriks diagonal berordo $n$ memakai $k$ pilihan nilai diagonal, termasuk nol. Berapa matriks yang tepat satu elemen diagonalnya nol dan semua elemen diagonal lain bukan nol?',{'n':n,'k':a},'n*(k-1)**(n-1)','Pilih posisi nol, kemudian isi posisi lain dengan nilai bukan nol.')
        if code=='B':
            if easy:return make('matrix_equal','Kesamaan elemen bersesuaian dari dua matriks memberi $ax+b=c$. Tentukan $x$.',{'a':a,'b':b,'c':a*t+b},'(c-b)/a','Elemen bersesuaian matriks yang sama harus sama.')
            return make('matrix_equal','Kesamaan dua matriks memberi $ax+b=u$ dan $cy-d=v$. Tentukan $x+y$.',{'a':a,'b':b,'c':c,'d':d,'u':a*t+b,'v':c*n-d},'(u-b)/a+(v+d)/c','Selesaikan kesamaan elemen untuk masing-masing variabel, kemudian jumlahkan.')
        if code=='C':
            if easy:return make('matrix_sum','Elemen posisi $(1,2)$ matriks A adalah $a$ dan posisi yang sama pada B adalah $b$. Tentukan elemen $(1,2)$ dari $A+B$.',{'a':a,'b':b},'a+b','Jumlahkan elemen pada posisi yang sama.')
            return make('matrix_sum','Matriks A mempunyai diagonal $a,d$ dan matriks B mempunyai diagonal $b,c$. Tentukan jumlah elemen diagonal dari $2A-B$.',{'a':a,'b':b,'c':c,'d':d},'2*(a+d)-b-c','Terapkan operasi skalar dan pengurangan pada diagonal, lalu jumlahkan hasilnya.')
        if code=='D':
            if easy:return make('matrix_product','Baris pertama A adalah $(a,b)$ dan kolom kedua B adalah $(c,d)$. Tentukan elemen $(1,2)$ dari $AB$.',{'a':a,'b':b,'c':c,'d':d},'a*c+b*d','Kalikan baris dengan kolom dan jumlahkan kedua hasil kali.')
            return make('matrix_product',r'Baris pertama A adalah $(a,b)$, matriks B adalah $\begin{pmatrix}c&d\\e&f\end{pmatrix}$, dan kolom pertama C adalah $(g,h)^T$. Tentukan elemen $(1,1)$ dari $ABC$.',{'a':a,'b':b,'c':c,'d':d,'e':t,'f':n,'g':r.randint(2,9),'h':r.randint(2,9)},'a*(c*g+d*h)+b*(e*g+f*h)','Hitung kolom pertama BC, lalu kalikan dengan baris pertama A.')
        if a*d==b*c:d+=1
        if easy:return make('matrix_inverse',r'Tentukan determinan $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$.',{'a':a,'b':b,'c':c,'d':d},'a*d-b*c','Gunakan selisih hasil kali kedua diagonal matriks dua kali dua.')
        return make('matrix_inverse',r'Matriks $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ mempunyai invers. Tentukan jumlah dua elemen diagonal $A^{-1}$.',{'a':a,'b':b,'c':c,'d':d},'(a+d)/(a*d-b*c)','Cari determinan, bentuk invers, kemudian jumlahkan elemen diagonalnya.')
    if bab==2:
        if code=='A':
            if easy:return make('polynomial_value','Untuk $P(x)=ax^2+bx+c$, hitung $P(t)$.',{'a':a,'b':b,'c':c,'t':t},'a*t*t+b*t+c','Substitusikan nilai argumen ke polinomial.')
            return make('polynomial_value','Polinomial $P(x)=ax^2+bx+c$ memenuhi $P(1)=u$. Tentukan $P(t)$.',{'a':a,'c':c,'u':a+b+c,'t':t},'a*t*t+(u-a-c)*t+c','Gunakan nilai pada x=1 untuk menemukan koefisien b, lalu evaluasi polinomial.')
        if code=='B':
            if easy:return make('polynomial_product','Koefisien x pada P adalah $a$ dan pada Q adalah $b$. Berapa koefisien x dari $P+Q$?',{'a':a,'b':b},'a+b','Gabungkan koefisien suku sejenis.')
            return make('polynomial_product','Untuk $P(x)=x^2+ax+b$ dan $Q(x)=x^2+cx+d$, berapa koefisien $x^2$ pada $P(x)Q(x)$?',{'a':a,'b':b,'c':c,'d':d},'a*c+b+d','Cari seluruh pasangan suku yang pangkatnya berjumlah dua, lalu jumlahkan kontribusinya.')
        if code=='C':
            if easy:return make('polynomial_remainder','Tentukan sisa pembagian $P(x)=ax^2+bx+c$ oleh $x-t$.',{'a':a,'b':b,'c':c,'t':t},'a*t*t+b*t+c','Teorema sisa menyatakan bahwa sisanya P(t).')
            u=r.randint(1,3);v=u+r.randint(1,4)
            pu=a*u**3+b*u*u+c*u+d;pv=a*v**3+b*v*v+c*v+d
            return make('polynomial_remainder','Diketahui $P(u)=p$ dan $P(v)=q$. Jika P dibagi oleh $(x-u)(x-v)$, sisanya R berderajat kurang dari dua. Tentukan $R(t)$.',{'u':u,'v':v,'p':pu,'q':pv,'t':v+r.randint(1,4)},'p+(t-u)*(q-p)/(v-u)','Sisa linear harus sama nilainya dengan P pada kedua akar pembagi. Tentukan garis melalui kedua data lalu evaluasi pada t.')
        if code=='D':
            if easy:return make('polynomial_factor','Polinomial $P(x)=(x-u)(x+v)$ mempunyai tepat satu akar positif. Tentukan akar positifnya.',{'u':a,'v':b},'u','Pembuat nol diperoleh dengan membuat salah satu faktor sama dengan nol.')
            # A supplied root gives a quadratic quotient by synthetic division.
            aa=-(a+b+c);bb=a*b+a*c+b*c
            return make('polynomial_factor','Polinomial monik $P(x)=x^3+ax^2+bx+c$ mempunyai akar $u$. Tentukan diskriminan polinomial kuadrat $P(x)/(x-u)$.',{'a':aa,'b':bb,'c':-a*b*c,'u':a},'(a+u)**2-4*(b+u*(a+u))','Gunakan pembagian sintetis untuk koefisien hasil bagi, lalu hitung diskriminan kuadratnya.')
        if easy:return make('polynomial_identity','Dalam identitas $(x+a)^n$, berapa koefisien $x^{n-1}$?',{'a':a,'n':n},'n*a','Pilih satu faktor konstanta dan x dari seluruh faktor lainnya.')
        return make('polynomial_identity','Dalam $(x+a)^n+(x+b)^n$, berapa koefisien $x^{n-2}$?',{'a':a,'b':b,'n':n},'binomial(n,2)*(a*a+b*b)','Gunakan koefisien binomial pada masing-masing bentuk lalu jumlahkan.')
    if bab==3:
        if code=='A':
            if easy:
                theta=r.choice([30,45,60,120,135,150,210,225,240,300,315,330]);k=r.randint(1,12)
                return make('unit_circle',r'Tentukan $\sin((t+360k)^\circ)$.',{'t':theta,'k':k},'sin(pi*t/180)','Putaran penuh tidak mengubah titik pada lingkaran satuan.')
            return make('unit_circle',r'Sisi akhir sudut $\theta$ di kuadran I melalui titik $(a,b)$. Tentukan $\sin\theta+\cos\theta$.',{'a':a,'b':b},'(a+b)/sqrt(a*a+b*b)','Cari jarak titik ke pusat, tentukan sinus dan kosinus, lalu jumlahkan.')
        if code=='B':
            if easy:return make('trig_graph',r'Fungsi $y=a\sin(bx)+c$ menggunakan radian. Tentukan periodenya.',{'a':a,'b':b,'c':c},'2*pi/b','Periode sinus dengan koefisien argumen b adalah dua pi dibagi b.')
            return make('trig_graph',r'Fungsi $f(x)=A\sin(bx)+C$ dengan A,b positif mempunyai maksimum $M$, minimum $m$, dan periode $T=2\pi/b$. Tentukan $f(\pi/(6b))$.',{'M':c+a,'m':c-a,'b':b},'(M-m)/4+(M+m)/2','Ekstrem menentukan amplitudo dan garis tengah. Pada argumen yang diminta sinus bernilai setengah.')
        if code=='C':
            if easy:return make('trig_identity',r'Sederhanakan $a(\sin^2\theta+\cos^2\theta)+b$.',{'a':a,'b':b},'a+b','Gunakan identitas dasar sinus kuadrat ditambah kosinus kuadrat sama dengan satu.')
            return make('trig_identity',r'Sudut $\theta$ lancip dan $\tan\theta=t$. Tentukan $\sec^2\theta+a\sin2\theta$.',{'t':s.Rational(a,b),'a':c},'1+t*t+a*2*t/(1+t*t)','Hubungkan sekan kuadrat dan sinus sudut ganda dengan tangen yang diketahui.')
        if code=='D':
            angle_a=r.choice([30,45,60]);angle_b=r.choice([30,45,60])
            if easy:return make('sine_rule','Segitiga ABC mempunyai sudut A dan B masing-masing $u,v$ derajat. Sisi di depan A panjangnya $a$. Tentukan sisi di depan B.',{'u':angle_a,'v':angle_b,'a':a},'a*sin(pi*v/180)/sin(pi*u/180)','Gunakan aturan sinus untuk dua sisi dan sudut di hadapannya.')
            return make('sine_rule','Segitiga ABC mempunyai sudut A dan B masing-masing $u,v$ derajat. Sisi di depan A panjangnya $a$. Tentukan sisi di depan C.',{'u':angle_a,'v':angle_b,'a':a},'a*sin(pi*(180-u-v)/180)/sin(pi*u/180)','Tentukan sudut ketiga dari jumlah sudut segitiga, kemudian terapkan aturan sinus.')
        if easy:return make('cosine_rule','Dua sisi segitiga panjangnya $a,b$ dengan sudut apit $t$ derajat. Tentukan panjang sisi di depan sudut apit tersebut.',{'a':a,'b':b,'t':r.choice([60,90,120])},'sqrt(a*a+b*b-2*a*b*cos(pi*t/180))','Gunakan aturan kosinus untuk sisi di depan sudut apit.')
        u=r.randint(3,9);v=r.randint(1,u-1);legs={'a':u*u-v*v,'b':2*u*v,'c':u*u+v*v}
        return make('cosine_rule','Segitiga mempunyai tiga sisi $a,b,c$. Gunakan aturan kosinus pada sudut di antara sisi a dan b, lalu tentukan luas segitiganya.',legs,'a*b*sqrt(1-((a*a+b*b-c*c)/(2*a*b))**2)/2','Dapatkan kosinus sudut apit, gunakan identitas kuadrat untuk sinus positif, lalu hitung setengah ab sinus sudut apit.')
    if bab==4:
        ux=r.randint(-12,12);uy=r.randint(-12,12);vx=r.randint(-12,12);vy=r.randint(-12,12)
        if vx==vy==0:vx=1
        data={'a':ux,'b':uy,'c':vx,'d':vy}
        if code=='A':
            if easy:return make('vector','Vektor $u=(a,b)$ dan $v=(c,d)$. Tentukan komponen pertama $u+v$.',data,'a+c','Penjumlahan vektor dilakukan per komponen.')
            return make('vector','Vektor $u=(a,b)$ dan $v=(c,d)$. Tentukan panjang $u+v$.',data,'sqrt((a+c)**2+(b+d)**2)','Jumlahkan komponen yang bersesuaian, kemudian gunakan rumus panjang vektor.')
        if code=='B':
            if easy:return make('dot_product',r'Vektor $u=(a,b)$ dan $v=(c,d)$. Tentukan $u\cdot v$.',data,'a*c+b*d','Jumlahkan hasil kali komponen yang bersesuaian.')
            return make('dot_product','Vektor $u=(a,b)$ dan vektor tak nol $v=(c,d)$. Tentukan kuadrat panjang proyeksi ortogonal u pada v.',data,'(a*c+b*d)**2/(c*c+d*d)','Cari hasil kali titik, kemudian bagi kuadratnya dengan kuadrat panjang arah proyeksi.')
        if easy:return make('vector_proof','Titik A adalah $(a,b)$ dan B adalah $(c,d)$. Dengan vektor posisi titik tengah, tentukan absis titik tengah AB.',data,'(a+c)/2','Vektor posisi titik tengah adalah setengah jumlah kedua vektor posisi.')
        if vx==ux and vy==uy:vx+=1
        if (vx-ux)*b==(vy-uy)*a:b+=1
        data={'a':ux,'b':uy,'c':vx,'d':vy,'e':vx+a,'f':vy+b}
        return make('vector_proof','Jajar genjang ABCD berurutan mempunyai $A=(a,b)$, $B=(c,d)$, dan $C=(e,f)$. Dengan sifat bahwa diagonal saling membagi dua, tentukan jumlah koordinat D.',data,'a+e-c+b+f-d','Samakan titik tengah AC dan BD untuk mendapatkan vektor posisi D, lalu jumlahkan komponennya.')
    if bab==5:
        px=r.randint(-15,15);py=r.randint(-15,15)
        if code=='A':
            if easy:return make('cartesian_transform','Titik P$(x,y)$ ditranslasikan oleh $(a,b)$. Tentukan absis bayangannya.',{'x':px,'y':py,'a':a,'b':b},'x+a','Tambahkan komponen mendatar translasi pada absis titik.')
            return make('cartesian_transform','Titik P$(x,y)$ ditranslasikan oleh $(a,b)$ lalu dicerminkan terhadap sumbu x. Tentukan jumlah koordinat bayangan terakhir.',{'x':px,'y':py,'a':a,'b':b},'x+a-y-b','Terapkan translasi, kemudian ubah tanda ordinat pada pencerminan terhadap sumbu x.')
        if code=='B':
            if a*d==b*c:d+=1
            if easy:return make('matrix_transform',r'Transformasi bermatriks $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ diterapkan pada P$(x,y)$. Tentukan ordinat bayangannya.',{'a':a,'b':b,'c':c,'d':d,'x':px,'y':py},'c*x+d*y','Kalikan baris kedua matriks dengan vektor posisi titik.')
            return make('matrix_transform',r'Transformasi bermatriks $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ memetakan P ke Q$(u,v)$. Tentukan absis P.',{'a':a,'b':b,'c':c,'d':d,'u':a*px+b*py,'v':c*px+d*py},'(d*u-b*v)/(a*d-b*c)','Hitung invers matriks transformasi lalu terapkan pada bayangan yang diketahui.')
        if easy:return make('composed_transform',r'Transformasi pertama bermatriks diagonal $\operatorname{diag}(a,b)$ dan kedua $\operatorname{diag}(c,d)$. Tentukan elemen $(1,1)$ matriks komposisi kedua setelah pertama.',{'a':a,'b':b,'c':c,'d':d},'a*c','Matriks komposisi adalah hasil kali kedua matriks dalam urutan penerapan yang tepat.')
        return make('composed_transform',r'Titik P$(x,y)$ dikenai transformasi diagonal $\operatorname{diag}(a,b)$ lalu rotasi 90 derajat berlawanan arah jarum jam terhadap O. Tentukan jumlah koordinat bayangannya.',{'a':a,'b':b,'x':px,'y':py},'a*x-b*y','Terapkan skala pada kedua komponen, lalu aturan rotasi seperempat putaran.')
    if bab==6:
        if code=='A':
            base=r.randint(2,12);power=r.randint(2,8)
            while base**power>100000000:power-=1
            if easy:return make('logarithm',r'Tentukan $\log_a N$.',{'a':base,'N':base**power},'log(N)/log(a)','Definisi logaritma mencari eksponen yang menghasilkan N dari basis a.')
            u=r.randint(1,5);v=r.randint(1,5)
            return make('logarithm',r'Tentukan $\log_a M+\log_a N$.',{'a':base,'M':base**u,'N':base**v},'log(M*N)/log(a)','Gabungkan logaritma penjumlahan menjadi logaritma hasil kali, lalu gunakan definisi eksponen.')
        if code=='B':
            if easy:return make('algebraic_function','Fungsi $f(x)=(ax+b)/(x+c)$. Tentukan $f(t)$.',{'a':a,'b':b,'c':c,'t':t},'(a*t+b)/(t+c)','Substitusikan t dan periksa penyebut tidak nol.')
            if b==a*c:b+=1
            y=s.Rational(a*t+b,t+c)
            return make('algebraic_function',r'Fungsi $f(x)=(ax+b)/(x+c)$ dengan $x\ne-c$ memenuhi $f(x)=u$. Tentukan $x$.',{'a':a,'b':b,'c':c,'u':y},'(b-u*c)/(u-a)','Kalikan silang lalu kumpulkan semua suku yang mengandung x; periksa domain hasilnya.')
        initial=r.randint(2,30)*100;growth=r.randint(2,4);periods=r.randint(2,6)
        if easy:return make('nonalgebraic_function','Model populasi adalah $N(t)=P a^t$. Tentukan $N(k)$.',{'P':initial,'a':growth,'k':periods},'P*a**k','Evaluasi model eksponensial pada waktu yang diketahui.')
        return make('nonalgebraic_function','Model populasi adalah $N(t)=P a^t$ dengan $a>1$. Setelah berapa periode populasi mencapai $Q$?',{'P':initial,'a':growth,'Q':initial*growth**periods},'log(Q/P)/log(a)','Bagi dengan populasi awal, kemudian gunakan logaritma untuk mendapatkan waktu.')
    return None


def _tl12(bab,code,tier,r,visual):
    easy=tier=='direct';a=r.randint(2,12);b=r.randint(2,13);c=r.randint(1,11);d=r.randint(2,12);t=r.randint(2,8);n=r.randint(3,8)
    make=lambda base,q,data,expr,why,**kw:_make(base,tier,q,data,expr,why,visual,**kw)
    if bab==1:
        h=r.randint(-10,10);k=r.randint(-10,10);rad=r.randint(3,15)
        if code=='A':
            if easy:return make('circle','Lingkaran mempunyai persamaan $(x-h)^2+(y-k)^2=R$. Tentukan jari-jarinya.',{'h':h,'k':k,'R':rad*rad},'sqrt(R)','Pada bentuk baku persamaan lingkaran, ruas kanan adalah kuadrat jari-jari.')
            return make('circle',r'Lingkaran mempunyai persamaan $x^2+y^2+Dx+Ey+F=0$. Tentukan luas daerah lingkarannya dalam bentuk $\pi$.',{'D':-2*h,'E':-2*k,'F':h*h+k*k-rad*rad},'pi*((D*D+E*E)/4-F)','Lengkapi kuadrat untuk mendapatkan jari-jari kuadrat, lalu gunakan rumus luas.')
        if code=='B':
            aa=r.randint(6,18);bb=r.randint(2,aa-1)
            if easy:return make('ellipse','Elips memenuhi $(x-h)^2/A+(y-k)^2/B=1$ dengan $A>B>0$. Tentukan panjang sumbu mayornya.',{'h':h,'k':k,'A':aa*aa,'B':bb*bb},'2*sqrt(A)','Penyebut terbesar adalah kuadrat setengah sumbu mayor.')
            return make('ellipse','Elips memenuhi $(x-h)^2/A+(y-k)^2/B=1$ dengan $A>B>0$. Tentukan jarak antara kedua fokus.',{'h':h,'k':k,'A':aa*aa,'B':bb*bb},'2*sqrt(A-B)','Hubungkan jarak fokus dari pusat dengan kedua setengah sumbu, kemudian gandakan jarak itu.')
        if code=='C':
            if easy:return make('circle_position','Lingkaran berpusat di $(h,k)$ dan titik P adalah $(u,v)$. Tentukan kuadrat jarak P ke pusat.',{'h':h,'k':k,'u':h+a,'v':k+b},'(u-h)**2+(v-k)**2','Gunakan jarak kuadrat dua titik sebagai dasar pemeriksaan kedudukan titik.')
            offset=r.randint(1,rad-1)
            return make('circle_position','Lingkaran berpusat di $(h,k)$ berjari-jari $r$. Garis $x=q$ memotong lingkaran pada dua titik. Tentukan panjang tali busur di antara kedua titik itu.',{'h':h,'k':k,'r':rad,'q':h+offset},'2*sqrt(r*r-(q-h)**2)','Jarak pusat ke garis menentukan setengah tali busur melalui segitiga siku-siku.')
        if easy:return make('circle_tangent','Lingkaran berpusat di $(h,k)$ dan berjari-jari $r$. Garis singgung di titik paling kanan berbentuk $x=c$. Tentukan $c$.',{'h':h,'k':k,'r':rad},'h+r','Jari-jari ke titik paling kanan mendatar, sehingga garis singgungnya tegak.')
        u=r.randint(2,10);v=r.randint(2,10)
        return make('circle_tangent','Lingkaran berpusat di $(h,k)$ melalui P$(u,v)$. Tentukan absis titik potong garis singgung di P dengan sumbu x.',{'h':h,'k':k,'u':h+u,'v':k+v},'((u-h)*u+(v-k)*v)/(u-h)','Vektor pusat ke P menjadi normal garis singgung. Susun persamaannya lalu substitusi y=0.')
    if bab==2:
        if code=='A':
            if easy:return make('derivative_definition',r'Gunakan limit hasil bagi selisih untuk $f(x)=ax+b$. Tentukan $f^\prime(t)$.',{'a':a,'b':b,'t':t},'a','Pada fungsi linear, hasil bagi selisih bernilai a untuk setiap langkah tak nol.')
            return make('derivative_definition',r'Gunakan definisi turunan untuk $f(x)=ax^2+bx+c$. Tentukan $f^\prime(t)$.',{'a':a,'b':b,'c':c,'t':t},'2*a*t+b','Kembangkan f(t+h)-f(t), bagi h, ambil limit, kemudian evaluasi koefisien pada t.')
        if code=='B':
            if easy:return make('derivative_rules',r'Fungsi $f(x)=ax^n$. Tentukan $f^\prime(t)$.',{'a':a,'n':n,'t':t},'n*a*t**(n-1)','Gunakan aturan pangkat lalu substitusikan argumen.')
            return make('derivative_rules',r'Fungsi $f(x)=(ax+b)(cx+d)$. Tentukan $f^\prime(t)$.',{'a':a,'b':b,'c':c,'d':d,'t':t},'2*a*c*t+a*d+b*c','Terapkan aturan hasil kali pada dua fungsi linear, sederhanakan, lalu evaluasi.')
        if code=='C':
            data={'a':a,'b':-2*a*t,'c':c}
            if easy:return make('stationary','Fungsi $f(x)=ax^2+bx+c$ dengan a positif mempunyai titik stasioner. Tentukan absisnya.',data,'-b/(2*a)','Setarakan turunan pertama dengan nol.')
            return make('stationary','Untuk $f(x)=ax^2+bx+c$ dengan a positif, tentukan nilai minimum f dengan bantuan turunan.',data,'c-b*b/(4*a)','Cari titik stasioner, periksa tanda turunan kedua, lalu evaluasi fungsi pada titik tersebut.')
        if easy:return make('derivative_application','Posisi benda adalah $s(t)=at^2+bt+c$ dalam meter. Tentukan kecepatan pada waktu $t=k$ detik.',{'a':a,'b':b,'c':c,'k':t},'2*a*k+b','Kecepatan adalah turunan posisi terhadap waktu.')
        return make('derivative_application','Pendapatan produksi q unit adalah $R(q)=pq$ dan biayanya $C(q)=aq^2+bq+c$, dengan a positif dan p>b. Untuk q real tak negatif, berapa keuntungan maksimum?',{'a':a,'b':b,'c':c,'p':b+a*t},'(p-b)**2/(4*a)-c','Bentuk fungsi keuntungan sebagai pendapatan dikurangi biaya, optimalkan dengan turunan, kemudian evaluasi keuntungannya.')
    if bab==3:
        if code=='A':
            if easy:return make('indefinite_integral',r'Fungsi F memenuhi $F^\prime(x)=ax^n$ dan $F(0)=0$. Tentukan $F(t)$.',{'a':a,'n':n,'t':t},'a*t**(n+1)/(n+1)','Integralkan aturan pangkat dan gunakan kondisi awal untuk konstanta integrasi.')
            return make('indefinite_integral',r'Fungsi F memenuhi $F^\prime(x)=ax^n$ dan $F(p)=u$. Tentukan $F(q)$.',{'a':a,'n':n,'p':r.randint(1,3),'q':r.randint(4,8),'u':b},'u+a*(q**(n+1)-p**(n+1))/(n+1)','Bentuk antiturunan, tentukan konstanta dari satu titik, lalu evaluasi pada titik lain.')
        if code=='B':
            lo=r.randint(0,4);hi=lo+r.randint(2,6)
            if easy:return make('definite_integral',r'Hitung $\int_L^U ax\,dx$.',{'a':a,'L':lo,'U':hi},'a*(U*U-L*L)/2','Cari antiturunan kemudian kurangi nilainya pada batas atas dan batas bawah.')
            return make('definite_integral',r'Hitung $\int_L^U (ax^2+bx+c)\,dx$.',{'a':a,'b':b,'c':c,'L':lo,'U':hi},'a*(U**3-L**3)/3+b*(U**2-L**2)/2+c*(U-L)','Integralkan setiap suku, kemudian terapkan kedua batas pada antiturunan gabungan.')
        if easy:return make('integral_area','Grafik $y=h$ dan sumbu x membatasi daerah pada interval $[0,w]$, dengan h positif. Hitung luasnya menggunakan integral.',{'h':a,'w':b},'h*w','Integralkan fungsi konstan di sepanjang interval.')
        return make('integral_area','Kurva $y=ax(L-x)$ dengan a positif membatasi daerah dengan sumbu x pada $[0,L]$. Tentukan luas daerahnya.',{'a':a,'L':b},'a*L**3/6','Pastikan kurva tidak negatif pada interval, kembangkan polinomial, lalu integralkan terhadap kedua batas.')
    if bab==4:
        if code=='A':
            if easy:return make('random_variable','X menyatakan jumlah sukses dalam $n$ percobaan Bernoulli independen dengan peluang sukses $p$. Tentukan $E(X)$.',{'n':n,'p':s.Rational(a,20)},'n*p','Harapan jumlah indikator adalah jumlah peluang suksesnya.')
            return make('random_variable','Permainan memberi hadiah $a$ dengan peluang $p$, atau hadiah $b$ dengan peluang sisanya. Biaya satu permainan $c$. Tentukan harapan keuntungan bersih.',{'a':a*1000,'b':b*100,'p':s.Rational(c,20),'c':d*100},'a*p+b*(1-p)-c','Hitung nilai harapan hadiah dari dua hasil, lalu kurangkan biaya permainan.')
        if code=='B':
            if easy:return make('discrete_variable','X hanya bernilai $a$ atau $b$, dengan $P(X=a)=p$. Tentukan $E(X)$.',{'a':a,'b':a+b,'p':s.Rational(c,20)},'a*p+b*(1-p)','Kalikan setiap nilai dengan peluangnya lalu jumlahkan.')
            return make('discrete_variable','X bernilai $a$ atau $b$ dengan $P(X=a)=p$. Tentukan varians X.',{'a':a,'b':a+b,'p':s.Rational(c,20)},'a*a*p+b*b*(1-p)-(a*p+b*(1-p))**2','Hitung momen pertama dan kedua, kemudian gunakan varians sebagai E(X kuadrat) dikurangi kuadrat E(X).')
        if code=='C':
            lo=r.randint(5,30);hi=lo+r.randint(8,30);cut=r.randint(lo+1,hi-1)
            if easy:return make('continuous_variable','X seragam kontinu pada $[a,b]$. Tentukan $P(X<t)$.',{'a':lo,'b':hi,'t':cut},'(t-a)/(b-a)','Peluang seragam adalah perbandingan panjang subinterval dengan seluruh interval.',probability=True)
            return make('continuous_variable',r'X seragam kontinu pada $[a,b]$. Diketahui $X>t$ dengan a<t<b. Tentukan nilai harapan bersyarat $E(X\mid X>t)$.',{'a':lo,'b':hi,'t':cut},'(t+b)/2','Kondisi memotong dukungan menjadi interval t sampai b; harapan sebaran seragam baru adalah titik tengah interval.')
        if code=='D':
            if easy:return make('probability_function',r'Fungsi peluang X pada nilai 1,2,3 sebanding dengan bobot $a,b,c$. Tentukan $P(X\ge2)$.',{'a':a,'b':b,'c':c},'(b+c)/(a+b+c)','Normalisasikan bobot menjadi peluang, lalu jumlahkan peluang pada nilai dua dan tiga.',probability=True)
            top=r.randint(5,22);cut=r.randint(2,top-1)
            return make('probability_function',r'Fungsi peluang adalah $P(X=j)=kj$ untuk $j=1,\ldots,n$ dan nol selainnya. Tentukan $P(X\ge t)$.',{'n':top,'t':cut},'(n*(n+1)-(t-1)*t)/(n*(n+1))','Cari konstanta normalisasi dari jumlah deret, kemudian jumlahkan peluang di bagian dukungan yang diminta.',probability=True)
        if code=='E':
            length=r.randint(5,30);cut=r.randint(1,length-1)
            if easy:return make('density','Densitas X konstan pada $[0,L]$ dan nol selainnya. Tentukan $P(X<t)$.',{'L':length,'t':cut},'t/L','Normalisasi densitas konstan dan hitung luas persegipanjang di bawah kurva.',probability=True)
            return make('density','Densitas X adalah $f(x)=kx$ pada $[0,L]$ dan nol selainnya. Tentukan $P(X>t)$ setelah menentukan k agar f menjadi densitas.',{'L':length,'t':cut},'1-t*t/(L*L)','Normalisasi integral seluruh densitas, kemudian integralkan pada interval di atas t.',probability=True)
        if code=='F':
            trials=r.randint(4,18);p=s.Rational(r.randint(2,8),10)
            if easy:return make('binomial','X binomial dengan parameter n dan p. Tentukan nilai harapannya.',{'n':trials,'p':p},'n*p','Gunakan sifat nilai harapan distribusi binomial.')
            return make('binomial','X binomial dengan parameter n dan p. Tentukan $P(X=k)$.',{'n':trials,'p':p,'k':r.randint(1,trials-1)},'binomial(n,k)*p**k*(1-p)**(n-k)','Pilih posisi sukses lalu kalikan peluang sukses dan gagal pada seluruh percobaan.',probability=True)
        mean=r.randint(30,100);sd=r.randint(2,15);z=r.choice([-2,-1,1,2]);score=mean+sd*z
        if easy:return make('normal','X normal dengan rata-rata $m$ dan simpangan baku $s$. Tentukan skor baku untuk nilai $x$.',{'m':mean,'s':sd,'x':score},'(x-m)/s','Standardisasi mengurangi rata-rata lalu membagi simpangan baku.')
        phi={-2:s.Rational(228,10000),-1:s.Rational(1587,10000),1:s.Rational(8413,10000),2:s.Rational(9772,10000)}
        return make('normal',r'X normal dengan rata-rata $m$ dan simpangan baku $s$. Tabel normal memberi $\Phi(-2)=F1$, $\Phi(-1)=F2$, $\Phi(1)=F3$, dan $\Phi(2)=F4$. Tentukan $P(X<x)$.',{'m':mean,'s':sd,'x':score,'F1':phi[-2],'F2':phi[-1],'F3':phi[1],'F4':phi[2]},'Piecewise((F1,Eq((x-m)/s,-2)),(F2,Eq((x-m)/s,-1)),(F3,Eq((x-m)/s,1)),(F4,Eq((x-m)/s,2)))','Standardisasi nilai x, pilih baris tabel yang sesuai, dan gunakan peluang kumulatifnya.',probability=True)
    return None


def _hard_missing(name,bab,code,r,visual):
    make=lambda base,q,data,expr,why,**kw:_make(base,'reconstruct',q,data,expr,why,visual,**kw)
    if name=='kelas10' and bab==5 and code=='A':
        a=r.randint(5,20);b=r.randint(1,a-1);total=a+b;square=a*a+b*b
        return make('quadratic_equation','Dua akar positif persamaan kuadrat adalah p dan q dengan p>q. Diketahui $p+q=S$ dan $p^2+q^2=Q$. Tentukan $p^3-q^3$.',{'S':total,'Q':square},'sqrt(2*Q-S*S)*(S*S+Q)/2','Rekonstruksi hasil kali akar dari kedua kendala, pilih selisih akar positif, lalu gunakan identitas selisih kubik.')
    if name=='kelas12' and bab==2 and code=='C':
        principal=r.randint(5,30)*100000;deposit=r.randint(1,9)*10000;f=1+s.Rational(r.randint(2,12),100);n=r.randint(2,4)
        u=principal*f+deposit;v=u*f+deposit;w=v*f+deposit
        factor='((W-V)/(V-U))';pay='(V-U*((W-V)/(V-U)))'
        return make('annuity','Sebuah investasi mempunyai saldo awal tak diketahui dan setoran akhir tahun tetap D. Bunga majemuk tahunan mempunyai faktor tetap f>1. Saldo sesudah setoran tahun pertama, kedua, ketiga adalah U,V,W. Jika pola diteruskan tanpa transaksi lain, berapa saldo n tahun setelah pengamatan ketiga?',{'U':u,'V':v,'W':w,'n':n},f'W*{factor}**n+{pay}*({factor}**n-1)/({factor}-1)','Rasio dua perubahan saldo menentukan faktor bunga; data dua saldo lalu menentukan setoran. Majemukkan saldo ketiga dan anuitas setoran berikutnya.')
    if name=='kelas12' and bab==2 and code=='D':
        principal=r.randint(10,40)*100000;payment=r.randint(1,8)*100000;f=1+s.Rational(r.randint(3,12),100);u=principal*f*f;v=principal*f**4-payment*f
        factor='((D+sqrt(D*D+4*U*V))/(2*U))'
        return make('compound_loan','Pinjaman awal P mempunyai faktor bunga tahunan tetap f>1. Utang akhir tahun kedua U. Tepat akhir tahun ketiga dibayar D dan utang akhir tahun keempat menjadi V. Tidak ada pembayaran lain. Tentukan P.',{'U':u,'V':v,'D':payment},f'U/{factor}**2','Hubungkan kedua saldo untuk persamaan kuadrat faktor bunga. Pilih akar positif f>1, kemudian kembalikan saldo tahun kedua ke modal pinjaman awal.')
    if name=='kelas12' and bab==4 and code=='B':
        pp=r.randint(25,90);qq=r.randint(15,60);ii=r.randint(max(1,pp+qq-100),min(pp,qq)-1)
        p=s.Rational(pp,100);q=s.Rational(qq,100);intersection=s.Rational(ii,100);union=p+q-intersection
        qb='((U+I)/(k+1))';pa=f'(k*{qb})'
        return make('joint_probability',r'Dua kejadian A dan B memenuhi $P(A\cup B)=U$, $P(A\cap B)=I$, dan $P(A)=kP(B)$. Tentukan $P(A\mid B^c)$.',{'U':union,'I':intersection,'k':p/q},f'({pa}-I)/(1-{qb})','Inklusi-eksklusi memberi jumlah dua peluang. Gunakan rasio untuk menentukan masing-masing peluang, lalu bentuk peluang bersyarat pada komplemen B.',probability=True)
    if name=='kelas11_tl' and bab==3 and code=='E':
        a=r.randint(6,20);b=r.randint(2,a-1);theta=r.choice([60,90,120]);sq=a*a+b*b-2*a*b*s.cos(s.pi*theta/180)
        prod='((S*S-Q)/(2*(1+cos(pi*t/180))))'
        return make('cosine_rule','Dua sisi segitiga adalah a>b>0 dengan jumlah S. Sudut apit kedua sisi t derajat dan kuadrat sisi di depannya Q. Tentukan $a^3-b^3$.',{'S':a+b,'Q':sq,'t':theta},f'sqrt(S*S-4*{prod})*(S*S-{prod})','Gabungkan jumlah sisi dengan aturan kosinus untuk mendapatkan hasil kali sisi, pilih selisih positif, lalu gunakan selisih kubik.')
    if name=='kelas11_tl' and bab==4 and code=='C':
        ux=r.randint(2,12);uy=r.randint(2,12);vx=r.randint(2,12);vy=r.randint(2,12);k=r.randint(2,7)
        if ux*vy==uy*vx:return None
        return make('vector_proof','Sisi-sisi jajar genjang dari satu titik diwakili vektor u dan v. Diketahui $|u|^2=A$, $|u+v|^2=P$, dan $|u-v|^2=Q$. Dengan identitas vektor, tentukan $|u+kv|^2$.',{'A':ux*ux+uy*uy,'P':(ux+vx)**2+(uy+vy)**2,'Q':(ux-vx)**2+(uy-vy)**2,'k':k},'A+k*k*((P+Q)/2-A)+k*(P-Q)/2','Buktikan hubungan kedua diagonal dengan jumlah kuadrat sisi dan hasil kali titik. Rekonstruksi panjang v dan u titik v, lalu kembangkan kuadrat panjang kombinasi baru.')
    if name=='kelas12_tl' and bab==4 and code=='G':
        mean=r.randint(35,90);sd=r.randint(3,12);z=r.choice([-1,1,2]);x1=mean-sd;x2=mean+2*sd;cut=mean+z*sd
        sigma='((B-A)/3)';mu=f'(A+{sigma})';zval=f'((C-{mu})/{sigma})'
        expr=f'1-Piecewise((F1,Eq({zval},-1)),(F2,Eq({zval},1)),(F3,Eq({zval},2)))'
        return make('normal',r'X berdistribusi normal dengan parameter belum diketahui. Nilai A mempunyai skor baku -1, sedangkan B mempunyai skor baku 2. Tabel memberikan $\Phi(-1)=F1$, $\Phi(1)=F2$, dan $\Phi(2)=F3$. Tentukan $P(X>C)$.',{'A':x1,'B':x2,'C':cut,'F1':s.Rational(1587,10000),'F2':s.Rational(8413,10000),'F3':s.Rational(9772,10000)},expr,'Dua data skor baku menentukan simpangan baku dan rata-rata. Standardisasi batas baru, baca tabel, lalu ambil peluang ekor kanan.',probability=True)
    return None
