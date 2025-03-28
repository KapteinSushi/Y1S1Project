import sys
import math
import stdio
import stdarray
import numpy as np

grid_size = sys.argv[1]
pospatsize = sys.argv[2]
allignpatsize = sys.argv[3]
string = sys.argv[4]

# If the pospatterns can't fit and/or there is no space for encoded message then error and exit program
if not grid_size >= grid_size - (2*pospatsize) + 2:
    print("Insert the errors and exit!")
    sys.exit()


########################################################

#-------------------------------------------------------
# Begining position pattern

def create_symmetrical_array(size):
    # Initialize a x size array filled with zeros
    arrpos = stdarray.create2D(size, size, 0)
    
    # Define the index for the center of the pattern
    startIndex = int((size / 2) - 1)

    # Place 1 in the center locations, always one
    centerOffcet = startIndex
    arrpos[centerOffcet][centerOffcet] = 1
    
    # Calculate the number or rims that must be generated
    runCount = int(size/2) 

    firstExecution = True

    # Run a for loop for the amount of rims that there must be
    for i in range(runCount):

        # Set the rim size based on the offset index
        rect_length = startIndex + i

            
        # Set values for first rim vale to one, always one. (only runs once and it is the first time)
        if  firstExecution:
            rimValue = int(1)
            rect_length = 3
            firstExecution = False

        # Get the bottom left index for the next outer rim (It represents )
        offset_position = (startIndex + (i+1), startIndex + (i+1))
        
        # Generate the positions for the rectangle      
        surrounding_positions = generate_rectangle_positions(offset_position, runCount - (i+2))

        # Insert the defined value in surrounding positions
        for row, col in surrounding_positions:
            # Check if the position is within the array bounds
            if 0 <= row < size and 0 <= col < size:
                arrpos[row][col] = rimValue

        # Check if it's the last iteration        
        if i == runCount - 1:
            return arrpos
        
        # Invert the the next rim value (1 to 0 and 0 to 1) (using the xor function)
        rimValue = rimValue ^ 1 
    


def generate_rectangle_positions(position, length):
    """
    Generates positions forming a rectangle around a specified position.
    
    Args:
        position (tuple): The (row, col) position to center the rectangle around
        length (int): Length of each side of the rectangle
    
    Returns:
        list: List of (row, col) tuples forming a rectangle
    """
    positions = []
    row, col = position

    # Calculate the rectangle corners
    top =  length
    bottom = row
    left = length
    right = row

    # Top edge
    for c in range(left, right + 1):
        positions.append((top, c))
    
    # Right edge
    for r in range(top, bottom + 1):
        positions.append((r, right))
    
    # Bottom edge
    for c in range(right, left - 1, -1):
        positions.append((bottom, c))
    
    # Left edge
    for r in range(bottom - 1, top, -1):
        positions.append((r, left))
    
    return positions

arrpos = create_symmetrical_array(size=8)

# End of position patern
#-------------------------------------------------------

########################################################

#-------------------------------------------------------
# Beginig of rotate position pattern

rotate_array = np.array(arrpos)
rotate_90 = np.rot90(rotate_array)
rotate_180 = np.rot90(np.rot90(rotate_90))
#stdio.writeln(rotate_180)

# 90 degree rotate goes in the bottom left corner
for i in rotate_90:
    stdio.writeln(" ".join(map(str, i)))

#stdio.writeln(" ")

# 180 degree rotate goes in the top right corner
for i in rotate_180:
    stdio.writeln(" ".join(map(str, i)))

# Ending of rotate position pattern
#-------------------------------------------------------

########################################################

#-------------------------------------------------------
# Begining of allignment pattern

allign_size = 13    # int(input("Value for a: "))     # value for a

#rows = grid
#cols = grid
#row = grid-1
#col = grid-1

if allign_size == 1:
    print(str(1))

# Method 2: Using list comprehension (more concise)
a = [[0 for j in range(allign_size)] for i in range(allign_size)]
middle = int((allign_size-1)/2)
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

while rowdown <= allign_size-1:
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

for i in range(allign_size):
    for j in range(allign_size):     #col
        if j != (allign_size-1):       #col
            stdio.write(str(a[i][j]) + " ")
        elif j == (allign_size-1):     #col
            stdio.write(str(a[i][j]))
    stdio.writeln()

# Ending of allignment pattern
#-------------------------------------------------------

########################################################

#-------------------------------------------------------
# Begining of adding everything together

grid = grid_size
arr_main = stdarray.create2D[grid, grid, 0]

firstflag = True
#topright = grid - pospatsize

for i in range(pospatsize):
    for j in range(pospatsize):
        arr_main[i][j] = arrpos[i][j]

# Top right pos pattern
for i in range(pospatsize):
    topright = grid - pospatsize    #p=4; grid=12; =8
    for j in range(pospatsize):
        arr_main[i][topright] = arrpos[i][j]
        topright += 1

# Ending of grid size and adding everything togrther
#-------------------------------------------------------