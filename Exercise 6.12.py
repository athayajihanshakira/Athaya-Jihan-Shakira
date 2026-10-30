cities = {
    'jakarta': {
        'negara': 'indonesia',
        'populasi': '10 juta jiwa',
        'fakta': 'Merupakan ibu kota negara dan pusat bisnis utama.',
        'zona_waktu': 'WIB (UTC+7)',
        'ikon': 'Monas (Monumen Nasional)',
    },
    'tokyo': {
        'negara': 'jepang',
        'populasi': '14 juta jiwa',
        'fakta': 'Salah satu kota metropolitan paling padat di dunia.',
        'zona_waktu': 'JST (UTC+9)',
        'ikon': 'Tokyo Tower',
    },
    'paris': {
        'negara': 'prancis',
        'populasi': '2 juta jiwa',
        'fakta': 'Terkenal dengan Menara Eiffel dan pusat mode dunia.',
        'zona_waktu': 'CET (UTC+1)',
        'ikon': 'Menara Eiffel',
    },
}

for nama_kota, info_kota in cities.items():
    print(f"\n========================================")
    print(f" INFORMASI KOTA: {nama_kota.upper()} ")
    print(f"========================================")
    print(f"Negara      : {info_kota['negara'].title()}")
    print(f"Populasi    : {info_kota['populasi']}")
    print(f"Zona Waktu  : {info_kota['zona_waktu']}")
    print(f"Ikon Utama  : {info_kota['ikon']}")
    print(f"Fakta Unik  : {info_kota['fakta']}")