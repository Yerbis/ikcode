from datetime import datetime

day = datetime.weekday()

print(day)
if day == [0, 1, 2, 3, 4]:
    print("Weekday")
elif day == [5, 6]:
    print("Weekend")