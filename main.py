import csv
import os
from sys import argv
arr_date = []
arr_high = []
arr_low = []
arr_close = []

script, location, name = argv
print(location, name)
for root, dirs, files in os.walk(location):
    for file in files:
        if file.endswith(".csv"):
            work_file = os.path.join(root, file)
            with open(work_file) as csvfile:
                reader = csv.DictReader(csvfile, delimiter = ";")
                for row in reader:
                    if row['Name'] == name:
                        arr_date.append(float(row['open']))
                        arr_high.append(float(row['high']))
                        arr_low.append(float(row['low']))
                        arr_close.append(float(row['close']))

def format(arr):
    arr = float('{:.3f}'.format(sum(arr)/len(arr)))
    return arr

if arr_date != [] or arr_high != [] or arr_low != [] or arr_close != []:

    arr_date = format(arr_date)
    arr_high = format(arr_high)
    arr_low = format(arr_low)
    arr_close = format(arr_close)
    print(arr_date),print(arr_high),print(arr_low), print(arr_close)
else:
    print('Данные не найдены')

