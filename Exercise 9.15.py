import random

daftar_undian = [
    "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10",
    "A", "B", "C", "D", "E"
]

my_ticket = ["1", "3", "A", "C"]

jumlah_perulangan = 0

while True:
    nomor_menang = random.sample(daftar_undian, 4)
    jumlah_perulangan += 1

    if sorted(nomor_menang) == sorted(my_ticket):
        print("Selamat! Tiket cocok!")
        print(f"Jumlah percobaan: {jumlah_perulangan}")
        break