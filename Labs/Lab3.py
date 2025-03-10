#Noah Simons
#Lab #3
#1/26/2024
#Variables used:
#idNumber: asks the user for the person's ID number
#numUnableReg: The number of people unable to register
#numOldEnough: the number of people old enough to vote but not registered
#totalEntrees: the number of entrees into the program
#numEligableNot: the number of people who are eligable to vote but did not vote
#numVoted: the number of people who voted
#idNumber: the id number attached to each user in the csv file
#age: the age attached to each user in the csv file
#ifRegistered: whether the user is eligable to vote. either "Y or N"
#ifVoted: whether the user voted or not. either "Y or N"

import csv

#Defining Variables
numUnableReg = 0
numOldEnough = 0
numVoted = 0
numEligableNot = 0
numVoted = 0
totalEntries = 0
#defines the lists as empty
idNumber = []
age = []
ifRegistered = []
ifVoted = []

with open("Text_File/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)
    #appends csv data to lists
    for rec in file:
        totalEntries = totalEntries + 1
        idNumber.append(rec[0])
        age.append(int(rec[1]))
        ifRegistered.append(rec[2])
        ifVoted.append(rec[3])

#Main process
for i in range(0, len(idNumber)):    
    if (age[i] < 18):
        numUnableReg = numUnableReg + 1
    else:
        numEligable = True 
        if (ifRegistered[i] == "N"):
            numOldEnough = numOldEnough + 1
        else:
            if (ifVoted[i] == "N"):
                numEligableNot = numEligableNot + 1
            else:
                numVoted = numVoted + 1


#prints the final number of people in each category

print("The number of people not eligable to register is ", numUnableReg)
print("The number of individuals who are able to vote but have not registered is ", numOldEnough)
print("The number of individuals who are registered to vote but have not voted is ", numEligableNot)
print("The number of individuals who did vote is ", numVoted)
print("The number of records processed is ", totalEntries)