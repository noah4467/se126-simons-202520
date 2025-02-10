#W2D2 - Text file Handling Review w/ filters

#PROGRAM PROMPT:


#Variable dictionary:
#diff: the difference between the max capacity and number of people
#total_rec: the total number of records
#rooms_over: the number of rooms that are over capacity
#file: the csv file that is being referenced
#name: the first record in the text file;
#max: the second record in the text file
#ppl: the third record in the text file
#remaining: the number of people remaining before the room is full

import csv


def difference(people, max_cap):
    '''this function is passed 2 values and returns the difference between them.'''
    diff = max_cap - people
    return diff

#main


#initialize needed counting variables
total_rec = 0
rooms_over = 0
print(f"{'NAME':20}    {'MAX':5}   {'PPL':5}   {'OVER'}") #FIELD HEADERS FOR DISPLAY
print("----------------------------------------------------")
#connect to file
with open("Text_File/classLab2.csv") as csvfile:
    #indent one level while connected to the file

    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) in the file (text file)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1]) #all text data read as a string, so cast as a num
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display rooms that are over capacity (remaing is negative)
        if remaining < 0 :
            rooms_over += 1
            print(f"{name:20}  {max:5}   {ppl:5}   {abs(remaining):5}")

        total_rec += 1


#connect to file
#display final data
print(f"\nRooms currently OVER CAPACITY: {rooms_over}")
print(f"Total rooms in file: {total_rec}\n\n")