def Search_Cyclically_Sorted(A):
    left, right = 0, len(A) - 1

    while (left < right):
        mid = (right + left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        elif A[mid] < A[right]:
            right = mid
    return left
