#Charles O'Connell
#SE126.02
#w6 Homework lab 
#2/11/2025

#prompt: A library catalog program that shows the availability of books as well as information about them that you can search by.



#var library 
#ans is used for while loop
#csv ----------------------------
#library_num is for library numbers
#title is used for title 
#author is used for authors 
#genre is used for genres
#page_count is used for the page count
#availability is used for on loan vs available 
#----------------------------------------------
#found_ is used to store found data depending on the type of search depending on what comes after the underscore
#user_ is used to get user input depending on the type of search depending on what comes after the underscore





#imports
import csv

from os import system,name #for clear screen func






#functions 

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



#for bubble 
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
    #gives menu to user
    
    print("\tSEARCHING MENU")
    print("1. Display all titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show all Available")
    print("7. Show all on loan")
    print("8. Exit")
    
    user_menu_choice = input("Please enter which menu choice you would like.") #gets user input
    
    #all the options for the menu used the bubble algorithem from the demo 
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
        
        found_title = []
        user_title =input("Please type in the name of the title you are looking for:")
        
        for i in range (0,len(title)):
            if user_title.lower() == title[i].lower():
                found_title.append(i)
                print(f"Found {user_title} department in INDEX {i}")
        
        if not found_title:
            print (f"Your search for {user_title} was not found.")
            
        else:
            print(f"Your search for {user_title} was found")
            for i in range(0, len(found_title)):
                
                print(f"{library_num[found_title[i]]:5}  {title[found_title[i]]:35} {author[found_title[i]]:15} {genre[found_title[i]]:20} {page_count[found_title[i]]:5} {availability[found_title[i]]:5}")
                


    elif user_menu_choice == "3":
        print("\nWelcome to search by author")
        print("--------------------------------------------------------")
        
        
        found_author = []
        user_author =input("Please type in the name of the author you are looking for:")
        
        
        for i in range (0,len(author)):
            if user_author.lower() == author[i].lower():
                found_author.append(i)
                print(f"Found {user_author} department in INDEX {i}")
        
        if not found_author:
            print (f"Your search for {user_author} was not found.")
            
        else:
            print(f"Your search for {user_author} was found")
            for i in range(0, len(found_author)):
                
                print(f"{library_num[found_author[i]]:5}  {title[found_author[i]]:35} {author[found_author[i]]:15} {genre[found_author[i]]:20} {page_count[found_author[i]]:5} {availability[found_author[i]]:5}")


    elif user_menu_choice == "4":
        print("\nWelcome to search by genre")
        print("--------------------------------------------------------")
        
        found_genre = []
        user_genre =input("Please type in the name of the genre you are looking for:")

        for i in range (0,len(genre)):
            if user_genre.lower() == genre[i].lower():
                found_genre.append(i)
                print(f"Found {user_genre} department in INDEX {i}")
        
        if not found_genre:
            print (f"Your search for {user_genre} was not found.")
            
        else:
            print(f"Your search for {user_genre} was found")
            for i in range(0, len(found_genre)):
                
                print(f"{library_num[found_genre[i]]:5}  {title[found_genre[i]]:35} {author[found_genre[i]]:15} {genre[found_genre[i]]:20} {page_count[found_genre[i]]:5} {availability[found_genre[i]]:5}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





    elif user_menu_choice == "5":
        print ("\nWelcome to search by library number")
        print("--------------------------------------------------------")
        
        found_lib_num = []
        user_lib_num =input("Please type in the name of the library number you are looking for:")
        
        for i in range (0,len(library_num)):
            if user_lib_num.lower() == library_num[i].lower():
                found_lib_num.append(i)
                print(f"Found {user_lib_num} department in INDEX {i}")
        
        if not found_lib_num:
            print (f"Your search for {user_lib_num} was not found.")
            
        else:
            print(f"Your search for {user_lib_num} was found")
            for i in range(0, len(found_lib_num)):
                
                print(f"{library_num[found_lib_num[i]]:5}  {title[found_lib_num[i]]:35} {author[found_lib_num[i]]:15} {genre[found_lib_num[i]]:20} {page_count[found_lib_num[i]]:5} {availability[found_lib_num[i]]:5}")
        
        
    elif user_menu_choice == "6":
        print("\nShowing all available")
        print("--------------------------------------------------------")
        for i in range(0,len(availability)):
            if availability[i] == "available":
                print(f"{library_num[i]:5}  {title[i]:35} {author[i]:15} {genre[i]:20} {page_count[i]:5} {availability[i]:5}")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "7":
        print("\nShowing all on loan.")
        print("--------------------------------------------------------")
        for i in range(0,len(availability)):
            if availability[i] == "on loan":
                print(f"{library_num[i]:5}  {title[i]:35} {author[i]:15} {genre[i]:20} {page_count[i]:5} {availability[i]:5}")
        print("--------------------------------------------------------")
        
    elif user_menu_choice == "8":
        print("\nExiting Program...")
        
        ans = "n"
    else:
        print("--------------------------------------------------------")
        print("*******************INVALID ENTRY*************************")
        ans = "y"

print("Goodbye have a good day.")












