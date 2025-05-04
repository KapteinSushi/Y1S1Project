import sys
import math
import stdio
import stdarray
from qrcodelib import get_error_codewords, get_format_information_bits

#REAL LAYOUT CONDITIONS: grid = 25; pospatsize = 8; allign_size = 5;
#DARK CELL: Must always be "1" at pos[17,8]

def main():

    #ERROR Messages:

    if len(sys.argv) < 5:
        stdio.writeln("ERROR: Too few arguments")
        sys.exit()
    elif len(sys.argv) > 5:
        stdio.writeln("ERROR: Too many arguments")
        sys.exit() 
    
    try:
        encoding_parameter = int(sys.argv[1])
        #grid_size = int(sys.argv[2])
        #pospatsize = int(sys.argv[3])
        #allign_size = int(sys.argv[4])
        #string = stdio.readAll()
    except ValueError:
        stdio.writeln("ERROR: May only use integer arguments: " + sys.argv[1])
        sys.exit()

    try:
        grid_size = int(sys.argv[2])
    except ValueError:
        stdio.writeln("ERROR: May only use integer arguments: " + sys.argv[2])
        sys.exit()
    
    try:
        pospatsize = int(sys.argv[3])
    except ValueError:
        stdio.writeln("ERROR: Invalid position pattern size argument: " + sys.argv[3])
        sys.exit()

    try:
        allign_size = int(sys.argv[4])
    except ValueError:
        stdio.writeln("ERROR: May only use integer arguments: " + sys.argv[4])
        sys.exit()

    string = stdio.readAll()

    #encoding_parameter = int(sys.argv[1])
    #grid_size = int(sys.argv[2])
    #pospatsize = int(sys.argv[3])
    #allign_size = int(sys.argv[4])
    #string = stdio.readAll()

    # Validate if all 4 arguments are give, no more and no less
    #print(len(sys.argv))
        

    #encoding_parameter = 18
    #grid_size = 12
    #pospatsize = 4
    #allign_size = 5
    #string = "Hi"

    #-------------------------------------------------------
    # Beginning Errors and conditions

    # encoding parameter validity test
    if encoding_parameter < 0 or encoding_parameter >= 32:
        stdio.writeln("ERROR: Invalid encoding argument: " + str(encoding_parameter))
        sys.exit()

    # grid size valididty test
    if grid_size < 10 or grid_size > 48:
        stdio.writeln("ERROR: Invalid size argument: " + str(grid_size))
        sys.exit()

    # position pattern validity test
    if (not pospatsize >= 4) or (not pospatsize % 2 == 0):
        stdio.writeln("ERROR: Invalid position pattern size argument: " + str(pospatsize))
        sys.exit()

    # alignment pattern validity test
    if allign_size %4 != 1 or allign_size < 1:
        stdio.writeln("ERROR: Invalid alignment pattern size argument: " + str(allign_size))
        sys.exit()

    # Function to turn each char into ascii then to binary
    def string_to_binary(text):
        return ''.join(format(ord(char), '08b') for char in text)

    #Call the text_to_binary function to convert the inputted string
    binary_string = "0100"
    binary_string += format(len(string), '08b')
    binary_string += string_to_binary(string)
    binary_string += "0000"
    payload_space = grid_size**2 - (3* pospatsize**2) - allign_size**2 #####Check!!!!!!!!!!!!!!!!!
    #stdio.writeln(binary_string)

    # Continue with error messages:
    # If one position pattern is bigger than the grid, error
    if pospatsize >= grid_size:
        stdio.writeln("ERROR: Alignment/position pattern out of bounds")
        sys.exit()
    # If one allign pattern is biggr than the grid, error
    elif allign_size >= grid_size:
        stdio.writeln("ERROR: Alignment/position pattern out of bounds")
        sys.exit()
    # If both position patterns are bigger than the grid, error
    elif 2*pospatsize > grid_size:
        stdio.writeln("ERROR: Alignment/position pattern out of bounds")
        sys.exit()
    elif pospatsize + allign_size > grid_size:
        stdio.writeln("ERROR: Alignment/position pattern out of bounds")
        sys.exit()

    if len(binary_string) > 255:
        stdio.writeln("ERROR: Payload too large")
        sys.exit()

    if len(binary_string) > payload_space:
        stdio.writeln("ERROR: Payload too large")
        sys.exit()

    binary_parameter = format(encoding_parameter, '05b')
    #print(binary)

    #stdio.writeln(binary_parameter)
    #stdio.writeln(binary_parameter[2:])

    # Determine if it is GUI mode or command-line mode
    #GUI_mode = False

    GUI_mode = None
    if binary_parameter[0] == "1":
        GUI_mode = True
    elif binary_parameter[0] == "0":
        GUI_mode = False

    #############################################REMEMBER####################################################
    # Hand-in 2 if GUI mode or Real mode then terminate program
    #if GUI_mode:
        #sys.exit()
    
    # If Real mode
    real_mode = None
    if binary_parameter[1] == "1":
        real_mode = True
    elif binary_parameter[1] == "0":
        real_mode = False
    
    ###### Check to see if this code is redundent!!!!
    # Determine snake or real mode
    if binary_parameter[1] == "0":
        snake_encode = True
    elif binary_parameter[1] == "1":
        snake_encode = False

    mask_pattern = binary_parameter[2:]   #Hand-in 2: 000, 001, 010;
    #Hand-in 3: 000, 001, 010, 011, 100, 101, 110, 111

    #print(mask_pattern)

    # End of position patern
    #-------------------------------------------------------

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

            # Get the bottom right index for the next outer rim (It represents )
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

    arrpos = create_symmetrical_array(size=pospatsize)      ################  CHECK AND MODIFY IF NEEDED!!!!!!!!!

    # End of position patern
    #-------------------------------------------------------

    ########################################################

    #-------------------------------------------------------
    # Beginig of rotate position pattern

    # Function for rotating the position pattern 90 dgrees counter clockwise
    # I do this by switching the data in the rows(down) with the data in the cols(across)
    def rotate90_cc(array):
        row = pospatsize
        col = pospatsize
        arr_rotate = stdarray.create2D(pospatsize, pospatsize, 0)
        for j in range(col):
            for i in range(row-1 , -1, -1):
                arr_rotate[col-j-1][i] = array[i][j]
        return arr_rotate
    
    # Using the rotate function, rotate position pattern 3 tipes to reach the desired angle
    rotate_90 = rotate90_cc(arrpos)
    rotate_180 = rotate90_cc(rotate_90)
    rotate_180 = rotate90_cc(rotate_180)


    # Ending of rotate position pattern
    #-------------------------------------------------------

    ########################################################

    #-------------------------------------------------------
    # Begining of allignment pattern

    # Create array and populate the middle with a 1
    a = [[0 for j in range(allign_size)] for i in range(allign_size)]
    middle = int((allign_size-1)/2)
    a[middle][middle] = 1

    rowcount = middle   # a=5; middle=2; rowcount=2     # a=9; middle=4; colcount=4
    colcount = middle   # a=5; middle=2; colcount=2     # a=9; middle=4; colcount=4
    rowup = middle - 1    # a=5; middle=2; rowup=1      # a=9; middle=4; rowup=3

    # Find the rows at the top of middle
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

    # Find the rows at the bottom of middle
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


    # Ending of allignment pattern
    #-------------------------------------------------------

    ########################################################

    #-------------------------------------------------------
    # Begining of adding everything

    grid = grid_size    # grid_size = 12
    
    # Sanke declare
    arr_main = stdarray.create2D(grid_size, grid_size, 2)
    arr_padding = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]  #16 data points
    
    #print(binary_string)

    # Check if the snake needs padding and how much is needed
    if len(binary_string) < payload_space:
        padding_amount = payload_space - len(binary_string)
        while len(binary_string) < payload_space:
            for i in range(len(arr_padding)):
                if padding_amount != 0:
                    binary_string += str(arr_padding[i])
                    padding_amount -= 1
    # End of Snake declare

    # Top left position pattern
    for i in range(pospatsize):
        for j in range(pospatsize):
            arr_main[i][j] = arrpos[i][j]

    #Top right position pattern
    for i in range(pospatsize):
        top_right = grid - pospatsize    #p=4; grid=12; =8
        for j in range(pospatsize):
            arr_main[i][top_right] = rotate_180[i][j]
            top_right += 1

    #Bottom left position pattern
    arr_90 = rotate_90

    bottom_left = grid - pospatsize
    for i in range(pospatsize):
        for j in range(pospatsize):
            arr_main[bottom_left][j] = arr_90[i][j]
        bottom_left += 1

    #Alignment pattern
    allign_corner = grid -pospatsize -1

    # Check if alignment pattern is inside the grid
    if ((allign_corner -1) + allign_size) > grid_size -1:
        stdio.writeln("ERROR: Alignment/position pattern out of bounds")

    if allign_size == 1:
        arr_main[allign_corner][allign_corner] = a[0][0]
    else:
        guide = allign_corner
        for i in range(allign_size):
            for j in range(allign_size):
                arr_main[guide][allign_corner + j] = a[i][j]
            guide += 1

    #SNAKE!!!
    string_counter = 0
    xor = None
    if mask_pattern == "000":
            #print("1 == 0 ; no masking")
            xor = False

    xor_num = 0

    for i in range(grid_size):

        # If the row index is even, go from left to right
        if i%2 == 0:
            for j in range(grid_size):
                if arr_main[i][j] == 2:
                    #print(string_counter)
                    if mask_pattern == "001":
                        #print("y%2 == 0")
                        if j%2 == 0 and i%2 == 0:
                            xor = True
                        else:
                            xor = False
                    elif mask_pattern == "010":
                        #print("x%3 == 0")
                        if i%3 == 0:
                            xor = True
                        else:
                            xor = False

                    if xor:
                        arr_main[i][j] = 1 - int(binary_string[string_counter]) 
                        string_counter += 1
                    else:
                        arr_main[i][j] = int(binary_string[string_counter])
                        string_counter += 1
        # If the row index is not even, go from right to left
        elif i%2 != 0:
            for j in range(grid_size -1, -1, -1):
                if arr_main[i][j] == 2:

                    if mask_pattern == "001":
                        #print("y%2 == 0")
                        if j%2 == 0:
                            xor = True
                        else:
                            xor = False
                    elif mask_pattern == "010":
                        #print("x%3 == 0")
                        if i%3 == 0:
                            xor = True
                        else:
                            xor = False

                    if xor:
                        arr_main[i][j] = 1 - int(binary_string[string_counter])
                        string_counter += 1
                    else:
                        arr_main[i][j] = int(binary_string[string_counter])
                        string_counter += 1
    #print(string_counter)

    # Display the Qr code
    for i in arr_main:
        line = " ".join([str(x) for x in i])
        stdio.writeln(line)
    # Ending of adding everything
    #-------------------------------------------------------
    
if __name__ == "__main__": main()