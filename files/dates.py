from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    minute = datetime.today().minute
    
    if minute == odds:
        print("Seems odd")
    else:
        print("No odds right now")



