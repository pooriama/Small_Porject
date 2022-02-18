def intersect_two_arry(A, B):
    i = 0
    j = 0
    result = []
    while (i < len(A) and j < len(B)):
        if A[i] == B[j] and A[i]!=A[i-1]:
            result.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1
    return result
A=[2,3,3,5,5,6,7,7,8,12]
B=[2,5,5,6,8,8,9,10,10]
print(intersect_two_arry(A,B))