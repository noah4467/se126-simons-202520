#W4D1 sequential searfch

#IMPORTS
import csv
#FUNCTIONS
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else:
        let = "ERROR"

    return let #let value replaces the function call in the main executing code.


#MAIN EXECUTING CODE

#create empty lists to hold the file data
fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("Text File/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #append the file data into appropriate lists
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnect from file -- can still access the stored data via the lists

#process the list data to calculate an avg score for each student, and find a letter grade equivalent
num_avg = [] #will hold each students numeric average of test scores
let_avg = [] #will hold each students letter average of test scores

for i in range(0, len(fName)):

    #calculate average of current student
    a = (test1[i] + test2[i] + test3[i]) / 3
    #add average to num_avg list
    num_avg.append(a)

    l = letter(a) #return value of letter() stored to l
    let_avg.append(l) #can also do: let_avg.append(letter(a))

#process the lists to display all student data back to the user

print(f"{'FNAME':10}   {'LNAME':10}   {'T1':3}  {'T2':3}  {'# AVG':6}   {'L AVG'}")

for i in range(0, len(fName)):
    print(f"{fName[i]:10}   {lName[i]:10}   {test1[i]:3}  {test2[i]:3}  {num_avg[i]:6.2f}   {let_avg[i]}")

print("---------------------------------------------------------------------------------------------------")

print(f"There are {len(fName)} students in the file. ")