# Advent of Code 2015 10 dic
# --- Day 10: Elves Look, Elves Say ---

# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

# For example:

#     1 becomes 11 (1 copy of digit 1).
#     11 becomes 21 (2 copies of digit 1).
#     21 becomes 1211 (one 2 followed by one 1).
#     1211 becomes 111221 (one 1, one 2, and two 1s).
#     111221 becomes 312211 (three 1s, two 2s, and one 1).

# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

# Your puzzle answer was 492982.

# --- Part Two ---

# Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

# Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

# Your puzzle answer was 6989950.


import re
line = '1321131112'
for i in range(40): #50 for part 2
    search = re.findall(r'(\d)(\1*)', line) # genero una lista del tipo [(carattere,ripetizioniDiCarattere)] [('1', ''), ('3', ''), ('2', ''), ('1', '1'), ('3', ''), ('1', '11'), ('2', '')]
    line = ''
    # result = list(map(lambda x: x[0]+x[1], search))    # concateno il carattere trovato alle sue ripetizioni per ogni carattere trovato ['1', '3', '2', '11', '3', '111', '2']
    # for c in result:
    #     line += str(len(c))+c[0]
    # oppure
    for c in search:
        line += str(len(c[0]+c[1]))+c[0]
print(f'Ho {len(line)} cifre.')