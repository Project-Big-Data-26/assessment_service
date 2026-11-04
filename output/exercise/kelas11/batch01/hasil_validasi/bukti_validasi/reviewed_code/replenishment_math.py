"""Authored, parameterized mathematics for reference-grounded candidate generation."""
from dataclasses import dataclass
from fractions import Fraction
import math
import random
import sympy as s

x = s.Symbol('x', real=True)


def latex(value):
    return s.latex(s.sympify(value))


def m(value):
    return '$' + latex(value) + '$'


def rp(value):
    return 'Rp' + f'{int(value):,}'.replace(',', '.') + ',00'


@dataclass
class Draft:
    question: str
    answer: str
    distractors: list[str]
    explanation: str
    kind: str
    proof: dict


def numeric(question, value, explanation, kind, wrong=None, unit=''):
    value = s.simplify(value)
    assert not value.has(s.nan, s.zoo, s.oo, -s.oo)
    proposals = list(wrong or []) + [value+1, value-1, value+2, value-2, value+3, value*2+1]
    selected = []
    for proposed in proposals:
        proposed = s.simplify(proposed)
        if proposed.has(s.nan,s.zoo,s.oo,-s.oo) or s.simplify(proposed-value)==0:
            continue
        if any(s.simplify(proposed-old)==0 for old in selected):
            continue
        selected.append(proposed)
        if len(selected)==3:
            break
    assert len(selected)==3
    fmt = lambda v: m(v) + (' '+unit if unit else '')
    return Draft(question, fmt(value), [fmt(v) for v in selected], explanation, kind,
                 {'check':'exact_value_and_four_distinct_options','value':str(value),
                  'options':[str(value),*[str(v) for v in selected]],'independent_ai_validation':'pending'})


def text(question, answer, wrong, explanation, kind):
    assert len(wrong)==3 and len(set([answer,*wrong]))==4
    return Draft(question, answer, list(wrong), explanation, kind,
                 {'check':'four_distinct_text_options','independent_ai_validation':'pending'})


def pair(a,b):
    return '$('+latex(a)+', '+latex(b)+')$'


def factors(n):
    return list(s.divisors(n))


def statistics(r,level,mode='mean'):
    a=r.randint(3,35); step=r.randint(1,6)
    data=[a,a+step,a+step,a+2*step,a+3*step]
    r.shuffle(data); listing=', '.join(map(str,data))
    if mode=='range':
        v=max(data)-min(data)
        return numeric(f'Data pengukuran lima benda adalah {listing}. Berapakah jangkauan data tersebut?',v,
                       f'Nilai terbesar {max(data)} dan terkecil {min(data)}. Jangkauan = {max(data)} - {min(data)} = {v}.','jangkauan')
    if mode=='median':
        ordered=sorted(data); v=ordered[2]
        return numeric(f'Data hasil pengamatan adalah {listing}. Setelah diurutkan, berapakah mediannya?',v,
                       f'Urutan data: {ordered}. Dari lima data, median adalah data ketiga, yaitu {v}.','median')
    v=s.Rational(sum(data),5)
    if level=='hard':
        extra=r.randint(2,9); target=v+extra
        needed=6*target-sum(data)
        return numeric(f'Lima nilai adalah {listing}. Satu nilai baru ditambahkan sehingga rata-rata enam nilai menjadi {m(target)}. Berapakah nilai yang ditambahkan?',needed,
                       f'Jumlah semula {sum(data)}. Jumlah baru harus 6 × {target} = {6*target}. Nilai tambahan = {6*target} - {sum(data)} = {needed}.','rata_rata_balik')
    return numeric(f'Data lima hasil pengukuran adalah {listing}. Berapakah rata-ratanya?',v,
                   f'Jumlah data = {sum(data)}. Rata-rata = {sum(data)}/5 = {v}.','rata_rata')


def linear(r,level,mode='equation'):
    a=r.randint(2,9); b=r.randint(2,18); root=r.randint(2,15); c=a*root+b
    if mode=='inequality':
        return numeric(f'Diketahui {m(a*x+b)} < {c} dengan $x$ bilangan cacah. Berapakah nilai $x$ terbesar yang memenuhi?',root-1,
                       f'Kurangi kedua ruas dengan {b}, lalu bagi dengan {a}>0: x < {root}. Bilangan cacah terbesar yang memenuhi adalah {root-1}.','pertidaksamaan')
    if level=='hard':
        d=r.randint(1,a-1); e=(a-d)*root+b
        return numeric(f'Seorang siswa memperoleh $x={root+1}$ dari persamaan {m(a*x+b)} = {m(d*x+e)}. Nilai $x$ yang sebenarnya adalah ....',root,
                       f'Pindahkan suku sejenis: ({a}-{d})x = {e}-{b}. Maka x = {root}. Substitusi menghasilkan kedua ruas sama.','evaluasi_persamaan')
    return numeric(f'Tentukan nilai $x$ yang memenuhi {m(a*x+b)} = {c}.',root,
                   f'{a}x = {c}-{b} = {a*root}, sehingga x = {root}.','persamaan_linear')


def probability(r,level,mode='single'):
    red=r.randint(3,12); blue=r.randint(3,12); n=red+blue
    if mode=='two':
        p=s.Rational(red*(red-1),n*(n-1))
        return numeric(f'Sebuah kotak berisi {red} bola merah dan {blue} bola biru. Dua bola diambil berturut-turut tanpa pengembalian. Peluang keduanya merah adalah ....',p,
                       f'Peluang merah pertama {red}/{n}; setelah itu merah kedua {red-1}/{n-1}. Hasil kali keduanya {p}.','peluang_tanpa_pengembalian',wrong=[s.Rational(red**2,n**2),s.Rational(blue,n),s.Rational(red,n)])
    if mode=='expected':
        trials=n*r.randint(3,15); v=s.Rational(red,n)*trials
        return numeric(f'Kotak berisi {red} bola merah dan {blue} bola biru. Dilakukan {trials} pengambilan acak dengan pengembalian. Frekuensi harapan terambil bola merah adalah ....',v,
                       f'P(merah)={red}/{n}. Frekuensi harapan = {trials} × {red}/{n} = {v}.','frekuensi_harapan')
    return numeric(f'Dari kotak berisi {red} bola merah dan {blue} bola biru diambil satu bola secara acak. Peluang bola yang terambil berwarna merah adalah ....',s.Rational(red,n),
                   f'Kejadian merah ada {red} dari {n} bola, sehingga peluangnya {red}/{n}.','peluang_satu_kejadian',wrong=[s.Rational(blue,n),s.Rational(red,blue),s.Rational(1,n)])


def sequences(r,level,mode='sequence'):
    a=r.randint(2,12); d=r.randint(2,9); n=r.randint(6,18)
    if mode=='sum':
        value=s.Rational(n,2)*(2*a+(n-1)*d)
        return numeric(f'Sebuah deret aritmetika memiliki suku pertama {a} dan beda {d}. Tentukan jumlah {n} suku pertamanya.',value,
                       f'S_n=n(2a+(n-1)b)/2 = {n}(2×{a}+({n}-1)×{d})/2 = {value}.','jumlah_deret')
    if level=='hard':
        k=r.randint(3,6); q=k+r.randint(2,5); uk=a+(k-1)*d; uq=a+(q-1)*d
        value=a+(n+q-1)*d
        return numeric(f'Pada barisan aritmetika diketahui $U_{k}={uk}$ dan $U_{q}={uq}$. Tentukan $U_{n+q}$.',value,
                       f'Beda = ({uq}-{uk})/({q}-{k}) = {d}. Suku pertama = {uk}-({k}-1)×{d} = {a}. Jadi U_{n+q}={value}.','barisan_dari_dua_suku')
    return numeric(f'Barisan aritmetika dimulai dengan {a}, {a+d}, {a+2*d}, .... Tentukan suku ke-{n}.',a+(n-1)*d,
                   f'U_n=a+(n-1)b = {a}+({n}-1)×{d} = {a+(n-1)*d}.','suku_barisan')
