pengguna_saat_ini = ['budi', 'admin', 'Siti', 'joko', 'eko']

pengguna_saat_ini_kecil = [pengguna.lower() for pengguna in pengguna_saat_ini]

pengguna_baru = ['siti', 'rudi', 'Andi', 'admin', 'mega']

for pengguna_baru_ini in pengguna_baru:
    if pengguna_baru_ini.lower() in pengguna_saat_ini_kecil:
        print(f"Maaf, username '{pengguna_baru_ini}' sudah digunakan. Anda harus memasukkan username baru.")
    else:
        print(f"Username '{pengguna_baru_ini}' tersedia dan bisa digunakan.")