#Charles O'Connell
#SE126.02
#w2d2 HW lab   
#1-14-2025 W2D2

#program prompt: This program reads a csv file and then lists all the computers in the csv file filehandling.csv.





# var dictionary





#imports
import csv







#------------------------------------Main Code-------------------------------------------

#header
print(f"{'Type':10}\t {'Brand':6}\t   {'Cpu':4} \t {'Ram':10} {'1st disk':10} {'No HDD':10} {'2nd disk':10} {'Os':10} {'Year':10}")

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
        #second_disk = record[6]
        #os = record[7]
        #year = record[8]
        
        
        
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








        print(f"{computer_type:16} {brand:9} {cpu_iteration:13} {ram:13} {first_disk:10} {no_hdd:9} {second_disk:3}")