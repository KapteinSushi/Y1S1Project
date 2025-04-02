import sys
import stdio
import stdarray
import numpy as np
def create_symmetrical_array(size):
    # Initialize a x size array filled with zeros
    array = stdarray.create2D(size, size, 0)
    
    # Define the index for the center of the pattern
    startIndex = int((size / 2) - 1)

    # Place 1 in the center locations, always one
    centerOffcet = startIndex
    array[centerOffcet][centerOffcet] = 1
    
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
<<<<<<< HEAD

        # Get the bottom left index for the next outer rim (It represents )
        offset_position = (startIndex + (i+1), startIndex + (i+1))
=======
        #print ("rect_length:" + str(rect_length))

        # Get the bottom left index for the next outer rim (It represents )
        offset_position = (startIndex + (i+1), startIndex + (i+1))
        #print ("offset_position:" + str(offset_position))
>>>>>>> 8706ce800e23220b44461e97f52dd94f4bdf0b36
        
        # Generate the positions for the rectangle      
        surrounding_positions = generate_rectangle_positions(offset_position, runCount - (i+2))

        # Insert the defined value in surrounding positions
        for row, col in surrounding_positions:
            # Check if the position is within the array bounds
            if 0 <= row < size and 0 <= col < size:
                array[row][col] = rimValue

        # Check if it's the last iteration        
        if i == runCount - 1:
            return array
        
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
<<<<<<< HEAD

    # Calculate the rectangle corners
    top =  length
    bottom = row
    left = length
    right = row
=======
    # subtract one form the length because indexing start at 0
    # length = length -1   

    # Calculate the rectangle corners
    #top = row - length 
    top =  length
    #print("top:" + str(top) )
    bottom = row
    #print("bottom:" + str(bottom) )
    #left = col - length
    left = length
    #print("left:" + str(left) )
    right = row
    #print("right:" + str(right))
    #print("---------------------")
    
>>>>>>> 8706ce800e23220b44461e97f52dd94f4bdf0b36

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

array = create_symmetrical_array(size=8)

<<<<<<< HEAD
# Rotate the array to go into the bottom left and top right corners
=======
>>>>>>> 8706ce800e23220b44461e97f52dd94f4bdf0b36
# Turn the array into a matrix
rotate_array = np.array(array)
rotate_90 = np.rot90(rotate_array)
rotate_180 = np.rot90(np.rot90(rotate_90))
#stdio.writeln(rotate_180)

<<<<<<< HEAD
for i in rotate_180:
    stdio.writeln(" ".join(map(str, i)))
=======
for i in rotate_array:
    stdio.writeln(" ".join(map(str, i)))

'''
# Call the function
array = create_symmetrical_array(size=16)
# Print result to the console.
for row in array:
    print(" ".join(map(str, row)))  '''
>>>>>>> 8706ce800e23220b44461e97f52dd94f4bdf0b36
