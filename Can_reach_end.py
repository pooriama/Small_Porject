def can_reach_end(A):
    last_index = len(A)
    further_can_reach = 0
    i = 0
    while further_can_reach < last_index and further_can_reach >= i:
        further_can_reach = max(further_can_reach, A[i] + i)
        i += 1
    return further_can_reach >= last_index


# A = [3, 3, 1, 0, 2, 0, 1]
A = [3, 2, 0, 0, 3, 0, 2]
print(can_reach_end(A))
