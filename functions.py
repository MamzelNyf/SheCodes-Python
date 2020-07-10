# Q1 
def temperature_convertor(fahrenheit):
    celsius = (fahrenheit - 32)*5/9
    print(f"{fahrenheit}°F is {celsius}°C")
    return celsius

temperature = int(input("Type a temperature in fahrenheit: "))
temperature_convertor(temperature)

# Q2
number_list = []
user_number = (input("Choose a number? "))

def calculate_mean(total_sum, user_number):
    while user_number != '':
        number_list.append(int(user_number))
        user_number = (input("Choose a number? "))
    total_sum = sum(number_list)
    print(total_sum)
    return total_sum

calculate_mean(user_number)

print()

# Q3
