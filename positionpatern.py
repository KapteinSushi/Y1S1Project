import stdio
import sys
import math
import random
import stdarray

grid = 12 #int(sys.argv[1])
rows = grid
cols = grid
#for i in range(grid):
#a = [[0]*grid] * grid
a = [[0 for j in range(grid)] for i in range(grid)]
#print(str(a))

if grid == 4:
    stdio.writeln('''1 1 1 0
1 1 1 0
1 1 1 0
0 0 0 0
''')

'''if grid == 4:
    for i in range(0,grid - 1):
        a[i][i] = 1
    a[grid - 1] = [0] * grid
    for row in a:
        print(row)'''

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
               
                # Next row if it has a row 0's:
                if (i % 2 != 0) and (i <= upper):  # if the row has a line of 0's
                    if ((j == 0) or (j%2 == 0)) and (j != upper) and (j != upper+1) and (j != upper+3): # Collum has 1's and is not part of the 3x3 in the middle    
                        a[i][j] = 1
                    else:
                        a[i][j] = 0
        
        print(a[i])