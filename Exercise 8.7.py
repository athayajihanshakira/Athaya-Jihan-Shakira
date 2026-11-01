def buat_album(nama_artis, judul_album, jumlah_lagu=None):
    album_musik = {
        'artis': nama_artis,
        'album': judul_album
    }
    
    # Jika jumlah lagu diberikan, masukkan ke dalam dictionary
    if jumlah_lagu:
        album_musik['jumlah_lagu'] = jumlah_lagu
        
    return album_musik

album_pertama = buat_album('Tulus', 'Manusia')
album_kedua = buat_album('Sheila on 7', 'Kisah Klasik Untuk Masa Depan')
album_ketiga = buat_album('Noah', 'Second Chance', jumlah_lagu=12) # 

print(album_pertama)
print(album_kedua)
print(album_ketiga)