#Charles O'Connell
#SE126.02
#w6 d1 demo lab 
#2/10/2025

#prompt: Binary Search 

from os import system,name
import csv 


#functionsw
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')







clear()

library_num =[]

title = []

author = []

genre = []

page_count = []

with open ("w6/library_books.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        library_num.append(rec[0])

        title.append(rec[1])

        author.append(rec[2])

        genre.append(rec[3])

        page_count.append(rec[4])

print (f" {'LIB#':5}  {'title':25} {'author':15} {'genre':20} {'page count':5}                                                           ")

for i in range(0, len(library_num)):
    print (f" {library_num[i]:5}  {title[i]:25} {author[i]:15} {genre[i]:20} {page_count[i]:5}                                                           ")

print("----------------------------------------------------------------------------------------------------------------------------")


found =[]
seq_count = 0
search_num = input ("Which num are you looking for")

for i in range (0, len(title)):

    seq_count +=1

    if search_num == library_num:

        found.append(i)


print(f"Seach Iterantions:{seq_count}")
if not found:
    print (f"Your search for {search_num} was not found")

else:
    print (f"Your search for {search_num} was found")

    print (f" {'LIB#':5}  {'title':25} {'author':15} {'genre':20} {'page count':5}                                                           ")

    print("----------------------------------------------------------------------------------------------------------------------------")

    for i in range(0, len(found)):
        print(f" {library_num[found[i]]:5}  {title[found[i]]:25} {author[found[i]]:15} {genre[found[i]]:20} {page_count[found[i]]:5}    ")

        print("----------------------------------------------------------------------------------------------------------------------------")



#binary search must be perfored on ordered lists (library_num)
        

min = 0

max = len(library_num) -1

mid = int((min+max)/2)

bin_count = 0

while min <max and search_num != library_num[mid]:

    #CHECKS TO MAKE SURE ALL VALUES ARE NOT EXHAUSTED AND MAKE SURE IT IS NOT IN MID Position

    if search_num < library_num[mid]:
        #everythijng after mid point is not possible
        max = mid -1

    else:
        min = mid +1


    mid = int ((min+max) /2)

    bin_count +=1

print(f"BIn COUNT IS {bin_count}")

if search_num == library_num [mid]:

    print (f"Your search for {search_num} was found")

    print (f" {'LIB#':5}  {'title':25} {'author':15} {'genre':20} {'page count':5}                                                           ")

    print("----------------------------------------------------------------------------------------------------------------------------")

    
    print(f" {library_num[mid]:5}  {title[mid]:25} {author[mid]:15} {genre[mid]:20} {page_count[mid]:5}    ")

    print("----------------------------------------------------------------------------------------------------------------------------")




