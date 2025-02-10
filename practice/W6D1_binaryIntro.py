#W6D! - Seatrching Algorithms: Binary vs Sequential Search

import csv
library_nums = [] #THE ONLY ORDERED FIELD
titles = []
authors = []
genres = []
pages = []

with open("Text_File/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        library_nums.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{'LIB#':5} {'TITLE':25}  {'AUTHOR':15} {'GENRE':20}  {'PAGES':5}")
print("---------------------------------------------------------------------------------------------")
for i in range(0, len(library_nums)):
    print(f"{library_nums[i]:5} {titles[i]:25}  {authors[i]:15} {genres[i]:20}  {pages[i]:5}")
print("-----------------------------------------------------------------------------------------")

#SEQUENTIAL SEARCH: allow a user to search for a specific title
#titles[] is NOT ordered

found = []
search_num = input("Which title are you looking for?")
seq_count = 0

for i in range(0, len(library_nums)):
    seq_count += 1
    if search_num.lower() in library_nums[i]:
        found.append(i)

if not found:
    print(f"Sorry, you search for {search_num} was not found")
else:
    print(f"Your search for {search_num} was found!")

    print(f"{'LIB#':5} {'TITLE':25}  {'AUTHOR':15} {'GENRE':20}  {'PAGES':5}")
    print("--------------------------------------------------------------------------------------------")

    for i in range(0, len(found)):
        print(f"{library_nums[found[i]]:5} {titles[found[i]]:25}  {authors[found[i]]:15} {genres[found[i]]:20}  {pages[found[i]]:5}")
    print("---------------------------------------------------------------------------------------------")


    #BINARY SEARCH

min = 0
max = len(library_nums) - 1
mid = int((min + max) / 2)

bin_count = 0

while min < max and search_num != library_nums[mid]:

    if search_num < library_nums[mid]:
            #everything after mid point is not possible
        max = mid - 1
    else:
            #everything before mid point is not possible
        min = mid + 1
        
    mid = int((min + max) / 2)
    bin_count += 1

print(f"BINARY SEARCH ITERATIONS: {bin_count}")

if search_num == library_nums[mid]:
    print(f"Your search for {search_num} was found")
    print(f"{'LIB#':5} {'TITLE':25}  {'AUTHOR':15} {'GENRE':20}  {'PAGES':5}")
    print("----------------------------------------------------")
    print(f"{library_nums[mid]:5} {titles[mid]:25}  {authors[mid]:15} {genres[mid]:20}  {pages[mid]:5}")
else:
    print(f"No results for {search_num}")