#Q1
number_1 = 3
number_2 = 9
print(number_1 + number_2)

number_1 = -3
number_2 = 9
print(number_1 + number_2)

number_1 = 3.0
number_2 = -9
print(number_1 + float(number_2))

print()

#Q2
number_1 = 3
number_2 = 9
result = number_1 * number_2
print(f"{number_1} * {number_2} = {result}")

number_1 = -3
number_2 = 9
result = number_1 * number_2
print(f"{number_1} * {number_2} = {result}")

number_1 = 3.0
number_2 = -9
result= float(number_1 * number_2)
print(f"{number_1} * {number_2} = {result}")

print()

#Q3
distance_km = 10
distance_m = distance_km * 1000
distance_cm = distance_km * 100000
print(f"{distance_km}km = {distance_m}m")
print(f"{distance_km}km = {distance_cm}cm")

distance_km = 5.4
distance_m = int(distance_km * 1000)
distance_cm = int(distance_km * 100000)
print(f"{distance_km}km = {distance_m}m")
print(f"{distance_km}km = {distance_cm}cm")

print()

#Q4
user_name = "William"
height_cm = 192
print(f"{user_name} is {height_cm}cms tall.")

user_name = "Roary"
height_cm = 27
print(f"{user_name} is {height_cm}cms tall.")