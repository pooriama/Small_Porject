def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one([1, 4, 2]))


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i - 1] += 1
        else:
            break
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A
