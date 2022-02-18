def intersect_two_sorted_array(A, B):
    intersect_list = []
    i, j = 0, 0
    while len(A) > i and len(B) > j:
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersect_list.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] > B[j]:
            j = j + 1
        else:
            i = i + 1
    return intersect_list


A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
print(intersect_two_sorted_array(A,B))
