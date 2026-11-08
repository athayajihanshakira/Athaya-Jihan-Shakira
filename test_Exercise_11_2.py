from fungsikota import kota_negara

def test_kota_negara():
    hasil = kota_negara('santiago', 'chile')
    assert hasil == 'Santiago, Chile'

def test_kota_negara_populasi():
    hasil = kota_negara('santiago', 'chile', populasi='5000000')
    assert hasil == 'Santiago, Chile - populasi 5000000'