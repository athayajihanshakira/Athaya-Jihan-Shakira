pesan = "\nMasukkan topping pizza yang kamu inginkan:"
pesan += "\n(Ketik 'quit' jika sudah selesai): "

while True:
    topping = input(pesan)
    
    if topping.lower() == 'quit':
        break
    else:
        print(f"Kami akan menambahkan {topping} ke pizza kamu!")