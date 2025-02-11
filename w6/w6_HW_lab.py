#Charles O'Connell
#SE126.02
#w6 Homework lab 
#2/11/2025

#prompt: A library catalog program that shows the avalibility of books as well as infomration about them that you can search by.



#var library 






#imports
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








#-------------------------Main code-----------------------------------



clear()

library_num =[]

title = []

author = []

genre = []

page_count = []

availablty = []





with open("w6/book_list.csv") as csvfile:

    file = csv.reader(csvfile)

    for record in file:

        library_num.append(record[0])

        title.append(record[1])

        author.append(record[2])

        genre.append(record[3])

        page_count.append(record[4])

        availablty.append(record[5])

















