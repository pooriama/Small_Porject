def solve(A, B):
    end = len(A) - 1
    summ = 0
    i = 0
    while B > 0:
        if A[i] < A[end]:
            summ = A[end] + summ
            end -= 1
        else:
            summ = A[i] + summ
            i += 1
        B -= 1
    return summ


A = [1, 2]
B = 1
print(solve(A,B))