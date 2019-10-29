
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

