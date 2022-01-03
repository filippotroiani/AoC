# Advent of Code 2021 09 dic
# --- Day 9: Smoke Basin ---

# These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

# If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

# Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

# Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

# In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

# The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

# Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

# Your puzzle answer was 535.

# --- Part Two ---

# Next, you need to find the largest basins so you know what areas are most important to avoid.

# A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

# The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

# The top-left basin, size 3:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The top-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The middle basin, size 14:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# The bottom-right basin, size 9:

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

# Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

# What do you get if you multiply together the sizes of the three largest basins?

# Your puzzle answer was 1122700.

import math
INPUT_PATH = 'input/09.txt'

def totalRiskLevel(heighmap):
    sum = 0
    for i in range(len(heighmap)):
        for j in range(len(heighmap[0])):
            up = down = left = right = True
            if i < len(heighmap) - 1 and heighmap[i + 1][j] <= heighmap[i][j]:  # if you're not on the upper edge check down
                down = False
            if i > 0 and heighmap[i - 1][j] <= heighmap[i][j]:  # if you're not on the lower edge check up
                up = False
            if j < len(heighmap[0]) - 1 and heighmap[i][j + 1] <= heighmap[i][j]:   # if you're not on the right edge check right
                right = False
            if j > 0 and heighmap[i][j - 1] <= heighmap[i][j]:  # if you're not on the left edge check left
                left = False
            if up and down and left and right:  # if every adjacent location has an higher heigh value the location [i][j] is a low point
                sum += 1 + int(heighmap[i][j])
    return sum

def calculateBasinSize(heighmap,x,y):   # recursive function: explore adjacent locations if they are part of the basin (heigh != 9)
    heighmap[x][y] = '9'    # mark the location as checked with a 9 so you'll not check it again
    size = 1
    if x < len(heighmap) - 1 and heighmap[x + 1][y] != '9':
        size += calculateBasinSize(heighmap, x + 1, y)
    if x > 0 and heighmap[x - 1][y] != '9':
        size += calculateBasinSize(heighmap, x - 1, y)
    if y < len(heighmap[0]) - 1 and heighmap[x][y + 1] != '9':
        size += calculateBasinSize(heighmap, x, y + 1)
    if y > 0 and heighmap[x][y - 1] != '9':
        size += calculateBasinSize(heighmap, x, y - 1)
    return size

def findBasins(heighmap):
    basins = []
    for i in range(len(heighmap)):
        for j in range(len(heighmap[0])):
            if heighmap[i][j] != '9':   # if a location has a heigh lower than 9 it is part of a basin -> explore basin
                basins.append(calculateBasinSize(heighmap,i,j))
    return basins

heighmap = []
visited = []
with open(INPUT_PATH) as file:
    for line in file:
        heighmap.append(list(line.strip()))
    print(f'the sum of the risk levels is {totalRiskLevel(heighmap)}.')
    basins = findBasins(heighmap)
    basins.sort(reverse=True)
    secondRequest = math.prod(basins[:3])   # assuming you have at least 3 basins
    print(f'if you multiply together the sizes of the three largest basins you get {secondRequest}')
    