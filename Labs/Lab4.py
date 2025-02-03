#Noah Simons
#Lab4
#1/28/2025
#variables used:

import random
import csv

fName = []
lName = []
age = []
sName = []
house = []
email = []
dept = []
ext = []

print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")

with open("Text_File/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        sName.append(rec[3])
        house.append(rec[4])
    
    for index in range(0, len(sName)):
        email.append(sName[index] + "@westeros.net")

        if (house[index] == "House Stark"):
            dept.append("Research & Development")
        elif (house[index] == "House Targaryen"):
            dept.append("Marketing")
        elif (house[index] == "House Tully"):
            dept.append("Human Resources")
        elif (house[index] == "House Lannister"):
            dept.append("Accounting")
        elif (house[index] == "House Baratheon"):
            dept.append("Sales")
        else:
            dept.append("Auditing")
        
        if (house[index] == "House Stark"):
            ext.append(random.randint(100, 199))
        elif (house[index] == "House Targaryen"):
            ext.append(random.randint(200, 299))
        elif (house[index] == "House Tully"):
            ext.append(random.randint(300, 399))
        elif (house[index] == "House Lannister"):
            ext.append(random.randint(400, 499))
        elif (house[index] == "House Baratheon"):
            ext.append(random.randint(500, 599))
        else:
            ext.append(random.randint(600, 699))

    for i in range(0, len(fName)):
        print(f"{fName[i]:8}   {lName[i]:10}  {email[i]:30}  {dept[i]:23}   {ext[i]:3}")
    
    file = open("Text_File/westeros.csv", "w")

    for i in range(0, len(fName)):
        file.write(f"{fName[i]}{','}{lName[i]}{','}{email[i]}{','}{dept[i]}{','}{ext[i]}\n")
