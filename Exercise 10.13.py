from pathlib import Path
import json

path = Path('user_profile.json')

if path.exists():
    isi_json = path.read_text(encoding='utf-8')
    profil_user = json.loads(isi_json)
    
    print("\n--- Selamat datang kembali! ---")
    print(f"Berikut data yang tersimpan tentangmu:")
    print(f"- Nama      : {profil_user['nama']}")
    print(f"- Umur      : {profil_user['umur']}")
    print(f"- Kota Asal : {profil_user['kota']}")
    print(f"- Hobi      : {profil_user['hobi']}")
else:
    profil_user = {}
    
    profil_user['nama'] = input("Siapa nama kamu? ")
    profil_user['umur'] = input("Berapa umurmu? ")
    profil_user['kota'] = input("Dari kota mana kamu berasal? ")
    profil_user['hobi'] = input("Apa hobimu? ")
    
    isi_json = json.dumps(profil_user)
    path.write_text(isi_json, encoding='utf-8')
    
    print("\nTerima kasih! Informasi profilmu telah disimpan.")