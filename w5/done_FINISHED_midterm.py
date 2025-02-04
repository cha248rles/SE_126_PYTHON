#Charles O'Connell
#SE126.02
#w5 MIDTERM PROMPT 1
#2/4/2025

#prompt: This program will use a csv file that contains employees names department and email and allows you to search for them and at the end it makes a new csv file after assigning office numbers.



#var library 
#total_recs is to count the amount of records procssed and used to give a total count of employees
#office_temp_num is used to get a random number that is later appended to a list
#answer is used in the while loop in order to keep the user trapped in it unless the exit option is selected
#choice is the option choosen by the user in the searching section
#user_email is the email that the user inputs
#search_department is the department that the user types in to search by




#LISTS LIBRARY 
#first_name is the first names of all of the people in the csv file
#last_name is the last names of all of the people in the csv file
#email is the emails of all of the people in the csv file
#department is the department of all of the people in the csv file
#phone_ext is the phone extensions of all of the people in the csv file
#office_num is the number randomlly genearted for all of the people in the csv file
#found is used to search by department in storing which employees match the department

#imports
from os import system, name #for clear screen

import csv #for csv

import random #for random sample later 




#functions
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')








#--------------------------------main code--------------------------------------

clear() #convinence 

#initalizing vars and lists 
first_name = []

last_name = []

email = []

department = []

phone_ext = []

office_num = []
total_recs = 0



#acessing the csvfile
with open ("w5/westeros.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        
        #keep count
        total_recs = total_recs +1
        #append data to lists

        first_name.append(record[0])

        last_name.append(record[1])

        email.append (record[2])

        department.append(record[3])

        phone_ext.append(record[4])

        #gets a random number for the office number without repeating numbers 
        
        office_temp_num = random.sample(range(100,200),1)[0]

        office_num.append(office_temp_num)
            












print(f"{'First Name':15}  {'Last Name':15} {'Email':40} {'Department':30}  {'Phone Extension':25} {'office_num'}                                                        ")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(first_name)):
    print(f"{first_name[i]:15}  {last_name[i]:15} {email[i]:40} {department[i]:35}  {phone_ext[i]:22}    {office_num[i]}                                                    ")

print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print(f"This is the total amount of employees record's processed {total_recs}.")



#opens a file up
with open('midterm_choice1.csv', 'w', newline ='') as file:

    writer_thing = csv.writer(file) #writes stuff in csv file 

    #header writer
    writer_thing.writerow(['First Name', 'Last Name', 'Email', 'Department', 'Phone Extension', 'Office Number'])

    #writes data in 
    for i in range(0, len(first_name)):
        writer_thing.writerow([first_name[i], last_name[i], email[i], department[i], phone_ext[i], office_num[i]])




print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("\nWelcome to the searching program.")



answer = "y"


while answer == "y":

#ask user what type of search they would like
    print ("Which option would you like to choose")
    print("\n1. Search by Email")

    print("\n2. Search by Department")

    print("\n3. Exit")


#get search type from user

    choice = input("\nPlease type a number 1 through 3 for each corrisponding option")

    if choice == "1":
        print("Search by email")
        user_email = input("Please type in the email of the employee you are looking for.")

        found = -1 #invalid index 

        #handles sequence and checks for email
        for i in range (0,len(email)):

            if user_email.lower() == email[i].lower():

                found = i
        
        if found != -1:
            print(f" Your search for {user_email} was found")
            print(f"{first_name[found]:15}  {last_name[found]:15} {email[found]:40} {department[found]:35}  {phone_ext[found]:22}    {office_num[found]}                                                     ")
        else:
            print(f" Your search for {user_email} was **NOT** found")

               

    
    elif choice == "2":
        print("Search by department")
    

        #will be useful later
        found = []

        #gets user input
        search_department = input ("Please type in the department name of the employee or employees you are looking for.")


        for i in range (0,len(department)):

            if search_department.lower() == department[i].lower():

                found.append(i)

                print(f"Found {search_department} department in INDEX {i}")

        if not found:
            #tells user the department was not found
            print(f" Your search for {search_department} was *NOT* found")

        else:
            #tells user the department was found 

            print(f" Your search for {search_department} was found")

            for i in range(0, len(found)):
                print(f"{first_name[found[i]]:15}  {last_name[found[i]]:15} {email[found[i]]:40} {department[found[i]]:35}  {phone_ext[found[i]]:22}    {office_num[found[i]]}  ")


                






    elif choice == "3":
        print("\nEXITING PROGRAM.....")
        answer = "n" 
    
    else:
        print(f"{choice} is an INVALID ANSWER")
        answer = "y"





print("Goodbye Thank you for using this program have a good day.")













