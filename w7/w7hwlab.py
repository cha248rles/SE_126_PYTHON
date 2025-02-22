#Charles O'Connell
#SE126.02
#w7 Homework lab 
#2/18/2025

#prompt: 

#var library









#imports
from os import system,name

import csv

#functions

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')






clear()

row_num = [1,2,3,4,5,6,7]
row_seat = ["A","B","C","D"]


def seating_chart():
    for num in row_num:
        
        print(f"{num}", row_seat, )





















