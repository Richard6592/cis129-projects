# Ask the user for the number of coffees and muffins they are purchasing

nbrOfCoffees = int(input('Enter the number of coffees you are purchasing: '))
nbrOfMuffins = int(input('Enter the number of muffins you are purchasing: '))
# Adding two new menu items 
nbrOfSandwiches = int(input('Enter the number of sandwiches you are purchasing: '))
nbrOfSodas = int(input('Enter the number of sodas you are purchasing: '))

# Establish prices of coffees and muffins
priceOfCoffee = 5
priceOfMuffin = 4
# Adding prices of two new menu items
priceOfSandwich = 7
priceOfSoda = 3


# Calculate subtotal
# Added prices of two new menu items to be calculated in subtotal
subtotal = (nbrOfCoffees * priceOfCoffee) + (nbrOfMuffins * priceOfMuffin) + (nbrOfSandwiches * priceOfSandwich) + (nbrOfSodas * priceOfSoda)

# Calculate tax
taxRate = 0.06
tax = subtotal * taxRate

# Calculate total
total = subtotal + taxRate

# Added two new menu items to be shown in receipt itemization
print('***************************************')
print('My Coffee and Muffins Shop')
print('Number of coffees bought?')
print(nbrOfCoffees)
print('Number of muffins bought?')
print(nbrOfMuffins)
print('Number of sandwiches bought?')
print(nbrOfSandwiches)
print('Number of sodas bought?')
print(nbrOfSodas)
print('***************************************')

print('***************************************')
print('My Coffee and Muffins Shop Receipt')
print(f'{nbrOfCoffees} coffees at $5 each: {priceOfCoffee * nbrOfCoffees}')
print(f'{nbrOfMuffins} muffins at $4 each: {priceOfMuffin * nbrOfMuffins}')
print(f'{nbrOfSandwiches} sandwiches at $7 each: {priceOfSandwich * nbrOfSandwiches}')
print(f'{nbrOfSodas} sodas at $3 each: {priceOfSoda * nbrOfSodas}')
print(f'tax: {tax}')
print('---------')
print(f'Total: {total}')
print('***************************************')

print('Thank you for choosing My Coffee and Muffins Shop!')
