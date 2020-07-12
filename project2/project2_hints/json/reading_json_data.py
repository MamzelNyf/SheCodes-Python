import json

# from pathlib import Path

##  figure out which directory this file is in
# dir_name = Path(__file__).parent
# print(dir_name)

## name the json file
# json_file = dir_name / "date / "quiz.json"
# print(json_file)
# print(json_file.exists())

## open the json file
# with json_file.open() as f:
    # data = json.load(f)


import os

# find the absolute path of the present file 
dir_name = os.path.dirname(os.path.abspath(__file__))
#print(dir_name)

# add the folder and filename to the absolute path to find the file
json_file_path = os.path.join(dir_name, "data", "quiz.json")
#print(json_file_path)

# load the json file
with open(json_file_path) as json_file:
    data = json.load(json_file)

#print(data)
# dumps function allows formatting on json file
#print(json.dumps(data, indent=2))
    
for key, value in data.items():
    for k1, v1 in value.items():
            print (f"Question {k1}: {v1['question']}")
            print ('\t'f"{v1['options'][0]}")
            print ('\t'f"{v1['options'][1]}")
            print ('\t'f"{v1['options'][2]}")
            print ('\t'f"{v1['options'][3]}")

