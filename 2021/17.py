# Advent of Code 2021
# --- Day 17: Trick Shot ---

# You finally decode the Elves' message. HI, the message says. You continue searching for the sleigh keys.

# Ahead of you is what appears to be a large ocean trench. Could the keys have fallen into it? You'd better send a probe to investigate.

# The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward) and y (upward, or downward if negative) directions. For example, an initial x,y velocity like 0,10 would fire the probe straight up, while an initial velocity like 10,-1 would fire the probe forward at a slight downward angle.

# The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

#     The probe's x position increases by its x velocity.
#     The probe's y position increases by its y velocity.
#     Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
#     Due to gravity, the probe's y velocity decreases by 1.

# For the probe to successfully make it into the trench, the probe must be on some trajectory that causes it to be within a target area after any step. The submarine computer has already calculated this target area (your puzzle input). For example:

# target area: x=20..30, y=-10..-5

# This target area means that you need to find initial x,y velocity values such that after any step, the probe's x position is at least 20 and at most 30, and the probe's y position is at least -10 and at most -5.

# Given this target area, one initial velocity that causes the probe to be within the target area after any step is 7,2:

# .............#....#............
# .......#..............#........
# ...............................
# S........................#.....
# ...............................
# ...............................
# ...........................#...
# ...............................
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTT#TT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT

# In this diagram, S is the probe's initial position, 0,0. The x coordinate increases to the right, and the y coordinate increases upward. In the bottom right, positions that are within the target area are shown as T. After each step (until the target area is reached), the position of the probe is marked with #. (The bottom-right # is both a position the probe reaches and a position in the target area.)

# Another initial velocity that causes the probe to be within the target area after any step is 6,3:

# ...............#..#............
# ...........#........#..........
# ...............................
# ......#..............#.........
# ...............................
# ...............................
# S....................#.........
# ...............................
# ...............................
# ...............................
# .....................#.........
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................T#TTTTTTTTT
# ....................TTTTTTTTTTT

# Another one is 9,0:

# S........#.....................
# .................#.............
# ...............................
# ........................#......
# ...............................
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTT#
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT
# ....................TTTTTTTTTTT

# One initial velocity that doesn't cause the probe to be within the target area after any step is 17,-4:

# S..............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# .................#.............................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT................................
# ....................TTTTTTTTTTT..#.............................
# ....................TTTTTTTTTTT................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ................................................#..............
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ...............................................................
# ..............................................................#

# The probe appears to pass through the target area, but is never within it after any step. Instead, it continues down and to the right - only the first few steps are shown.

# If you're going to fire a highly scientific probe out of a super cool probe launcher, you might as well do it with style. How high can you make the probe go while still reaching the target area?

# In the above example, using an initial velocity of 6,9 is the best you can do, causing the probe to reach a maximum y position of 45. (Any higher initial y velocity causes the probe to overshoot the target area entirely.)

# Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?

# Your puzzle answer was 11175.

# --- Part Two ---

# Maybe a fancy trick shot isn't the best idea; after all, you only have one probe, so you had better not miss.

# To get the best idea of what your options are for launching the probe, you need to find every initial velocity that causes the probe to eventually be within the target area after any step.

# In the above example, there are 112 different initial velocity values that meet these criteria:

# 23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
# 25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
# 8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
# 26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
# 20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
# 25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
# 25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
# 8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
# 24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
# 7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
# 23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
# 27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
# 8,-2    27,-8   30,-5   24,-7

# How many distinct initial velocity values cause the probe to be within the target area after any step?

# Your puzzle answer was 3540.

INPUT_PATH = './input/17.txt'
import re

class TargetArea:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.probe = None

    def __str__(self):  # displays an image of the target area and the trajectory of the last probe launch
        offsety = 0 if self.probe is None else max(map(lambda x: x[1],self.probe['motion']))
        targetPosx = (min([abs(self.x1), abs(self.x2)]), max([abs(self.x1), abs(self.x2)]))
        targetPosy = (offsety + min([abs(self.y1), abs(self.y2)]), offsety + max([abs(self.y1), abs(self.y2)]))

        maxx = targetPosx[1] + 1
        maxy = targetPosy[1] + 1

        grid = [['.']*maxx for _ in range(maxy)]
        grid[offsety][0] = 'S'
        for i in range(targetPosy[0], targetPosy[1] + 1):
            for j in range(targetPosx[0], targetPosx[1] + 1):
                grid[i][j] = 'T'
        if self.probe is not None:
            for i,j in self.probe['motion'][1:]:
                grid[-j+offsety][i] = '#'
        return ''.join(map(lambda x: ''.join(x)+'\n', grid))

    def fireProbe(self, velx, vely):
        self.probe = {'motion' : [], 'vel' : [velx,vely]}
        self.checkProbeTrajectory()
        print(self)

    def isWithin(self): # returns (True) if the last position of the trajectory is inside the target area, (False) if not, (None) if there is no trajectory
        if self.probe is None:
            return None
        x = self.probe['motion'][-1][0]
        y = self.probe['motion'][-1][1]
        return self.x1<=x<=self.x2 and self.y1<=y<=self.y2

    def checkProbeTrajectory(self): # calculates the trajectory of the input initial velocity
        if self.probe is None:
            return None
        x = y = 0
        while x <= max([abs(self.x1), abs(self.x2)]) and y >= min([self.y1, self.y2]):
            self.probe['motion'].append((x,y))
            x, y, self.probe['vel'][0], self.probe['vel'][1] = self.findNextStep(x, y, self.probe['vel'][0], self.probe['vel'][1])

    def findNextStep(self, x, y, velx, vely):   # calculate the next position in the trajectory
        x += velx
        y += vely
        if velx > 0:
            velx -= 1
        vely -= 1
        return x, y, velx, vely


def calculateYTrajectory(targetYCoordinates,vely) -> list:  # returns a list of ints, the steps in which the trajectory is inside the target area for the input Y velocity
    step = 0
    steps = []
    y = 0
    if vely > 0:    # if velY>0 calculate the steps to the highest position 
        tempvely = vely
        while tempvely != 0:
            y += tempvely
            tempvely -= 1
            step += 1
        step = step * 2 + 1 # and double it, because you need the same number of steps +1 to return at y = 0 
        y = 0
        vely = - vely - 1
    while y >= min(targetYCoordinates):
        if y <= max(targetYCoordinates):
            steps.append(step)
        y += vely
        vely -= 1
        step += 1
    return steps



with open(INPUT_PATH, 'r') as file:
    targetAreaCoordinates = list(map(lambda x: int(x), re.findall(r'(-?\d+)', file.readline())))
    # To display the path of a trajectory use the following two instructions. (velX and velY are initial velocity values)
    # targetArea = TargetArea(*targetAreaCoordinates)
    # targetArea.fireProbe(velX,velY)
    velYmax = max(abs(targetAreaCoordinates[2]),abs(targetAreaCoordinates[3])) - 1

    # PART 1
    ymax = 0
    steps = 0
    for i in range(velYmax, 0, -1):
        ymax += i
        steps+=1
    print(f'The highest Y position is {ymax} at the initial Y velocity of {velYmax}.')

    # PART 2
    maxStepsY = 0
    steps = {}  # for every step (key) the possibles initial velocity values {velY (y) and velX (x)} that cause the probe to hit the target area in that step. Ex.: steps = {'2':{'x':[1,2,3],'y':[4.7]}, '3':{'x':[],'y':[1,4]}}
    for velY in range(-velYmax-1, velYmax+1):   # calculates the initial Y velocity for every step
        hitSteps = calculateYTrajectory(targetAreaCoordinates[2:], velY)
        for s in hitSteps:
            if s > maxStepsY:
                maxStepsY = s
            steps[str(s)] = steps.get(str(s),{'x':[], 'y':[]})
            steps[str(s)]['y'].append(velY)

    velXmax = max(abs(targetAreaCoordinates[0]),abs(targetAreaCoordinates[1]))
    initVelCombinations = []
    for velX in range(velXmax+1):   # calculates the initial X velocity for every step
        x = 0
        initialVelX = velX
        for step in range(1,maxStepsY+1):
            x += velX
            if str(step) in steps and targetAreaCoordinates[0]<=x<=targetAreaCoordinates[1]:
                for j in steps[str(step)]['y']:
                    if (initialVelX,j) not in initVelCombinations:  # to avoid duplicates
                        initVelCombinations.append((initialVelX,j))
                steps[str(step)]['x'].append(initialVelX)
            if velX > 0:
                velX -= 1
    print(f'There are {len(initVelCombinations)} distinct initial velocity values that cause the probe to be within the target area after any step.')