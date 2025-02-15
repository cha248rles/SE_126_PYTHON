#Charles O'Connell
#SE126.02
#w6 Homework lab 
#2/11/2025

#prompt: A library catalog program that shows the availability of books as well as information about them that you can search by.



#var library 






#imports
import csv

from os import system,name






#functions 

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




def swap(i,listName):
    temp = listName[i]

    listName[i] = listName[i + 1]

    listName[i+1] = temp



#-------------------------Main code-----------------------------------


#Initalizing lists and vars 
clear()

library_num =[]

title = []

author = []

genre = []

page_count = []

availability = []


ans = "y"

#opening csv file and appending necessary data 

with open("w6/book_list.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:

        library_num.append(record[0])

        title.append(record[1])

        author.append(record[2])

        genre.append(record[3])

        page_count.append(record[4])

        availability.append(record[5])

#displays the entire data to user one time 
print("This is the program to look at items in a book csv file and search the csv file.")
print("----------------------------------------------------------------------------------------------------------------------")

print (f"{'LIB#':5}  {'Title':35} {'Author':15} {'Genre':20} {'Page Count':5} {'Availability':5}")

for i in range(0,len(genre)):
    print(f"{library_num[i]:5}  {title[i]:35} {author[i]:15} {genre[i]:20} {page_count[i]:5} {availability[i]:5}")
print("----------------------------------------------------------------------------------------------------------------------")

#Menu driven part of program put the csv display out of while loop
while ans == "y":
    
    
    print("\tSEARCHING MENU")
    print("1. Display all titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show all Available")
    print("7. Show all on loan")
    print("8. Exit")
    
    user_menu_choice = input("Please enter which menu choice you would like.")
    
    if user_menu_choice == "1":
        print("\nShowing all titles Alphabetically")
        #BUBBLE SORT----------------------------------------

        for i in range(0, len(title) - 1):#outer loop

            

            for index in range(0, len(title) - 1):#inner loop

                

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(title[index] > title[index + 1]):


                    #if above is true, swap places!

                    swap(index,title)

                    #swap all other values

                    swap(index,library_num)
                    swap(index,author)
                    swap(index,genre)
                    swap(index,page_count)
                    swap(index,availability)

        for i in range(0,len(genre)):
            print(f"{library_num[i]:5}  {title[i]:35} {author[i]:15} {genre[i]:20} {page_count[i]:5} {availability[i]:5}")
        print("--------------------------------------------------------")
        

    elif user_menu_choice == "2":
        print("\nWelcome to search by title")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "3":
        print("\nWelcome to search by author")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "4":
        print("\nWelcome to search by genre")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "5":
        print ("\nWelcome to search by library number")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "6":
        print("\nShowing all available")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "7":
        print("\nShowing all on loan.")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "8":
        print("\nExiting Program...")
        
        ans = "n"
    else:
        print("--------------------------------------------------------")
        print("*******************INVALID ENTRY*************************")
        ans = "y"

print("Goodbye have a good day.")












