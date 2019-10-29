# This implementation uses the numpy library, it got the right answers however failed tests, most likely due to speed

from __future__ import division

# import numpy.matlib
import numpy as np


from itertools import compress
import fractions
from fractions import Fraction


# Test cases. Uncomment a single test case to use it as the input to the
# answer method. Each test case is a 2d array, m, which represents a given
# transition matrix for a Markov chain

# Case 1. Expected output: [7, 6, 8, 21]

# m = [
#           [0, 2, 1, 0, 0],
#           [0, 0, 0, 3, 4],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0]
#     ]

# Case 2. Expected output: [0, 3, 2, 9, 14]

m = [
      [0, 1, 0, 0, 0, 1],
      [4, 0, 0, 3, 2, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0]
    ]

# Case 3. Expected output: [1, 2, 3]
# m = [
#         [1, 2, 3, 0, 0, 0],
#         [4, 5, 6, 0, 0, 0],
#         [7, 8, 9, 1, 0, 0],
#         [0, 0, 0, 0, 1, 2],
#         [0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]
#     ]

# Case 4. Expected output: [1, 1]
# m = [
#         [0]
#     ]

# Case 5. Expected output: [1, 2, 3, 4, 5, 15]
# m = [
#         [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
#         [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
#         [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
#         [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]

# Case 6. Expected output: [4, 5, 5, 4, 2, 20]
# m = [
#         [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
#         [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
#         [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
#         [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
#         [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]

# Case 7. Expected output: [1, 1, 1, 1, 1, 5]
# m = [
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]

# Case 8. Expected output: [2, 1, 1, 1, 1, 6]
# m = [
#         [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]

# Case 9. Expected output = [6, 44, 4, 11, 22, 13, 100]
# m = [
#         [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
#         [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
#         [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
#         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]

# Case 10. Expected output = [1, 1, 1, 2, 5]
# m = [
#         [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
#         [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
#         [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
#         [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
#         [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]


def convertMatrix(transMatrix):
    probMatrix = []

    for i in range(len(transMatrix)):
        row = transMatrix[i]
        newRow = []
        rowSum = sum(transMatrix[i])

        if all([v == 0 for v in transMatrix[i]]):
            for j in transMatrix[i]:
                newRow.append(0)

            # create identity matrix
            # newRow[i] = 1
            probMatrix.append(newRow)

        else:
            for j in transMatrix[i]:
                newRow.append(j / rowSum)

            probMatrix.append(newRow)

    return probMatrix


def terminalStateFilter(matrix):
    terminalStates = []

    for row in range(len(matrix)):

        if all(x == 0 for x in matrix[row]):
            terminalStates.append(True)

        else:
            terminalStates.append(False)

    return terminalStates


def standardForm(m):
    term = []
    nonTerm = []
    for row in range(len(m)):
        if all(x == 0 for x in m[row]):
            term.append(m[row])
        else:
            nonTerm.append(m[row])
    standardM = term + nonTerm
    return standardM


def solution(m):
    if len(m) == 1:
        return [1, 1]

    probMatrix = convertMatrix(m)

    standardMProb = standardForm(probMatrix)
    terminalStates = terminalStateFilter(standardMProb)
    nonTerminalCount = len(list(filter(lambda x: x is False, terminalStates)))

    Q = []
    R = []
    for i, x in enumerate(terminalStates):
        if not x:
            Q.append(standardMProb[i][0:nonTerminalCount])
            R.append(standardMProb[i][nonTerminalCount:])

    Q = np.matrix(Q)
    R = np.matrix(R)

    # print("Q {0}".format(Q))
    # print("R {0}".format(R))

    I = np.identity(nonTerminalCount)

    F_tmp = np.subtract(I, Q)
    # print(F_tmp)
    F = np.linalg.inv(F_tmp)
    # print(F)
    limiting_matrix = np.matmul(F, R)
    # print(limiting_matrix)

    probVector = np.matrix.tolist(limiting_matrix[0])
    probVector = probVector[0]

    numerators = []
    for i in probVector:
        numerator = fractions.Fraction(i).limit_denominator().numerator
        numerators.append(numerator)

    denominators = []
    for i in probVector:
        denominator = fractions.Fraction(i).limit_denominator().denominator
        denominators.append(denominator)

    factors = [max(denominators) / x for x in denominators]
    numeratorsTimesFactors = [a * b for a, b in zip(numerators, factors)]
    terminalStateNumerators = list(compress(numeratorsTimesFactors, terminalStates))

    # append numerators and denominator to answerList
    answerlist = list(map(int, terminalStateNumerators))
    answerlist.append(max(denominators))

    return answerlist


print(solution(m))

