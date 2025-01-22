#Charles O'Connell
#SE126.02
#w3 hw lab 
#1/22/2025

#prompt:Determine voters from a csv file and if they can and did vote.

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







#-------------------------Main code-------------------------

clear() 

#standard csv file steps 
with open ("w3/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for record in file:
        










