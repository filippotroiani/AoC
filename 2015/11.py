# Advent of code 2015 11 dic
# --- Day 11: Corporate Policy ---

# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

#     Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
#     Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
#     Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

# For example:

#     hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
#     abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
#     abbcegjk fails the third requirement, because it only has one double letter (bb).
#     The next password after abcdefgh is abcdffaa.
#     The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle answer was hxbxxyzz.

# --- Part Two ---

# Santa's password expired again. What's the next one?

# Your puzzle answer was hxcaabcc.


import re
def increment(s):
    if s[-1] in ['h','k','n']:  # avoid the Is, Ls and Os to match the secondo requirement
        return s[:-1]+ chr(ord(s[-1]) + 2)
    if s[-1] == 'z':    # se la lettera da incrementare è z, la trasformo in a ed incremento la successiva
        return (increment(s[:-1]) if len(s)>1 else '') + 'a'    # se devo incrementare la prima lettera la trasformo in a e basta, perché non posso incrementare la successiva
    return s[:-1]+ chr(ord(s[-1]) + 1)

def newPassword(psw):
    while True:
        firstRequirement = thirdRequirement = False
        psw = increment(psw)
        for i in range(len(psw)-2):
            if psw[i+1] == chr(ord(psw[i]) + 1) and psw[i+2] == chr(ord(psw[i]) + 2):
                firstRequirement = True
        if len(re.findall(r'(.)\1{1}',psw)) > 1:
            thirdRequirement = True
        if firstRequirement and thirdRequirement:
            break
    return psw

psw = 'hxbxwxba'
psw = newPassword(psw)
print(f'Your next password is {psw}')
psw = newPassword(psw)
print(f'and the next one will be {psw}')