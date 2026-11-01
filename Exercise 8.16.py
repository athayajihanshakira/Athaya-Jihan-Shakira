# CARA 1: import nama_modul
import buat_modul

album_1 = buat_modul.buat_album('Tulus', 'Manusia')
print("Cara 1:", album_1)


# CARA 2: from nama_modul import nama_fungsi
from buat_modul import buat_album

album_2 = buat_album('Sheila on 7', 'Kisah Klasik Untuk Masa Depan')
print("Cara 2:", album_2)


# CARA 3: from nama_modul import nama_fungsi as fn
from buat_modul import buat_album as buat_album_fn

album_3 = buat_album_fn('Noah', 'Second Chance', jumlah_lagu=12)
print("Cara 3:", album_3)


# CARA 4: import nama_modul as mn
import buat_modul as bm

album_4 = bm.buat_album('Dewa 19', 'Bintang Lima')
print("Cara 4:", album_4)

# CARA 5: from nama_modul import 
from buat_modul import *

album_5 = buat_album('Raisa', 'HearttoHeart')
print("Cara 5:", album_5)