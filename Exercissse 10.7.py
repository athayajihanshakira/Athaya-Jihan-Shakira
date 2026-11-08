print("(Ketik 'q' atau 'keluar' kapan saja untuk menghentikan program)\n")

while True:
    angka_pertama = input("\nMasukkan angka pertama: ")
    if angka_pertama.lower() in ['q', 'keluar']:
        break
        
    angka_kedua = input("Masukkan angka kedua: ")
    if angka_kedua.lower() in ['q', 'keluar']:
        break

    try:
        hasil = int(angka_pertama) + int(angka_kedua)
        
    except ValueError:
        print("-> Maaf, mohon hanya masukkan angka (bukan huruf/teks). Silakan coba lagi!")
        
    else:
        print(f"-> Hasil penjumlahannya adalah: {hasil}")