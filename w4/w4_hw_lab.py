#Charles O'Connell
#SE126.02
#w4 in class lab 
#1/27/2025

#prompt:

#var library 





#imports
from os import system, name

import csv




#functions
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')









#----------------------main code--------------------

#clears screen
clear()


#making blank lists and initalizing variables 

first_name = []

last_name = []

age = []

screen_name =[]

house_alligence = []

total_count = 0 

email = []

with open("w4/got_emails.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for record in file:
        
        first_name.append(record[0])
        
        last_name.append(record[1])
        
        age.append(record[2])
        
        screen_name.append(record[3])
        
        house_alligence.append(record[4])
        
        total_count = total_count + 1
        
        
        email.append(record[3] +"@westeros.net")
        
        



#output to user 
print (f"There are a total of {total_count} employees.")
print(f"{email}")