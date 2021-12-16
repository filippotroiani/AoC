#Advent of code 13 dic

import re

def DFS(valori, visited,k):
    # print(f'si siede {k}')
    visited.append(k)
    if len(visited) == len(valori):
        # print(f'sono tutti a tavola {visited} ritorno')
        tot = 0
        for i in range(1,len(visited)):
            tot += valori[visited[i-1]][visited[i]] + valori[visited[i]][visited[i-1]]
        tot += valori[visited[0]][visited[-1]] + valori[visited[-1]][visited[0]]
        return tot, visited.copy()
    global max
    max = -10000000
    maxL = []
    i = 1
    for k2 in valori:
        # print(f'{i}a tavola ci sono {visited}')
        # print(f'controllo {k2}')
        i+=1
        if k2 not in visited:
            tot,l = DFS(valori, visited.copy(),k2)
            if tot > max:
                max = tot
                maxL = l.copy()
        # else:
        #     print(f'{k2} si è già seduto {visited}')
    # print(f'il mio lavoro è finito, ritorno')
    return max,maxL.copy()


with open('input/13.txt') as file:
    valori = {}
    for line in file:
        l = re.findall('(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', line)
        if l[0][0] not in valori.keys():
            valori[l[0][0]] = {}
        valori[l[0][0]][l[0][3]] = int(l[0][2]) if l[0][1] == 'gain' else - int(l[0][2])
    # max = -10000000
    maxL = []
    for k in valori:
        tot,l = DFS(valori, [],k)
        if tot > max:
            max = tot
            maxL = l.copy()
    print(max,maxL)
    print (valori)

