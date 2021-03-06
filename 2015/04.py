#Advent of code 2015 4 dic
# --- Day 4: The Ideal Stocking Stuffer ---

# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

# For example:

#     If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
#     If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

# Your puzzle answer was 117946.
# --- Part Two ---

# Now find one that starts with six zeroes.

# Your puzzle answer was 3938038.

import hashlib
INPUT_PATH = 'input/04.txt'
PART = 1    # 1 for part 1 or 2 for part 2

skey = ''
with open(INPUT_PATH) as f:
    skey = f.read().strip()
# skey = 'ckczppom'
for num in range(1,4000000):
    str2hash = skey+str(num)  # formo la stringa da hashare
    result = hashlib.md5(str2hash.encode())
    hexresult = result.hexdigest()    # trasformo in esadecimale
    #print(num,' -> ',hexresult)
    if PART == 1 and '00000' == hexresult[0:5] or PART == 2 and '000000'==hexresult[0:6]:
        print(f'TROVATO!! il numero è: {num}')
        break