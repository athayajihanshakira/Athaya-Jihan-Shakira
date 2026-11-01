def buat_profil(nama_depan, nama_belakang, **info_tambahan):
    
    info_tambahan['nama_depan'] = nama_depan
    info_tambahan['nama_belakang'] = nama_belakang
    return info_tambahan

profil_saya = buat_profil(
    'athaya', 
    'Santoso', 
    lokasi='Surakarta', 
    bidang_studi='Teknik Industri', 
    hobi='menonton film'
)

print("Profil Pengguna:")
print(profil_saya)