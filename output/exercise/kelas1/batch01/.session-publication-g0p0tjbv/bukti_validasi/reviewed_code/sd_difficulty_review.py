"""Content-based, quota-independent SD difficulty decisions.

The policy is a local editorial judgement, not an empirical IRT calibration.
The requested level, filename, confidence and quota are never classifier inputs.
"""
from copy import deepcopy
import sympy as s

POLICY='codex-sd-content-difficulty-v2'
EASY=set('''sd3_banding_terbesar sd3_bangun_a_langsung sd3_bangun_b_langsung
sd3_berat_konversi_c sd3_berat_konversi_d sd3_data_terbesar
sd3_kalimat_pengurangan_kosong sd3_kalimat_penjumlahan_kosong sd3_konversi_meter_cm
sd3_lambang_nilai_tempat sd3_nilai_digit sd3_panjang_penggaris_offset sd3_pembagian_rata
sd3_pengurangan_stok sd3_penjumlahan_dua_stok sd3_perkalian_kelompok
sd3_relasi_garis_easy sd3_relasi_garis_medium sd3_tabel_frekuensi_langsung
sd4_banding_terbesar sd4_dekomposisi_petakan sd4_desimal_perseratusan
sd4_diagram_a_baca sd4_diagram_b_baca sd4_faktor_pembagian_langsung
sd4_komposisi_lengkap sd4_lambang_nilai_tempat sd4_luas_petak_satuan sd4_nilai_digit
sd4_pecahan_pembilang_satu sd4_pecahan_penyebut_banding sd4_pecahan_senilai_sederhana
sd4_pecahan_satuan_beberapa sd4_pembagian_rata sd4_pengurangan_stok sd4_penjumlahan_dua_stok
sd4_perkalian_kelompok sd4_persen_grid sd4_pola_bilangan_lanjut sd4_volume_susunan_penuh
sd_low_baca_jam_tepat sd_low_bagian_kue_seperempat sd_low_bagian_kue_setengah
sd_low_banding_selisih sd_low_berat_banding sd_low_ciri_bentuk sd_low_data_frekuensi
sd_low_hitung_maju sd_low_membilang_langsung sd_low_panjang_langsung
sd_low_pasangan_pelengkap sd_low_pengurangan_konkret sd_low_penjumlahan_gabung
sd_low_ruang_permukaan_datar sd_low_setengah_kumpulan sd_low_susun_dua_segitiga
sd_low_tempat_satuan sd_low_waktu_sampai_jam sd_review_pattern_read'''.split())
MEDIUM=set('''sd3_banding_jangkauan sd3_berat_konversi_pakai_c sd3_berat_konversi_pakai_d
sd3_data_banding_dua_ujung sd3_kalimat_pengurangan_balik sd3_kalimat_penjumlahan_balik
sd3_konversi_potong_panjang sd3_lambang_perubahan sd3_nilai_tempat_tukar
sd3_panjang_potong_dua_ujung sd3_pembagian_setelah_cadangan sd3_pengurangan_dua_tahap
sd3_penjumlahan_tiga_stok sd3_perkalian_sisa_perkelompok sd3_tabel_gabung_kategori
sd4_banding_jangkauan sd4_dekomposisi_banding_bagian sd4_dekomposisi_ribuan
sd4_desimal_tambah_petak sd4_diagram_a_banding sd4_diagram_b_banding
sd4_faktor_persekutuan sd4_lambang_perubahan sd4_luas_potong_baris
sd4_nilai_tempat_tukar sd4_pecahan_penyebut_selisih sd4_pecahan_senilai_pembilang
sd4_pembagian_setelah_cadangan sd4_pengurangan_dua_tahap sd4_penjumlahan_tiga_stok
sd4_perkalian_sisa_perkelompok sd4_persen_perubahan sd4_pola_bilangan_urutan
sd4_volume_ambil_lapisan sd_low_banding_setelah_tambah sd_low_berat_perubahan
sd_low_kelompok_berdasarkan_sudut sd_low_lengkapi_seperempat sd_low_lengkapi_setengah
sd_low_maju_mundur sd_low_panjang_potong_banding sd_low_pasangan_setelah_pindah
sd_low_pengurangan_pemulihan sd_low_penjumlahan_tiga_bagian
sd_low_ruang_kelompok_lengkung sd_low_setengah_dua_kumpulan sd_low_susun_gabung_persegi
sd_low_tempat_ubah_satuan sd_low_tempat_tukar_ikatan sd4_pecahan_penyebut_transfer
sd4_persen_target_setelah_hapus sd4_diagram_a_transfer_gabung sd4_diagram_b_transfer_gabung
sd_review_count_update sd_review_data_update sd_review_clock_interval
sd_review_fraction_update sd_review_lines_after_removal'''.split())
HARD=set('''sd3_berat_gabungan_bagi_c sd3_berat_gabungan_bagi_d sd3_data_kelompok_perubahan
sd3_kalimat_pengurangan_kembali sd3_kalimat_penjumlahan_urutan_balik
sd3_konversi_panjang_pembagian sd3_lambang_susun_bersyarat sd3_nilai_tempat_regroup
sd3_panjang_sambung_tumpang sd3_pembagian_gabungan_cadangan
sd3_pengurangan_audit_perubahan sd3_penjumlahan_balik_stok
sd3_perkalian_kebutuhan_cadangan sd3_tabel_koreksi_tambah sd3_urut_perubahan_tengah
sd4_dekomposisi_bertingkat sd4_desimal_perubahan_banding sd4_faktor_kantong_terbatas
sd4_komposisi_setelah_urai sd4_lambang_susun_bersyarat sd4_luas_gabungan_tumpang_potong
sd4_nilai_tempat_regroup sd4_pecahan_senilai_dua_bentuk sd4_pembagian_gabungan_cadangan
sd4_pengurangan_audit_perubahan sd4_penjumlahan_balik_stok sd4_perkalian_kebutuhan_cadangan
sd4_pola_bilangan_batas_urutan sd4_urut_perubahan_tengah sd4_volume_lapisan_tiang_bertahap
sd_low_banding_dua_perubahan sd_low_berat_pindah_tambah sd_low_ciri_klasifikasi_perubahan
sd_low_data_koreksi_kategori sd_low_membilang_pindah_banding sd_low_panjang_perubahan_banding
sd_low_pasangan_ubah_banding sd_low_pengurangan_tiga_perubahan sd_low_penjumlahan_konteks_berubah
sd_low_perbaiki_dua_pecahan_seperempat sd_low_perbaiki_dua_pecahan_setengah
sd_low_ruang_klasifikasi_perubahan sd_low_setengah_setelah_perubahan sd_low_susun_dua_tahap
sd_low_urutan_tiga_gerak sd_low_waktu_tiga_kegiatan
sd_review_place_minimum_open sd_review_pattern_minimum sd_review_grid_route
sd_review_fraction_minimum sd_review_fraction_balance sd_review_percent_packages
sd_review_shape_budget sd_review_lines_mixed sd_review_diagram_reorder'''.split())


def assess(question,certificate,family,grade,scene=None):
    """Use the actual model and wording; never look at an intended difficulty."""
    values=certificate.get('inputs',{});v={k:s.sympify(x) for k,x in values.items() if isinstance(x,(int,float,str))}
    reason=None;level=None;flags=[]
    if family=='sd3_relasi_garis_hard':
        return decision(None,'Tiga garis tersisa semuanya mendatar atau tegak. Setiap pasangan otomatis sejajar atau tegak lurus, sehingga jumlah gabungannya selalu 3 tanpa melihat gambar.', ['image_independent_constant_answer'])
    if family=='sd_low_posisi_berurutan':
        moves=values['moves'];net=[sum(t[i] for t in moves) for i in range(2)];distance=sum(map(abs,net))
        level='easy' if distance<=1 else 'medium';reason=f'Gerakan dapat disederhanakan menjadi {distance} langkah posisi; lintasan yang saling membatalkan tidak menambah kesulitan.'
    elif family in {'sd_low_pola_lanjut_hitung','sd4_pola_gambar_posisi_hitung'}:
        visible=0 if scene is None else len(scene['items'])
        end=values.get('end',certificate.get('length',0));start=values.get('start',certificate.get('skip',0))
        level='easy' if family=='sd_low_pola_lanjut_hitung' and start==0 and end<=visible else 'medium'
        reason='Menghitung simbol yang sudah terlihat secara langsung.' if level=='easy' else 'Menemukan unit berulang dan menghitung pada rentang yang ditentukan; rentang yang lebih panjang saja tidak menjadikannya hard.'
    elif family in {'sd3_bangun_a_gabung_sifat','sd3_bangun_b_gabung_sifat','sd4_ciri_bangun_klasifikasi_hitung'}:
        query=certificate['query'];shapes=certificate['shapes']
        level='easy' if len(shapes)==1 else 'medium'
        reason='Mengenali satu sifat bangun.' if level=='easy' else 'Mengelompokkan sifat bangun dan menjumlahkan hasilnya; belum ada kendala atau strategi tambahan untuk hard.'
        if query=='filtered_sum' and not any(t in {'square','rectangle','right_triangle'} for t in shapes):
            level='easy';reason='Tidak ada bangun bersudut siku-siku; hasil nol diperoleh lewat pengenalan langsung.'
    elif family=='sd4_pecahan_satuan_perubahan':
        level='easy' if v['t']==1 else 'medium';reason='Pengembalian dan pengambilan kembali saling membatalkan.' if level=='easy' else 'Dua perubahan jumlah bagian dilanjutkan penulisan pecahan; prosedurnya rutin.'
    elif family in {'sd_low_membilang_gabungan','sd_low_data_gabung_kategori'}:
        level='medium' if scene else 'easy';reason='Membaca dua kelompok dalam representasi visual kemudian menggabungkannya.' if scene else 'Dua jumlah sudah tertulis; hanya satu penjumlahan langsung.'
    elif family in EASY:level='easy'
    elif family in MEDIUM:level='medium'
    elif family in HARD:level='hard'
    else:raise ValueError('Unreviewed SD family: '+family)
    # Review the shortest meaningful solution for each numerical instance.
    if family in {'sd_low_pengurangan_tiga_perubahan','sd_low_urutan_tiga_gerak','sd_low_penjumlahan_konteks_berubah'}:
        cancel=(v.get('p')==v.get('q') or v.get('q')==v.get('t') or v.get('p',0)+v.get('t',0)==v.get('q')) if family!='sd_low_penjumlahan_konteks_berubah' else v['c']==v['d']
        if cancel:level='easy';reason='Perubahan yang berlawanan bernilai sama saling menghapus; tersisa paling banyak satu operasi langsung.';flags.append('numerical_shortcut')
    if family.endswith('nilai_tempat_regroup') and v['taken']==v['added']:
        level='medium';reason='Pengambilan dan penambahan sama besar. Yang dibutuhkan hanya mengubah ratusan ke puluhan dan menggabungkan sisanya.';flags.append('numerical_shortcut')
    if family=='sd_low_panjang_perubahan_banding' and v['t']==v['g']:
        level='medium';reason='Potongan dan sambungan sama panjang, jadi cukup membaca panjang awal dan membandingkan.';flags.append('numerical_shortcut')
    if family.startswith('sd3_berat_gabungan_bagi') and v['added']==v['reserved']:
        level='medium';reason='Tambahan dan cadangan sama besar; setelah konversi satuan tinggal pembagian rutin.';flags.append('numerical_shortcut')
    if family=='sd4_desimal_perubahan_banding' and v['erase']==v['add']:
        level='medium';reason='Jumlah arsiran tidak berubah; cukup mengubah ke desimal dan mencari selisih.';flags.append('numerical_shortcut')
    if family in {'sd3_pengurangan_audit_perubahan','sd4_pengurangan_audit_perubahan'} and v['returned']==v['damage']:
        level='medium';reason='Pengembalian dan kerusakan saling menghapus; sisa dihitung lewat dua pengurangan rutin.';flags.append('numerical_shortcut')
    if reason is None:
        reason={
          'easy':'Pengenalan representasi atau satu prosedur langsung dalam lingkup kelas.',
          'medium':'Dua atau tiga hubungan rutin perlu diterapkan; belum memerlukan strategi tambahan.',
          'hard':'Beberapa keadaan atau syarat yang saling bergantung harus digabungkan, dibalik, dipilih, atau dibandingkan sesuai usia kelas.'}[level]
    return decision(level,reason,flags)


def decision(level,reason,flags):
    return {'assessedLevel':level,'reason':reason,'flags':flags,'policyVersion':POLICY,'confidenceScore':0,'confidenceMeasured':False,'apiCalls':0,'steps':{'easy':1,'medium':2,'hard':4,None:0}[level]}
