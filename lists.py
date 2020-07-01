# Q1

foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
#when going backwards, add starting point at the end
print(foods[-1:-4:-1])
print(foods[6][-1])

print()

# Q2

mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")

print()

# Q3

# with extend
user_name_1 = input("You will have to enter 3 names. Enter the first name: ")
user_name_2 = input("Enter the second name: ")
user_name_3 = input("Enter the third name: ")
user_list = []

user_list.extend([user_name_1,user_name_2,user_name_3])
print(user_list)

# with append
user_name_1="Izzy"
user_name_2="Archie"
user_name_3="Boston"
user_list = []

user_list.append(user_name_1)
user_list.append(user_name_2)
user_list.append(user_name_3)

print(user_list)

print()

# Q4

# user_string = input("Enter a string: ")

user_string = "this is a string"
string_list = user_string.split()
letter_list = list(user_string)
print(string_list)
print(letter_list)

user_string = "what a lovely day!"
string_list = user_string.split()
letter_list = list(user_string)
print(len(string_list), string_list)
print(len(letter_list), letter_list)

