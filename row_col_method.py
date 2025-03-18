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

upper = math.floor((grid - 5) / 2)  #p = 4, upper = 1   p = 12, upper = 3
right = upper + 1

counter = 1

if grid % 4 == 0:
    for i in range(0,rows):
        for j in range(0,cols):
            if i == 0 and j < grid-1:
                a[i][j] = 1
                a[j][i] = 1
                counter += 1
            
            if i > 0 and j > 0:
                if (((i%2 == 0) and (i < upper) and j) or ((i%2 == 0) and (i > upper+4))) and (j < grid-1):
                    a[i][j] = 1
                #if (i%2 == 0): 
                    a[j][i] = 1    


        print(a[i])