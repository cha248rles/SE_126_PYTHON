#w4d2 -Sequential search review + creating and writing to text files



#import 
import csv 





#functions










#----------main code----------------------

dragons =[]
riders=[]
count=[]
color1=[]
color2=[]



with open("w4\dragons.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])

        else: 
            color2.append("---")


#disconnected from file 

#process list to display

for i in range(0,len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]}              ")
    print("--------------------------------------------------------------------------------------------------")

found ="x"

search = input("Which dragon are you looking for")
for i in range (0,len(dragons)):

    if search.lower() in dragons[i].lower():
        found = i

if found != "x":
    print(f"Your search for {search} was found")
    print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]}              ")

else:
    print(f"Your search for {search} was not found ")

found = []

search = input ("enter your dragon color you are looking for")

for i in range(0, len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append[i]


if not found:
    print(f"Your search for {search} was not found ")

else:
    print(f"Your search for {search} was found")
    print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]}              ")

