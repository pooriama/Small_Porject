def Search_sorted_first_occurance(A, k):
    l, u = 0, len(A) - 1

    while l <= u:
        mid = (u - l) // 2
        if A[mid] == k:
            result = mid
            u = mid - 1
        elif A[mid] > k:
            u = mid - 1
        else:
            l = mid + 1
    return result
