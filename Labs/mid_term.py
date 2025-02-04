#Noah Simons
#2/4/2025
#Mid-Term prompt #1
#Prompt:
#Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have
#been fully populated with file data, create a new list to hold an office number for each of the employees.
#Office numbers should start at 100 and not exceed 200. Assign each employee an office number and
#store to the newly created list, then process through the six lists to display all of the data to the user as
#well as the total number of records in the file

#Variables used:
#totalRec: the total number of records in the file
#fName: the first names listed in the file
#lName: the lasts names listed in the file
#email: the emails listed in the file
#dept: the departments of the employees listed in the file
#ext: the phone extensions of the employees listed in the file
#offNum: the random office number assigned to each employee 


#imports
import random
import csv
#defines empty variable
totalRec = 0
#defines lists as empty
fName = []
lName = []
email = []
dept = []
ext = []
offNum = []

#Header
print(f"{'FIRST':10}   {'LAST':12}  {'EMAIL':30}    {'DEPT':21} {'EXTENSION':8}    {'OFFICE NUMBER'}")
#Main Process
with open("Text_File/westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        totalRec = totalRec + 1
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        dept.append(rec[3])
        ext.append(rec[4])
    #assign each employee a random office number from 100-200
    for i in range(0, len(fName)):
        offNum.append(random.randint(100, 200))
    #prints all of the employee data
    for index in range(0, len(fName)):
        print(f"{fName[index]:10}  {lName[index]:12}  {email[index]:30}  {dept[index]:23}   {ext[index]:10} {offNum[index]}")
    #shows the total number of records
    print()
    print("Total records: ", totalRec)

    file = open("Text_File/midterm_choice1.csv", "w")
    #writes the data in a seperate file
    for i in range(0, len(fName)):
        file.write(f"{fName[i]}{','}{lName[i]}{','}{email[i]}{','}{dept[i]}{','}{ext[i]}{','}{offNum[i]}\n")
    
    print("1. Search by email")
    print("2. Search by department")
    print("3. Exit")
    #allows the user to search for a specific employee by their department or email

    #email search
    def searchEmail():

        found = -1

        emailSearch = input("Search email here:")
        for i in range(0, len(email)):
            if emailSearch.lower() == email[i].lower():
                found = i
            
        if found != -1:
            print(f"Your search for {emailSearch} was found!")
            print(f"{fName[found]:10}   {lName[found]:10}   {email[found]:13}   {ext[found]:10}    {offNum[found]}")
        else:
            print(f"Your search for {emailSearch} was not found.")
    #department search
    def searchDept():

        found = []

        deptSearch = input("Search by department here:")
        for i in range(0, len(dept)):
            if deptSearch.lower() == dept[i].lower():
                found.append(i)
        
        if not found:
            print(f"Your search for {deptSearch} was not found.")
        else:
            print(f"Your search for {deptSearch} was found!")
            for i in range(0, len(found)):
                print(f"{found[i]}: {fName[found[i]]:10}    {lName[found[i]]:10}   {email[found[i]]:13} {dept[found[i]]:10} {ext[found[i]]:10} {offNum[found[i]]}")
        
    
    
    #handles the search type provided by the user
    def search():
        searchType = input("What would you like to search by?")

        if (searchType == "1"):
            searchEmail()
        elif (searchType == "2"):
            searchDept()
        elif (searchType == "3"):
            print("Goodbye!")
        else:
            search()
        #loops the search process if the user has entered a valid search type and has requested another search
        if (searchType == "1" or searchType == "2"):
            anyMoreData = input("Would you like to search again? (y or n)").lower()
            if anyMoreData == "y":
                search()
            else:
                print("Goodbye!")
    #calls the above functions
    search()
    
        
    











    
