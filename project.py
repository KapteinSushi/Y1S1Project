import stdio
import math
import sys

p = int(input())
num0 = '0'
num1 = '1'
k = 1

while k <= p:
    
    if (p % 4 == 0):

        #Cases for line 1 (top of position pattern)
        #Line1

        top1 = p - 1                     # e.g. p = 8 d.w.s. top1 = 7 d.w.s. there are 7 1's
        i = 1
        holder1 = '1'

        while i != top1:
            holder1 = holder1 + ' 1'
            i = i + 1

        holder1 = holder1 + ' 0'
        stdio.writeln(holder1) 

        k = k + 1                        # k = 1 + 1 = 2 d.w.s. first line is done   


        #-------------------------------------------------------------------------------------

        #Line 2


        #------------------------------------------------------------------------------------

        if (p > 4):         #if p > 4, MUST STILL FIGURE OUT WHEN p = 4!!!!!!!!!!!!

            upperl = math.floor((p - 5) / 2)
        
            if upperl != 0:        #infinate while loop (FIXED)

                if ((upperl % 3) == 0):        #this means the left from the second line starts with a 1                FIX! did not account when line is a longer row of 0's
                                                                    
                  temp = upperl
                  string = '1'
                  temp = temp - 1
                #elif 


      #  if upper == 1:
       #     stdio.writeln("1 0 0 0 0 0 1 0")


        #------------------------------------------------------------------------------------

        #end   
        if k == p:
            
            i = 1
            holder0 = '0'

            while i != p:
                holder0 = holder0 + ' 0'
                i = i + 1
            stdio.writeln(holder0)


    '''k = k + 1
    top1 = p - 1
    i = 1
    holder1 = '1'

    while i != top1:
        holder1 = holder1 + ' 1'
        i = i + 1

    holder1 = holder1 + ' 0'
    stdio.writeln(holder1)
    exit()'''

exit()