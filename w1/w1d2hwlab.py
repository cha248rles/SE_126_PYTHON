#Charles O'Connell
#SE126.02
#w1d2 Homework lab   
#1-7-2025 W1D2


#Program Prompt:

#Variable Dictionary






#function hangout

def ppl(max_ppl,amt_ppl):
    max_ppl = int(max_ppl)
    amt_ppl = int(amt_ppl)
    diff = max_ppl - amt_ppl
    
    
    
    return diff  








# Main Code
print ("Welcome to the room occupancy checker.")


max_ppl = (input("\n\t Please enter the maximum occupancy of the room:\t"))

amt_ppl = (input("\n\t Please enter the amount of people that are supposed to be attending the meeting:\t"))

while "." in max_ppl or "." in amt_ppl:
    print("Illogical response values responding to people must be whole numbers")
    
    max_ppl = input("\n\t Please enter the maximum occupancy of the room:\t")
    
    amt_ppl = input("\n\t Please enter the amount of people that are supposed to be attending the meeting:\t")

diff = ppl(max_ppl,amt_ppl)
diff_forced_pos = diff*-1
if diff == 0:
        print("You have enough room to occupy everyone however you cannot fit anyone else.")
elif diff > 0:
        print (f"You have enough room in the room to fit {diff} more people ")
elif diff<0:
        print (f"You need to remove at least {diff_forced_pos} people to make sure the room is not over filled.")
    