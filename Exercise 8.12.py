def buat_sandwich(*daftar_bahan):
    """Mencetak ringkasan bahan-bahan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan bahan-bahan berikut:")
    for bahan in daftar_bahan:
        print(f"- {bahan}")
        
buat_sandwich('Keju', 'Tomat', 'Selada')
buat_sandwich('Daging Sapi', 'Keju Cheddar', 'Saus Tomat', 'Mayones')
buat_sandwich('Telur Dadar')