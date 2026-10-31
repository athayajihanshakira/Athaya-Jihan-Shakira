pesanan_sandwich = [
    'spesial', 'tuna', 'spesial', 'ayam', 'keju', 'spesial', 'daging sapi'
]
sandwich_selesai = []

print("Maaf, toko deli kami sedang kehabisan menu 'spesial' hari ini!\n")

while 'spesial' in pesanan_sandwich:
    pesanan_sandwich.remove('spesial')

while pesanan_sandwich:
    sandwich_ini = pesanan_sandwich.pop(0)
    
    print(f"Saya sedang membuat sandwich {sandwich_ini} Anda.")
    sandwich_selesai.append(sandwich_ini)

print("\nDaftar sandwich yang berhasil dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich}")