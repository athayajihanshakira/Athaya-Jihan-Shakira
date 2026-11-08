from pathlib import Path

path = Path('guest_book.txt')

print("=== BUKU TAMU ===")
print("Ketik 'selesai' jika sudah selesai.\n")

daftar_tamu = ""

while True:
    nama = input("Masukkan nama Anda: ")
    
    if nama.lower() == 'selesai':
        break

    daftar_tamu += f"{nama}\n"
    print(f"Halo {nama}, nama Anda telah dicatat!")

path.write_text(daftar_tamu)
