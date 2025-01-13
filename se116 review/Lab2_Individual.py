import csv

totalRecords = 0

with open("Text File/filehandling.csv") as csvfile:\
    file = csv.reader(csvfile)

    for record in file:
    totalRecords += 1
    print(record)

    type = record[0]
    brand = record[1]
    cpu = record[2]
    ram = record[3]
    firstDisk = [4]
    noHDD = record[5]
    secondDisk = record[6]
    os = record[7]
    yr = record[8]