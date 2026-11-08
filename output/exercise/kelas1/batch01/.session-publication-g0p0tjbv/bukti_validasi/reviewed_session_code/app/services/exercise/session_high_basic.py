"""Direct and linked curriculum recipes for SD5/6 and SMP.

The registry describes the actual task; a requested quota is never a label input.
"""
from __future__ import annotations
import math
import sympy as s

POLICY='codex-session-content-v3'


def solve(cert):
    if cert['type']=='session_basic_linked':
        a=solve(cert['left']);b=solve(cert['right'])
        return s.simplify(a+b if cert['operation']=='sum' else a-b)
    assert cert['type']=='session_basic_expression'
    names={k:s.sympify(v) for k,v in cert['inputs'].items()};names.update(Max=s.Max,Min=s.Min,floor=s.floor,ceiling=s.ceiling,sqrt=s.sqrt,pi=s.pi,gcd=s.gcd,lcm=s.lcm,Mod=s.Mod,factorial=s.factorial)
    value=s.simplify(s.sympify(cert['expression'],locals=names));assert not value.free_symbols and value.is_finite is True
    return value


def fmt(value):return '$'+s.latex(s.sympify(value))+'$'


def model(question,expression,inputs,kind,explanation,visual=False):
    cert={'type':'session_basic_expression','expression':expression,'inputs':inputs,'reviewedTask':'direct_concept_procedure','family':kind}
    value=solve(cert);scene=None
    if visual:
        # Symbols in the question refer to factual data in the retained table.
        scene={'kind':'table','headers':['Data','Nilai'],'rows':[[key,str(v)] for key,v in inputs.items()]}
        cert['visual_bindings']=[{'input':key,'path':['rows',i,1],'display_string':True} for i,key in enumerate(inputs)]
        question='Gunakan data pada tabel gambar. '+question
    else:
        question='Diketahui '+', '.join(f'${key}={s.latex(s.sympify(v))}$' for key,v in inputs.items())+'. '+question
    wrong=[]
    proposals=[value+1,value-1,value+2,value/2,2*value,-value]
    if 0<value<1:proposals=[1-value,value/2,(value+1)/2,value**2,s.Rational(1,3),s.Rational(2,3)]
    for t in proposals:
        t=s.simplify(t)
        if t==value or t in wrong:continue
        wrong.append(t)
        if len(wrong)==3:break
    answer=fmt(value)
    result={'question':question,'answer':answer,'wrong':list(map(fmt,wrong)),'explanation':explanation+' Substitusi data memberi '+answer+'.','kind':kind,'steps':1,'rationale':'Menerapkan satu konsep melalui prosedur langsung; data dan hubungan yang diperlukan diberikan.','scene':scene,'visual_kind':'math_scene','certificate':cert}
    result['assessment']=assess(result,0);return result


def assess(item,grade):
    cert=item['certificate'];kind=cert['type']
    if kind=='session_basic_expression':
        assert cert['reviewedTask']=='direct_concept_procedure' and cert['family'].startswith(('s5_','s6_','s7_','s8_','s9_'))
        level='easy';reason='Satu konsep dengan data dan rumus/hubungan langsung yang cukup; tidak ada parameter tersembunyi.';steps=1
    elif kind=='session_basic_linked':
        assert cert['left']['type']==cert['right']['type']=='session_basic_expression'
        level='medium';reason='Menyelesaikan dua penerapan rutin pada data berbeda lalu menghubungkan kedua hasil sesuai pertanyaan.';steps=3
    else:raise ValueError('Unreviewed basic task')
    return {'assessedLevel':level,'reason':reason,'steps':steps,'flags':[],'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,'apiCalls':0}


def direct(grade,bab,code,r,visual=False):
    a=r.randint(3,32);b=r.randint(2,21);c=r.randint(2,15);k=r.randint(2,9)
    def q(stem,expr,data,topic,why):return model(stem,expr,data,f's{grade}_{topic}',why,visual)
    if grade==5:
        if bab in (1,9):
            limit=100000 if bab==1 else 1000000;n=r.randint(limit//10,limit-1);pos=r.choice([10,100,1000,10000])
            if code=='A':return q('Tentukan nilai tempat digit pada posisi $P$ dalam bilangan $N$. Gunakan $((N\\div P)\\text{ dibulatkan ke bawah}\\bmod10)P$.','Mod(floor(N/P),10)*P',{'N':n,'P':pos},'nilai_tempat','Ambil digit pada posisi P, lalu kalikan dengan nilai posisinya')
            if code=='B':return q('Manakah bilangan terbesar di antara $A,B,C$?','Max(A,B,C)',{'A':n,'B':r.randint(limit//10,limit-1),'C':r.randint(limit//10,limit-1)},'banding','Bandingkan digit mulai nilai tempat terbesar')
            if code=='C':return q('Bilangan tersusun dari $A$ puluh ribuan, $B$ ribuan, dan $C$ satuan. Tentukan bilangan itu.','10000*A+1000*B+C',{'A':r.randint(1,9) if bab==1 else r.randint(10,89),'B':r.randint(1,9),'C':r.randint(1,999)},'komposisi','Jumlahkan nilai setiap kelompok')
            return q('Terdapat $A$ benda dan datang lagi $B$ benda. Berapa jumlahnya?','A+B',{'A':r.randint(1000,40000),'B':r.randint(1000,40000)},'operasi_cacah','Penjumlahan menggabungkan kedua jumlah')
        if bab==2:
            if code=='A':return q('Berapa kelipatan positif ke-$K$ dari $A$?','A*K',{'A':a,'K':k},'kelipatan','Kelipatan ke-K adalah A dikali K')
            if code=='B':return q('Kelipatan persekutuan terkecil $A$ dan $B$ adalah ....','lcm(A,B)',{'A':a,'B':b},'kelipatan_persekutuan','Cari kelipatan positif terkecil yang habis dibagi kedua bilangan')
            if code=='C':return q('Bilangan $N$ memiliki faktor prima berbentuk $p^Aq^B$, dengan p dan q berbeda. Banyak faktornya diberikan oleh $(A+1)(B+1)$. Tentukan banyak faktor tersebut.','(A+1)*(B+1)',{'A':r.randint(1,6),'B':r.randint(1,5)},'faktor','Eksponen faktor dapat dipilih dari nol sampai pangkat masing-masing')
            if code=='D':return q('Tentukan faktor persekutuan terbesar dari $A$ dan $B$.','gcd(A,B)',{'A':a*k,'B':b*k},'faktor_persekutuan','Faktor yang membagi kedua bilangan dipilih yang terbesar')
            return q('Faktorisasi dua bilangan adalah $2^A3^B$ dan $2^C3^D$. Tentukan FPB-nya dengan mengambil pangkat terkecil setiap prima.','2**Min(A,C)*3**Min(B,D)',{'A':r.randint(1,5),'B':r.randint(1,4),'C':r.randint(1,5),'D':r.randint(1,4)},'fpb_prima','FPB memakai pangkat terkecil pada setiap faktor prima')
        if bab==3:
            den=r.randint(5,35);u=r.randint(1,den-2);v=r.randint(1,den-u)
            if code=='A':return q('Pecahan terbesar di antara $A/D$ dan $B/D$ adalah ....','Max(A,B)/D',{'A':u,'B':v,'D':den},'banding_pecahan','Penyebut sama, bandingkan pembilang')
            op='+' if code=='B' else '-';u,v=max(u,v),min(u,v)
            return q(f'Hitung $A/D{op}B/D$.',f'(A{op}B)/D',{'A':u,'B':v,'D':den},'operasi_pecahan','Untuk penyebut sama, operasikan pembilang dan pertahankan penyebut')
        if bab==4:
            if code=='B':return q('Segitiga sama kaki mempunyai kaki $A$ cm dan alas $B$ cm. Tentukan kelilingnya.','2*A+B',{'A':a+20,'B':b},'keliling_segitiga','Keliling adalah jumlah ketiga sisi')
            if code=='D':return q('Segi banyak beraturan mempunyai $N$ sisi, masing-masing $S$ cm. Tentukan kelilingnya.','N*S',{'N':r.randint(5,12),'S':a},'keliling_poligon','Jumlahkan semua sisi yang sama panjang')
            if code=='E':return q('Dua persegi panjang berukuran $A\\times B$ dan $C\\times D$ cm ditempel pada ruas batas sepanjang $T$ cm. Gunakan $K=2(A+B)+2(C+D)-2T$. Tentukan K.','2*(A+B+C+D)-2*T',{'A':a+10,'B':b+10,'C':c+10,'D':k+10,'T':r.randint(1,8)},'keliling_gabungan_terpandu','Ruas bersama tidak berada pada batas luar dan semula terhitung dua kali')
            return q('Persegi panjang mempunyai panjang $A$ cm dan lebar $B$ cm. Tentukan kelilingnya.','2*(A+B)',{'A':a+20,'B':b},'keliling','Keliling merupakan dua panjang ditambah dua lebar')
        if bab==5:
            if code=='C':return q('Dua daerah persegi panjang berukuran $A\\times B$ dan $C\\times D$ cm tidak bertumpang tindih. Tentukan luas gabungannya.','A*B+C*D',{'A':a,'B':b,'C':c,'D':k},'luas_gabungan','Jumlahkan luas dua daerah yang tidak bertumpang tindih')
            if code=='D':return q('Persegi mempunyai sisi $S$ cm. Tentukan luasnya.','S**2',{'S':a},'hubungan_luas','Persegi luasnya sisi dikali sisi')
            return q('Daerah persegi panjang terdiri atas $A$ baris dan $B$ petak satuan tiap baris. Tentukan luas dalam petak satuan.','A*B',{'A':a,'B':b},'luas','Luas dihitung dari banyak seluruh petak satuan')
        if bab==6:
            if code=='A':return q('Ada $N$ persegi panjang. Setiap bangun memiliki empat sudut siku-siku. Berapa sudut siku-siku seluruhnya?','4*N',{'N':a},'sudut_siku','Setiap persegi panjang menyumbang empat sudut siku-siku')
            return q('Dua sinar dibaca pada skala busur yang sama, masing-masing $A$ dan $B$ derajat, dengan A>B. Besar sudut di antaranya adalah ....','A-B',{'A':r.randint(100,170),'B':r.randint(5,85)},'ukur_sudut','Selisih pembacaan pada skala yang sama memberi besar sudut')
        if bab==7:
            if code=='A':return q('Segitiga memiliki dua sudut $A$ dan $B$ derajat. Tentukan sudut ketiganya.','180-A-B',{'A':r.randint(25,70),'B':r.randint(25,70)},'ciri_segitiga','Jumlah sudut segitiga adalah 180 derajat')
            return q('Setiap persegi dan persegi panjang mempunyai empat sudut siku-siku. Ada $A$ persegi dan $B$ persegi panjang. Berapa seluruh sudut siku-sikunya?','4*(A+B)',{'A':a,'B':b},'ciri_segiempat','Kedua jenis bangun sama-sama memiliki empat sudut siku-siku')
        if bab==8:
            if code=='B':return q('Satu simbol piktogram mewakili $S$ siswa. Ada $N$ simbol utuh. Berapa siswa yang ditunjukkan?','S*N',{'S':r.randint(2,8),'N':a},'piktogram','Kalikan banyak simbol dengan nilai setiap simbol')
            return q('Data banyak benda pada kategori A, B, C adalah $A,B,C$. Berapa banyak pada kategori terbanyak?','Max(A,B,C)',{'A':a,'B':b,'C':c},'data_baca','Bandingkan ketiga frekuensi dan ambil yang terbesar')
    if grade==6:
        if bab==1:
            if code=='C':return q('Massa dua benda adalah $A/10$ kg dan $B/10$ kg. Berapa massa totalnya dalam kg?','(A+B)/10',{'A':r.randint(12,99),'B':r.randint(12,99)},'desimal','Jumlahkan nilai desimal dengan menyamakan nilai tempat')
            den=r.randint(5,30);u=r.randint(1,den-1);v=r.randint(1,den-1)
            expr='A*B/D**2' if code=='A' else 'A/B';op='\\times' if code=='A' else '\\div'
            return q(f'Hitung $(A/D){op}(B/D)$.',expr,{'A':u,'B':v,'D':den},'operasi_pecahan','Terapkan aturan perkalian atau pembagian pecahan, lalu sederhanakan')
        if bab==2:
            if code=='A':return q('Kelompok A dan B masing-masing berisi $A$ dan $B$ benda. Nyatakan rasio A terhadap B dalam bentuk pecahan paling sederhana.','A/B',{'A':a,'B':b},'rasio','Rasio A terhadap B adalah A dibagi B')
            if code=='B':return q('Untuk $A$ sajian diperlukan $B$ sendok sirup. Berapa sendok untuk $C$ sajian dengan rasio yang sama?','B*C/A',{'A':a,'B':b,'C':c},'rasio_senilai','Jumlah sirup per sajian dikalikan jumlah sajian baru')
            return q('Paket berisi $N$ barang berharga $H$ rupiah. Berapa harga satu barang?','H/N',{'N':a,'H':a*b*1000},'penerapan_rasio','Bagi harga paket dengan banyak barang')
        if bab==3:
            if code=='A':return q('Balok tersusun dari kubus satuan dengan panjang $P$, lebar $L$, dan tinggi $T$ kubus. Berapa kubus satuan seluruhnya?','P*L*T',{'P':r.randint(2,12),'L':r.randint(2,12),'T':r.randint(2,12)},'konstruksi_kubus','Hitung kubus setiap lapisan lalu banyak lapisan')
            if code=='B':return q('Susunan menara kubus menempati $A$ petak pada baris depan dan $B$ petak lain pada baris belakang, tanpa petak berimpit. Dilihat dari atas, berapa petak tertutup?','A+B',{'A':r.randint(1,12),'B':r.randint(1,12)},'visualisasi_spasial','Tampak atas menghitung posisi yang ditempati, bukan tinggi menara')
            return q('Dari titik $(A,B)$ bergerak $U$ petak ke kanan dan $V$ ke atas. Berapa jumlah koordinat titik akhirnya?','A+B+U+V',{'A':a,'B':b,'U':c,'V':k},'lokasi','Koordinat akhir adalah (A+U,B+V), kemudian jumlahkan')
        if bab==4:
            if code=='A':return q('Kantong memuat $A$ bola merah dan $B$ bola biru. Jika satu bola dipilih acak, berapa peluang merah?','A/(A+B)',{'A':a,'B':b},'skala_peluang','Peluang adalah banyak hasil yang diinginkan dibagi semua hasil sama mungkin')
            return q('Dua kantong masing-masing mempunyai $A$ dan $B$ bola merah dari total sama, yaitu $N$ bola. Berapa selisih peluang merah keduanya?','Abs(A-B)/N',{'A':a,'B':b,'N':a+b+c},'banding_peluang','Total sama, selisih peluang adalah selisih banyak merah dibagi total')
    if grade==7:
        if bab==1:
            if code=='C':return q('Tentukan FPB dari bilangan $A$ dan $B$.','gcd(A,B)',{'A':a*k,'B':b*k},'faktor_bulat','Cari faktor positif terbesar yang membagi kedua bilangan')
            if code=='A':return q('Di antara bilangan bulat $A,B,C$, tentukan yang terbesar.','Max(A,B,C)',{'A':r.randint(-45,40),'B':r.randint(-45,40),'C':r.randint(-45,40)},'bilangan_bulat','Pada garis bilangan, nilai terbesar terletak paling kanan')
            return q('Hitung operasi bilangan bulat $A+B$.','A+B',{'A':r.randint(-40,40),'B':r.randint(-40,40)},'operasi_bulat','Terapkan penjumlahan sesuai tanda kedua bilangan')
        if bab==2:
            if code=='A':return q('Tentukan titik tengah antara bilangan rasional $A/D$ dan $B/D$.','(A+B)/(2*D)',{'A':a,'B':a+b,'D':c},'letak_rasional','Titik tengah adalah jumlah kedua bilangan dibagi dua')
            if code=='B':return q('Manakah yang lebih besar antara $-A/D$ dan $-B/D$?','Max(-A,-B)/D',{'A':a,'B':b,'D':c},'banding_rasional','Untuk bilangan negatif, yang lebih dekat nol lebih besar')
            return q('Hitung $A/D+B/D$.','(A+B)/D',{'A':a,'B':b,'D':c},'operasi_rasional','Jumlahkan pembilang karena penyebut sama')
        if bab==3:
            if code=='A':return q('Rasio kelompok A:B adalah $A:B$, jumlah seluruhnya $N(A+B)$ benda. Berapa benda kelompok B?','N*B',{'A':a,'B':b,'N':c},'rasio','Satu bagian bernilai N benda')
            if code=='B':return q('Panjang pada peta $P$ cm, skala $1:S$. Berapa panjang sebenarnya dalam meter?','P*S/100',{'P':a,'S':r.choice([100,200,250,500,1000,2000])},'skala','Kalikan panjang peta dengan penyebut skala lalu ubah cm ke meter')
            return q('Mesin menghasilkan $N$ benda dalam $T$ menit. Berapa laju per menit?','N/T',{'N':a*b,'T':a},'laju','Laju satuan adalah banyak hasil dibagi waktu')
        if bab==4:
            if code=='A':return q('Bentuk aljabar $Ax+By+C$ memiliki koefisien x dan y. Tentukan jumlah kedua koefisien itu.','A+B',{'A':a,'B':-b,'C':c},'unsur_aljabar','Koefisien x adalah A dan koefisien y adalah B')
            if code=='B':return q('Tentukan nilai $P(X)$ jika $P(x)=Ax+B$.','A*X+B',{'A':a,'B':b,'X':c},'operasi_aljabar','Substitusikan nilai X ke bentuk aljabar')
            return q('Biaya sewa terdiri dari biaya tetap $B$ ribu rupiah dan $A$ ribu rupiah per jam. Tentukan biaya untuk $T$ jam dalam ribu rupiah.','B+A*T',{'A':a,'B':b,'T':c},'model_aljabar','Biaya total adalah biaya tetap ditambah tarif dikali waktu')
        if bab==5:
            if code=='A':return q('Dua sudut saling berpelurus. Jika satu sudut $A$ derajat, tentukan yang lain.','180-A',{'A':r.randint(12,167)},'hubungan_sudut','Sudut berpelurus berjumlah 180 derajat')
            return q('Dua segitiga sebangun memiliki faktor skala $K$. Sisi bersesuaian pada segitiga kecil $A$ cm. Berapa sisi pada segitiga besar?','A*K',{'A':a,'K':k},'kesebangunan','Sisi bersesuaian dikalikan faktor skala yang sama')
        if bab==6:
            if code=='E':return q('Kategori memiliki frekuensi $F$ dari total $N$ data. Berapa sudut sektornya pada diagram lingkaran?','360*F/N',{'F':a,'N':a+b+c},'diagram_lingkaran','Sudut kategori adalah proporsi dikali 360 derajat')
            if code=='B':return q('Dari $N$ responden, $A$ jawaban berupa data numerik dan sisanya nama kategori. Berapa jawaban berupa data kategori?','N-A',{'N':a+b,'A':a},'jenis_data','Pisahkan jawaban numerik dan kategori dari jumlah seluruh responden')
            if code=='F':return q('Data berupa frekuensi $A,B,C$ untuk tiga kategori. Bila disajikan dengan diagram batang, berapa tinggi batang kategori terbanyak?','Max(A,B,C)',{'A':a,'B':b,'C':c},'pilih_diagram','Diagram batang membandingkan frekuensi kategori; batang tertinggi sesuai frekuensi terbesar')
            return q('Hasil pengumpulan data memiliki frekuensi $A,B,C$ pada tiga kategori. Berapa total data?','A+B+C',{'A':a,'B':b,'C':c},'statistika_data','Jumlah seluruh kategori memberi banyak data')
    if grade==8:
        if bab==1:
            if code=='A':return q('Jika $2^A\\times2^B=2^n$, tentukan n.','A+B',{'A':a,'B':b},'pangkat','Perkalian dengan basis sama menjumlahkan pangkat')
            if code=='B':return q('Sederhanakan $\\sqrt{A^2D}$, dengan A positif dan D tidak memiliki faktor kuadrat lebih dari satu.','A*sqrt(D)',{'A':a,'D':r.choice([2,3,5,6,7,10,11,13])},'akar','Keluarkan faktor kuadrat A kuadrat dari akar')
            return q('Bilangan bentuk baku $A\\times10^N$ dikalikan $10^K$. Pangkat sepuluh bentuk baku hasilnya adalah ....','N+K',{'A':r.randint(2,9),'N':r.randint(-10,10),'K':r.randint(1,9)},'bentuk_baku','Koefisien tetap dan pangkat sepuluh dijumlahkan')
        if bab==2:
            u,v,h=r.choice([(3,4,5),(5,12,13),(8,15,17),(7,24,25)]);scale=r.randint(1,25)
            if code=='E':return q('Dua titik berkoordinat $(0,0)$ dan $(A,B)$. Tentukan jarak kedua titik.','sqrt(A**2+B**2)',{'A':u*scale,'B':v*scale},'jarak','Jarak koordinat memakai akar jumlah kuadrat selisih koordinat')
            if code=='C':return q('Segitiga siku-siku sama kaki mempunyai kaki $A$ cm. Tentukan sisi miringnya.','A*sqrt(2)',{'A':r.randint(2,80)},'segitiga_istimewa','Segitiga 45-45-90 memiliki sisi miring kaki dikali akar dua')
            return q('Segitiga siku-siku mempunyai dua kaki $A$ dan $B$ cm. Tentukan panjang sisi miringnya.','sqrt(A**2+B**2)',{'A':u*scale,'B':v*scale},'pythagoras','Gunakan kuadrat sisi miring sama dengan jumlah kuadrat kedua kaki')
        if bab==3:
            if code in 'AB':return q('Tentukan x yang memenuhi $Ax+B=C$.','(C-B)/A',{'A':a,'B':b,'C':a*c+b},'persamaan_linear','Kurangi B dari kedua ruas lalu bagi dengan A')
            return q('Untuk x bilangan cacah dan $Ax+B\\le C$, tentukan x terbesar.','floor((C-B)/A)',{'A':a,'B':b,'C':a*c+b+k},'pertidaksamaan','Isolasi x lalu ambil bilangan cacah terbesar yang memenuhi batas')
        if bab==4:
            if code=='A':return q('Relasi R dinyatakan oleh pasangan $(1,A),(2,B),(3,C)$. Berapa jumlah nilai pada daerah hasil jika A,B,C semuanya berbeda?','A+B+C',{'A':a,'B':a+b,'C':a+b+c},'relasi','Daerah hasil berisi komponen kedua pasangan; jumlahkan tiga nilai berbeda itu')
            if code=='B':return q('Fungsi $f(x)=Ax+B$. Tentukan $f(T)$.','A*T+B',{'A':a,'B':b,'T':c},'fungsi','Setiap input dipasangkan ke nilai fungsi melalui substitusi')
            return q('Terdapat N unsur pada masing-masing dua himpunan. Satu pasangan unsur sudah ditetapkan dan sisanya bebas. Dengan rumus $(N-1)!$, berapa korespondensi satu-satu yang mungkin?','factorial(N-1)',{'N':r.randint(3,12)},'bijeksi','Pasangan tetap menyisakan N-1 unsur yang dapat dipermutasi')
        if bab==5:
            return q('Garis melalui titik $(0,B)$ dan $(T,B+A T)$. Tentukan gradiennya.','(B+A*T-B)/T',{'A':r.randint(-12,12) or 2,'B':r.randint(-15,15),'T':r.randint(1,15)},'garis_gradien','Gradien adalah perubahan y dibagi perubahan x')
        if bab==6:
            if code=='A':return q('Tiga data adalah $A,B,C$. Tentukan rata-ratanya.','(A+B+C)/3',{'A':a,'B':b,'C':c},'pemusatan','Rata-rata adalah jumlah data dibagi banyaknya')
            return q('Tiga data adalah $A,B,C$. Tentukan jangkauannya.','Max(A,B,C)-Min(A,B,C)',{'A':a,'B':b,'C':c},'penyebaran','Jangkauan adalah nilai terbesar dikurangi terkecil')
    if grade==9:
        if bab==1:
            if code=='A':return q('Pasangan $(x,Y)$ memenuhi $Ax+BY=C$. Tentukan x.','(C-B*Y)/A',{'A':a,'B':b,'Y':c,'C':a*k+b*c},'pldv','Substitusi nilai Y kemudian isolasi x')
            return q('Sistem $x+y=S$ dan $x-y=D$ diberikan. Tentukan x.','(S+D)/2',{'S':a+b,'D':a-b},'spldv','Jumlahkan kedua persamaan untuk memperoleh 2x')
        if bab==2:
            if code=='A':return q('Prisma beralas segi-N mempunyai N rusuk alas, N rusuk atas dan N rusuk tegak. Berapa seluruh rusuknya?','3*N',{'N':r.randint(3,40)},'bangun_ruang','Jumlahkan tiga kelompok rusuk prisma')
            if code=='B':return q('Balok memiliki panjang P, lebar L, tinggi T cm. Tentukan luas permukaannya.','2*(P*L+P*T+L*T)',{'P':a,'L':b,'T':c},'luas_permukaan','Jumlahkan luas enam sisi balok dalam tiga pasang')
            if code=='C':return q('Balok berukuran P, L, T cm. Tentukan volumenya.','P*L*T',{'P':a,'L':b,'T':c},'volume','Volume balok adalah panjang dikali lebar dikali tinggi')
            if code=='D':return q('Lingkaran berjari-jari R cm. Tentukan kelilingnya dalam bentuk eksak yang memuat pi.','2*pi*R',{'R':a},'lingkaran','Keliling lingkaran adalah dua kali pi kali jari-jari')
            if code=='E':return q('Tabung tertutup berjari-jari R dan tinggi T cm. Tentukan luas permukaannya dalam bentuk eksak.','2*pi*R*(R+T)',{'R':a,'T':b},'luas_lengkung','Dua lingkaran alas dan tutup ditambah selimut tabung')
            return q('Tabung berjari-jari R dan tinggi T cm. Tentukan volumenya dalam bentuk eksak.','pi*R**2*T',{'R':a,'T':b},'volume_lengkung','Volume adalah luas alas lingkaran dikali tinggi')
        if bab==3:
            if code=='A':return q('Titik $(X,Y)$ ditranslasi oleh $(U,V)$. Tentukan jumlah koordinat bayangannya.','X+U+Y+V',{'X':a,'Y':b,'U':-c,'V':k},'translasi','Tambahkan komponen translasi ke koordinat bersesuaian')
            if code=='B':return q('Titik $(X,Y)$ dicerminkan terhadap sumbu y. Tentukan jumlah koordinat bayangannya.','-X+Y',{'X':a,'Y':b},'refleksi','Pencerminan sumbu y mengubah tanda koordinat x')
            if code=='C':return q('Titik $(X,Y)$ diputar 90 derajat berlawanan arah jarum jam terhadap pusat O. Tentukan jumlah koordinat bayangannya.','X-Y',{'X':a,'Y':b},'rotasi','Rotasi 90 derajat mengubah (X,Y) menjadi (-Y,X)')
            if code=='D':return q('Dua segitiga kongruen mempunyai sisi bersesuaian $Ax+B$ dan C cm. Tentukan x.','(C-B)/A',{'A':a,'B':b,'C':a*k+b},'kongruen','Sisi bersesuaian bangun kongruen sama panjang')
            return q('Titik $(X,Y)$ didilatasi berpusat O dengan faktor K. Tentukan jumlah koordinat bayangannya.','K*(X+Y)',{'X':a,'Y':b,'K':k},'dilatasi','Kalikan kedua koordinat dengan faktor dilatasi yang sama')
        if bab==4:
            if code=='A':return q('Ada A hasil yang diinginkan dari N hasil sama mungkin. Tentukan peluangnya.','A/N',{'A':a,'N':a+b},'peluang','Peluang adalah banyak kejadian dibagi semua hasil sama mungkin')
            if code=='B':return q('Dalam N percobaan, kejadian muncul F kali. Tentukan peluang empirisnya.','F/N',{'F':a,'N':a+b+c},'empiris','Frekuensi relatif adalah banyak kemunculan dibagi banyak percobaan')
            if code=='C':return q('Peluang suatu kejadian A/B. Percobaan dilakukan N kali. Tentukan frekuensi harapannya.','N*A/B',{'A':a,'B':a+b,'N':r.randint(10,300)},'harapan','Frekuensi harapan adalah peluang dikali banyak percobaan')
            return q('Populasi memiliki A anggota kelompok tertentu dari total N. Sampel proporsional berukuran S. Berapa alokasi sampel kelompok itu?','A*S/N',{'A':a*k,'N':(a+b)*k,'S':a+b},'sampel','Alokasi proporsional memakai proporsi kelompok dikali ukuran sampel')
    raise ValueError(('Unknown direct curriculum',grade,bab,code))


def generate(grade,bab,code,level,r,visual,index):
    if level=='easy':return direct(grade,bab,code,r,visual)
    if level!='medium':return None
    left=direct(grade,bab,code,r,visual);right=direct(grade,bab,code,r,visual)
    cert={'type':'session_basic_linked','left':left['certificate'],'right':right['certificate'],'operation':'difference'}
    value=solve(cert)
    scene=None
    if visual:
        # Both panels retain their own meaningful input labels.
        scene={'kind':'table','headers':['Situasi','Data','Nilai'],'rows':[['I',key,str(v)] for key,v in cert['left']['inputs'].items()]+[['II',key,str(v)] for key,v in cert['right']['inputs'].items()]}
    first=left['question'].replace('Gunakan data pada tabel gambar. ','');second=right['question'].replace('Gunakan data pada tabel gambar. ','')
    text='Kerjakan dua situasi berikut secara terpisah. Situasi I: '+first+' Situasi II: '+second+' Berapa hasil situasi I dikurangi hasil situasi II?'
    if visual:text='Data masing-masing situasi terdapat pada tabel gambar. '+text
    answer=fmt(value);wrong=[]
    for t in [value+1,value-1,value+2,-value,2*value]:
        if t!=value and t not in wrong:wrong.append(t)
        if len(wrong)==3:break
    item={'question':text,'answer':answer,'wrong':list(map(fmt,wrong)),'explanation':'Selesaikan situasi I: '+left['explanation']+' Situasi II: '+right['explanation']+' Selisih hasilnya '+answer+'.','kind':left['kind']+'_linked','steps':3,'rationale':'Dua penerapan konsep rutin dihubungkan melalui selisih hasil.','scene':scene,'visual_kind':'math_scene','certificate':cert}
    item['assessment']=assess(item,grade);return item
