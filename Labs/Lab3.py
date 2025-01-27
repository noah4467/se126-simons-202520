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

import csv

#Defining Variables
numUnableReg = 0
numOldEnough = 0
numVoted = 0
numEligableNot = 0
numVoted = 0
totalEntries = 0

with open("Text File/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        totalEntries = totalEntries + 1
        idNumber = rec[0]
        age = int(rec[1])
        ifRegistered = rec[2]
        ifVoted = rec[3]

#Main process
        
        if (age < 18):
            numUnableReg = numUnableReg + 1
        else:
            numEligable = True 
            if (ifRegistered == "N"):
                numOldEnough = numOldEnough + 1
            else:
                if (ifVoted == "N"):
                    numEligableNot = numEligableNot + 1
                else:
                    numVoted = numVoted + 1


#prints the final result of the user-inputted data

print("The number of people not eligable to register is ", numUnableReg)
print("The number of individuals who are able to vote but have not registered is ", numOldEnough)
print("The number of individuals who are registered to vote but have not voted is ", numEligableNot)
print("The number of individuals who did vote is ", numVoted)
print("The number of records processed is ", totalEntries)