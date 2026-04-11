#calculate execution time

import time

start_time = time .perf_counter() 
# Your code goes here

for i in range(1000000):
    pass

end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.3f} seconds")

import datetime

date = datetime.date(2005, 9, 16)
print(date) #prints the date in the format YYYY-MM-DD

today = datetime.date.today()
print(today) #prints the current date in the format YYYY-MM-DD

time = datetime.time(14, 30, 0)
print(time) #prints the time in the format HH:MM:SS

now = datetime.datetime.now()
print(now) #prints the current date and time in the format YYYY-MM-DD HH:MM

now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now) #prints the current time in the format HH:MM:SS

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("The target date has passed.")
else:
    print("The target date is in the future.")