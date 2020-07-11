# Q1

groceries = {
"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Bacon": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}

number_purchase = 0
unit_price = 0

def calculate_cost(unit_price, number_purchase):
    for item in groceries:
        items_prices = []
        number_purchase = int(input(f"How many units of {item} did you buy? "))
        unit_price = number_purchase * groceries[item]
        items_prices.append(unit_price)
    
    print()

    print("{:=^28}".format("Izzy's Food Emporium"))
    for (item, price) in zip(groceries, items_prices):
        print(f"{item:<17} ${price:.2f}")
    print("{:=^28}".format(""))
    total_prices = sum(items_prices)
    print("{:>24}".format(f"${total_prices:.2f}"))


calculate_cost(unit_price, number_purchase)

print()

# Q2

#  count the frequency of elements in a list using a dictionary 
def CountFrequency(my_list): 
    # Creating an empty dictionary  
    dictionaryNames = {} 
    for items in my_list: 
        dictionaryNames[items] = my_list.count(items) 
        # print(items)
        # print(dictionaryNames[items])

    for key, value in dictionaryNames.items(): 
        print(key, value) 
    

names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]    
CountFrequency(names) 

print()

#Q3

def read_csv_file(filepath):
    import csv
    import pprint
    with open(filepath) as csv_file:
        # use function DictReader to convert a csv in a dictionary 
        reader = csv.DictReader(csv_file, skipinitialspace=True)
        colours = []
        for line in reader:
            colours.append(line)
        print(f"colours =")
        # import pretty printer to priont a dictionary line by line 
        pprint.pprint(colours)

read_csv_file("exercise_data/colours_20.csv")
read_csv_file("exercise_data/colours_213.csv")
