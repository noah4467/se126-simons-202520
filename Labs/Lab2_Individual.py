#Noah Simons
#Lab2
#1/20/2025
#Variables used:
#file: the filehandling.csv file
#type_: the type of device
#brand: the brand of device
#cpu: the cpu being stored in the file
#firstDisk: the number of storage on the first disk being store in the file
#noHDD: the number of hard disk drives on the device
#os: the os value store in the file
#yr: the year value stored in the file


import csv

#Header
print(f"{'TYPE':10}    {'BRAND':10}   {'CPU':5} {'RAM':3} {'FIRST DISK':10}  {'NO HDD':5}   {'2ND DISK':10}   {'OS':4}  {'YR'}")

#Main Process
with open("Text_File/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    #repeats the process as many times as there are records in the file
    for record in file:
        #defines the variables as each record in the file
        type_ = record[0]
        brand = record[1]
        cpu = record[2]
        ram = record[3]
        firstDisk = record[4]
        noHDD = int (record[5])
        os = record[6]
        yr = record[7]
        #translates the letters to the device's full name
        if (type_ == "D"):
            type_ = "Desktop"
        else:
            type_ = "Laptop"
        #Translates the brand's abreviation to its full name
        if (brand == "DL"):
            brand = "Dell"
        elif (brand == "GW"):
            brand = "Gateway"
        else:
            brand = "HP"
        #redefines variables based upon the number of disk drives
        if (noHDD == 2):
            os = record[7]
            yr = record[8]
            secondDisk = record[6]
        else:
            secondDisk = "     "

        #prints the final result
        print(f"{type_:10}    {brand:10}   {cpu:5} {ram:3}  {firstDisk:10}  {noHDD:5}   {secondDisk:10}   {os:4}  {yr}")