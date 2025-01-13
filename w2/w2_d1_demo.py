#Charles O'Connell
#SE126.02
#w2d1 In class lab   
#1-13-2025 W2D1

# Text File Handiling intro 


#Step-1: import csv library
import csv


total_records = 0 # the total number of records (rows) in file 



#connecting to files path swap slash \ to / 
with open ("w2/simple.csv") as csvfile:
    #indent one level

    #allow processer to read file data 
    file = csv.reader(csvfile)

    #loop through every record (row) in the file

    for record in file:
        #add to a var
        total_records += 1

print (f"\nTotal Records: {total_records}\n")




