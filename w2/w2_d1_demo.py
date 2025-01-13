#Charles O'Connell
#SE126.02
#w2d1 In class lab   
#1-13-2025 W2D1

# Text File Handiling intro 


#import csv library
import csv


total_records = 0 # the total number of records (rows) in file 



#connecting to files path swap slash \ to / 
print(f"{'Name':7} \t {'Age':9}     {'Color'} ")
print("---------------------------------------")
with open ("w2/simple.csv") as csvfile:
    #indent one level

    #allow processer to read file data 
    file = csv.reader(csvfile)

    #loop through every record (row) in the file

    for record in file:
        #add to a var
        total_records += 1
        
        #all records
        #print(record)

        #set items to var 
        name = record[0]
        number = record[1]
        color = record[2]
        print(f"{name:10} \t {number:8} \t {color}")


print("---------------------------------------")
print (f"\nTotal Records: {total_records}\n")




