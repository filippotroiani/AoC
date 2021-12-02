# Advent of code 2021 2 dic

import re
with open('input/02.txt') as f:
    horPosition = depth = 0
    depth2 = aim = 0
    for line in f:
        command = re.findall(r'(\w+) (\d+)', line)
        match command[0][0]:
            case 'forward':
                horPosition += int(command[0][1])
                depth2 += aim * int(command[0][1])
            case 'up':
                depth -= int(command[0][1])
                aim -= int(command[0][1])
            case 'down':
                depth += int(command[0][1])
                aim += int(command[0][1])
    print(f'Results:\nPart 1: {horPosition*depth}\nPart 2: {horPosition*depth2}')
