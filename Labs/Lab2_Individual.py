import csv

totalRecords = 0

print(f"{'TYPE':10}    {'BRAND':10}   {'CPU':5} {'RAM':3} {'FIRST DISK':10}  {'NO HDD':5}   {'2ND DISK':10}   {'OS':4}  {'YR'}")

with open("Text File/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)

    for record in file:

        type_ = record[0]
        brand = record[1]
        cpu = record[2]
        ram = record[3]
        firstDisk = record[4]
        noHDD = int (record[5])
        os = record[6]
        yr = record[7]

        if (type_ == "D"):
            type_ = "Desktop"
        else:
            type_ = "Laptop"

        if (brand == "DL"):
            brand = "Dell"
        elif (brand == "GW"):
            brand = "Gateway"
        else:
            brand = "HP"
    
        if (noHDD == 2):
            os = record[7]
            yr = record[8]
            secondDisk = record[6]
        else:
            secondDisk = "     "
    
        print(f"{type_:10}    {brand:10}   {cpu:5} {ram:3}  {firstDisk:10}  {noHDD:5}   {secondDisk:10}   {os:4}  {yr}")