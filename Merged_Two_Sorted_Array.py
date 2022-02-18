def Merged_two_sorted_array(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            print("A[a]", A[a])
            A[write_idx] = A[a]
            a -= 1
            write_idx -= 1
        else:
            print("B[b]", B[b])
            A[write_idx] = B[b]
            b -= 1
            write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        b -= 1
        write_idx -= 1
    return A


A = [5, 13, 17, 0, 0, 0, 0]
m = 3
B = [3, 7, 11, 19]
n = 4

print(Merged_two_sorted_array(A, m, B, n))

# def Merged_two_sorted_array(A, m, B, n):
#     a, b = m - 1, n - 1
#     write_index = m + n - 1
#     while (a >= 0 and b >= 0):
#         if (A[a] > B[b]):
#             A[write_index] = A[a]
#             a = a - 1
#             write_index -= 1
#         else:
#             print(write_index)
#             A[write_index] = B[b]
#             b = b - 1
#             write_index -= 1
#     while b > 0:
#         A[write_index] = B[b]
#         b = b - 1
#         write_index -= 1
#
#     return A
