import time

utime = int(input("Enter the countdown time in seconds: "))


for x in range(utime, 0, -1): # alt:
    seconds = x % 60          # for x in reversed(range(0, utime)):
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)