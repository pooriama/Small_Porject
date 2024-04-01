def search_entry_equal_index(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = left + (right - left) // 2
        diffrence = A[mid] - mid
        if diffrence == 0:
            return mid
        elif diffrence > 0:
            right = mid - 1
        else:
            left = mid + 1
    return -1
