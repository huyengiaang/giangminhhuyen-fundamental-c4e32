prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}

# Create a variable called total to determine how much all the fruits worth.
total = 0

for k, v in prices.items():
    print(k)
    print('price: ', v)
    i = stock.get(k)
    print('stock: ', i)

    money = v*i
    total += money
print("Total: ", total)
