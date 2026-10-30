nama_pengguna = []

if nama_pengguna:
    for nama in nama_pengguna:
        if nama == 'admin':
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {nama.title()}, terima kasih sudah masuk kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")