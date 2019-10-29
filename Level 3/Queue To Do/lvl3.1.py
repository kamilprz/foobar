
# This implementation was too slow, so I rewrote it in Java
# Java implementation, though the same code, is faster :~)

start = 0
length = 5


def solution(start, length):
    # Your code here
    current = start
    tmpLength = length
    checksum = 0

    while tmpLength > 0:
        for i in range(current, current + tmpLength):
            checksum ^= i
        current += length
        tmpLength -= 1

    return checksum


print(solution(start, length))
