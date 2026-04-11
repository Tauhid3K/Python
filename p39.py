# Read (.text, .json, .csv)

file_path = "C:/Users/Username/Documents/sample.txt"

try:
    with open(file_path, 'r') as file:  # 'r' is used to read the file
        content = file.read()           # read() method is used to read the entire content of the file
        print(content)
except FileNotFoundError:               # to handle the case when the file does not exist
    print(f"The file {file_path} was not found.")
except PermissionError:                 # to handle the case when there is a permission issue
    print(f"You do not have permission to read the file {file_path}.")

import json

file_path = "C:/Users/Username/Documents/employee_data.json"

try:
    with open(file_path, 'r') as file:
        content = json.load(file)   # json.load() is used to read json data from a file and convert it to a Python dictionary
        print(content)
        print(content["name"])      # to access specific data from the dictionary
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except json.JSONDecodeError:        # to handle the case when the file is not in valid json format
    print(f"The file {file_path} is not in valid JSON format.")

import csv

file_path = "C:/Users/Username/Documents/employee_data.csv"

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)   # csv.reader() is used to read csv data from a file
        for line in content:         # to iterate through each row in the csv file
            print(line)
            print(line[2])           # to access specific data from the row (e.g., job title)
except FileNotFoundError:
    print(f"The file {file_path} was not found.")