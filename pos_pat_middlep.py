import stdio
import stdarray

grid = int(input("Insert the value of p: "))
rows = grid
cols = grid
middle = (grid/2) -1

a = [[0 for j in range(grid)] for i in range(grid)]

for i in range(rows):
    for j in range(cols):
