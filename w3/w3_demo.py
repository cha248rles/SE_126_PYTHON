#Charles O'Connell
#SE126.02
#w3d2 demo lab  
#1/21/2025
#1d list and parallel list 

#this file uses: class_grade.csv


#imports
import csv
from os import system, name



#functions


#clear screen function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')




clear()        


total_records = 0 


#create a list 
firstName=[]
lastName=[]
test1=[]
test2=[]
test3=[]


with open("w3/class_grades.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file:
        #for each record in file 
        #print(f"{rec[0]:10} \t {rec[1]:10}")


        #append rec
        firstName.append(rec[0])

        lastName.append(rec[1])

        test1.append(int(rec[2]))

        test2.append(int(rec[3]))

        test3.append(int(rec[4]))


#disconnect from file

#procees list means for loop
        
print(f"\nindex{'#':3} {'first':10} {'last':10} {'test1':3} {'test2':3} {'test3':3} {'avg':3}")

# create a new list to hold test score averages

avg = []

#process the current student data to find and store studentr test scoire avg to the avg list 

for i in range(0, len(test1)):

    a = (test1 + test2 +test3) / int(3)
    avg.append(a)
for index in range(0, len(firstName)): #len is colllection returns # of items 

    #index allows to acess one specific value
    print(f"Index: {index:3} {firstName[index]:10} {lastName[index]:10} {test1[index]:3} {test2[index]:3} {test3[index]:3} {avg[index]:.2f}")

total_avg = 0

for i in range(0,len(avg)):
    total_avg += avg[i]





