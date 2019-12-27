number_grid = [
    [1, 2, 3],  # // row 0 ; 1 = 0 2 = 1 3 = 2
    [4, 5, 6],  # we are creating a grid with 4 rows; 3 columns // row 1
    [7, 8 ,9],  # // row 2
    [0]  # // row 3
]

print(number_grid[0][0])  # this is how we can access elements outside a 2d list

for row in number_grid:
    for col in row:
        print(col)
