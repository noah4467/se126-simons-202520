#W3D2 - List Review - 1Dimsensional Lists and parallel lists

#this file uses: class_grades.csv

#IMPORTS-----------
import csv
#Functions

#Main Executing code

total_records = 0

#create an empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []

with open("Text File/class_grades.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        #for every record in th efile do the following
        #print(f"{rec[0]:10}\t{rec[1]:10}")
        
        #fname = rec[0]
        #lname = rec[1]
        #test_1 = rec[2]

        #add the record data to its corresponding list (1 list per field)
        #append --> to add the to the end
        firstName.append(rec[0])
        lastName.append(rec[1])

        test1.append(int(rec[2])) #cast as integer for easier maths later
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))
#disconnect from the file -- all file data is retained bc we are using lists

#basic processing - use the 1D parallel lists to print all data to the console
for index in range(0, len(firstName)): #len() --> length of collectionm returns number of items
    #index --> key of the list, allows access to ONE specific value
    print(f"INDEX {index:4} : {firstName[index]:10}  {lastName[index]:10}  {test1[index]:10}  {test2[index]:3} {test3[index]:3} {avg[index]:3.2f}")
    print("------------------------------------------------------------------------------------------------------------------------\n")

    #create a NEW list to hold each student's test score average

    avg = []

    #process the current student data to find and store each student's test score average to the avg list
    for i in range(0, len(test1)):

        a = (test1 + test2 + test3) / 3
        avg.append(a)
        #could also: avg.append((test[i] + test[i] + test3[i]) / 3)

        total_avg = 0

        for i in range(0, len(avg)):
            total_avg += avg[i] #adds each avg value to the total_avg variable
        
        #calculate the average
        class_avg = total_avg / len(avg)
        print(f"\nThe CLASS AVERAGE of these {len(avg)} students is: {class_avg:.2f}")
