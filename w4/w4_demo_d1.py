#Charles O'Connell
#SE126.02
#w4 d1 demo lab 
#1/27/2025

#prompt: Sequential Search 
# "We will continue to work with the class_grades.csv file, as used in the W3D2 demo. We will practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository."

#var library 





#imports
import csv
from os import system, name


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


with open ("w3/class_grades.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        #append the file data into appropriate lists 

        first_Name.append(record[0])

        last_Name.append(record[1])

        test_1.append(int(record[2]))

        test_2.append(int(record[3]))

        test_3.append(int(record[4]))




#disconnected from file -- can still acess stored data in lists 

#process list data to get avg score and letter grade for each student 

num_avg = [] #will hold students avg

let_avg = [] #will hold each students letter avg of test scores 


for i in range (0, len(first_Name)):

    a = (test_1[i] +test_2[i] + test_3[i] ) /3 #calculates avg for each student 
    
    num_avg.append(a)

    l = letter(a) # return val of letter() stored to l 

    let_avg.append(l) 



#process list to display all data to user

for i in range(0, len(first_Name)):
    print(f"{first_Name[i]:10}    {test_1[i]:10}  {test_2[i]:10} {test_3[i]:10} {num_avg[i]:10.2f}   {let_avg [i]} ")

print(f"There are {len(first_Name)} students in the file.")

