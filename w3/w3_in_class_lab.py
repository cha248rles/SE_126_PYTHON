#Charles O'Connell
#SE126.02
#w2d2 HW lab   
#REV for hw lab 1/20/2025                                   Origin 1-14-2025 W2D2  

#program prompt: This program reads a csv file and then lists all the computers in the csv file filehandling.csv.





# var dictionary
#name is for clear screen function
#file is for csv file
#record is the rows within the csv file
#computer_type is if the device is a labtop or desktop
#brand is the brand of the computer 
#cpu_iteration is the model of cpu
#ram is the amount of ram in gigabites 
#first_disk is the amount of storage on the first disk
#no_hdd is which hard disk drive is no answer choices are 1 and 2 
#second_disk is the amount of storage if any in the 2nd disk 
#os is the operating system on the computer 
#year is the year of the computer 
#year_checker is used to check the year of computer to see if it needs to be replaced



#imports
import csv
from os import system, name


#functions: clear screen function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#------------------------------------Main Code-------------------------------------------

clear() #clears screen
#inital starting things 
count = 0


price_list = []


#header

print(f"{'Type':10}\t {'Brand':6}\t   {'Cpu':4} \t {'Ram':10} {'1st disk':10} {'No HDD':10} {'2nd disk':10} {'Os':10} {'Year':10}")
print("------------------------------------------------------------------------------------------------------") #organization 

#opening csv file

with open ("w2/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:
        #make variables for items in row of csv files
        computer_type = record[0]
        brand = record[1]
        cpu_iteration = record[2]
        ram = record[3]
        first_disk = record[4]
        no_hdd = record[5]
        year_checker= record[-1]
        


        
        
        
        #turning records into output values 
        #getting computer type 
        if computer_type == "L":
            computer_type = "Labtop"
        elif computer_type == "D":
            computer_type = "Desktop"
        
        
        
        #getting the brand 
        if brand =="DL":
            brand = "Dell"
        elif brand == "HP":
            brand = "HP"
        elif brand == "GW":
            brand = "Gateway"

        
        #getting the cpu model 
        if cpu_iteration =="i5":
            cpu_iteration = "Intel I5"
        elif cpu_iteration =="i7":
            cpu_iteration = "Intel I7"

        #getting the ram amount
        if ram =="08":
            ram =" 8 GB"
        elif ram == "16":
            ram ="16 GB"

        #getting 1st disk amount
        if first_disk =="500GB":
            first_disk ="500GB"
        elif first_disk == "001TB":
            first_disk ="1TB"

        #getting the no hdd

        if no_hdd =="1":
            no_hdd ="1"
        elif no_hdd == "2":
            no_hdd ="2"


        #trying to get second disk to work
        if record[6] == "500GB" or record [6] == "001TB": #filtering what is read 

            second_disk = record[6] # setting second_disk to record 

            #changing what is displayed out
            if second_disk == "500GB":
                second_disk = "500GB"
            elif second_disk == "001TB": 
                second_disk = "1TB"

        else:
            second_disk = ""  #second_disk is now fully defined 
            

        #os getting the os 

        if record[6] == "W07":
            os = "W07"
        elif record[6] == "W10":
            os = "W10"
        else:
            os= record[7]
        
    
        #getting the year 
        if record [7] == "15":
            year = record[7]  

        elif record [7] == "16":
            year = record[7]

        elif record [7] == "17":
            year = record[7]

        elif record [7] == "18":
            year = record[7]
            
        else:
            year = record[8]

        year_used = int (year)

            #output 
        print(f"{computer_type:16} {brand:9} {cpu_iteration:13} {ram:13} {first_disk:10} {no_hdd:8} {second_disk:9} {os:11} {year:3}")
        
        
            # checks and adds count to everything and gets price if old
            
        if computer_type == "Desktop": #desktop iteration 
            
                count += count  #counter
                
                if year_used <=16:
                    
                    price = 2000

        elif computer_type == "Labtop": #labtop iteration
        count += count 
                
                if year_used <=16:
                    
                    price = 2000
            
            price_list.append(price)




print(price_list)
print("------------------------------------------------------------------------------------------------------") #organization 
