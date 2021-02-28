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

if arr_date != [] or arr_high != [] or arr_low != [] or arr_close != []:
    arr_date = float('{:.3f}'.format(sum(arr_date)/len(arr_date)))
    arr_high = float('{:.3f}'.format(sum(arr_high)/len(arr_high)))
    arr_low = float('{:.3f}'.format(sum(arr_low)/len(arr_low)))
    arr_close = float('{:.3f}'.format(sum(arr_close)/len(arr_close)))
    print(arr_date)
    print(arr_high)
    print(arr_low)
    print(arr_close)
else:
    print('Данные не найдены')

