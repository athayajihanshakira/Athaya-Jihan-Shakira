print("Pilih cara keluar loop yang ingin dicoba:")
print("1. Menggunakan kondisi di while")
print("2. Menggunakan variabel aktif (flag)")
print("3. Menggunakan break")

pilihan = input("Masukkan pilihanmu (1/2/3): ")

if pilihan == '1':
    print("\n--- Menjalankan Cara 1 (Kondisi While) ---")
    topping = ""
    while topping != 'quit':
        topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
        if topping != 'quit':
            print(f"Menambahkan {topping}!")

elif pilihan == '2':
    print("\n--- Menjalankan Cara 2 (Variabel Aktif) ---")
    aktif = True
    while aktif:
        topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
        if topping == 'quit':
            aktif = False
        else:
            print(f"Menambahkan {topping}!")

elif pilihan == '3':
    print("\n--- Menjalankan Cara 3 (Pernyataan Break) ---")
    while True:
        topping = input("Masukkan topping pizza (ketik 'quit' untuk berhenti): ")
        if topping == 'quit':
            break
        print(f"Menambahkan {topping}!")

else:
    print("Pilihan tidak valid, jalankan ulang program.")