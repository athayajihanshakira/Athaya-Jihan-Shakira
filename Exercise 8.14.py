def buat_mobil(pabrikan, model, **fitur_lain):
    mobil = {
        'pabrikan_mobil': pabrikan,
        'model_mobil': model
    }
    
    for kunci, nilai in fitur_lain.items():
        mobil[kunci] = nilai
        
    return mobil

mobil = buat_mobil('subaru', 'outback', warna='blue', tow_package=True)

print("\nInformasi Mobil:")
print(mobil)