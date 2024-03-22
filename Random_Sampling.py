import random


def random_sampling(k, A):
    for i in range(k):
        randnum = random.randint(i, len(A) - 1)
        A[randnum], A[i] = A[i], A[randnum]
    return A[:k]


def random_sampling(A, k):
    n = len(A)-1
    for i in range(0, k):
        randnum = random.randint(i, n)
        A[randnum], A[i] = A[i], A[randnum]
    return A[:k]
