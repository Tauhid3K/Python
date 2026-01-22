import time
my_timer = int(input("Enter time in seconds: "))

'''
# Countdown timer
for x in range(0, my_timer):
    print (x)
    time.sleep(1)

print("Times up!")

# Countdown timer in reverse
for x in range(my_timer, 0, -1):
    print (x)
    time.sleep(1)

print("Times up!")
'''
# Countdown timer in reverse HH:MM:SS format
for x in range(my_timer, 0, -1):
    seconds = x % 60
    minutes = int((x / 60) % 60)
    hours = int((x / 3600) % 24)
    print (f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up!")