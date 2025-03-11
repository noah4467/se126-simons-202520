#Noah Simons
#Final Project
#3/10/2025
#variables used:
#atomicNum: list that appends the atomic number of each element
#name:: list that appends the elements names
#abbrev: list that appends the elements abbrevations
#category: list that appends the category of each list
#mass: list that appends the atomic mass of each element
#nameSearch: the element name that the user searches for
#abbrSearch: the element abbrevation that the user searches for
#searchCat: the element category that the user searches for
#searchType: the type of search that the user requests
#anyMoreData: Whether the user wants to enter another search or not

#imports
import csv
#empty lists
atomicNum = []
name = []
abbrev = []
category = []
mass = []
#connect to csv file elements.csv
with open("Text_File/elements.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        atomicNum.append(rec[0])
        name.append(rec[1])
        abbrev.append(rec[2])
        category.append(rec[3])
        mass.append(rec[4])
#disconnect from file

#displays all of the elements
def display():
    print(f"{'ATOMIC NUM':10} {'ELEMENT':17} {'ABBR.':6} {'CATEGORY':23} {'MASS'}")
    for i in range(0, len(atomicNum)):
        print(f"{atomicNum[i]:10} {name[i]:17} {abbrev[i]:6} {category[i]:23} {mass[i]}")

#function that searches for an element by its name
def searchName():

    found = -1

    nameSearch = input("Enter element to search for: ")
    for i in range(0, len(name)):
        if nameSearch.lower() == name[i].lower():
            found = i
    if found != -1:
        print(f"Displaying results for {nameSearch}.")
        print()
        print(f"{'ATOMIC #':10} {'ELEMENT':17} {'ABBR.':6} {'CATEGORY':23} {'MASS'}")
        print(f"{atomicNum[found]:10} {name[found]:17} {abbrev[found]:6} {category[found]:23} {mass[found]}")
    else:
        print(f"No results for {nameSearch}.")

#function that searches for an element by its abbrevation
def searchAbbr():

    found = -1

    abbrSearch = input("Enter element abbrevation to search for: ")
    for i in range(0, len(abbrev)):
        if abbrSearch.lower() == abbrev[i].lower():
            found = i
    if found != -1:
        print(f"Displaying results for {abbrSearch}.")
        print()
        print(f"{'ATOMIC #':10} {'ELEMENT':17} {'ABBR.':6} {'CATEGORY':23} {'MASS'}")
        print(f"{atomicNum[found]:10} {name[found]:17} {abbrev[found]:6} {category[found]:23} {mass[found]}")
    else:
        print(f"No results for {abbrSearch}.")

# function that searches for element category
def searchCat():

    found = []

    catSearch = input("Enter a category or category keyword to search for: ")
    for i in range(0, len(category)):
        if catSearch.lower() in category[i].lower():
            found.append(i)
        
    if not found:
        print(f"No results for {catSearch}")
    else:
        print(f"Displaying results for {catSearch}")
        print()
        print(f"{'ATOMIC #':10} {'ELEMENT':17} {'ABBR.':6} {'CATEGORY':23} {'MASS'}")
        for i in range(0, len(found)):
            print(f"{atomicNum[found[i]]:10} {name[found[i]]:17} {abbrev[found[i]]:6} {category[found[i]]:23} {mass[found[i]]}")


#prompts the user for a search type and executes each search type
def search():
    display()
    print()
    print("1. Search an element by name")
    print("2. Search an element by abbrevation")
    print("3. Search for a category")
    print("4. Exit")
    print()
    #asks the user if they want to search by name, abbrevation, or category
    searchType = input("What would you like to search by?")

    if searchType == "1":
        searchName()
    elif searchType == "2":
        searchAbbr()
    elif searchType  == "3":
        searchCat()
    elif searchType == "4":
        print("Goodbye!")
    else:
        print("Invalid search type")
        search()
    #asks the user if they would like to search again and repeats the process if the answer is yes.
    if searchType == "1" or searchType == "2" or searchType == "3":
        anyMoreData = input("Would you like to search again? (y or n)").lower()
        if anyMoreData == "y":
            search()
        else:
            print("Goodbye!")



#calls the above functions
search()