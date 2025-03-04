#W9D2 - SE126 Course Review

#---IMPORTS----------------------------------------------------
import csv
from os import system, name

#---FUNCTIONS--------------------------------------------------

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def swap(j,listName):
    temp = listName[j]
    listName[j] = listName[j+1]
    listName[j +1] = temp



#---MAIN EXECUTING CODE----------------------------------------
clear()
#creation & population of lists 
names_list = ["Abby", "Bobby", "Carol"]
print(names_list)                                   #entire list
print(names_list[0])                                #first value  
print(names_list[len(names_list) -1 ])              #last value

#create an empty list for each potential field
#must remain at same length to be parallel
names = []
riders = []
nums = []
color1 = []
color2 = []

#creation & population of dictionaries
people_dictionary ={
    #"key" : value
    "fname" : "George",
    "mname" : "Bulleit",
    "lname" : "Wayne",
    "age"   : 12, #no key name duplicates 
    "age"   : 12.5

}



print(people_dictionary)
print(people_dictionary["fname"]) #replaces with val assigned to "fname" key


dragon_dict = {} #empty dictoniary to be populated by file



#gaining data from a text file 
with open("w9/dragons-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #print() #we will replace this during demo

        #adding data to a list 
        names.append(rec[0]) #adds to end only works with lsits 
        riders.append(rec[1])
        nums.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
            color_var=rec[4]
        else:
            #still need to assign data to color2
            color2.append("---")
            color_var = "---"





        #adding data to a dictionary
        dragon_dict.update({rec[0] : [rec[1], rec[2], rec[3], color_var]})



#processing data from collections
#lists --> for i in range()
print(f"{'NAMES':12} {'Riders':30} {'NUM':3} {'COLOR1':8} {'COLOR2'}")
print("-"*70)
for i in range (0,len(names)):
    print(f"{names[i]:12} {riders[i]:30} {nums[i]:3} {color1[i]:8} {color2[i]}")

print("-"*70)

# dictionaries --> for key in dictrionary
for key in dragon_dict:
    print(f"{key.upper():15}{dragon_dict[key]}")# this shows us the list data found at each key 

    for value in dragon_dict[key]:
        print(f"{key} - {value}", end = "")
    print()
    for i in range (len(dragon_dict[key])):
        print(f"{key}/{dragon_dict[key][i]}", end = "")
    print("\n")
print("-"*70)


#searching & sorting

#sequential search for multiple return values 
search = input ("\nEnter the rider name you wish to find")
found = []

for key in dragon_dict:
    if search.lower() in dragon_dict[key][0].lower():
        found.append(key) #adds key of found location to the list 

if not found:
    #found list is still empty, no search return
    print(f"\nYour search for {search} came up empty :[\n")


else:
    print(f"\n Here is the results of your search for {search}")
    for i in range (len(found)):
        print(f" {found[i].upper():15}     {dragon_dict[found[i]][0]:30}          {dragon_dict[found[i]][1]:30}   {dragon_dict[found[i]][1]:30}    {dragon_dict[found[i]][2]:30}               {dragon_dict[found[i]][3]:30}  ")
#Binary search requires the sorting of data before searching
#We must also  ensure the collection we search through is populated with unique values


#bubble sort algorithem loop in a loop
for i in range (len(names)-1):
    for j in range(len(names)-1):
        if names [j] > names[j+1]:
            swap(j,names)
            swap(j,riders)
            swap(j,nums)
            swap(j,color1)
            swap(j,color2)

search = input("\nEnter the DRAGON NAME you wish to find: ")

min = 0
max = len(names)-1
mid = int((min+max)/2)

while min < max and search.lower() != names[mid].lower():
    if search.lower() < names[mid].lower():
        max = mid - 1
    else:
        min = mid +1
    mid = int((min+max)/2)

if search.lower() == names[mid].lower():
    print(f"We found your search for {search} in record # {mid} see info below")
    print(f"{names[mid]:12} {riders[mid]:30} {nums[mid]:3} {color1[mid]:8} {color2[mid]}")
else:
    print(f"\nSorry, we could not find your search for {search} :[\n")


    



#2D lists - lists of lists! 


letters = [
    ["A","B","C"],
    ["D","E","F"],
    ["G","H","I"],
]
print(letters) # whole 2d list
print(letters[0]) # first list inside of 2d letters
print(letters[0][0]) # first val in first lsit of 2d letters
print(letters[0] [len(letters[0])-1 ]) #last val of first list of 2d letters



