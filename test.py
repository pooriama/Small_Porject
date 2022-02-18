import bisect
import collections
import sys
import random

# list1 = [3, 6, 8]
# list2 = [6, 8, 12, 16]
# list3 = [2, 7, 9, 14, 36]
#
# list_compare = []
# result = []
# i = 0
# while True:
#     if i < len(list1):
#         list_compare.append(list1[i])
#     if i < len(list2):
#         list_compare.append(list2[i])
#     if i < len(list3):
#         list_compare.append(list3[i])
#     list_compare.sort()
#     result.append(list_compare.pop(0))
#     if (list_compare == []):
#         break
#     else:
#         i += 1
#
# print(result)

#
# N = [1,2,5,7,8,11,12,14,18,21,26,29]
#
# print(bisect.bisect_left(N,0))

#
# c=collections.Counter(a=3, b=1,d=1)
# d=collections.Counter(a=1, b=2, g=1)
# print(c|d)


n=[1,2,3,4,5]

for i in range(len(n)-1,-1,-1):
    print(n[i])