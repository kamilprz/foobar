# Queue To Do

start = 0
length = 5

# def solution(start, length):
#     # Your code here
#     current = start
#     tmpLength = length
#     ids = []
#
#     for i in range(length):
#         ids = ids + list(range(current, current + tmpLength))
#         current = current + length
#         tmpLength -= 1
#
#     res = start
#     print(ids)
#     for i in ids[1:]:
#         res = res ^ i
#
#     return res

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
