import random

daftar_undian = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10",
    "A", "B", "C", "D", "E"
]

nomor_menang = random.sample(daftar_undian, 4)

print("Nomor undian yang menang:")
print(nomor_menang)

print("Tiket yang cocok dengan 4 angka atau huruf ini memenangkan hadiah!")