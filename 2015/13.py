#Advent of code 13 dic

import re

def DFS(valori, visited):
    if len(visited) == len(valori):
        return valori[visited[0]][visited[-1]] + valori[visited[-1]][visited[0]]
    max = -1000000
    for k in valori:
        if k not in visited:
            visited.append(k)
            tot = DFS(valori, visited.copy()) + valori[visited[-2]][visited[-1]] + valori[visited[-1]][visited[-2]]
            if tot > max:
                max = tot
    return max


with open('input/13.txt') as file:
    valori = {}
    for line in file:
        l = re.findall('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', line)
        if l[0][0] not in valori.keys():
            valori[l[0][0]] = {}
        valori[l[0][0]][l[0][3]] = int(l[0][2]) if l[0][1] == 'gain' else - int(l[0][2])
    max = -10000000
    for k in valori:
        tot = DFS(valori, [k].copy())
        if tot > max:
            max = tot
    print(max)

