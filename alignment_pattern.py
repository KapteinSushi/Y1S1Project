import stdio
import sys
import math
import random
import stdarray

grid = 13    # int(input("Value for a: "))     # value for a

#rows = grid
#cols = grid
#row = grid-1
#col = grid-1

if grid == 1:
    print(str(1))

# Method 2: Using list comprehension (more concise)
a = [[0 for j in range(grid)] for i in range(grid)]
middle = int((grid-1)/2)
a[middle][middle] = 1

rowcount = middle   # a=5; middle=2; rowcount=2     # a=9; middle=4; colcount=4
colcount = middle   # a=5; middle=2; colcount=2     # a=9; middle=4; colcount=4
rowup = middle - 1    # a=5; middle=2; rowup=1      # a=9; middle=4; rowup=3

# Find the rows at the top of middle:
while rowup >= 0:
    if (rowup != 0) and (rowup%2 != 0):     # if it is in a row that contains many 0's
        rowcount -= 1   # a=5: 1 ; a=9: 3, 
        colcount += 1   # a=5: 3 ; a=9: 5, 
        for j in range(rowcount,(colcount+1)):  # find the begin and enpoint of the row of 0's and loop from the begining to the end of it
            a[rowup][j] = 0      # Correct rows, but one col to much and to few for 9 and get futher
    elif (rowup == 0) or (rowup%2 == 0):    # if it is a row of 1's
        rowcount -= 1   # a=5: 0 ; a=9: 2,
        colcount += 1   # a=5: 4 ; a=9: 6,
        for j in range(rowcount,(colcount+1)):
            a[rowup][j] = 1
        for i in range(rowcount,(middle+1)):
            a[i][rowcount] = 1
            a[i][colcount] = 1
    rowup -= 1

rowcount = middle #how far from top and botom   # a=5; middle=2; rowcount=2     # a=9; middle=4; colcount=4
colcount = middle       # a=5; middle=2; colcount=2     # a=9; middle=4; colcount=4
rowdown = middle + 1    # a=5, middle=2; rowdown=3      # a=9; middle=4; rowdown=5

# Find the rows at the bottom of middle:

while rowdown <= grid-1:
    if (rowdown != 8) and (rowdown%2 != 0):     # if it is in a row that contains many 0's
        rowcount -= 1   # a=5: 1 ; a=9: 3, 
        colcount += 1   # a=5: 3 ; a=9: 5, 
        for j in range(rowcount,(colcount+1)):  # find the begin and enpoint of the row of 0's and loop from the begining to the end of it
            a[rowdown][j] = 0      # Correct rows, but one col to much and to few for 9 and get futher
    elif (rowdown == 8) or (rowdown%2 == 0):    # if it is a row of 1's
        rowcount -= 1   # a=5: 0 ; a=9: 2,
        colcount += 1   # a=5: 4 ; a=9: 6,
        for j in range(rowcount,(colcount+1)):
            a[rowdown][j] = 1
        for i in range((middle+1), colcount):
            a[i][rowcount] = 1
            a[i][colcount] = 1
    rowdown += 1

for i in range(grid):
    for j in range(grid):     #col
        if j != (grid-1):       #col
            stdio.write(str(a[i][j]) + " ")
        elif j == (grid-1):     #col
            stdio.write(str(a[i][j]))
    stdio.writeln()

'''
for i in range(0,rows):
    print(i)
    for j in range(0,cols):
        # where there is a row of 1's

        #print(i)
        if i == 0:
            #print('row1')
            a[i][j] = 1
            #print(a)
            count += 1
       # if (i%2 == 0) and (i != middle):    # if the row is even and not the middle i.e. if the row is 1's
        #    for l in range(j+1, j-1):
          #      a[i][l] = 1
    print(a[i])'''

