hasil_polling = {}

polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa nama kamu? ")
    destinasi = input("Jika kamu bisa mengunjungi satu tempat di dunia, di mana kamu akan pergi? ")
    
    hasil_polling[nama] = destinasi
    
    ulangi = input("Apakah ada orang lain yang ingin ikutan polling? (ya/tidak): ")
    if ulangi.lower() == 'tidak':
        polling_aktif = False

print("\n--- Hasil Polling Liburan Impian ---")
for nama, destinasi in hasil_polling.items():
    print(f"{nama} ingin sekali berkunjung ke {destinasi}.")