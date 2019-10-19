# Please Pass the Coded Messages
# ==============================
#
# You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.
#
# You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

from itertools import combinations


def solution(l):
    # Your code here
    l.sort(reverse=True)
    for i in reversed(range(1, len(l) + 1)):
        for comb in list(combinations(l, i)):
            if sum(comb) % 3 == 0:
                return int(''.join(map(str, comb)))
    return 0


array = [3, 1, 4, 1, 5, 9]
print(solution(array))

jaeff = list(combinations(array, 3))

for i in reversed(range(1, len(array))):
    print(array[i])

for i in reversed(range(1, len(array))):
    for x in list(combinations(array, i)):
        print(x)

