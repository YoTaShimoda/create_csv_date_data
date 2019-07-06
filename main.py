import csv
import random

def getdays(year, month):
    long_month = [1, 3, 5, 7, 10, 12]
    half_month = [4, 6, 9, 11]
    if month in long_month:
        return 31

    elif month in half_month:
        return 30

    else:
        if year % 4 == 0:
            return 29
        else:
            return 28

with open('csvdata.csv', 'a') as f:
    csvwrite = csv.writer(f)
    data_list = []
    for i in range(3000):
        year = random.randint(1990, 2018)
        month = random.randint(1, 12)
        day = getdays(year, month)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        secound = random.randint(0,59)
        data_list.append(str(year) + '/' + str(month) + '/' + str(day) + '/' + str(hour) + ':' + str(minute) + ':'+ str(secound))

    csvwrite.writerow(data_list)






