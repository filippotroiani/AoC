#Advent of code 2015 5 dic
# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

# Your puzzle answer was 258.
# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

# Your puzzle answer was 53.

INPUT_PATH = 'input/05.txt'

def isNice1(line):
    chprec = ' '
    vocali = 0
    good2 = False
    good3 = True
    for ch in line:
        if ch in ['a','e','i','o','u']:
            vocali += 1
        if ch == chprec:
            good2 = True
        if chprec+ch in ['ab','cd','pq','xy']:
            good3 = False
            break
        chprec = ch
    if vocali >= 3 and good2 and good3:
        return True
    return False
def isNice2(line):
    chprec = ' '
    chprecprec = ' '
    good1 = False
    good2 = False
    for ch in line:
        if ch == chprecprec:
            good1 = True
        if  not good2 and line.count(chprec+ch)>=2: #oppure chprec+ch in line.replace(chprec+ch,'  ',1):
            good2 = True
        chprecprec = chprec
        chprec = ch
    if good1 and good2:
        return True
    return False

count1 = 0
count2 = 0
with open(INPUT_PATH) as file:
    for line in file:
        if isNice1(line):
            count1 += 1
        if isNice2(line):
            count2 += 1
print(f'(parte 1) il numero delle parole buone ??: {count1}')
print(f'(parte 2) il numero delle parole buone ??: {count2}')