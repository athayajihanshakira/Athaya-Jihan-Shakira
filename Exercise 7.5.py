prompt = "\nBerapa usia kamu?"
prompt += "\n(Ketik 'keluar' untuk berhenti): "

while True:
    usia = input(prompt)
    
    if usia.lower() == 'keluar':
        break
        
    usia = int(usia)
    
    if usia < 3:
        print("Tiket kamu gratis!")
    elif usia <= 12:
        print("Harga tiket kamu adalah $10.")
    else:
        print("Harga tiket kamu adalah $15.")