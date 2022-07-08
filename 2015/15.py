# Advent of Code 2015
# --- Day 15: Science for Hungry People ---

# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

#     capacity (how well it helps the cookie absorb milk)
#     durability (how well it keeps the cookie intact when full of milk)
#     flavor (how tasty it makes the cookie)
#     texture (how it improves the feel of the cookie)
#     calories (how many calories it adds to the cookie)

# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

#     A capacity of 44*-1 + 56*2 = 68
#     A durability of 44*-2 + 56*3 = 80
#     A flavor of 44*6 + 56*-2 = 152
#     A texture of 44*3 + 56*-1 = 76

# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

# Your puzzle answer was 21367368.
# --- Part Two ---

# Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?

# Your puzzle answer was 1766400.

import os
import time
import logging
import re
from itertools import permutations

logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
SCRIPT_DIR = os.path.dirname(__file__)
INPUT_PATH = f'input/{os.path.basename(__file__).split(".")[0]}.txt'    # 'input/<day_number>.txt'
MAXSPOONS = 100
MAXCALORIES = 500
    
def calcCombinations(MAXSPOONS: int, n: int) -> list:   # returns a list of combinations of recepes that respect the condition sum of teasspoons = 100
    return [perm for perm in permutations(range(MAXSPOONS + 1), n) if sum(perm) == MAXSPOONS]   # list(filter(lambda x: sum(x)<=MAXSPOONS, permutations([i for i in range(MAXSPOONS + 1)]*n,n)))

def calculateMaxTotScore(ingredientsList = []) -> int:  # returns maxTotScore for part 1 and maxTotScorePart2 for part 2
    # quantities = [44,56]  # example quantities
    maxTotScore = maxTotScorePart2 = 0
    combs = calcCombinations(MAXSPOONS, len(ingredientsList))
    for quantities in combs:
        newTotScore = calculateTotScore(ingredientsList, quantities)
        if newTotScore > maxTotScore:
            maxTotScore = newTotScore
        if calculateCalories(ingredientsList, quantities) == MAXCALORIES and newTotScore > maxTotScorePart2:
            maxTotScorePart2 = newTotScore
    return maxTotScore, maxTotScorePart2

def calculateTotScore(ingredientsList: list, quantities = list) -> int: # given the recipe (quantities) returns the total score
    totScore = 1
    for propertyIndex in range(len(ingredientsList[0]) - 1):   # for every property except (calories the last one)
        propScore = 0
        for ingredientIndex, ingredient in enumerate(ingredientsList):
            propScore += ingredient[propertyIndex] * quantities[ingredientIndex]
        if propScore <= 0: return 0
        totScore *= propScore
    return totScore

def calculateCalories(ingredientsList: list, quantities: list) -> int:  # given the recipe (quantities) returns the calories of that combination
    totCalories = 0
    for ingredientIndex, quantity in enumerate(quantities):
        totCalories += ingredientsList[ingredientIndex][-1] * quantity
    return totCalories

def main():
    input_file = os.path.join(SCRIPT_DIR, INPUT_PATH)
    with open(input_file, 'r') as file:
        report = file.readlines()
    ingredientsList = []
    for ingredient in report:
        ingredientsList.append(list(map(int, re.findall("(-?\d+)", ingredient))))
    maxTotScore, maxTotScorePart2 = calculateMaxTotScore(ingredientsList)
    print(f'The award-winning cookie has a total score of {maxTotScore}.\nThe best cookie with a 500 calories has a total score of {maxTotScorePart2}.')
    
if __name__ == '__main__':
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    logger.info('Execution time: %0.4f seconds', t2 - t1)