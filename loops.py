# Q1

number_list = []
user_number = (input("Choose a number? "))
#print(user_number)

while user_number != '':
    #print(user_number)
    number_list.append(int(user_number))
    #print(number_list)
    user_number = (input("Choose a number? "))

print(sum(number_list))

print()

# Q2

mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

for mailing in mailing_list:
    print(f"{mailing[0]}: {mailing[1]}")

print()

# Q3

user_name = (input("Choose a name? "))
name_list = []

while len(name_list) < 3:
    name_list.append(user_name)
    #print(len(name_list))
    if len(name_list) < 3:
        user_name = (input("Choose a name? "))

for name in name_list:
    print(f"{name}")
    

print()

# Q4

groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]
items_prices = []


for item in groceries:
    units_price = int(input(f"how many units of {item[0]} did you buy? "))
    units_price = item[1] * units_price
    #print (units_price)
    items_prices.append(units_price)
    #print (items_prices)

# {:sign^number} to center an element with signs around
print("{:=^28}".format("Izzy's Food Emporium"))

# zip function to iterate through 2 loops
for (item, price) in zip(groceries, items_prices):
    print(f"{item[0]:<17} ${price:.2f}")

#print a lign of =
print("{:=^28}".format(""))

# sum function to add all int or float elements in an array
total_prices = sum(items_prices)

# to format a string, can combined with f"" to format a variable, :.2f to format a number with two decimals
print("{:>24}".format(f"${total_prices:.2f}"))