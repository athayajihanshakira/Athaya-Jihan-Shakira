import random

class Dadu:
    def __init__(self, jumlah_sisi=6):
        self.jumlah_sisi = jumlah_sisi

    def lempar_dadu(self):
        angka = random.randint(1, self.jumlah_sisi)
        print(angka)

print("Dadu 6 sisi:")
dadu1 = Dadu()

for i in range(10):
    dadu1.lempar_dadu()
print("Dadu 10 sisi:")
dadu2 = Dadu(10)

for i in range(10):
    dadu2.lempar_dadu()
print("Dadu 20 sisi:")
dadu3 = Dadu(20)

for i in range(10):
    dadu3.lempar_dadu()