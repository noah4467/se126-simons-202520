#Lab 7
#Noah Simons
#3/3/2025
#variables used:
#library: dictionary of the words.csv file
#search: the word that the user searches for
#found: the results found from the search
#wordInput: the added word to the file by the user
#defInput: the definition inputted by the user
#actionType: the type of action inputted by the user, 1, 2, 3
#anyMoreData: asks the user if they would like to perform another action

#imports
import csv
#defines library as an empty dictionary
library = {}
#Title
print("My Programming Dictionary Menu")
#appends csv data to library dictionary
with open("Text_File/words.csv") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        library.update({rec[0] : rec[1]})
#prints the data the first time without command
print(f"\n{'WORD':8}\t{'DEFINITION'}")
for key in library:
    print(f"{key:8}\t{library[key]}")
#input info
print("1. Display word list")
print("2. Search for a word")
print("3. Add a word")
print("3. Exit")

#the function to search for a word
def wordSearch():
    search = input("Enter a word to search for: ").lower()
    found = 0
    for key in library:
        if search.lower() == key.lower():
            found = key
    if found != 0:
        print(f"{found.upper():8} : {library[found]}")
    else:
        print(f"No results for {search}")
#the function to add a word
def addWord():
    wordInput = input("Enter a word to add: ").lower()
    defInput = input("Enter word definition: ").lower()
    file = open("Text_File/words.csv", "a")
    file.write(f"\n{wordInput}{','}{defInput}")
#the function to display the dictionary data
def display():
    print(f"{'WORD'}\t{'DEFINITION'}")
    for key in library:
        print(f"{key:8}\t{library[key]}")

#function to perform each of the above functions
def perfAction():
    actionType = input("Which action would you like to perform?")

    if actionType != "4":
        if actionType == "1":
            display()
        elif actionType == "2":
            wordSearch()
        elif actionType == "3":
            addWord()
        else:
            print("Action not recognized.")
            perfAction()
        
    else:
        print("Goodbye!")



#function that asks the user if they want to perform another action
def anyMore():
    anyMoreData = input("Perform another action? (y or n) ").lower()

    if anyMoreData == "y":
        perfAction()
        anyMore()
    else:
        print("Goodbye!")
#asks the user which action type to perform (1,2,3)
actionType = input("Which action would you like to perform?")

if actionType != "4":
    if actionType == "1":
        display()
    elif actionType == "2":
        wordSearch()
    elif actionType == "3":
        addWord()
    else:
        print("Action not recognized.")
        perfAction()
        
else:
    print("Goodbye!")

anyMore()