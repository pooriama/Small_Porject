def Search_Sorted_Equal_Index(A):
    l, u = 0, len(A) - 1

    while l <= u:
        mid = (u - l) // 2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            l = mid + 1
        else:
            u = mid - 1
    return 0
