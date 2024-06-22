# def binary_search(t, A):
#     L, U = 0, len(A) - 1
#
#     while L <= U:
#         M = L + (U - L) / 2
#         if t == A[M]:
#             return M
#         elif t < A[M]:
#             U = M - 1
#         else:
#             L = M + 1
#
#     return -1
#
#
# def bsearch(t, A):
#     l, u = 0, len(A)
#     while l <= u:
#         m = l + (u - l) / 2
#         if A[m] < t:
#             l = m + 1
#         elif A[m] == t:
#             return m
#         else:
#             u = m - 1
#     return -1


res =[[0,3] for i in range(3)]
print(res)
