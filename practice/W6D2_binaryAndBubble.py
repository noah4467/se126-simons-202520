#W6D2 Binary search + bubble sort

#this file uses:party.csv

#PROGRAM PROMPT: BUILD A REPEATABLE, menu driven program to access and search for data within the file.

#IMPORTS
import csv

#Functions
def display(x, foundList, records):
    '''
    PARAMETERS
    x   signifier for if we are printing a single record or multiple
    when x = "x" it is an index and we have one value, otherwise we have multiple

    records     the length of a list we are going to process through (# of  loops/prints)
    '''
    print(f"{'CLASS':8} {'NAME':10} {'MEANING':20}  {'CULTURE'}")
    print("---------------------------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{class_type[x]:8}   {name[x]:10}    {meaning[x]:20} {culture[x]}")

    elif foundList:

        for i in range(0, records):
            print(f"{class_type[foundList[i]]:8}   {name[foundList[i]]:10}    {meaning[foundList[i]]:20} {culture[foundList[i]]}")
    else:
        for i in range(0, records):
            print(f"{class_type[i]:8}   {name[i]:10}    {meaning[i]:20} {culture[i]}")
    print("------------------------------------------------------------------------------")


#main process


class_type = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

with open("Text_File/party.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#Disconnect from file

#display whole
display("x",0,len(class_type)) #practice with function

ans = input("Would you like to enter the search program? [y/n]").lower()

while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]").lower()

#main searching loop
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by TYPE")
    print("2. Search by NAME") #binary search review
    print("3. Search by MEANING")
    print("4. EXIT")

    search_type = input("\nHow would you like to search today? [1-4]: ")

    #using not in for user validity checks
    if search_type not in ["1", "2", "3", "4"]:
        print("INVALID ENTRY***\nPlease try again")
    elif search_type == "1":
        print(f"You have chosen to search by TYPE")

        search = input("Which type: 'dragon or 'elf':").lower()

        if search not in ["dragon", "elf"]:
            #could also be if search.title() not in class_type
            print("INVALID ENTRY\nPlease try again")
        else:
            found = []
            for i in range(0, len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)
                
            if not found:
                print(f"Sorry, your search could not be completed.")
            else:
                print(f"Your search for {search} is complete! Details below:")
                display("x", found, len(found))

    print(f"You have chosen Menu Option #{search_type}")

    if search_type == 
