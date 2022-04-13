


def binary_search(t,A):
    L, U = 0, len(A) - 1


    while L <= U:
        M= L + (U-L)/2
        if t ==A[M]:
            return M
        elif t < A[M]:
            U= M-1
        else:
            L = M+1

    return -1


