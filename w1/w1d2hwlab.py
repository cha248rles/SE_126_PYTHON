#Charles O'Connell
#SE126.02
#w1d2 Homework lab   
#1-7-2025 W1D2


#Program Prompt: This program will check the capacity of a room and check it with the amount of people scheduled for a meeting and seeing how many people are allowed in it or how many people is over capacity.   

#Variable Dictionary
#response is used for while loop for main code
#max_ppl is the max allowed people for regulations
#amt_ppl is the amount of people that are attending a meeting
#diff is the difference between both the amount of people attending vs max allowed


#imports
# import only system from os
from os import system, name



#Variable Initialization 
response = "y"


#function hangout


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def ppl(max_ppl,amt_ppl):
    #necessary casting and math
    max_ppl = int(max_ppl)
    
    amt_ppl = int(amt_ppl)
    
    diff = max_ppl - amt_ppl
    
    return diff  


def decision(response):
    #while loop input
    respo= input ("Would you like to use again [y/n]").lower()
    
    while respo != "y" and respo != "n":
        
        print("***Invalid entry***")
        
        respo= input ("Would you like to use again [y/n]").lower()
        
        
    return respo



# Main Code
clear()
print ("Welcome to the room occupancy checker.") #Program Prompt to User

while response == "y":
    max_ppl = (input("\n\t Please enter the maximum occupancy of the room:\t"))
    
    amt_ppl = (input("\n\t Please enter the amount of people that are supposed to be attending the meeting:\t"))
    meeting_name = (input("\n\t Please enter the name of the meeting:\t"))

    while "." in max_ppl or "." in amt_ppl:
        print("Illogical response values responding to people must be whole numbers")
        
        max_ppl =input("\n\t Please enter the maximum occupancy of the room:\t")
        
        amt_ppl =  input("\n\t Please enter the amount of people that are supposed to be attending the meeting:\t")

    diff = ppl(max_ppl,amt_ppl)
    
    diff_forced_pos = diff*-1
    
    if diff == 0:
            print(f"You have enough room to occupy everyone however you cannot fit anyone else. The {meeting_name} meeting is legal for fire regulations")
    elif diff > 0:
            print (f"You have enough room in the {meeting_name} meeting to fit {diff} more people the meeting is legal for fire regulations")
    elif diff<0:
            print (f"You need to remove at least {diff_forced_pos} people from the {meeting_name} meeting to make sure the room is not over filled. The meeting is currently illegal for fire regulatins")
    response = decision(response)


print ("Thank you for using the program :) ")