#W8D1 - intro to dictionaries

#Dictionaries in Python are a collection set similar to associative arrays in Javascript but 
# also look similar to JS object builds. Most importantly, they store data in key and value pairs. 
# the keys are referred to as properties and the values can be any data type.

#IMPORTS

#MAIN EXECUTING CODE

#start by creating a opulated dictionary
myCar = {
    #'key' : value,
    "make":"Ford",
    "model": "SE Hatchback",
    "year": 2014,
    "name": "Gwendoline",
    "color": "black",
    #keys cannot be repeated/NO DUPLICATES allowed
    #repeats will replace first value, see 'color' key below in print
    "color": "red"

}

#display the entire dictionary -> 'myCar'
print(myCar)
#displays just the 'make' and 'model' values of the dictionary 'myCar'
print(f"My car is a {myCar["make"]} {myCar["model"]}")

#dictionaryName["keyName"] --> accesses stored value
#"keyName" will always be a STRING index, created by developer

yourCar = {
    #'key' : value,
    "make":"GMC",
    "model": "Canyon",
    "year": 2014,
    "name": "Jolly",
    "color": "black",
}



print(f"Rob's car is a {yourCar["make"]} {yourCar["model"]}")



for key in yourCar:
    print(f"{key.upper()} : {yourCar[key]}")

#processing through a dictoinary and its keys
#add a key and value to a pre existing dictionary
yourCar["plate"] = "12345"