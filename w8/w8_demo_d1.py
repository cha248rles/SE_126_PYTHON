# W8 demo day 1 intor to dictionaries 

#Dictionaries in Python are a collection set similar to associative arrays in JavaScript but also look similar to JS object builds. Most importantly, they store data in key and value pairs. They keys are referred to as properties and the values can be any data type. 



#-----------------------imports--------------------------------------------------










#----------------------------Main code--------------------------------------------------



#----------------------------populated dictionary--------------------------------------------
myCar = {
    #'key' : value,
    "make" : "Ford",
    "model" : "C-max",
    "year" : 2016,
    "name" : "n/a",
    "color" : "tan",
    #keys cannot be repeated /NO Duplicates allowed 
}
#repeats will update the prior key 



#keys cannot be repeated within a dictionary, but they can be reused across unique dictionarys
yourCar = {
    #'key' : value,
    "make" : "GMC",
    "model" : "CANYON",
    "year" : 2019,
    "name" : "Jolly",
    "color" : "black",
}




#display entire dictonary -> 'myCar

print(myCar)
#display just the make and model values of the dictonary 'myCar'

#"keyName" will always be a string index, created by a developer 

print(f"My car is a {myCar["make"]} {myCar["model"]}")

print(f"Rob's car is a {yourCar["make"]} {yourCar["model"]}")

for key in myCar:
    print(f"{key.upper()} : {myCar[key]}")
    