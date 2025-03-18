def generate_pattern(p):
    # Initialize a p x p grid filled with 0s
    grid = [[0 for _ in range(p)] for _ in range(p)]
    
    # Fill the grid based on the pattern rules
    for i in range(p):
        for j in range(p):
            # Fill the outermost square (except the last column)
            if i == 0 or i == p - 1 or j == 0 or j == p - 2:
                grid[i][j] = 1
            # Fill the inner squares for p >= 6
            if p >= 6:
                if i == 1 or i == p - 2 or j == 1 or j == p - 3:
                    grid[i][j] = 1
            # Fill the innermost squares for p >= 8
            if p >= 8:
                if i == 2 or i == p - 3 or j == 2 or j == p - 4:
                    grid[i][j] = 1
            # Handle the last column
            if j == p - 1:
                grid[i][j] = 1 if i == p - 1 else 0
    
    return grid

def print_pattern(grid):
    for row in grid:
        print(" ".join(map(str, row)))

# Example usage
p_values = [4, 6, 8]  # Test for p = 4, 6, 8
for p in p_values:
    print(f"Pattern for p = {p}:")
    pattern = generate_pattern(p)
    print_pattern(pattern)
    print()