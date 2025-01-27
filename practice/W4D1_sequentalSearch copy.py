print("\n\nWelcome to the Student Search Program\n\n")
answer = input("Would you like to begin searching? (y or n)").lower()

while answer == "y":
    #get search type from user
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by LAST name")
    print("2. Search by LETTER GRADE")
    print("3. EXIT")

    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
       print("\tSEARCH BY LAST NAME") 

       found = -1 #invalid index number, will use to check later to see if a student has been found
       
        #get search item from user
       search_name = input("Enter the LAST NAME of the student you are searching for: ")

    #perform search
    for i in range(0 , len(lName))
    #display results
    if not found: #the list is empty
       print(f"Your search for {search_grade} was *NOT* found!")

    #build a way out of the loop
    if search_type == "1" or search_type == "2":
        answer = input("Would you like to search again? (y or n)").lower()