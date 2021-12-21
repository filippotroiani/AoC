# Advent of code 2015 9 dic
# --- Day 9: All in a Single Night ---

# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141

# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982

# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

# Your puzzle answer was 141.

# --- Part Two ---

# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

# Your puzzle answer was 736.

import re


def DFS(node, graph, visited = [], mode = 'min'):
    visited.append(node)
    if len(graph) == len(visited):
        print
    if mode == 'min':
        minDistance = 10000000
    else:   # mode == 'max'
        minDistance = -1
    for nextNode in graph[node]:
        if nextNode not in visited:
                distance = graph[node][nextNode] + DFS(nextNode, graph, visited.copy(), mode)
                if (mode == 'min' and distance < minDistance) or (mode == 'max' and distance > minDistance):
                    minDistance = distance
    if (mode == 'min' and minDistance < 10000000) or (mode == 'max' and minDistance > - 1):          
        return minDistance
    return 0


graph = {}
with open('input/09.txt', 'r') as file:
    for line in file:
        route = re.findall('(\w*) to (\w*) = (\d+)',line.strip())
        if route[0][0] not in graph:
            graph[route[0][0]] = {}
        if route[0][1] not in graph:
            graph[route[0][1]] = {}
        graph[route[0][1]][route[0][0]] = graph[route[0][0]][route[0][1]] = int(route[0][2])
minDistance = 10000000
for start in graph:
    distance = DFS(start, graph, [])
    if distance < minDistance:
        minDistance = distance
print('The distance of the shortest route is', minDistance)
maxDistance = -1
for start in graph:
    distance = DFS(start, graph, [], 'max')
    if distance > maxDistance:
        maxDistance = distance
print('The distance of the longest route is', maxDistance)

    