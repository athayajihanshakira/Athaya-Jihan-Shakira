from pathlib import Path
nama = input ('masukkan nama :')

path = Path ("guest.txt")
path.write_text(nama)
