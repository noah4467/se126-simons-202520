#Noah Simons
#2/21/2025
#Lab 5
#Intermediate Prog. Using Python
#Variables used:
#libNum: the library number attached to the book
#title: the title attached to the book
#author: the author of the book
#genre: the genre category listed as
#pageCount: the number of pages in the book
#status:the status of the book, on loan or available

#imports
import csv

#lists
libNum = []
title = []
author = []
genre = []
pageCount = []
status = []
#appends the csv data to the lists
with open("Text_File/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        libNum.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pageCount.append(rec[4])
        status.append(rec[5])
#prints the different search options
print("1. Show all titles")
print("2. Search by title")
print("3. Search by author")
print("4. Search by genre")
print("5. Search by library number")
print("6. Show all available")
print("7. Show all on loan")
print("8. Exit")
print()

#functions for different search types
#search by title function
def searchTitle():
    
    found = []

    searchedTitle = input("Enter a title to search for: ")
    for i in range(0, len(title)):
        if searchedTitle.lower() == title[i].lower():
            found.append(i)
        elif searchedTitle.lower() in title:
            found.append(i)
    if not found:
        print(f"No results for '{searchedTitle}'")
    else:
        print(f"Showing results for {searchedTitle}")
        for i in range(0, len(found)):
            print(f"{title[found[i]]:40}  {libNum[found[i]]:5}  {author[found[i]]:15} {genre[found[i]]:20}  {pageCount[found[i]]:12}   {status[found[i]]}")
#search by author function
def searchAuth():

    found = []

    searchedAuth = input("Enter an author to search for: ")

    for i in range(0, len(author)):
        if searchedAuth.lower() == author[i].lower():
            found.append(i)
    if not found:
        print(f"No results for {searchedAuth}")
    else:
        print(f"Showing results for {searchedAuth}")
        for i in range(0, len(found)):
            print(f"{title[found[i]]:40}  {libNum[found[i]]:5}  {author[found[i]]:15} {genre[found[i]]:20}  {pageCount[found[i]]:12}   {status[found[i]]}")
#Search by genre function
def searchGenre():

    found = []

    genreSearch = input("Enter a genre to search for: ")

    for i in range(0, len(genre)):
        if genreSearch.lower() == genre[i].lower():
            found.append(i)
    if not found:
        print(f"No results for {genreSearch}")
    else:
        print(f"Showing results for {genreSearch}")
        for i in range(0, len(found)):
            print(f"{title[found[i]]:40}  {libNum[found[i]]:5}  {author[found[i]]:15} {genre[found[i]]:20}  {pageCount[found[i]]:12}   {status[found[i]]}")
#search by number function
def searchNum():
    found = []

    numSearch = input("Enter a number to search for: ")

    for i in range(0, len(genre)):
        if numSearch.lower() == libNum[i].lower():
            found.append(i)
    if not found:
        print(f"No results for {numSearch}")
    else:
        print(f"Showing results for {numSearch}")
        for i in range(0, len(found)):
            print(f"{title[found[i]]:40}  {libNum[found[i]]:5}  {author[found[i]]:15} {genre[found[i]]:20}  {pageCount[found[i]]:12}   {status[found[i]]}")
#display available books
def available():
    found = []

    for i in range(0, len(status)):
        if status[i] == "available":
            found.append(i)
    for i in range(0, len(found)):
        print(f"{title[found[i]]:40}  {libNum[found[i]]:5}  {author[found[i]]:15} {genre[found[i]]:20}  {pageCount[found[i]]:12}   {status[found[i]]}")
#display on loan books
def onLoan():
    found = []

    for i in range(0, len(status)):
        if status[i] == "on loan":
            found.append(i)
    for i in range(0, len(found)):
        print(f"{title[found[i]]:40}  {libNum[found[i]]:5}  {author[found[i]]:15} {genre[found[i]]:20}  {pageCount[found[i]]:12}   {status[found[i]]}")
        




#search type user choice sequence
def search():

    searchType = input("What would you like to search by?")

    if searchType not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid entry.")
        search()
    elif searchType == "1":
        print(f"{'TITLE':40}    {'LIB#':5}  {'AUTHOR':15}   {'GENRE':20}    {'PAGES':12} {'STATUS'}")
        for i in range(0, len(title)):
            print(f"{title[i]:40}    {libNum[i]:5}  {author[i]:15}   {genre[i]:20}    {pageCount[i]:12} {status[i]}")
    elif searchType == "2":
        searchTitle()
        search()
    elif searchType == "3":
        searchAuth()
        search()
    elif searchType == "4":
        searchGenre()
        search()
    elif searchType == "5":
        searchNum()
        search()
    elif searchType == "6":
        available()
        search()
    elif searchType == "7":
        onLoan()
        search()
    elif searchType == "8":
        print("Goodbye!")
#calls the search function
search()

