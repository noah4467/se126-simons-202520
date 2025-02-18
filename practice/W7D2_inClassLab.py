#W7D - Live Class Review of Binary Search and bubble Sort + 2D Lists


def menu():
    print("Simple Searching Menu")
    print("1. Search by name")
    print("2. Search by num")
    print("3. Search by color")
    print("4. Exit")

    menu_choice = input("Enter your search type [1-4]")
    return menu_choice

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName [index + 1] = temp

import csv

#create your empt 1D parallel lists
names = []
nums = []
colors = []

valid_menu = ["1", "2", "3", "4"]

with open("Text_file/simple.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2].title())
#disconnect from file

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu:
        print("Invalid entry.")

    elif choice == "1":
        print("\n~Search by name~")
        min = 0
        max = len(names) - 1
        mid = int((min + max) / 2)

        search = input("Enter the NAME you are looking for: ")

        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                #search.lower() > names[mid].lower()
                min = mid + 1
            mid = int((min + max) / 2)

        if search.lower() == names[mid].lower():
            print(f"Your search for {search} is complete, see below details:")
            print(f"{'NAME':8}  {'NUM':3}   {'COLOR'}")
            print("---------------------------------------------------")
            print(f"{names[mid]:8}   {nums[mid]:3}    {colors[mid]}")
            print("---------------------------------------------------")
        else:
            print(f"No results for {search}.")
            
    elif choice == "2":
        print("\n~Search by num")

        for i in range(len(colors) - 1):
            for j in range(len(colors) - 1):
                #see if "larger" value is in front of "smaller"
                if colors[j] > colors[j + 1]:
                    #swap places! - not just THIS value but all associated values !
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)
        
        min = 0
        max = len(names) - 1
        mid = int((min + max) / 2)

        search = input("Enter the nam eyou are looking for.")

    elif choice == "3":
        print("\n~Search by color~")
    else:
        print("\n~EXIT~")
        ans = "X" #ans chanes from y to end the loop; condition will now eval as false
print("\nThank you for using my program.\n\tGOODBYE~\n")

dataFile = [
    names,
    nums,
    colors
]

'''with open("Text_File/simple.csv) as csvfile:
        file = csv.reader(csvfile)
        for rec in file:
            dataFile.append(rec)
'''

for i in range(0, len(dataFile)):
    #accessing each lists within the 2D list datafile
    print(f"INDEX {i} of 'DataFile':  {dataFile[i]}")
    for j in range(0, len(dataFile[i])):
        #accessing each value within the list currently looked at from outter for loop
        print(f"INDEX {i} and value DataFile[{j}]: {dataFile[i][j]}")