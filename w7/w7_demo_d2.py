#Charles O'Connell
#SE126.02
#w7 demo d2 lab 
#2/18/2025

#prompt: bubble search and binary search review

#var library







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



def menu():
    print("Simple Search Menu")
    print("1. Search by Name")
    print("2. Search by NUM")
    print("3. Search by Color")
    print("4. Exit")

    menu_choice = input("Enter your search type [1-4]: ")

    return menu_choice

def swap(index,listName):
    temp = listName[index]
    listName[index] = listName[index+1]
    listName[index+1]= temp


clear()

names = []

nums = []

colors = []

valid_menu = ["1","2","3","4"]

with open("w7/simple-2.csv") as csvfile:


    file =csv.reader(csvfile)

    for rec in file:

        names.append(rec[0])

        nums.append(rec[1])

        colors.append(rec[2])



ans = "y"

while ans == "y":

    choice = menu()

    if choice not in valid_menu:
        print("********!INVALID ENTRY**********")


    elif choice == "1":
        print("search by name")
        #bubble sort
        for i in range(len(names)-1):
            for j in range(len(names)-1):
                #see if "larger" val is in front of "smaller"
                if colors[j] > colors[j+1]:
                    #swap places not just this val but all associated values 
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums) 
 
        min = 0         #first index value

        max = len(names) -1 # Last index 

        mid = int((min+max) /2)

        search_name = input("Enter the name you are looking for: ")

        while min < max and search_name.lower() != names[mid].lower():

            if search_name.lower() < names[mid].lower():
                max = mid - 1
            else:
                min = mid +1

            mid = int((min+max) /2)

            if search_name.lower() == names[mid].lower():
                print(f"Your search for {search_name} was found")
                print(f"{'Name':8}   {'Num':3}  {'Color'}")
                print("---------------------------------------------------------")
                print(f"{names[mid]:8}   {nums[mid]:3}  {colors[mid]}")
                print("---------------------------------------------------------")

            else:
                print(f"Your search for {search_name} was not found")


    elif choice == "2":
        print("search by numbers")
        


    elif choice == "3":
        print("search by color")

        #bubble sort
        for i in range(len(colors)-1):
            for j in range(len(colors)-1):
                #see if "larger" val is in front of "smaller"
                if colors[j] > colors[j+1]:
                    #swap places not just this val but all associated values 
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums) 
            min = 0         #first index value

        max = len(names) -1 # Last index 

        mid = int((min+max) /2)

        search_name = input("Enter the color you are looking for: ")

        while min < max and search_name.lower() != colors[mid].lower():

            if search_name.lower() < colors[mid].lower():
                max = mid - 1
            else:
                min = mid +1

            mid = int((min+max) /2)

            if search_name.lower() == colors[mid].lower():
                print(f"Your search for {search_name} was found")
                print(f"{'Name':8}   {'Num':3}  {'Color'}")
                print("---------------------------------------------------------")
                print(f"{names[mid]:8}   {nums[mid]:3}  {colors[mid]}")
                print("---------------------------------------------------------")

            else:
                print(f"Your search for {search_name} was not found")

        




    else:
        print("EXITING...")
        ans = "n"


print("Thank you for using my program. Goodbye.")





#2d lists
dataFile = [
    names, 
    nums, 
    colors
]


for i in range(0,len(dataFile)):
    print(f"Index {i} of 'DataFile' : {dataFile[i]}")

    
    for j in range(0, len(dataFile[i])):
        print(f"Index {i} and value DataFile [{j}]: {dataFile[i][j]}")
