print('Working with 2D lists.')

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][2])

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)
