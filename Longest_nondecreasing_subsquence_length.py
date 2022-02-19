def longest_length(A):
    result = [1] * len(A)
    for i in range(1, len(A)):
        result[i] = max(1 + max([result[j] for j in range(0, i) if A[j] <= A[i]]), result[i])
    return max(result)


A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
print(longest_length(A))
