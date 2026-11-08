from fungsikota import kota_negara

def test_kota_negara ():
    hasil = kota_negara ("santiago", "chile")
    assert hasil == "Santiago, Chile"