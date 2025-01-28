#Charles O'Connell
#SE126.02
#w4 d2 in class lab 
#1/27/2025

#prompt: This program will add searching to a grade program that can be used with csv files

#var library 
#first_Name is used to get the first name of the people in the csv list
#last_name is used to get the last name of the people in the csv list
#test_1 test_2 and test_3 are used for each test grade 
#num_avg is the numeric grade avg for each student
#let_avg is the letter avg for each student 
#answer is used to maintain a while loop
#found is used for indexing 
#total_num is the total of the grades 
#a and num are the local avg of a student numerically 




#imports
import csv
from os import system, name

numtotal = 0
#functions

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



def letter(num):

    if num>= 90:
        let = "A"
    elif num >= 80:
        let = "B"
    elif num >=70:
        let="C"
    elif num >= 60:
        let = "D"
    elif num <60:
        let = "F"
    else:
        let = "ERROR"
    

    return let #let val replaces function call in main code 




#----------------------main code--------------------

clear()

#create empty lists

first_Name = []

last_Name = []

test_1= []

test_2= []

test_3= []

student_count = 0
total_num = 0

with open ("w3/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        #append the file data into appropriate lists 

        first_Name.append(record[0])

        last_Name.append(record[1])

        test_1.append(int(record[2]))

        test_2.append(int(record[3]))

        test_3.append(int(record[4]))

        student_count = student_count +1 




#disconnected from file -- can still acess stored data in lists 

#process list data to get avg score and letter grade for each student 

num_avg = [] #will hold students avg

let_avg = [] #will hold each students letter avg of test scores 


for i in range (0, len(first_Name)):

    a = (test_1[i] +test_2[i] + test_3[i] ) /3 #calculates avg for each student 
    num=a
    
    num_avg.append(a)

    l = letter(a) # return val of letter() stored to l 

    let_avg.append(l) 
    total_num = num + total_num
    

    
student_count = total_num/student_count


#process list to display all data to user
print(f"{'first_Name':10}  {'last_Name':15}  {'test_1':10}  {'test_2':11} {'test_3':7} {'num_avg':7}   {'let_avg'} ")
print(f"------------------------------------------------------------------------------------")
for i in range(0, len(first_Name)):
    print(f"{first_Name[i]:10}  {last_Name[i]:10}  {test_1[i]:10}  {test_2[i]:10} {test_3[i]:10} {num_avg[i]:9.2f} \t  {let_avg [i]} ")
print(f"-------------------------------------------------------------------------")

print(f"There are {len(first_Name)} students in the file.")

print(f"-------------------------------------------------------------------------")

print(f"The class average is a {student_count:.2f}")
print(f"-------------------------------------------------------------------------")
#search part


print("\nwelcome to the student search program\n\n")
print(f"-------------------------------------------------------------------------")

answer = input("Would you like to start searching [y/n]").lower()

while answer == "y":

    #get search type from user

    print("\tSEARCH MENU OPTIONS")

    print("1. SEARCH by Last NAME")

    print("2. SEARCH by First Name")

    print("3. Search by Letter Grade ")

    print("4. EXIT")

    search_type = input("Enter your search type 1-4")

    if search_type == "1":
        print("\nSEARCH BY LAST NAME")
        
        #get search item from user 
        
        search_name = input("ENTER LAST NAME OF THE STUDENT YOU ARE SEARCHING FOR")

        
        found = -1 #invalid index 
        for i in range (0,len(last_Name)):
            
                #for loop handles sequence 

            if search_name.lower() == last_Name[i].lower():
                #the if statment allows for the search part 
                found = i #makes found the current index can be used later to display 

        if found != -1:
            print(f" Your search for {search_name} was found")
            print(f"{first_Name[found]:10} {last_Name[found]:10}   {test_1[found]:10}  {test_2[found]:10} {test_3[found]:10} {num_avg[found]:10.2f}   {let_avg [found]} ")
                
        else:
            print(f" Your search for {search_name} was **NOT** found")
                    


    elif search_type == "2":

        print("\nSEARCH BY FIRST NAME")
        
        #get search item from user 
        
        search_name = input("ENTER FIRST NAME OF THE STUDENT YOU ARE SEARCHING FOR")

        
        found = -1 #invalid index 
        for i in range (0,len(first_Name)):
            
                #for loop handles sequence 

            if search_name.lower() == first_Name[i].lower():
                #the if Statement allows for the search part 
                found = i #makes found the current index can be used later to display 

        if found != -1:
            print(f" Your search for {search_name} was found")
            print(f"{first_Name[found]:10} {last_Name[found]:10}   {test_1[found]:10}  {test_2[found]:10} {test_3[found]:10} {num_avg[found]:10.2f}   {let_avg [found]} ")
        else:
            print(f" Your search for {search_name} was **NOT** found")



    elif search_type == "3":
        
        print("\nSearch by letter grade")
        
        found = []
        
        search_let = input("ENTER letter grade")
        
        
        for i in range (0,len(let_avg)):
            

            #for loop handles sequence 

            if search_let.upper() == let_avg[i]:
                #the if statment allows for the search part 
                
                found.append(i) #makes found the current index can be used later to display 
                
                print(f"Found a {search_let} grade in INDEX {i}")

            #display to user
            
        if not found:
                #last name has been found display data 
            print(f" Your search for {search_let} was *NOT* found")
            
            
        else:
                
            print(f" Your search for {search_let} was found")
                
            for i in range(0, len(found)):
                print(f"{first_Name[found[i]]:10} {last_Name[found[i]]:10}   {test_1[found[i]]:10}  {test_2[found[i]]:10} {test_3[found[i]]:10} {num_avg[found[i]]:10.2f}   {let_avg [found[i]]} ") 



    elif search_type == "4":
        print("EXIT")
        answer = "n"
    
    else:
        print("ERROR ")



print("Bye Have a good DAY.")