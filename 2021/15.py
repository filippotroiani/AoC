# Advent of Code 2021 https://adventofcode.com/2021/day/15
# --- Day 15: Chiton ---

# You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.

# The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581

# You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).

# Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581

# The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).

# What is the lowest total risk of any path from the top left to the bottom right?

# Your puzzle answer was 717.

# --- Part Two ---

# Now that you know how to find low-risk paths in the cave, you can try to find your way out.

# The entire cave is actually five times larger in both dimensions than you thought; the area you originally scanned is just one tile in a 5x5 tile area that forms the full map. Your original map tile repeats to the right and downward; each time the tile repeats to the right or downward, all of its risk levels are 1 higher than the tile immediately up or left of it. However, risk levels above 9 wrap back around to 1. So, if your original map had some position with a risk level of 8, then that same position on each of the 25 total tiles would be as follows:

# 8 9 1 2 3
# 9 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7

# Each single digit above corresponds to the example position with a value of 8 on the top-left tile. Because the full map is actually five times larger in both dimensions, that position appears a total of 25 times, once in each duplicated tile, with the values shown above.

# Here is the full five-times-as-large version of the first example above, with the original map in the top left corner highlighted:

# 11637517422274862853338597396444961841755517295286
# 13813736722492484783351359589446246169155735727126
# 21365113283247622439435873354154698446526571955763
# 36949315694715142671582625378269373648937148475914
# 74634171118574528222968563933317967414442817852555
# 13191281372421239248353234135946434524615754563572
# 13599124212461123532357223464346833457545794456865
# 31254216394236532741534764385264587549637569865174
# 12931385212314249632342535174345364628545647573965
# 23119445813422155692453326671356443778246755488935
# 22748628533385973964449618417555172952866628316397
# 24924847833513595894462461691557357271266846838237
# 32476224394358733541546984465265719557637682166874
# 47151426715826253782693736489371484759148259586125
# 85745282229685639333179674144428178525553928963666
# 24212392483532341359464345246157545635726865674683
# 24611235323572234643468334575457944568656815567976
# 42365327415347643852645875496375698651748671976285
# 23142496323425351743453646285456475739656758684176
# 34221556924533266713564437782467554889357866599146
# 33859739644496184175551729528666283163977739427418
# 35135958944624616915573572712668468382377957949348
# 43587335415469844652657195576376821668748793277985
# 58262537826937364893714847591482595861259361697236
# 96856393331796741444281785255539289636664139174777
# 35323413594643452461575456357268656746837976785794
# 35722346434683345754579445686568155679767926678187
# 53476438526458754963756986517486719762859782187396
# 34253517434536462854564757396567586841767869795287
# 45332667135644377824675548893578665991468977611257
# 44961841755517295286662831639777394274188841538529
# 46246169155735727126684683823779579493488168151459
# 54698446526571955763768216687487932779859814388196
# 69373648937148475914825958612593616972361472718347
# 17967414442817852555392896366641391747775241285888
# 46434524615754563572686567468379767857948187896815
# 46833457545794456865681556797679266781878137789298
# 64587549637569865174867197628597821873961893298417
# 45364628545647573965675868417678697952878971816398
# 56443778246755488935786659914689776112579188722368
# 55172952866628316397773942741888415385299952649631
# 57357271266846838237795794934881681514599279262561
# 65719557637682166874879327798598143881961925499217
# 71484759148259586125936169723614727183472583829458
# 28178525553928963666413917477752412858886352396999
# 57545635726865674683797678579481878968159298917926
# 57944568656815567976792667818781377892989248891319
# 75698651748671976285978218739618932984172914319528
# 56475739656758684176786979528789718163989182927419
# 67554889357866599146897761125791887223681299833479

# Equipped with the full map, you can now find a path from the top left corner to the bottom right corner with the lowest total risk:

# The total risk of this path is 315 (the starting position is still never entered, so its risk is not counted).

# Using the full map, what is the lowest total risk of any path from the top left to the bottom right?

# Your puzzle answer was 2993.

import math
import os
INPUT_PATH = 'input/15.txt'

class Spot: # using a class. slower for bigger input
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight
        self.g = 9999
        self.h = 0
        self.f = self.g + self.h
        self.neighbors = []
        self.cameFrom = None

    def __repr__(self):
        return 'Spot object {'f' x: {self.x}, y: {self.y}, weight: {self.weight}, g: {self.g}, neighbors: {self.neighbors}, cameFrom: {self.cameFrom}'+'}'

    def findNeighbors(self, grid): 
        if self.x < len(grid) - 1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.y < len(grid[0]) - 1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])

    def getCoordinates(self):
        return (self.x, self.y)

def printGrid(grid,last = (0,0)):
    os.system('clear')
    print('last: ',last)
    path = reconstruct_path(grid[last[0]][last[1]])
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if (i,j) == last:
                mark1 = mark2 = '-'
            elif (i,j) in path:
                mark1 = '['
                mark2 = ']'
            elif (i,j) in list(map(lambda e: e.getCoordinates(),grid[last[0]][last[1]].neighbors)):
                mark1 = '('
                mark2 = ')'
            else:
                mark1 = mark2 = ' '
            print(f'{mark1}{element.weight}{mark2}',end='')
            
        print()
    input()

def heuristic(a, b):
    return math.dist((a.x, a.y), (b.x, b.y))    # euclidean distance
    # return abs(a.x - b.x) + abs(a.y - b.y)  # manhattan distance

def reconstruct_path(current):
    path = []
    while current.cameFrom is not None:
       path.insert(0,current.getCoordinates())
       current = current.cameFrom
    return path

# A* finds a path from start to goal.
# h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def A_Star(grid, start, goal):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = [start]
    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    cameFrom = []

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    # gScore = map with default value of Infinity
    start.g = 0

    # For node n, fScore[n] = gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how short a path from start to finish can be if it goes through n.
    # fScore = map with default value of Infinity
    start.f = start.h

    while len(openSet) != 0:
        
        # This operation can occur in O(1) time if openSet is a min-heap or a priority queue
        current = openSet[0]
        for node in openSet[1:]:
            if node.f < current.f:
                current = node
        # printGrid(grid,current.getCoordinates())  # for debug purpose
        if current == goal:
            # print('END')
            return goal.g   # returns the shortest path's distance. Use reconstruct_path(current) for the path

        openSet.remove(current)
        for neighbor in current.neighbors:
            
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = current.g + neighbor.weight
            if tentative_gScore < neighbor.g:
                # printGrid(grid,current.getCoordinates())  # for debug purpose
                # This path to neighbor is better than any previous one. Record it!
                neighbor.cameFrom = current
                cameFrom.append(current)
                neighbor.g = tentative_gScore
                neighbor.f = tentative_gScore + neighbor.h
                if neighbor not in openSet:
                    openSet.append(neighbor)
    # Open set is empty but goal was never reached
    return None   # Failure

def extendCaveMap(grid):    # prepare the cave map for part 2
    initialRowNum = len(grid)
    initialColNum = len(grid[0])
    for i in range(initialRowNum):
        for k in range(1,5):
            for j in range(initialColNum):
                grid[i].append(Spot(i, j+initialColNum*k, (grid[i][j].weight+k) if grid[i][j].weight+k < 10 else (grid[i][j].weight+k)%9))
    for k in range(1,5):
        for i in range(initialRowNum):
            newRow = []
            for j in range(len(grid[i])):
                newRow.append(Spot(i+initialRowNum*k, j, (grid[i][j].weight+k) if grid[i][j].weight+k < 10 else (grid[i][j].weight+k)%9))
            grid.append(newRow)


caveMap = []
caveMap2 = []
with open(INPUT_PATH) as file:
    for i, line in enumerate(file):
        row = []
        row2 = []
        for j, ch in enumerate(line.rstrip()):
            row.append(Spot(i, j, int(ch)))
            row2.append(Spot(i, j, int(ch)))
        caveMap.append(row)
        caveMap2.append(row2)
# PART 1
# printGrid(caveMap,(0,0))   # for debug purpose
start = caveMap[0][0]
start.weight = 0    # the start position risk will not be considered
goal = caveMap[-1][-1]
for row in caveMap:
    for element in row:
        element.findNeighbors(caveMap)
        element.h = heuristic(element, goal)
minRisk = A_Star(caveMap, start, goal)
if minRisk is not None:
    # printGrid(caveMap, goal)   # for debug purpose
    print(f'The lowest total risk of any path through the cave is {minRisk}')
else:
    print('FAIL')

# PART 2
extendCaveMap(caveMap2) # prepare Cave map for part 2
start = caveMap2[0][0]
start.weight = 0    # the start position risk will not be considered
goal = caveMap2[-1][-1]
for row in caveMap2:
    for element in row:
        element.findNeighbors(caveMap2)
        element.h = heuristic(element, goal)
minRisk = A_Star(caveMap2, start, goal)
if minRisk is not None:
    # printGrid(caveMap2, goal)   # for debug purpose
    print(f'The lowest total risk of any path through the cave is {minRisk}')
else:
    print('FAIL')