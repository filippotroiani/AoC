"""Advent of Code 2024
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a 
device and pushes the only button on it. After a brief flash, you recognize
the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station 
tugs on your shirt; she'd like to know if you could help her with her word 
search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written 
backwards, or even overlapping other words. It's a little unusual, though, as 
you don't merely need to find one instance of XMAS - you need to find all of 
them. Here are a few ways XMAS might appear, where irrelevant characters have 
been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word 
search again, but where letters not involved in any XMAS have been replaced 
with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search. How many times does XMAS appear?

Your puzzle answer was 2468.

--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this 
isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed 
to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. 
Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have 
been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side
and try again. How many times does an X-MAS appear?

Your puzzle answer was 1864.
"""


import logging
import os
import time
from typing import List


logging.basicConfig(
    format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_PATH = f'input/{os.path.basename(__file__).split(".")[0][:2]}.txt'  # 'input/<day_number>.txt'

XMAS_WORD = 'XMAS'
_xmas_end_state = XMAS_WORD.__len__()
_directions = [
    (-1, 0),
    (-1, +1),
    (0, +1),
    (+1, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
    (-1, -1)
]


def xmas_word_search(report: List[str]) -> int:
    """Part 1.
    Searches for XMAS through the entire report. Vertically, horizontally and diagonally.
    """
    word_count = 0
    for y, line in enumerate(report):
        for x, char in enumerate(line):
            if char is XMAS_WORD[0]:
                word_count += _find_all_xmas_from_point(report, x, y)
    return word_count


def _find_all_xmas_from_point(report: List[str], x: int, y: int) -> int:
    xmasCount = 0
    for direction in _directions:
        if _explore(report, x, y, direction, 1):
            xmasCount += 1
    
    return xmasCount


def _explore(report: List[str], x: int, y: int, direction: tuple[int,int], state: int = 0) -> bool:
    (x, y) = tuple(map(sum, zip((x, y), direction)))
    
    if x < 0 or y < 0 or x >= report[0].__len__() or y >= report.__len__():
        return False  # out of bounds
    
    if report[y][x] is not XMAS_WORD[state]:
        return False
    
    state += 1
    
    if state is _xmas_end_state:
        return True
    return _explore(report, x, y, direction, state)


def x_word_search(report: List[str]) -> int:
    """Part 2.
    Searches for X shaped MAS through the entire report.
    """
    x_count = 0
    for y, line in enumerate(report[1:-1]):  # ignores first and last line
        for x, char in enumerate(line[1:-1]):  # ignores first and last character
            if char == 'A' and check_x_shaped_mas(report, x+1, y+1):  # +1 to adjust enumerators
                x_count += 1
    return x_count


def check_x_shaped_mas(report: List[str], x_origin: int, y_origin: int) -> bool:
    return _check_diagonal(report, x_origin, y_origin, (1, 1)) and \
        _check_diagonal(report, x_origin, y_origin, (1, -1))


def _check_diagonal(report: List[str], x_origin: int, y_origin: int, direction: tuple[int, int]) -> bool:
    (x1, y1) = tuple(map(sum, zip((x_origin, y_origin), direction)))
    (x2, y2) = tuple(map(sum, zip((x_origin, y_origin), 
                                  tuple(map((-1).__mul__, direction)))))
    if report[y1][x1] == 'M' and report[y2][x2] == 'S' or \
        report[y1][x1] == 'S' and report[y2][x2] == 'M':
        return True
    return False


def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_PATH)
    with open(input_file, 'r') as file:
        report = file.read().split('\n')
    result_part_1 = xmas_word_search(report)
    print('Part 1 result ', result_part_1)
    result_part_2 = x_word_search(report)
    print('Part 2 result ', result_part_2)
    
    
if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info('Execution time: %0.4f seconds', t2 - t1)
