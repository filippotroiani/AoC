"""Advent of Code 2015 Day 18
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.
The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......
After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

Your puzzle answer was 768.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life. At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#
After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?
"""


from itertools import product
import logging
import os
import utility

logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_PATH = f'input/{os.path.basename(__file__).split(".")[0][:2]}.txt'  # 'input/<day_number>.txt'

STEPS_NUMBER = 100

def display_grid(grid: list[list[bool]], step:int = -1):
    if step >= 0:
        print('Step', step)
    for row in grid:
        print(*['#' if e else '.' for e in row])

def process_step(grid: list[list[bool]]) -> list[list[bool]]:
    grid_dimension = len(grid)
    next_grid = [[False] * grid_dimension for _ in range(grid_dimension)]
    for y,row in enumerate(grid):
        for x,el in enumerate(row):
            neighbors_count = count_neighbors(grid, x,y)
            if el and neighbors_count == 2 or neighbors_count == 3:
                next_grid[y][x] = True
    return next_grid


def count_neighbors(grid: list[list[bool]], x: int, y:int) -> int:
    grid_dimension = len(grid)
    neighbors_count = 0
    for i,j in product([-1,1,0], [-1,1,0]):
        if (j,i)!=(0,0) and x+i>=0 and x+i<grid_dimension and y+j>=0 and y+j<grid_dimension:
            if grid[y+j][x+i]:
                neighbors_count+=1
    return neighbors_count

def solve(grid: list[str]) -> int:
    converted_grid = convert_grid(grid)
    for i in range(STEPS_NUMBER):
        converted_grid = process_step(converted_grid)
        # display_grid(converted_grid, i + 1)
        # print()
    
    on_count = 0
    for row in converted_grid:
        on_count += row.count(True)
    return on_count

def convert_grid(grid: list[str]) -> list[list[bool]]:
    converted_grid:list[list[bool]] = []
    for line in grid:
        converted_grid.append([])
        for c in line:
            if c == '#':
                converted_grid[-1].append(True)
            else:
                converted_grid[-1].append(False)
    return converted_grid

def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_PATH)
    with open(input_file, 'r') as file:
        grid = file.read().splitlines()
    part1_result = solve(grid)
    print('Part 1 result:', part1_result)


if __name__ == '__main__':
    utility.monitor_execution(main)