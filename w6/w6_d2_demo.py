#Charles O'Connell
#SE126.02
#w6 d2 demo lab 
#2/11/2025

#prompt: BINARY SEARCH AND BUBBLE 

#Build a repetable, menu driven program  




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




def display(x, foundList, records):
    '''
        Parameters:
        x signifier for if we are printing a single record or multiple
            when x is the value of x we have one value otherwise we have multiple

            records     the length of a list we are going to process 
    '''
    print(f"{'Class':8} {'name':10} {'meaning':25} {'culture'} ")
    print("--------------------------------------------------------------------------------")
    if x != "x":
        #printing one rec
        print(f"{class_type[x]:8} {name[x]:10} {meaning[x]:25} {culture[x]} ")


    elif foundList:
        for i in range(0,records):
            print(f"{class_type[foundList[i]]:8} {name[foundList[i]]:10} {meaning[foundList[i]]:25} {culture[foundList[i]]} ")


    else:
        for i in range(0,records):
            print(f"{class_type[i]:8} {name[i]:10} {meaning[i]:25} {culture[i]} ")





    print("--------------------------------------------------------------------------------\n")
        













#-------------------------------------------MAIN CODE-----------------------------------------------
clear()

class_type = []

name = []

meaning = []

culture= []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]










with open("w6/party.csv", encoding="utf-8") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        class_type.append(rec[0])

        name.append(rec[1])

        meaning.append(rec[2])

        culture.append(rec[3])






display("x",0, len(class_type))







ans = input("Would you like to enter the search program? [y/n]").lower()

while ans != "y" and ans != "n":

    print("INVALID ENTRY")

    ans = input("Would you like to enter the search program? [y/n]").lower()

#main searching loop
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by Type")
    print("2. Search by Name")
    print("3. Search by Menu")
    print("4. Exit")

    search_type = input("\nHow would you like to search today? [1-4]")

    #using not in for user validity checks
    if search_type not in ["1", "2", "3", "4"]:
        print("*****INVALID ENTRY*****\nPlease Try Again")


    elif search_type == "1":
        

        print(f"\n You have choosen to search by type")

        search = input("which type 'dragons' or 'elf' : ").lower()

        if search not in ["dragons", "elf"]:

            print("INVLAID ENTRY")
        else:
            found = []
            for i in range(0,len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)


            if not found:
                print(f"Sorry, your search could not be completed")

            else:
                print(f"Your search for {search} is complete! details below")

                display("x", found, len(found))



    
