#write

text_data = "This is a sample text data that will be written to a file."

file_path = "sample.txt"
# there are absolute path and relative path
# absolute path is the full path to the file, for example: C:\Users\Username\Documents\sample.txt
# relative path is the path to the file relative to the current working directory, for example: sample.txt

with open(file_path, 'w') as file: # w will overwrite 
    # using 'with' statement to handle file opening and closing
    # w = write a = append x = create a new file, if file already exists it will raise an error
    file.write(text_data)
    print(f"Text file  {file_path} has been created.")
    
file_path = "c:/Users/Username/Documents/sample.txt"
    
try: # to handle exceptions that may occur during file handling
    with open(file_path, 'x') as file: 
        file.write(text_data)
        print(f"Text file  {file_path} has been created.")
except FileExistsError:
    print(f"The file {file_path} already exists. ")
    
try:
    with open(file_path, 'a') as file:
        file.write("\n" + text_data) # \n is used to add a new line before the text data
        print(f"Data has been appended to {file_path}")
except FileExistsError:
    print(f"The file {file_path} already exists. ")
    
employees = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"]
# write method can only write string data to a file
# 
try:
    with open("employees.txt", 'w') as file:
        for employee in employees:      # used loop to write each employee name to the file
            file.write(employee + "\n") 
        print("Employee names have been written to employees.txt")
except Exception as e:
    print(f"An error occurred: {e}")
    
import json

employee_data = {
    "John Doe": 30,
    "Jane Smith": 28,
    "Alice Johnson": 35,
    "Bob Brown": 40
}
file_path = "C:/Users/Username/Documents/employee_data.txt"
try:
    with open(file_path, 'w') as file:
        json.dump(employee_data, file, indent=4) 
        # indent is used to format the json data in a readable way
        # json.dump() is used to write a dictionary to a file in json format
        print(f"Employee data has been written to '{file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")
    
    
import csv

employee_data = [
    ["Name", "Age", "Job"],
    ["John Doe", 30, "Software Engineer"],
    ["Jane Smith", 28, "Data Analyst"]
    ["Bob Brown", 40, "Project Manager"]
]

file_path = "C:/Users/Username/Documents/employee_data.csv"

try:
    with open(file_path, 'w') as file:
        writer = csv.writer(file)      # create a csv writer object
        for employee in employee_data: # write each employee data to the csv file
            writer.writerow(employee)  # writerow() is used to write a single row of data to the csv file
        print(f"Employee data has been written to '{file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")