pizzas = ["pepperoni", "meat lovers", "cheese"]

teman_pizzas = pizzas[:]
pizzas.append("hawaiian")
teman_pizzas.append("suae")
print("Pizza favorit saya adalah:")

for pizza in pizzas:
    print(pizza)

print("\nPizza favorit teman saya adalah:")
for pizza in teman_pizzas:
    print(pizza)