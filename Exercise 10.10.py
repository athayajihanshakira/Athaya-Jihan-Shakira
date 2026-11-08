from pathlib import Path

nama_file = 'cerita.txt'
path = Path(nama_file)

try:
    teks = path.read_text(encoding='utf-8')
    
except FileNotFoundError:
    print(f"Maaf, file '{nama_file}' tidak ditemukan.")
    
else:
    kata_dicari = 'the'
    
    jumlah_kemunculan = teks.lower().count(kata_dicari)
    
    print(f"Kata '{kata_dicari}' muncul sebanyak {jumlah_kemunculan} kali di dalam file {nama_file}.")