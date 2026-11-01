def buat_album(nama_artis, judul_album, jumlah_lagu=None):
    
    album_musik = {
        'artis': nama_artis,
        'album': judul_album
    }
    if jumlah_lagu:
        album_musik['jumlah_lagu'] = jumlah_lagu
    return album_musik

print("Masukkan informasi album musik.")
print("(ketik 'q' kapan saja untuk berhenti)\n")

while True:
    masukkan_artis = input("Nama Artis: ")
    if masukkan_artis.lower() == 'q':
        break
        
    masukkan_album = input("Judul Album: ")
    if masukkan_album.lower() == 'q':
        break
        
    info_album_baru = buat_album(masukkan_artis, masukkan_album)
    
    print("\nAlbum yang berhasil dibuat:")
    print(info_album_baru)
    print("\n----------------------------------------\n")