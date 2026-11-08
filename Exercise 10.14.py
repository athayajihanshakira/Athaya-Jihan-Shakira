from pathlib import Path
import json

def get_stored_username(path):
    """Ambil nama pengguna yang sudah tersimpan jika filenya ada."""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Minta nama baru dari pengguna lalu simpan ke file JSON."""
    username = input("Siapa nama kamu? ")
    contents = json.dumps(username)
    path.write_text(contents, encoding='utf-8')
    return username

def greet_user():
    """Menyapa pengguna, dengan fitur verifikasi apakah pengguna saat ini benar."""
    path = Path('username.json')
    username = get_stored_username(path)
    
    if username:
        konfirmasi = input(f"Apakah kamu {username}? (y/n): ")
        if konfirmasi.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu saat kamu kembali, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu saat kamu kembali, {username}!")

greet_user()