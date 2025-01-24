#Charles O'Connell
#SE126.02
#w3 hw lab 
#1/22/2025

#prompt:Determine voters from a csv file and if they can and did vote.

#var library 
#age_count_eligb counts after seeing if there age is eligible to vote
#age_count_uneligb counts after seeing if they are too young to vote 
#eligibility_voted_counter is for counting the amount of people who are registered to vote that are old enough
#eligibility_did_not_vote_counteris for counting the amount of people who are not registered to vote that are old enough
#did_vote_counter is the amount of people who voted
#did_not_vote_counter is the amount of people who are registered and eligible to vote that did not 
#total_recs is the total amount of records processed
#age is the age of the voter
#registration_status is if the person is registered or not
#voted is the check to see if the person voted 



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


#initalizations for variables 
age_count_eligb = 0
        
age_count_uneligb = 0

eligibility_voted_counter = 0

eligibility_did_not_vote_counter = 0

did_vote_counter = 0

did_not_vote_counter = 0 

total_recs = 0 

#standard csv file steps 
with open ("w3/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for record in file:
        total_recs = total_recs + 1
        
        #getting values assigned
        
        age = int(record[1])
        
        registration_status = record[2]
        
        voted = record[3]

        
        #strict conditionals in order to evalute and extrapulate the data needed for the print statements later on 
        if age >=18:
            
            age_count_eligb = age_count_eligb +1
            
            if registration_status == "Y":
                    
                eligibility_voted_counter = eligibility_voted_counter +1
                
                if voted == "Y":
                    
                    did_vote_counter = did_vote_counter +1
                
                elif voted == "N":
                    
                    did_not_vote_counter = did_not_vote_counter + 1
                
                
            elif registration_status == "N":
                eligibility_did_not_vote_counter = eligibility_did_not_vote_counter +1
            
        elif age <18:
            
            age_count_uneligb = age_count_uneligb +1
        
        
        

#output to user 
print(f"This is the amount of people not old enough to register is {age_count_uneligb}.")
print(f"This is the amount of people who are old enough to vote but did not register to vote {eligibility_did_not_vote_counter}")
print(f"This is the amount of people registered to vote who did not vote {did_not_vote_counter}")
print(f"This is the amount of people who did vote {did_vote_counter}")
print(f"This is the amount of records processed {total_recs}")






