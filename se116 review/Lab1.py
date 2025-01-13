#Noah Simons
#Lab1
#1/7/2024
#Variables used:
#max_cap: the max capacity of people allowed in the room
#people: the number of people in the room
#dif: the difference between the max capacity and number of people
#response: the response from the user to the question of if they want to add another room

#Main process

def difference():
    max_cap = int(input("Enter the max capacity of the room"))
    people = int(input("Enter the number of people in the room"))
    dif = max_cap - people
    if (dif >= 0):
         print("This meeting meets fire safety requirements.")
         print("The room is ", dif, "people under capacity.") 
    else:
        print("This meeting does not meet fire safety requirements.")
        print("This room is ", dif * -1, "people over capacity.")

#Allows the user to enter another room.

def decision():
    response = str(input("Would you like to add another room?"))
    if (response == "y"):
        difference()
        decision()
    elif (response == "n"):
        print("Goodbye!")
    else:
        decision()

#Calls the above functions

difference()
decision()
