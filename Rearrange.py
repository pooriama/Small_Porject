def rearrange(A):
    for i in range(len(A) - 1):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=i % 2)
    return A


A = [1, 3, 5, 6, 8, 3, 6, 7]
print(rearrange(A))
