def generate_pattern(a):
    """
    Generate a pattern of 1s and 0s based on the input value a.

    Args:
        a (int): The size of the pattern.

    Returns:
        None
    """
    # Calculate the middle row index
    mid_row = a // 2

    # Iterate over each row
    for i in range(a):
        # Iterate over each column
        for j in range(a):
            # Check if it's the first or last row, or the first or last column
            if i == 0 or i == a - 1 or j == 0 or j == a - 1:
                print(1, end=' ')
            # Check if it's the middle rows and columns
            elif i > 1 and i < a - 2 and j > 1 and j < a - 2:
                if (i - 1) % 2 == (j - 1) % 2:
                    print(1, end=' ')
                else:
                    print(0, end=' ')
            # If none of the above conditions are met, print 0
            else:
                print(0, end=' ')
        # Move to the next line
        print()

# Test the function
a = 9
generate_pattern(a)
