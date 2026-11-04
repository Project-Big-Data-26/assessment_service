"""SD5/6 variation families grounded in the corresponding validated subchapters."""
import math
import sympy as s
from .replenishment_math import numeric,text,m,rp,factors,statistics,probability,pair


def decimal_text(value):
    return f'{float(value):.1f}'.replace('.',',')


def prime_product(value):
    return ' × '.join(f'${p}^{{{e}}}$' if e>1 else str(p) for p,e in s.factorint(value).items())


def generate(book,bab,code,level,r):
    grade=int(book[5:]); a=r.randint(3,15); b=r.randint(2,12); k=r.randint(2,8)
    if grade==6:
        if bab==1 and code in 'AB':
            p=s.Rational(a,a+b); q=s.Rational(b,b+k)
            if code=='A':
                value=p*q
                return numeric(f'Panjang seutas pita {m(p)} meter. Sebanyak {m(q)} bagian dari pita itu digunakan. Berapa meter panjang pita yang digunakan?',value,
                               f'Panjang yang dipakai = {p} × {q} = {value} meter.','perkalian_pecahan',wrong=[p+q,p/q,p-q])
            total=s.Rational(a*b,2); part=s.Rational(b,2); count=total/part
            if level=='hard':
                total+=s.Rational(1,4); count=s.floor(total/part)
                return numeric(f'Tersedia {m(total)} kg adonan. Tiap loyang memerlukan {m(part)} kg. Berapa loyang penuh paling banyak yang dapat dibuat?',count,
                               f'Jumlah loyang = ({total})/({part}) = {total/part}. Karena yang dihitung loyang penuh, ambil bagian bulatnya, yaitu {count}.','pembagian_pecahan_bersyarat')
            return numeric(f'Sebanyak {m(total)} liter minuman dituangkan ke botol berkapasitas {m(part)} liter. Berapa botol yang terisi penuh?',count,
                           f'Banyak botol = {total} ÷ {part} = {count}.','pembagian_pecahan')
        if bab==1 and code=='C':
            v=s.Rational(a*10+b,10); w=s.Rational(k,10)
            draft=numeric(f'Massa sebuah paket {decimal_text(v)} kg. Setelah ditambah kemasan, massanya bertambah {decimal_text(w)} kg. Berapa massa paket beserta kemasan?',v+w,
                          f'Samakan nilai tempat desimal, lalu jumlahkan: {decimal_text(v)} + {decimal_text(w)} = {decimal_text(v+w)} kg.','operasi_desimal',wrong=[v-w,v+w*10,v+w/10])
            fmt=lambda z: f'{float(s.sympify(z)):.2f}'.rstrip('0').rstrip('.').replace('.',',')
            draft.answer=fmt(draft.proof['value']);draft.distractors=[fmt(z) for z in draft.proof['options'][1:]]
            return draft
        if bab==2:
            if code=='A':
                return numeric(f'Satu paket berisi {a} bibit dan harganya {rp(a*b*1000)}. Berapa harga setiap bibit jika harganya sama?',b*1000,
                               f'Harga satuan = {a*b*1000}/{a} = {b*1000} rupiah.','rasio_satuan')
            if code=='B':
                return numeric(f'Untuk membuat {a} gelas minuman dibutuhkan {b} sendok sirup. Dengan takaran yang sama, berapa sendok sirup untuk {a*k} gelas?',b*k,
                               f'Banyak gelas menjadi {k} kali, sehingga sirup juga {k} kali: {b}×{k}={b*k}.','rasio_senilai')
            return numeric(f'Rasio bibit mawar terhadap melati adalah {a}:{b}. Jika jumlah seluruh bibit {k*(a+b)}, berapa banyak bibit mawar?',a*k,
                           f'Jumlah bagian rasio {a+b}. Tiap bagian bernilai {k}. Bibit mawar {a}×{k}={a*k}.','penerapan_rasio')
        if bab==3:
            if code=='A':
                c=r.randint(2,7); value=a*b*c
                return numeric(f'Model balok tersusun dari kubus satuan. Susunan alas {a} baris dan {b} kubus tiap baris, dengan {c} lapisan penuh. Berapa kubus satuan penyusunnya?',value,
                               f'Tiap lapisan memuat {a*b} kubus. Dengan {c} lapisan ada {a*b}×{c}={value} kubus.','susunan_kubus')
            if code=='B':
                heights=[r.randint(1,6) for _ in range(3)]
                return numeric(f'Tiga menara kubus diletakkan berjajar dari kiri ke kanan, dengan tinggi {heights[0]}, {heights[1]}, dan {heights[2]} kubus. Jika dilihat dari atas, setiap menara menempati satu petak terpisah. Berapa petak yang tampak terisi dari atas?',3,
                               'Setiap menara menempati satu petak alas. Perbedaan tinggi tidak mengubah banyak petak pada tampak atas, sehingga ada 3 petak.','visualisasi_spasial')
            x1=r.randint(1,5); y1=r.randint(1,6); x2=x1+r.randint(2,5); y2=y1+r.randint(2,5)
            return numeric(f'Pada denah berpetak, sebuah bidak berpindah dari {pair(x1,y1)} ke {pair(x2,y2)}. Tiap langkah hanya boleh satu petak mendatar atau tegak. Berapa langkah paling sedikit?',x2-x1+y2-y1,
                           f'Perpindahan mendatar {x2-x1} petak dan tegak {y2-y1} petak. Minimum jumlah langkah = {x2-x1+y2-y1}.','lokasi_pada_petak')
        if bab==4:
            if code=='A':return probability(r,level)
            p=s.Rational(a,a+b); q=s.Rational(a+1,a+b+1)
            return text(f'Kotak P memuat {a} bola merah dan {b} biru. Kotak Q memuat {a+1} merah dan {b} biru. Satu bola diambil acak dari masing-masing kotak. Pernyataan yang tepat adalah ....',
                        'Peluang merah di Q lebih besar daripada di P.',
                        ['Peluang merah di P lebih besar daripada di Q.','Peluang merah di kedua kotak sama.','Peluang merah di kedua kotak pasti 1.'],
                        f'Peluang P={p} dan Q={q}. Karena {q}>{p}, peluang di Q lebih besar.','membandingkan_peluang')
    if bab in (1,9):
        limit=100000 if bab==1 else 1000000
        n=r.randint(limit//10,limit-1)
        if code=='A':
            position=r.randint(1,4 if bab==1 else 5); digit=(n//10**position)%10
            if level=='hard':
                delta=r.randint(1,4); new=n+delta*10**position
                if new>=limit:new=n-delta*10**position
                return numeric(f'Bilangan {n:,} diubah menjadi {new:,}. Berapa besar perubahan nilai bilangan tersebut?'.replace(',','.'),abs(new-n),
                               f'Selisih kedua bilangan = |{new}-{n}| = {abs(new-n)}. Perubahan ditentukan oleh nilai tempat digit.','perubahan_nilai_tempat')
            place_name={1:'puluhan',2:'ratusan',3:'ribuan',4:'puluh ribuan',5:'ratus ribuan'}[position]
            return numeric(f'Pada bilangan {n:,}, berapa nilai angka pada tempat {place_name}?'.replace(',','.'),digit*10**position,
                           f'Digit pada tempat tersebut adalah {digit}, sehingga nilainya {digit}×{10**position}={digit*10**position}.','nilai_tempat')
        if code=='B':
            values=r.sample(range(max(10000,n-500),min(limit,n+500)),4); high=max(values)
            return numeric(f'Empat bilangan adalah {"; ".join(f"{v:,}".replace(",",".") for v in values)}. Bilangan terbesar adalah ....',high,
                           f'Bandingkan digit dari nilai tempat tertinggi. Urutan naiknya {sorted(values)}; yang terbesar {high}.','membandingkan_bilangan')
        if code=='C':
            place=1000 if bab==1 else 10000; rest=r.randint(1,9)*100; total=a*place+rest
            return numeric(f'Sebuah bilangan terdiri atas {a} kelompok {place} dan {rest} satuan. Berapakah bilangan itu?',total,
                           f'Komposisi bilangan = {a}×{place}+{rest}={total}.','komposisi_bilangan')
        cost=a*b*100; money=cost+r.randint(2,10)*100
        return numeric(f'Rina membawa {rp(money)} dan membeli {a} buku tulis dengan harga {rp(b*100)} per buku. Berapa sisa uangnya?',money-cost,
                       f'Biaya pembelian {a}×{b*100}={cost}. Sisa uang {money}-{cost}={money-cost} rupiah.','operasi_bilangan_cacah')
    if bab==2:
        if code=='A':
            lo=r.randint(2,8); upper=lo+r.randint(3,8); multiples=[a*n for n in range(lo,upper+1)]
            return numeric(f'Berapa banyak kelipatan {a} dari {multiples[0]} sampai {multiples[-1]}, termasuk kedua batasnya?',len(multiples),
                           f'Kelipatannya {multiples}. Ada {len(multiples)} bilangan.','kelipatan_dalam_rentang')
        if code=='B':
            value=s.ilcm(a,b)
            return numeric(f'Dua lampu menyala masing-masing setiap {a} detik dan {b} detik. Keduanya menyala bersama sekarang. Setelah berapa detik keduanya pertama kali menyala bersama lagi?',value,
                           f'Waktu bersama adalah kelipatan persekutuan terkecil. KPK({a},{b})={value}.','kelipatan_persekutuan')
        if code=='C':
            n=a*b
            if level=='easy':return numeric(f'Berapakah banyak faktor positif dari {n}?',len(factors(n)),f'Faktor positif {n} adalah {factors(n)}; jumlahnya {len(factors(n))}.','menghitung_faktor')
            eligible=[d for d in factors(n) if d>=k]
            return numeric(f'Sebanyak {n} kartu dibagi ke beberapa kotak, tiap kotak sama banyak dan tanpa sisa. Jumlah kotak paling sedikit {k}. Ada berapa pilihan jumlah kotak?',len(eligible),
                           f'Jumlah kotak merupakan faktor {n} yang minimal {k}: {eligible}. Ada {len(eligible)} pilihan.','faktor_dengan_syarat')
        if code=='D':
            u=a*k; v=b*k; common=factors(math.gcd(u,v))
            if level=='hard':
                threshold=r.choice(common); answer=sum(d>=threshold for d in common)
                return numeric(f'Kelompok akan membagi {u} pensil dan {v} penghapus ke paket identik tanpa sisa. Banyak paket minimal {threshold}. Ada berapa kemungkinan banyak paket?',answer,
                               f'Banyak paket adalah faktor bersama {common}. Yang minimal {threshold} ada {answer}.','faktor_persekutuan_bersyarat')
            return numeric(f'Berapakah faktor persekutuan terbesar dari {u} dan {v}?',math.gcd(u,v),f'Faktor persekutuannya {common}; yang terbesar {max(common)}.','faktor_persekutuan')
        u=a*k;v=b*k;g=math.gcd(u,v)
        return numeric(f'Dengan faktorisasi prima, tentukan FPB dari {u} dan {v}.',g,
                       f'Faktorisasi prima: {u} = {prime_product(u)} dan {v} = {prime_product(v)}. Ambil faktor prima bersama dengan pangkat terkecil, sehingga FPB-nya {g}.','fpb_faktorisasi')
    if bab==3:
        p=s.Rational(a,a+b);q=s.Rational(b,b+k)
        if code=='A':
            low=min(p,q); high=max(p,q)
            if p==q:return generate(book,bab,code,level,r)
            return numeric(f'Diketahui pecahan {m(p)} dan {m(q)}. Berapa selisih pecahan yang lebih besar terhadap yang lebih kecil?',high-low,
                           f'Samakan penyebut. Pecahan lebih besar {high}, lebih kecil {low}; selisihnya {high-low}.','membandingkan_pecahan',wrong=[p+q,high/low,high*low])
        value=p+q if code=='B' else max(p,q)-min(p,q)
        if level=='hard' and code=='C':
            initial=p+q+k; needed=r.randint(2,6); remaining=initial-p-q
            value=max(0,needed-remaining)
            return numeric(f'Ibu memiliki {m(initial)} kg tepung. Dipakai {m(p)} kg untuk roti dan {m(q)} kg untuk kue. Jika berikutnya dibutuhkan {needed} kg, berapa kg tepung tambahan paling sedikit yang diperlukan?',value,
                           f'Tepung tersisa {initial}-{p}-{q}={remaining} kg. Tambahan yang diperlukan maksimum antara 0 dan {needed}-{remaining}, yaitu {value} kg.','pengurangan_pecahan_bertahap')
        op='+' if code=='B' else '-';one,two=(p,q) if code=='B' else (max(p,q),min(p,q))
        return numeric(f'Hitung {m(one)} {op} {m(two)}.',value,f'Samakan penyebut, lalu lakukan operasi pembilang. Hasilnya {value}.','operasi_pecahan')
    if bab==4:
        if code=='A':
            sides=[a,b,k,a+b];v=sum(sides)
            return numeric(f'Sebuah bangun tertutup memiliki empat sisi berturut-turut {sides[0]}, {sides[1]}, {sides[2]}, dan {sides[3]} cm. Berapa kelilingnya?',v,f'Keliling adalah jumlah seluruh sisi batas: {" + ".join(map(str,sides))}={v} cm.','konsep_keliling')
        if code=='B':
            sides=sorted([a+4,b+5,k+6]);sides[2]=min(sides[2],sides[0]+sides[1]-1);v=sum(sides)
            if level=='hard':return numeric(f'Segitiga sama kaki mempunyai keliling {2*a+b} cm dan alas {b} cm. Berapa panjang masing-masing sisi yang sama?',a,f'Dua sisi sama berjumlah {2*a+b}-{b}={2*a}; tiap sisi {a} cm.','keliling_segitiga_balik') if b<2*a else generate(book,bab,code,level,r)
            return numeric(f'Segitiga memiliki panjang sisi {sides[0]}, {sides[1]}, dan {sides[2]} cm. Berapakah kelilingnya?',v,f'Jumlah panjang ketiga sisi = {v} cm.','keliling_segitiga')
        if code=='C':
            if level=='hard':return numeric(f'Keliling persegi panjang {2*(a+b)} cm. Panjangnya {a} cm. Berapakah lebarnya?',b,f'Panjang + lebar = {a+b}; lebar = {a+b}-{a}={b} cm.','keliling_segiempat_balik')
            return numeric(f'Persegi panjang berukuran {a} cm × {b} cm. Kelilingnya adalah ....',2*(a+b),f'K=2(p+l)=2({a}+{b})={2*(a+b)} cm.','keliling_segiempat')
        if code=='D':
            n=r.randint(5,12);value=n*a
            return numeric(f'Sebuah segi-{n} beraturan mempunyai sisi {a} cm. Berapakah kelilingnya?',value,f'Ada {n} sisi sama panjang. Keliling={n}×{a}={value} cm.','keliling_segi_banyak')
        w=a+8;h=b+8;cutw=r.randint(2,5);cuth=r.randint(2,5)
        return numeric(f'Pojok persegi panjang berukuran {w} cm × {h} cm dipotong menjadi takikan persegi panjang {cutw} cm × {cuth} cm sehingga tersisa bangun L. Berapa keliling bangun L?',2*(w+h),
                       f'Dua ruas yang hilang pada pojok digantikan dua ruas sama panjang di dalam takikan. Keliling tetap 2({w}+{h})={2*(w+h)} cm.','keliling_bangun_gabungan')
    if bab==5:
        if code in 'AB':
            if level=='hard':
                perimeter=2*(a+b);delta=r.randint(1,min(a,b)-1);area1=a*b;area2=(a+delta)*(b-delta)
                return numeric(f'Persegi panjang P berukuran {a} cm × {b} cm. Bangun Q berukuran {a+delta} cm × {b-delta} cm. Berapa selisih luas kedua bangun yang berkeliling sama tersebut?',abs(area1-area2),
                               f'Keliling keduanya {perimeter} cm. Luas P={area1}, luas Q={area2}; selisih luas={abs(area1-area2)} cm².','membandingkan_luas')
            return numeric(f'Daerah persegi panjang memiliki {a} baris petak dan {b} petak tiap baris. Luas daerah itu berapa satuan luas?',a*b,f'Banyak petak = {a}×{b}={a*b}.','konsep_luas')
        if code=='C':
            c=r.randint(2,a);d=r.randint(1,b);value=a*b+c*d
            return numeric(f'Hiasan tersusun dari dua persegi panjang yang tidak saling menutupi, berukuran {a} cm × {b} cm dan {c} cm × {d} cm. Berapa luas seluruh hiasan?',value,
                           f'Luas gabungan={a}×{b}+{c}×{d}={value} cm².','luas_bangun_gabungan')
        p=a+b
        return numeric(f'Kawat sepanjang {2*p} cm dibuat persegi panjang dengan panjang {a} cm. Berapa luas persegi panjang tersebut?',a*b,
                       f'Panjang+lebar={p}, sehingga lebar={p}-{a}={b}. Luas={a}×{b}={a*b} cm².','hubungan_keliling_luas')
    if bab==6:
        if code=='A':
            triangles=r.randint(2,8);rectangles=r.randint(2,8);value=triangles+4*rectangles
            return numeric(f'Ada {rectangles} kertas persegi panjang dan {triangles} kertas segitiga siku-siku. Berapa jumlah sudut siku-siku seluruh kertas itu?',value,
                           f'Setiap persegi panjang memiliki 4 sudut siku-siku, tiap segitiga siku-siku tepat 1. Total={rectangles}×4+{triangles}={value}.','sudut_siku_siku')
        if code=='D':
            angle=r.choice([35,45,55,65,75,105,115,125,135,145]);outer=180-angle
            return numeric(f'Dita hendak melukis sudut {angle}° menggunakan busur derajat. Jika kaki awal berimpit dengan skala yang mulai 0°, dan tanda yang dipilih terbaca {outer}° pada skala lainnya, berapa angka pada skala yang benar?',angle,
                           f'Dua skala pada satu tanda berjumlah 180°. Bacaan skala yang dimulai dari kaki awal ialah 180°-{outer}°={angle}°.','membaca_skala_busur')
        if code=='C':
            start=r.randint(5,70);end=r.randint(90,175)
            return numeric(f'Dua sinar OA dan OB dibaca pada skala busur derajat yang sama, masing-masing pada {start}° dan {end}°. Keduanya berada pada setengah bidang yang sama. Berapa besar sudut AOB?',end-start,
                           f'Pada skala yang sama, besar sudut adalah selisih kedua bacaan: {end}°-{start}°={end-start}°.','mengukur_sudut_busur',unit='derajat')
        hour=r.randint(1,11);v=min(hour*30,360-hour*30)
        return numeric(f'Jarum jam menunjukkan tepat pukul {hour:02d}.00. Besar sudut terkecil antara kedua jarum adalah ....',v,
                       f'Tiap selang angka bernilai 30°. Sudut dari angka 12 ke {hour} adalah {hour*30}°; sudut terkecilnya {v}°.','mengukur_sudut_jam',unit='derajat')
    if bab==7:
        if code=='A':
            base=r.randint(4,10);leg=base+r.randint(1,5);v=2*leg+base
            return numeric(f'Sebuah segitiga sama kaki mempunyai alas {base} cm dan kedua sisi lainnya masing-masing {leg} cm. Berapa kelilingnya?',v,
                           f'Dua sisi sama panjang merupakan ciri segitiga sama kaki. Keliling={base}+{leg}+{leg}={v} cm.','ciri_segitiga')
        if a+2==b+1:return generate(book,bab,code,level,r)
        return text(f'Persegi panjang memiliki panjang {a+2} cm dan lebar {b+1} cm. Sifat yang selalu dimiliki bangun tersebut adalah ....',
                    'Keempat sudutnya siku-siku dan sisi-sisi yang berhadapan sama panjang.',
                    ['Semua sisinya harus sama panjang.','Tepat satu pasang sisi sejajar.','Tidak memiliki sudut siku-siku.'],
                    'Definisi persegi panjang menjamin empat sudut siku-siku dan dua pasang sisi berhadapan sama panjang.','ciri_segiempat')
    if bab==8:
        if code=='A':
            first=r.randint(30,36);sizes=list(range(first,first+4));counts=[r.randint(2,8) for _ in sizes];threshold=r.randint(3,7)
            data=[size for size,count in zip(sizes,counts) for _ in range(count)];r.shuffle(data)
            value=sum(count for count in counts if count<threshold)
            table='; '.join(f'ukuran {size}: {count} siswa' for size,count in zip(sizes,counts))
            return numeric(f'Data ukuran sepatu siswa adalah {", ".join(map(str,data))}. Penjual hanya membawa ukuran yang dipakai paling sedikit {threshold} siswa. Berapa siswa yang ukuran sepatunya belum terlayani?',value,
                           f'Kelompokkan hasil pendataan: {table}. Jumlahkan frekuensi ukuran yang dipakai kurang dari {threshold} siswa; diperoleh {value} siswa.','mengelompokkan_data_frekuensi')
        if code=='B':
            symbols=r.randint(3,12);legend=r.randint(2,10)
            return numeric(f'Pada piktogram, satu simbol mewakili {legend} buku. Perpustakaan A memiliki {symbols} simbol penuh. Berapa buku yang ditunjukkan?',symbols*legend,
                           f'Banyak buku = jumlah simbol × nilai tiap simbol = {symbols}×{legend}={symbols*legend}.','piktogram')
        values=r.sample(range(5,30),3);scale=r.randint(2,5);index=r.randrange(3)
        return numeric(f'Diagram batang penjualan memuat produk A, B, C dengan tinggi {values[0]}, {values[1]}, {values[2]} satuan skala. Tiap satuan mewakili {scale} barang. Berapa barang terjual untuk produk {"ABC"[index]}?',values[index]*scale,
                       f'Tinggi produk {"ABC"[index]} = {values[index]} satuan. Jumlahnya {values[index]}×{scale}={values[index]*scale}.','diagram_batang')
    raise ValueError(f'Unsupported SD topic {book}/{bab}/{code}')
