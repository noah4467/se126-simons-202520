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

with open("Text_File/class_grades.csv") as csvfile:
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




#---------------------------------------------------------------------------------------------------------------------------------------------------------





print("\n\nWelcome to the Student Search Program\n\n")
answer = input("Would you like to begin searching? (y or n)").lower()

while answer == "y":
    #get search type from user
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")

    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
       print("\tSEARCH BY LAST NAME") 

       found = -1 #invalid index number, will use to check later to see if a student has been found
       
        #get search item from user
       search_last = input("Enter the LAST NAME of the student you are searching for: ")

    #perform search
       for i in range(0, len(lName)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_last.lower() == lName[i].lower(): 
                #if performs the search
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user
       if found != -1:
            #last name FOUND!
            print(f"Your search for {search_last} was FOUND! Here is their data: ")
            print(f"{fName[found]:10}  {lName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3}  {num_avg[found]:6.1f}  {let_avg[found]}")
       else: 
            #NOT found
            print(f"Your search for {search_last} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
    
    elif search_type == "2": #LETTER GRADE
        print("\tLETTER GRADE SEARCH")

        #sequential search - search for a collection of students based on their Letter Grade Average
        found = []
        search_let= input("Enter the LETTER GRADE you wish to find: ")

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(let_avg)):
            #for loop performs the sequence

            if search_let.upper() == let_avg[i]: 
                #if performs the SEARCH -
                found.append(i)
                print(f"Found a {search_let} grade in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found:
            #NOT found
            print(f"Your search for {search_let} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #last name FOUND
            print(f"Your search for {search_let} was FOUND! Here is their data: ")

            #found is a list populated with index locations
            for i in range(0, len(found)):
                print(f"{found[i]}:  {fName[found[i]]:10}  {lName[found[i]]:10}  {test1[found[i]]:3}  {test2[found[i]]:3}  {test3[found[i]]:3}  {num_avg[found[i]]:6.1f}  {let_avg[found[i]]}")
    elif search_type == "3": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change valu
    if search_type == "1" or search_type == "2":
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")