#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv


#---FUNCTIONS--------------------------------------------------

def swap(j,listName):
    temp = listName[j]
    listName[j] = listName[j + 1]
    listName[j + 1] = temp

#---MAIN EXECUTING CODE----------------------------------------

#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)                            #entire list
print(names_list[0])                         #first value   [INDEX]  
print(names_list[len(names_list) - 1])       #last value

#create an empty list for reach potential field - these must remain the same length
names = []
riders = []
nums = []
color1 = []
color2 = []


people_dictionary ={
    #"key" : value
    "fname" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age" : 12, #no key name duplicates
    "age" : 12.5,

}
#creation & population of dictionaries
people_dictionary ={
    #"key" : value
}
print(people_dictionary) #entire dictoinary
print(people_dictionary["fname"]) # replaces with value assigned to fname key )))

dragon_dict = {} #empty dictionary to be populated by the file

#gaining data from a text file 
with open("Text_File/dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #print() #we will replace this during demo

        #adding data to a list 

        names.append(rec[0])
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
            colorvar = rec[4]
        else:
            #still need to assign data for this dragon into color2 list so lists remain parallel.
            color2.append("---")
        #adding data to a dictionary
        dragon_dict.update({rec[0] : [rec[1], rec[2], rec[3], colorvar]})





#processing data from collections

print(f"{'NAMES':12} {'RIDERS':30} {'NUM':3} {'COLOR1':8} {'COLOR2'}")
for i in range(0, len(names)):
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")
print("-" * 50)
#searching & sorting
#BINARY SEARCH *requires* the sorting of data before searching
#we must also ensure the collection we search through is populated with unique values
#dictionary for key in diciontary
for key in dragon_dict:
    print(f"{dragon_dict[key]}") #this shows us the list data found at each key
    


#2D lists - lists of lists! 

#bubble sort
for i in range(len(names) - 1):
    for j in range(len(names) - 1):
        if names[j] > names[j + 1]:
            swap(j, names)
            swap(j, riders)
            swap(j, nums)
            swap(j, color1)
            swap(j, color2)

search = input("\nEnter the dragon name you wish to find: ")

min = 0
max = len(names) - 1
mid = int((min + max) / 2)

while min < max and search.lower() == names [mid].lower():
    print(min, max, mid, names[mid])
    if search.lower() < names[mid].lower():
        max = mid - 1
    else:
        min = mid + 1
    mid = int((min + max) / 2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record #{mid}, see info below:")
    print(f"{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]}\n")
else:
    print(f"\nNo results for {search}.\n")