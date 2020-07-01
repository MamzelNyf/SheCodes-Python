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