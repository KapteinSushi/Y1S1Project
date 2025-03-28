import stdio
import stdarray

grid = 6
middle = int((grid/2) -1)   #p=6, middle=2
a = [[0 for j in range(grid)] for i in range(grid)]
a[middle][middle] = 1
holder = 1
middeldist = 1

if grid == 4:
    a = [[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    print(a)

row = middle -1     #p=6, middle=2, row=1
bottom = grid-1

for i in range(row, 0, -1):
    print("test")
    if row == middle -1:
        for j in range(row, middeldist+1):
            a[i][j] = 1
            a[bottom - (i+1)][j] = 1
        holder = 0
        row -= 1
        middeldist += 1

    if holder == 0:
        if (row + grid) == grid:    # checks if we have reached the top and not the bottom
            for j in range 


    print(a[i])


'''
for i in range(middle,0):   # 2 to 0
    if row >= 0:    # if row is still within the grid
        if row == middle-1:     #if the row is 
            for j in range(row,row+3):
                a[row][j] = 1
                a[j][row] = 1
    row -= 1
    
    print(a[i]) '''