print("=== PROGRAM PENJUMLAHAN DUA ANGKA ===")

angka_pertama = input("Masukkan angka pertama: ")
angka_kedua = input("Masukkan angka kedua: ")

try:
    hasil = int(angka_pertama) + int(angka_kedua)
    
except ValueError:
    print("Maaf, Anda memasukkan teks, bukan angka. Mohon masukkan angka yang valid!")
    
else:
    print(f"Hasil penjumlahannya adalah: {hasil}")