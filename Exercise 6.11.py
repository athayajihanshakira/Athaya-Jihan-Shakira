cities = {
    'jakarta': {
        'negara': 'indonesia',
        'populasi': '10 juta jiwa',
        'fakta': 'Merupakan ibu kota negara dan pusat bisnis utama.',
    },
    'tokyo': {
        'negara': 'jepang',
        'populasi': '14 juta jiwa',
        'fakta': 'Salah satu kota metropolitan paling padat di dunia.',
    },
    'paris': {
        'negara': 'prancis',
        'populasi': '2 juta jiwa',
        'fakta': 'Terkenal dengan Menara Eiffel dan pusat mode dunia.',
    },
}

for nama_kota, info_kota in cities.items():
    print(f"\nKota: {nama_kota.title()}")
    print(f"- Negara: {info_kota['negara'].title()}")
    print(f"- Populasi: {info_kota['populasi']}")
    print(f"- Fakta Unik: {info_kota['fakta']}")