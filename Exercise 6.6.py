bahasa_favorit = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
orang_yang_harus_polling = ['jen', 'sarah', 'budi', 'siti', 'edward']

for orang in orang_yang_harus_polling:
    if orang in bahasa_favorit.keys():
        print(f"Halo {orang.title()}, terima kasih sudah meluangkan waktu untuk mengikuti polling!")
    else:
        print(f"Halo {orang.title()}, kami mengundang Anda untuk mengikuti polling bahasa favorit kami.")