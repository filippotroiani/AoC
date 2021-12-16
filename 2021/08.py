# Advent of Code 2021 08 dic
# --- Day 8: Seven Segment Search ---

# You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

# As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

# Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

# The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

# So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

# For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

# For example, here is what you might see in a single entry in your notes:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf

# (The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

# Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

# For now, focus on the easy digits. Consider this larger example:

# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
# fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
# cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
# efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
# gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
# cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
# ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
# gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
# fgae cfgab fg bagce

# Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

# In the output values, how many times do digits 1, 4, 7, or 8 appear?

# Your puzzle answer was 381.
# --- Part Two ---

# Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:

# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf

# After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:

#  dddd
# e    a
# e    a
#  ffff
# g    b
# g    b
#  cccc

# So, the unique signal patterns would correspond to the following digits:

#     acedgfb: 8
#     cdfbe: 5
#     gcdfa: 2
#     fbcad: 3
#     dab: 7
#     cefabd: 9
#     cdfgeb: 6
#     eafb: 4
#     cagedb: 0
#     ab: 1

# Then, the four digits of the output value can be decoded:

#     cdfeb: 5
#     fcadb: 3
#     cdfeb: 5
#     cdbaf: 3

# Therefore, the output value for this entry is 5353.

# Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:

#     fdgacbe cefdb cefbgd gcbe: 8394
#     fcgedb cgb dgebacf gc: 9781
#     cg cg fdcagb cbg: 1197
#     efabcd cedba gadfec cb: 9361
#     gecf egdcabf bgf bfgea: 4873
#     gebdcfa ecba ca fadegcb: 8418
#     cefg dcbef fcge gbcadfe: 4548
#     ed bcgafe cdgba cbgef: 1625
#     gbdfcae bgc cg cgb: 8717
#     fgae cfgab fg bagce: 4315

# Adding all of the output values in this larger example produces 61229.

# For each entry, determine all of the wire/segment connections and decode the four-digit output values. What do you get if you add up all of the output values?

# Your puzzle answer was 1023686.

def part1(outputDigits):
    count = 0
    for digit in outputDigits:
            if len(digit) in [2,3,4,7]:
                count += 1
    return count

def removeFromString(s, r):
    return ''.join(list(filter(lambda c: c not in r, s)))

def commonSignals(s1, s2):
    return ''.join(list(filter(lambda c: c in s1, s2)))

def filterDigitsInSet(filt, s, condition = None):
    if condition is None:
        condition = len(filt)
    return list(filter(lambda d: len(commonSignals(d,filt)) == condition, s))[0]

def decryptOutputValue(encryptedDigits, outputDigits):
    digits = ['']*10
    fiveSegmentDigits = []
    sixSegmentDigits = []
    for digit in encryptedDigits:
        match len(digit):
            case 2: # 1 is the only 2-segment digit
                digits[1] = ''.join(sorted(digit))
            case 3: # 7 is the only 3-segment digit
                digits[7] = ''.join(sorted(digit))
            case 4: # 4 is the only 4-segment digit
                digits[4] = ''.join(sorted(digit))
            case 7: # 8 is the only 7-segment digit
                digits[8] = ''.join(sorted(digit))
            case 5:
                fiveSegmentDigits.append(''.join(sorted(digit)))
            case 6:
                sixSegmentDigits.append(''.join(sorted(digit)))
    ef = removeFromString(digits[4], digits[1])   # or four.replace(ab[0],'').replace(ab[1],'')
    d = removeFromString(digits[7], digits[1])
    # find 3 in 5-segment digits 
    digits[3] = filterDigitsInSet(digits[1], fiveSegmentDigits)
    fiveSegmentDigits.remove(digits[3])
    cf = removeFromString(digits[3], digits[7])
    f = commonSignals(ef, cf)
    # find 0 in 6-segment digits
    digits[0] = filterDigitsInSet(f, sixSegmentDigits, 0)
    sixSegmentDigits.remove(digits[0])
    # find 9 in remaining 6-segment digits 
    digits[9] = filterDigitsInSet(digits[1], sixSegmentDigits)
    sixSegmentDigits.remove(digits[9])
    # the last element in 6-segment digits is 6
    digits[6] = sixSegmentDigits[0]
    e = removeFromString(ef, f)
    # find 5 in remaining 5-segment digits 
    digits[5] = filterDigitsInSet(e, fiveSegmentDigits)
    fiveSegmentDigits.remove(digits[5])
    # the last element in 5-segment digits is 2
    digits[2] = fiveSegmentDigits[0]
    # now assemble the number
    num = ''
    for digit in outputDigits:
        num += str(digits.index(''.join(sorted(digit))))
    return int(num)
                

with open('input/08.txt') as file:
    count = 0
    sum = 0
    for line in file:
        dLine = line.split('|')
        digits = dLine[0].split()
        outputDigits = dLine[1].split()
        count += part1(outputDigits)
        sum += decryptOutputValue(digits, outputDigits)
    print(f'The digits 1, 4, 7 and 8 apear {count} times.')
    print(f'The sum of the output values is {sum}.')