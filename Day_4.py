'''
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 136760-595730.

Your puzzle answer was 1873.

--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?
'''
#range(136760-595730) given range (puzzle input)
list_range = [*range(136760, 595730)]

def ascending(pw):
    new_pw = []
    for x in pw:
        temp_pw = [int(a) for a in str(x)]
        if temp_pw == sorted(temp_pw):
            new_pw.append(temp_pw)
    return new_pw        

def same_digits(pw):
    pwds = []                       #pwds is passwords
    for x in pw:
        for i in range(0, len(x)-2):
            if x[i] == x[i+1] and x[i+1] == x[i+2]:
                #print(x[i], x[i+1], x[i+2], 's')
                continue
            if x[i] == x[i+1] and not x[i+1] == x[i+2]:
                #print(x[i], x[i+1], x[i+2])
                pw_set = [str(a) for a in x]
                pwds.append("".join(pw_set))
                break
                
    return pwds
    
def passwords(pw):
    new_list = ascending(pw)
    print(len(same_digits(new_list)))

temp = [112233, 123444, 111122]
passwords(temp)


#Part 1: Your puzzle answer was 1873.