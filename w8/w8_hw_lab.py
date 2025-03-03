#Charles O'Connell
#SE126.02
#w8 Homework lab 
#2/28/2025

#prompt: A dictionary program that works with programming terms and definitions.

#var library
#ans is used for while loop control
#user_choice is the users choice for the menu option
#user_key is the users input term
#user_definition is the user inputed definition 
#found is used for searching






#imports
from os import system,name

import csv







#functions

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




#main code

clear()


#initializations
ans = "y"
#dictionary
dictionary = {

}

#getting data from csv file 
with open("w8/words.csv") as csvfile:

    file =csv.reader(csvfile)

    for record in file:
        dictionary.update({record[0] : record[1]})









# main loop
while ans == "y":

    print("Here is the menu")
    print("1.Show all words")
    print("2.Search for a word")
    print("3.Add a word")
    print("4.Exit")

    user_choice = input("Please enter your choice")

    if user_choice == "1":

        print(f"{'term':15}\t{'Definition'}")

        for key in dictionary:

            print(f"{key:15}\t{dictionary[key]}")

    elif user_choice == "2":

        search = input("Enter the term you are looking for:")

        found = 0


        for key in dictionary:
            if search.lower() == key.lower():
            #store the found title's location in the dictionary 
                found = key

        if found != 0:

            print(f"\nTerm: {found:15}\t Definition: {dictionary[found]}")

        else:
            print(f"Your search for {search} came up empty :[")

    elif user_choice == "3":
        user_key = input("Please enter the term you would like to enter:")
        user_definition = input("Please enter the definition of the term:")
        dictionary.update({user_key : user_definition}) 
    
    elif user_choice == "4":
        
        print("EXITING PROGRAM...")
        ans = "n"
    
    else:
        print("***INVALID ENTRY***")


print("Have a good day")








    
    










