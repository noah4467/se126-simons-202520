#Noah Simons
#Lab4
#1/28/2025
#variables used:
#numRes: the number of employees in the Research & Development department.
#numMar: the number of employees in the Marketing department.
#numHu: the number of employees in the Human Resources department
#numAcc: the number of employees in the accounting department
#numSal: the number of employees in the Sales department
#numAud: the number of employees in the Auditing department
#fName: the first name of the employee
#lName: the last name of the employee
#age: the age of the employee
#sName: the screen name of the employee
#house: the house allegiance of the employee
#email: the compiled email of the employee
#dept: the employee's department
#ext: the random phone extension assigned to the employee

import random
import csv

#starts number of employees in each department at zero
numRes = 0
numMar = 0
numHu = 0
numAcc = 0
numSal = 0
numAud = 0

#defines the fields as empty lists
fName = []
lName = []
age = []
sName = []
house = []
email = []
dept = []
ext = []

#Header
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")

#opens got_emails.csv
with open("Text_File/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)
    #adds the different records to the empty lists
    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        sName.append(rec[3])
        house.append(rec[4])

    #compiles the screen name to an email
    for index in range(0, len(sName)):
        email.append(sName[index] + "@westeros.net")

        #assigns the employee department based on house and logs the number in each department
        if (house[index] == "House Stark"):
            dept.append("Research & Development")
            numRes = numRes + 1
        elif (house[index] == "House Targaryen"):
            dept.append("Marketing")
            numMar = numMar + 1
        elif (house[index] == "House Tully"):
            dept.append("Human Resources")
            numHu = numHu + 1
        elif (house[index] == "House Lannister"):
            dept.append("Accounting")
            numAcc = numAcc + 1
        elif (house[index] == "House Baratheon"):
            dept.append("Sales")
            numSal = numSal + 1
        else:
            dept.append("Auditing")
            numAud = numAud + 1

        #assigns the employee a random extension in a range based on their house
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

    #prints the data from got_emails.csv
    for i in range(0, len(fName)):
        print(f"{fName[i]:8}   {lName[i]:10}  {email[i]:30}  {dept[i]:23}   {ext[i]:3}")

    #prints the data to westeros.csv file and closes the file.
    file = open("Text_File/westeros1.csv", "w")

    for i in range(0, len(fName)):
        file.write(f"{fName[i]}{','}{lName[i]}{','}{email[i]}{','}{dept[i]}{','}{ext[i]}\n")
    file.close()

    print()
    print("File closed.")
    
    #prints the number of employees and the number of employees in each department
    print()
    print("There are ", len(fName), " employees.")
    print()
    print("There are ", numRes, " employees in the Research & Development department.")
    print("There are ", numMar, "employees in the Marketing department.")
    print("There are ", numHu, "employees in the Human Resources department.")
    print("There are ", numAcc, "employees in the Accounting department.")
    print("There are ", numSal, "employees in the Sales department.")
    print("There are ", numAud, "employees in the Auditing department.")
