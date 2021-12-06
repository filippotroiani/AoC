# Advent of Code 2021 4 dic
# --- Day 4: Giant Squid ---

# You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

# Maybe it wants to play bingo?

# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

# The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7

# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# Finally, 24 is drawn:

# 22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#  8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
# 21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#  6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#  1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

# At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

# The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

# To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

# Your puzzle answer was 54275.

# --- Part Two ---

# On the other hand, it might be wise to try a different strategy: let the giant squid win.

# You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

# In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

# Figure out which board will win last. Once it wins, what would its final score be?

# Your puzzle answer was 13158.

def calculatePoints(board, marked, num):
    points = 0
    for y,row in enumerate(marked):
        for x,element in enumerate(row):
            if element == 0:
                points += int(board[y][x])
    points *= int(num)
    return points

def checkNum(boards, markedBoards, num):
    for b, board in enumerate(boards):
        for y,row in enumerate(board):
            try:
                x = row.index(str(num))
                markedBoards[b][y][x] = 1
                count = 0
                for i in range(5):
                    if markedBoards[b][i][x] == 1:
                        count += 1
                if count >= 5 or markedBoards[b][y].count(1) >= 5:
                    return calculatePoints(board, markedBoards[b], num)
            except:
                continue
    return -1

def findLoser(boards, markedBoards, boardsPlaying, num):
    for b, board in enumerate(boards):
        if b in boardsPlaying:
            for y,row in enumerate(board):
                try:
                    x = row.index(str(num))
                    markedBoards[b][y][x] = 1
                    count = 0
                    for i in range(5):
                        if markedBoards[b][i][x] == 1:
                            count += 1
                    if count >= 5 or markedBoards[b][y].count(1) >= 5:
                        if len(boardsPlaying) == 1:
                            return calculatePoints(boards[b], markedBoards[b], num)
                        else:
                            boardsPlaying.remove(b)
                except:
                    continue
    return -1


import re
with open('input/04.txt') as file:
    nums = re.findall(r'(\d+)',file.readline())
    boards = []
    markedBoards = []
    for line in file:
        board = []
        for i in range(5):
            board.append(re.findall(r'(\d+)',file.readline()))
        markedBoards.append([[0]*5 for col in range(5)])
        boards.append(board)
    boardsPlaying = [*range(len(boards))]
    try:
        for num in nums:
            points = checkNum(boards, markedBoards, num)  # part 1
            # points = findLoser(boards, markedBoards, boardsPlaying, num)    # part 2
            if points != -1:
                print(f'the winner board got {points} points.')   # part 1
                # print(f'the loser board got {points} points.')  # part 2
                break
    except:
        print('Errore.')

