# Module 4 Lab 4
# Richard Valenzuela 
# 2/27/2024
# This program reads the monthly sales and percent of sales increase
# and returns the store bonus amount and employe bonus amount

# Declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
salesIncrease = 0 # percent of sales increase
empAmount = 0 # employee bonus amount 

# This code gets the monthly sales amount 
monthlySales = float(input("Enter your monthly sales amount (example - 87000): ")) 

#This code determines the store bonus amount 
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000: 
    storeAmount = 3000
elif monthlySales <80000:
    storeAmount = 0

# This code gets the percent of increase in sales
salesIncrease = float(input("Enter the percent increase of your monthly sales (example - 3): "))
salesIncrease = salesIncrease / 100


# This code determines the employee bonus
if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
elif salesIncrease <.03:
    empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000 and empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible!')


