# Q1
names = []

with open("names.txt") as txt_file:
    # enumerate is a function to create index before lines from a text file
    for index, line in enumerate(txt_file):
        line = line.strip()
        print(f"{index}. {line}")
        names.extend([index,line])

print()

# Q2
import csv

colours_output_20 = []
colours_output_213 = []


with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    for line in reader:
        colours_output_20.append(line)

for colours_english in colours_output_20:
    print(f"{colours_english[1]:<15} {colours_english[2]:<15} {colours_english[4]}")

print()

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file, skipinitialspace=True)
    for line in reader:
        colours_output_213.append(line)

for colours_english in colours_output_213:
    print(f"{colours_english[1]:<15} {colours_english[2]:<15} {colours_english[4]}")

print()

# Q3
# create a function to count a number aof element in a list with sublists 
def countColour(colourList, colour):
    colourList = [item for sublist in colourList for item in sublist]
    #   flatten the sublists in a list to be able to count the occurences
    #     flat_list = []
    #     for sublist in colour_list:
    #       for item in sublist:
    #           flat_list.append(item)
    count = 0
    for i in range(len(colourList)): 
        if colour in colourList[i]: 
            count+= 1
    return count

colour_csv = input("Choose between colours_20.csv and colours_213.csv: ")

while colour_csv != "colours_20.csv" or colour_csv != "colours_213.csv" :
    if colour_csv == "colours_20.csv":
        red = countColour(colours_output_20,"red")
        green = countColour(colours_output_20,"green")
        blue = countColour(colours_output_20,"blue")
        print(f"Red: {red} \nGreen: {green} \nBlue: {blue} ")
        break

    elif colour_csv == "colours_213.csv":
        red = countColour(colours_output_213,"red")
        green = countColour(colours_output_213,"green")
        blue = countColour(colours_output_213,"blue")
        print(f"Red: {red} \nGreen: {green} \nBlue: {blue} ")
        break

    else:
        print("Please choose between the 2 files provided")
        colour_csv = input("Choose between colours_20.csv and colours_213.csv: ")

        

