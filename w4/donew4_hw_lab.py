#Charles O'Connell
#SE126.02
#w4 in class lab 
#1/27/2025

#prompt: This program will read through a csv file in order to give outputs based on house alligence and make a new csv file.

#var library 
#first_name is first names
#last_name is last names
#age are ages 
#screen_name are screen names
#house_alligence are house alligences
#total_count is used for counts 
#email is for emails 
#ext is for phone extensions 
#department is for the department 
#random_s,t,tu,l,b,nw dictates the random range of number extensions 
#writer_thing is used to write stuff in csv file




#imports
from os import system, name

import csv

import random





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

ext = []

department = []




with open("w4/got_emails.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for record in file:
        
        #appending data to lists
        first_name.append(record[0])
        
        last_name.append(record[1])
        
        age.append(record[2])
        
        screen_name.append(record[3])
        
        house_alligence.append(record[4])
        
        total_count = total_count + 1 #counter 
        
        
        email.append(record[3] +"@westeros.net")
        
        #appending to department based on house-alligence via conditionals 
        
        if record[4] == "House Stark":
            
            random_s = random.sample(range(100,199),1)[0]
            ext.append(random_s)
            department.append("Research and Development")
        
        elif record[4] == "House Targaryen":
            
            random_t = random.sample(range(200,299),1)[0]
            ext.append(random_t)
            department.append("Marketing")
        
        elif record[4] == "House Tully":
            
            random_tu = random.sample(range(300,399),1)[0]
            ext.append(random_tu)
            department.append("Human Resources")
            
        
        elif record[4] == "House Lannister":
            
            random_l = random.sample(range(400,499),1)[0]
            ext.append(random_l)
            department.append("Accounting")
        
        elif record[4] == "House Baratheon":
            
            random_b = random.sample(range(500,599),1)[0]
            ext.append(random_b)
            department.append("Sales")
        
        elif record[4] == "The Night's Watch":
            
            random_nw = random.sample(range(600,699),1)[0]
            ext.append(random_nw)
            department.append("Auditing")
        
        else:
            
            a="error"
            ext.append(a)
        
        
        

#HEADER 
    print(f"{'FirstName':20} {'LastName':20} {'Email':30} {'Department':34} {'Extension':15}                           ")
    print("-------------------------------------------------------------------------------------------------------------------------")
#output to user 

for i in range(0, len(first_name)):
    print(f"{first_name[i]:20} {last_name[i]:20} {email[i]:30} {department[i]:25} {ext[i]:15}")




print (f"There are a total of {total_count} employees.")


#opens a file up
with open('westeros.csv', 'w', newline ='') as file:

    writer_thing = csv.writer(file) #writes stuff in csv file 
    
    #writes header
    writer_thing.writerow(['first_name', 'last_name', 'email', 'department', 'ext'])
    #writes data in 
    for i in range(0, len(first_name)):
        writer_thing.writerow([first_name[i], last_name[i], email[i], department[i], ext[i]])
    
    
    #TRIED DOING EXTRA CREDIT WHICH AFFECTED FORMATTING OF CODE BUT COULDNT MAKE IT WORK 
with open('westeros.csv', 'r') as file:
    recs = list(csv.reader(file))
    




with open('westeros.csv', 'w', newline ='') as file:
    
    
    writer_thing = csv.writer(file)
    
    writer_thing.writerows(recs)
    






