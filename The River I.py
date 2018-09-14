import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def numbertolist(number):
    number = str(number)
    number = list(number)
    number = [int(i) for i in number]
    number = sum(number)
    
    return number
        
def logic(smallriver, bigriver):
    final_result =  smallriver + numbertolist(smallriver)
    meeting = final_result == bigriver
            
    if meeting == True:
        return final_result 
    else:
        while (meeting == False):
            if final_result > bigriver:
                newbigriver = final_result
                newsmallriver = bigriver
                final_result = logic(newsmallriver, newbigriver)
                return final_result
            else:    
                final_result =  final_result + numbertolist(final_result)
                meeting = final_result == bigriver
        else:
            return final_result

meeting = r_1 == r_2      

if meeting == True:
    finalresult = r_1
elif r_1 < r_2:
    final_result = logic(r_1, r_2)
elif r_1 > r_2:
    final_result = logic(r_2, r_1)

print(final_result)
