#W4D2 Sequential Search Revview + Creating & Writing to Text Files

#IMPORTS
import csv
#FUNCTIONS

#MAIN EXECUTING CODE

#create empty list one for each field
dragons = []
riders = []
count = []
color1 = []
color2 = []

with open("Text_File/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])

        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        elif rec[2] == "1":
            color2.append("---")
        else:
            color2.append("ERROR")
            
#disconnected from file

#process the lists to display data to the console
print(f"{'DRAGONS':15}  {'RIDERS':30}  {'#':3}  {'COLOR1':8}  {'COLOR2'}")
print("------------------------------------------------------------------------")

for i in range(0, len(dragons)):
    print(f"{dragons[i]:15}  {riders[i]:30}  {count[i]:3}  {color1[i]:8}  {color2[i]}")

#SEARCH FOR A SPECIFIC DRAGON
found = "x"
search = input("Which dragon are you looking for:")

for i in range(0, len(dragons)):
    if search.lower() == dragons[i].lower():
        #hold onto the found location of our searched for calue
        found = i
#filter and display results
if found != "x": #search was found!
    print(f"Your search for {search} was FOUND:")
    print(f"{dragons[found]:15}  {riders[found]:30}  {count[found]:3}  {color1[found]:8}  {color2[found]}")
    
else:
    print(f"Your search for {search} was NOT found:")


#SEARCH FOR COLOR SET
found = []
search = input("Enter the dragon color you are looking for: ")

for i in range(0, len(color1)):

    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

if not found: #if the found list is empty*
    print(f"your search for {search} could not be found")
else:
    print(f"your search for {search} was found")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15}  {riders[found[i]:30]}   {count[found[i]]:3} {color1[found[i]]:8}    {color2[found[i]]:8}")

#WRITE DATA TO NEW FILE

file = open('Text File/test3.csv', 'w')
for i in range(0, len(dragons)):
    file.write(f"{dragons[i]},{riders[i]}\n")

file.close()