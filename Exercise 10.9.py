from pathlib import Path

file_hewan = ['kucing.txt', 'anjing.txt']

for nama_file in file_hewan:
    print(f"\nMembaca file: {nama_file}")
    
    path = Path(nama_file)
    
    try:
        isi = path.read_text(encoding='utf-8')
        
    except FileNotFoundError:
        pass
        
    else:
        print(isi.strip())