sungai_utama = {
    'sungai nil': 'mesir',
    'sungai amazon': 'brasil',
    'sungai panjang (yangtze)': 'cina'
}

for sungai, negara in sungai_utama.items():
    print(f"Sungai {sungai.title()} mengalir melewati negara {negara.title()}.")

print("\nDaftar Sungai:")
for sungai in sungai_utama.keys():
    print(f"- {sungai.title()}")

print("\nDaftar Negara:")
for negara in sungai_utama.values():
    print(f"- {negara.title()}")