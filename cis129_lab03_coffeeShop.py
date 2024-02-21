# Ask the user for the number of coffees and muffins they are purchasing

nbrOfCoffees = int(input('Enter the number of coffees you are purchasing: '))
nbrOfMuffins = int(input('Enter the number of muffins you are purchasing: '))

# Establish prices of coffees and muffins
priceOfCoffee = 5
priceOfMuffin = 4

# Calculate subtotal
subtotal = (nbrOfCoffees * priceOfCoffee) + (nbrOfMuffins * priceOfMuffin)

# Calculate tax
taxRate = 0.06
tax = subtotal * taxRate

# Calculate total
total = subtotal + taxRate

print('***************************************')
print('My Coffee and Muffins Shop')
print('Number of coffees bought?')
print(nbrOfCoffees)
print('Number of muffins bought?')
print(nbrOfMuffins)
print('***************************************')

print('***************************************')
print('My Coffee and Muffins Shop Receipt')
print(f'{nbrOfCoffees} coffees at $5 each: {priceOfCoffee * nbrOfCoffees}')
print(f'{nbrOfMuffins} muffins at $4 each: {priceOfMuffin * nbrOfMuffins}')
print(f'tax: {tax}')
print('---------')
print(f'Total: {total}')
print('***************************************')
