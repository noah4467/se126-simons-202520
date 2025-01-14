import csv

totalRecords = 0

print(f"{'TYPE'}    {'BRAND'}   {'CPU'} {'RAM'} {'FIRST DISK'}  {'NO HDD'}   {'2ND DISK'}   {'OS'}  {'YR'}")

with open("Text File/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:
        totalRecords += 1
        print(record)

        type_ = record[0]
        brand = record[1]
        cpu = record[2]
        ram = record[3]
        firstDisk = [4]
        noHDD = record[5]
        secondDisk = record[6]
        os = record[7]
        yr = record[8]

    if (type_ == "D"):
        type_ = "Desktop"
    else:
        type_ = "Laptop"
    if (noHDD == 2):
        