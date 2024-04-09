from collections import namedtuple

MinMax = tuple("MinMax", ("smallest", "largest"))


def find_min_max(A):
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    result = min_max(A[0], A[1])
    for i in range(2, len(A) - 1, 2):
        localMinMax = min_max(A[i], A[i + 1])
        result = MinMax(min(localMinMax.smallest, result.smallest), max(localMinMax.largest, result.largest))

    if len(A) % 2:
        result = MinMax(min(result.smallest, A[-1]), max(result.largest, A[-1]))

    return result
