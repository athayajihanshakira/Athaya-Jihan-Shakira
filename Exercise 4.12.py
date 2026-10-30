makanan_saya = ['pizza', 'falafel', 'kue wortel', 'cannoli']
makanan_teman = makanan_saya[:]

makanan_saya.append('es krim')
makanan_teman.append('brownies')

print("Makanan kesukaan saya adalah:")
for makanan in makanan_saya:
    print(makanan)

print("\nMakanan kesukaan teman saya adalah:")
for makanan in makanan_teman:
    print(makanan)