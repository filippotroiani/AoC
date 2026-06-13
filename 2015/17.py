"""Advent of Code 2015 Day 17
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

Your puzzle answer was 654.

--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

Your puzzle answer was 57.
"""


import logging
import os
import time
import tracemalloc
from collections import Counter

logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

SCRIPT_DIR = os.path.dirname(__file__)
INPUT_PATH = f'input/{os.path.basename(__file__).split(".")[0][:2]}.txt'  # 'input/<day_number>.txt'

TOTAL_EGGNOG_LITERS = 150

def solve(container_sizes: list[int]) -> tuple[int, tuple[int,int]]:
    total_container_num = len(container_sizes)
    container_sizes = sorted(container_sizes)
    counts_per_containers_num = Counter()
        
    def find_combinations(starting_index: int, remaining_liters: int, containers_count: int) -> int:
        found_combinations = 0
        index = starting_index
        while index < total_container_num:
            container = container_sizes[index]
            if container == remaining_liters:
                # found a combination of containers that fits TOTAL_EGGNOG_LITERS
                found_combinations+=1
                # update the count for this number of containers
                counts_per_containers_num[containers_count+1] += 1
            elif container > remaining_liters:
                # the array is sorted so if this is too big we can skip the remaining containers
                break
            elif index + 1 < total_container_num:
                # if there are others element to explore
                found_combinations += find_combinations(index+1, remaining_liters - container, containers_count+1)
            index += 1
        return found_combinations
    
    found_combinations = find_combinations(0, TOTAL_EGGNOG_LITERS, 0)
    min_combination_num = min(counts_per_containers_num.keys())
    return found_combinations, (min_combination_num, counts_per_containers_num[min_combination_num])


def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_PATH)
    with open(input_file, 'r') as file:
        container_sizes = [int(line) for line in file.readlines()]
    
    part1_result, part2_result = solve(container_sizes)
    print(f"Part 1 result: {part1_result}")
    print(f"Part 2 result: min num of containers {part2_result[0]}, found {part2_result[1]} times ")


if __name__ == '__main__':
    tracemalloc.start()
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    logger.info('Execution time: %0.4f seconds', t2 - t1)
    logger.info('Peak memory usage: %0.2f KB', peak / 1024)