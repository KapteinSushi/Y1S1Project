import stdio
import random
import sys
import math

grid = int(sys.argv[1])
rows = grid
cols = grid
#for i in range(grid):
#a = [[0]*grid] * grid

a = [[0 for j in range(grid)] for i in range(grid)]

#print(str(a))

if grid == 4:
    for i in range(0,grid - 1):
        a[i][i] = 1
    a[grid - 1] = [0] * grid
    for row in a:
        print(row)

upper = math.floor((grid - 5) / 2)  #p = 4, upper = 1   p = 12, upper = 3
right = upper + 1

if grid % 4 == 0:
    for i in range(0,rows):
        for j in range(0,cols):

            # First row:
            if i == 0:
                if j < cols-1:   # Write the row of 1's
                    a[i][j] = 1
                elif j == cols-1:
                    a[i][j] = 0
                    right -= 1

            if i != 0: 
                
               # Second collum = 0
                if j%2 != 0:
                    a[i][j] = 0

                # Next row if it has a row 0's:
                if (i%2 != 0) and (i <= upper):       # if the row has a line of 0's (every uneven row) and the row is just above the middle 3x3
                    if ((j == upper) or (j == upper+1) or (j == upper+2) or (j == upper+3) or (j == upper+4)) or (j == cols-1):
                        a[i][j] = 0
                    else:
                        a[i][j] = 1  

                # Next row if it has 1's
               # if ((i%2 == 0) and (i <= upper)) or ((i%2 == 0) and (i >= upper+4)):  # if the row is a even row and it is above or below the middle 3x3
                #    if (j%2 == 0):
                 #       a[i][j] = 1
                
                # if we are in the middle 3x3
                if (i == upper+1) or (i == upper+2) or (i == upper+3):
                    if (j == 0) or (upper+1 <= j <= upper+4) or (j%2 == 0):
                        a[i][j] = 1
                
                # after middle 3x3
                #if i > upper
                
                
                   
        


        print(a[i])