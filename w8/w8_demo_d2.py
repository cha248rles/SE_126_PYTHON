#W8D2 Dictionaries and Text File Data


#-----------------imports------------------------------
import csv

from os import system,name
#functions
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#-----------------------main code-----------------------------

clear()

#review on dictionaries
library = {
    #indexes are STRINGS set by the developer
    #'key' : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open("w8/dictionary_file.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #add record data as a kay + val pair from text file

        #key --> rec[0] ; value --> rec[1] 

        library.update({rec[0] : rec[1]})

print(f"{'KEY':6}\t{'TITLE'}")
for key in library:
    #for every key and val pair within the library dictionary 

    print(f"{key:6}\t{library[key]}")




#sequential search for a title 

search = input("Enter the title you are looking for")

found = 0


for key in library:
    if search.lower() == library[key].lower():
        #store the found title's location in the dictionary 
        found = key

if found != 0:

    print(f"\nKEY: {found:6}\t TITLE: {library[found]}")

else:
    print(f"Your search for {search} came up empty :[")


#binary search for lib# (dictionary keys)

#in order to binary search a set of keys you must FIRST ...






#type() returns the class type of the data passed to it
if type(library) is dict:
    print("'library' is a DICTIONARY")
