# Q1 
def temperature_convertor(fahrenheit):
    celsius = round((fahrenheit - 32)*5/9,1)
    print(f"{fahrenheit}°F is {celsius}°C")
    return celsius

temperature = int(input("Type a temperature in fahrenheit: "))
temperature_convertor(temperature)

print()

# Q2
number_list = []
user_number = (input("Choose a number? "))

while user_number != '':
    number_list.append(int(user_number))
    user_number = (input("Choose a number? "))
total_sum = sum(number_list)

def calculate_mean(total_sum, user_number):
    sumOfNumbers = 0
    for n in number_list:
        sumOfNumbers += n 
    mean = sumOfNumbers / len(number_list)
    return mean

if user_number != 0 :
    print(calculate_mean(total_sum, user_number))

print()

# Q3
colour_data = []

def read_csv_file(filepath):
    import csv
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file, skipinitialspace=True)
        for line in reader:
            colour_data.append(line)
    return colour_data

def format_colour_line(colour_data):
    for colour_english in colour_data:
        print(f"{colour_english[1]:<15} {colour_english[2]:<15} {colour_english[4]}")

read_csv_file("exercise_data/colours_20.csv")
format_colour_line(colour_data)

print()

read_csv_file("exercise_data/colours_213.csv")
format_colour_line(colour_data)

print()

# Q4
items_prices = []
number_purchase = 0
unit_price = 0

def calculate_cost(unit_price, number_purchase):
    for item in groceries:
        number_purchase = int(input(f"How many units of {item[0]} did you buy? "))
        unit_price = number_purchase * item[1]
        items_prices.append(unit_price)
    
    print()

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

groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

calculate_cost(unit_price, number_purchase)




