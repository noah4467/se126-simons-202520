#W8D2 Dictionaries an dText File Data

#IMPORTS
import csv
#main

#review on dictionaries

library = {
    #indexes are strings set by the developer
    #'key' : value
    "1230" : "Red Rising", 
    "1231" : "The Little Prince"
    
}

with open("Text_File/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #add each records data as a new key + value pair from the text file
        #key --> rec[0] ;value --> rec[1]
        library.update({rec[0] : rec[1]})
        #when using update(), pass {'key' : value}

#disconnect from file
print(f"\n{'KEY':6}\t{'TITLE'}")
print("-" * 40)
for key in library:
    #for every key and value pair found within the library dictionary
    print(f"{key:6}\t{library[key]}")


#SEQUENTIAL SEARCH FOR TITLE

search = input("Enter the title you are looking for: ")
found = 0

for key in library:
    if search.lower() == library[key].lower():
        #store the found titles location in the dictionary -->
        found = key

if found != 0:
    print(f"We found your search for {search}, here is the info: ")
    print("-" * 50)
    '''
    for i in range(0, len(found)):
        print(f"{found[i].upper():4} : {library[found[i]]}")
    '''
    print(f"{found.upper():4} : {library[found]}")
    print("-" * 50)
else:
    print(f"We could not find your search for {search} :[ ")

#BINARY SEARCH FOR LIBRARY NUMBER DICTIONARY KEYS
#in order to binary search a set of keys you mut first

#type() returns the class type of the data passed to it
if type(library) is dict:
    print("Library is a DICTIONARY")