
def solution(xs):
    # Your code here
    if len(xs) == 1:
        return str(xs[0])

    xs.sort()
    # eliminates the zeros
    xs = list(filter(lambda x: x != 0, xs))
    # counts how many negative numbers
    negativeCount = sum(1 for i in xs if i < 0)

    if negativeCount % 2 != 0:
        # remove the largest negative number
        xs.remove(max([x for x in xs if x < 0]))

    if not xs:
        return "0"

    maxEnergy = 1
    for x in xs:
        maxEnergy *= x

    return str(maxEnergy)


arr = [0]
print(solution(arr))
