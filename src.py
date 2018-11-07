import time
import os

print("Press enter to start the stopwatch")
input()
os.system('cls' if os.name == 'nt' else 'clear')

global i
i=0

global min
min=0

while True:
    i+=1
    if i == 60:
        min+=1
        i=0
    if min == 0:
        if i == 1:
            print(str(i) + " second")
        else:
            print(str(i) + " seconds")
    else:
        if i == 1 and min == 1:
            print(str(min) + " minute " + str(i) + " second")
        elif i != 1 and min == 1:
            print(str(min) + " minute " + str(i) + " seconds")
        elif i == 1 and min != 1:
            print(str(min) + " minutes " + str(i) + " second")
        elif i != 1 and min != 1:
            print(str(min) + " minutes " + str(i) + " seconds")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
