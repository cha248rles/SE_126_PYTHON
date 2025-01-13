#Charles O'Connell
#SE126.02
#w2d2 In class lab   
#1-14-2025 W2D2

#program prompt: Room checking program to see how over booked a room is.


#var dictionary
#total_rec is the total amount of records
#total_over is the amount of records that have a attending higher than the maximum
#room is the name of room
#max is the max amount of people allowed in a room
#attending is the people that are supposed to be in the room
#diff is the amount of people attending minus the max and is used only for rooms that are over capacity 
#file is the csv file (Comma separated values file)


#imports
import csv


#var initalization
total_rec = 0 
total_over =0


#--------------main code starts here-------------

print(f"{'Room':61}\t {'Max':6}\t       {'Attending':4} \t {'Over':10}")
print("------------------------------------------------------------------------------------------------------") #organization 

#does the csv file opening stuff
#main processing stuff
with open ("w2/classLab2.csv") as csvfile:


    file = csv.reader(csvfile)

    for record in file:
        #making vars from record 
        room = record[0]
        max = int(record[1])
        attending = int(record[2]) 
        diff = int(attending-max)

        #counter thing used later for print 
        total_rec += 1

        if record [2] > record [1]:
            print (f"{room:50}   {max:15} {attending:15} {diff:15} ")
            total_over +=1


#organization
print("------------------------------------------------------------------------------------------------------")
print(f"\n There are {total_over} rooms over the allowed limit.")
print(f"\n There are {total_rec} rooms.")




