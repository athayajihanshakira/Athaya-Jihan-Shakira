pesanan_sandwich = ['tuna', 'ayam', 'keju', 'daging sapi', 'telur']

sandwich_selesai = []

while pesanan_sandwich:
    sandwich_ini = pesanan_sandwich.pop(0)
    
    print(f"Saya sedang membuat sandwich {sandwich_ini} Anda.")
    
    sandwich_selesai.append(sandwich_ini)

print("\nSemua sandwich berikut telah selesai dibuat:")
for sandwich in sandwich_selesai:
    print(f"- Sandwich {sandwich}")