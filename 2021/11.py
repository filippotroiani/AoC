# Advent of Code 11 dic
# Puzzle at https://adventofcode.com/2021/day/11

INPUT_PATH = 'input/11.txt'

def flash(grid, i, j):
    up = down = False
    if i < len(grid) - 1 :  # if you're not on the upper edge check down
        down = True
        grid[i + 1][j] += 1
        if grid[i + 1][j] == 10:  flash(grid, i + 1, j)
    if i > 0 :  # if you're not on the lower edge check up
        up = True
        grid[i - 1][j] += 1
        if grid[i - 1][j] == 10:  flash(grid, i - 1, j)
    if j < len(grid[0]) - 1 :   # if you're not on the right edge check right
        grid[i][j + 1] += 1
        if grid[i][j + 1] == 10:  flash(grid, i, j + 1)
        if down:    # lower right angle
            grid[i + 1][j + 1] += 1
            if grid[i + 1][j + 1] == 10:  flash(grid, i + 1, j + 1)
        if up:  # upper right angle
            grid[i - 1][j + 1] += 1
            if grid[i - 1][j + 1] == 10:  flash(grid, i - 1, j + 1)    
    if j > 0 :  # if you're not on the left edge check left
        grid[i][j - 1] += 1
        if grid[i][j - 1] == 10:  flash(grid, i, j - 1)
        if down:    # lower left angle
            grid[i + 1][j - 1] += 1
            if grid[i + 1][j - 1] == 10:  flash(grid, i + 1, j - 1)
        if up:  # upper left angle
            grid[i - 1][j - 1] += 1
            if grid[i - 1][j - 1] == 10:  flash(grid, i - 1, j - 1)

def step(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] += 1
            if grid[i][j] == 10:  flash(grid, i, j)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] > 9:
                count += 1
                grid[i][j] = 0
    return count


grid = []
with open(INPUT_PATH) as file:
    for line in file:
        grid.append(list(map(lambda n: int(n), line.strip())))
totalFlash = 0
i = 0
while True:
    nFlash = step(grid)
    if i < 100: totalFlash += nFlash
    i += 1
    if nFlash == len(grid)**2: break
print(f'Total flashes after 100 steps {totalFlash}.')
print(f'The first synchronized flash appens at step {i}.')