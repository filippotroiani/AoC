#Advent of code 13 dic
#--- Day 13: Knights of the Dinner Table ---

# In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

# You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

# For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.

# Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

# If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

#      +41 +46
# +55   David    -2
# Carol       Alice
# +60    Bob    +54
#      -7  +83

# After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

# What is the total change in happiness for the optimal seating arrangement of the actual guest list?

# Your puzzle answer was 733.

# --- Part Two ---

# In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

# So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

# What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

# Your puzzle answer was 725.

import re

# def DFS(k, valori, visited = []): # not optimize, it does the sum of the happiness level at the end of every combinationation
#     visited.append(k)
#     if len(visited) == len(valori):
#         tot = 0
#         for i in range(len(visited)):
#             tot += valori[visited[i-1]][visited[i]] + valori[visited[i]][visited[i-1]]
#         return tot
#     max = -10000
#     for key2 in valori:
#         if key2 not in visited:
#             tot = DFS(key2, valori, visited.copy())
#             if tot > max:
#                 max = tot
#     return max

INPUT_PATH = './input/13.txt'

def DFS(k, valori, visited = []):   # optimized, it does the sum of the happiness level step by step
    visited.append(k)
    if len(visited) == len(valori):
        max = valori[k][visited[0]] + valori[visited[0]][k]
    else:
        max = -10000
        for key2 in valori:
            if key2 not in visited:
                happiness = DFS(key2, valori, visited.copy())
                if happiness > max:
                    max = happiness
    return max + (valori[k][visited[-2]] + valori[visited[-2]][k] if len(visited) > 1 else 0)


with open(INPUT_PATH) as file:
    valori = {}
    for line in file:
        l = re.findall('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', line)
        if l[0][0] not in valori:
            valori[l[0][0]] = {}
        valori[l[0][0]][l[0][3]] = int(l[0][2]) if l[0][1] == 'gain' else - int(l[0][2])
    # part 1
    max= DFS(list(valori.keys())[0], valori, [])
    print(f'The total change in happiness for the optimal seating arrangement is {max}')
    # part 2
    me = {}        
    for key in valori:
        me[key] = 0
        valori[key]['me'] = 0
    valori['me'] = me
    max2 = DFS(list(valori.keys())[0], valori, [])
    
    print(f'the total change in happiness for the optimal seating arrangement that actually includes yourself is {max2}')
