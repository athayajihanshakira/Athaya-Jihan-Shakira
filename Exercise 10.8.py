from pathlib import Path

file_hewan = ['kucing.txt', 'anjing.txt']

for nama_file in file_hewan:
    print(f"\n Membaca file: {nama_file}")
    
    path = Path(nama_file)
    
    try:
        isi = path.read_text(encoding='utf-8')
        
    except FileNotFoundError:
        print(f"Maaf, file '{nama_file}' tidak dapat ditemukan.")
        
    else:
        print(isi.strip())
