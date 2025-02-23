#Charles O'Connell
#SE126.02
#w7 Homework lab 
#2/18/2025

#prompt: Airplane seating program where it responds in real time of marking off seats.

#var library
#row_num is the row numbers
#seat_A,B,C,D are the seats at their respective positions A B C and D
#ans_seat is a loop controlling var for seat value inputs
#seat_val is the seat letter and number typed in by the user
#row_num_user is the row number that is input by the user 
#seat_let is the seat letter typed in by the user 
#ans is for the main loop control for the program
#ans_loop_checker is for validation for the ans loop 











#imports
from os import system,name

import csv

#functions

def seating_chart():
    print("ROW  A,   B,   C,   D")
    for i in range(len(row_num)):
        
        print(f"{row_num[i]},   {seat_A[i]},   {seat_B[i]},   {seat_C[i]},   {seat_D [i]}")

def reserving_seat():
    ans_seat = "y"
    while ans_seat == "y":
        seat_val = input("Please enter your desired seat number and letter example (3C)").upper()
        
        row_num_user = int(seat_val[0])-1
        
        seat_let = seat_val[1]
        
        if row_num_user <0:
            print("***Invalid Entry***")
            print("ROW NUMBER CANNOT BE LESS THAN 1")
            ans_seat ="y"
            
        elif row_num_user > len(row_num) -1 :
            print("***INVALID ENTRY***")
            print("ROW NUMBER IS HIGHER THAN THE AMOUNT OF ROWS ON THE AIRPLANE")
            ans_seat ="y"
        
        
        elif seat_let !="A" and seat_let !="B" and seat_let !="C" and seat_let !="D":
            print("***INVALID ENTRY***")
            print("SEAT WAS NOT ONE OF THE 4 OPTIONS A B C OR D")
            ans_seat ="y"
        else:
            ans_seat = "n"
    
    
    if seat_let == "A" and seat_A[row_num_user] != "X":
        seat_A[row_num_user] = "X"
        print(f"Seat {seat_val} was successfully booked.")
    elif seat_let == "B" and seat_B[row_num_user] != "X":
        seat_B[row_num_user] = "X"
        print(f"Seat {seat_val} was successfully booked.")
    
    elif seat_let == "C" and seat_C[row_num_user] != "X":
        seat_C[row_num_user] = "X"
        print(f"Seat {seat_val} was successfully booked.")
    
    elif seat_let == "D" and seat_D[row_num_user] != "X":
        seat_D[row_num_user] = "X"
        print(f"Seat {seat_val} was successfully booked.")
    else:
        print(f"SORRY this {seat_val} seat is already booked")


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')






clear()

row_num = []

seat_A = []

seat_B = []

seat_C = []

seat_D = []


ans = "y"

ans_loop_checker = "y"


with open("w7/airplane.csv") as csvfile:

    file =csv.reader(csvfile)

    for record in file:
        
        row_num.append(record[0])
        
        seat_A.append(record[1])
        
        seat_B.append(record[2])
        
        seat_C.append(record[3])
        
        seat_D.append(record[4])





while ans == "y":
    
    ans_loop_checker = "y"

    seating_chart()


    reserving_seat()

    seating_chart()
    while ans_loop_checker == "y":
        ans = input("Would you like to book again [y/n]").lower()
        
        if ans != "y" and ans != "n":
            print ("INVALID ENTRY")
            ans_loop_checker = "y"
            
        else:
            ans_loop_checker = "n"
    
print("HAVE A GOOD DAY :)")






