#Noah Simons
#Lab 6
#2/23/2025
#Variables used:

import csv

row = []
seatA = []
seatB = []
seatC = []
seatD = []

with open("Text_File/seating.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        row.append(rec[0])
        seatA.append(rec[1])
        seatB.append(rec[2])
        seatC.append(rec[3])
        seatD.append(rec[4])

def display():
    for i in range(0, len(row)):
        print(f"\t{row[i]:3}   {seatA[i]:3}   {seatB[i]:3}   {seatC[i]:3}   {seatD[i]}")

display()

answer = input("Please select a seat. Ex. 1A, 3C ").upper()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#row 1
if answer == "1A":
    seatA[0] = "X"
    display()
elif answer == "1B":
    seatB[0] = "X"
    display()
elif answer == "1C":
    seatC[0] = "X"
    display()
elif answer == "1D":
    seatD[0] = "X"
    display()
#row 2
elif answer == "2A":
    seatA[1] = "X"
    display()
elif answer == "2B":
    seatB[1] = "X"
    display()
elif answer == "2C":
    seatC[1] = "X"
    display()
elif answer == "2D":
    seatD[1] = "X"
    display()
#row 3
elif answer == "3A":
    seatA[2] = "X"
    display()
elif answer == "3B":
    seatB[2] = "X"
    display()
elif answer == "3C":
    seatC[2] = "X"
    display()
elif answer == "3D":
    seatD[2] = "X"
    display()
#row 4
elif answer == "4A":
    seatA[3] = "X"
    display()
elif answer == "4B":
    seatB[3] = "X"
    display()
elif answer == "4C":
    seatC[3] = "X"
    display()
elif answer == "4D":
    seatD[3] = "X"
    display()
#row 5
elif answer == "5A":
    seatA[4] = "X"
    display()
elif answer == "5B":
    seatB[4] = "X"
    display()
elif answer == "5C":
    seatC[4] = "X"
    display()
elif answer == "5D":
    seatD[4] = "X"
    display()
#row 6
elif answer == "6A":
    seatA[5] = "X"
    display()
elif answer == "6B":
    seatB[5] = "X"
    display()
elif answer == "6C":
    seatC[5] = "X"
    display()
elif answer == "6D":
    seatD[5] = "X"
    display()
#row 7
elif answer == "7A":
    seatA[6] = "X"
    display()
elif answer == "7B":
    seatB[6] = "X"
    display()
elif answer == "7C":
    seatC[6] = "X"
    display()
elif answer == "7D":
    seatD[6] = "X"
    display()
else:
    print("Seat does not exist.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def moreData():
    anyMoreData = input("Would you like to book another seat? (y or n) ").lower()

    if anyMoreData == "y":
        answer = input("Please select a seat. Ex. 1A, 3B ").upper()
        #row 1
        if answer == "1A" and seatA[0] != "X":
            seatA[0] = "X"
        elif answer == "1B" and seatB[0] != "X":
            seatB[0] = "X"
        elif answer == "1C" and seatC[0] != "X":
            seatC[0] = "X"
        elif answer == "1D" and seatD[0] != "X":
            seatD[0] = "X"
        #row 2
        elif answer == "2A" and seatA[1] != "X":
            seatA[1] = "X"
        elif answer == "2B" and seatB[1] != "X":
            seatB[1] = "X"
        elif answer == "2C" and seatC[1] != "X":
            seatC[1] = "X"
        elif answer == "2D" and seatD[1] != "X":
            seatD[1] = "X"
        #row3
        elif answer == "3A" and seatA[2] != "X":
            seatA[2] = "X"
        elif answer == "3B" and seatB[2] != "X":
            seatB[2] = "X"
        elif answer == "3C" and seatC[2] != "X":
            seatC[2] = "X"
        elif answer == "3D" and seatD[2] != "X":
            seatD[2] = "X"
        #row 4
        elif answer == "4A" and seatA[3] != "X":
            seatA[3] = "X"
        elif answer == "4B" and seatB[3] != "X":
            seatB[3] = "X"
        elif answer == "4C" and seatC[3] != "X":
            seatC[3] = "X"
        elif answer == "4D" and seatD[3] != "X":
            seatD[3] = "X"
        #row 5
        elif answer == "5A" and seatA[4] != "X":
            seatA[4] = "X"
        elif answer == "5B" and seatB[4] != "X":
            seatB[4] = "X"
        elif answer == "5C" and seatC[4] != "X":
            seatC[4] = "X"
        elif answer == "5D" and seatD[4] != "X":
            seatD[4] = "X"
        #row 6
        elif answer == "6A" and seatA[5] != "X":
            seatA[5] = "X"
        elif answer == "6B" and seatB[5] != "X":
            seatB[5] = "X"
        elif answer == "6C" and seatC[5] != "X":
            seatC[5] = "X"
        elif answer == "6D" and seatD[5] != "X":
            seatD[5] = "X"
        #row 7
        elif answer == "7A" and seatA[6] != "X":
            seatA[6] = "X"
        elif answer == "7B" and seatB[6] != "X":
            seatB[6] = "X"
        elif answer == "7C" and seatC[6] != "X":
            seatC[6] = "X"
        elif answer == "7D" and seatD[6] != "X":
            seatD[6] = "X"
        else:
            print("Seat occupied or does not exist.")
        display()
        moreData()
    elif anyMoreData == "n":
        print("Goodbye!")
    else:
        print("Invalid entry.")
        moreData()

moreData()