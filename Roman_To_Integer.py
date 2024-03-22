from functools import reduce


# def roman_to_integer(s):
#     T = {'I': 1, 'V': 5, "X": 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#     num = T[s[len(s) - 1]]
#     for i in range(len(s) - 2, -1, -1):
#         if T[s[i]] < T[s[i + 1]]:
#             num -= T[s[i]]
#         else:
#             num += T[s[i]]
#     return num


# def roman_to_integer(s):
#     T = {'I': 1, 'V': 5, "X": 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#
#     number = T[s[len(s) - 1]]
#     for i in reversed(range(len(s) - 1)):
#         if T[s[i + 1]] <= T[s[i]]:
#             number += T[s[i]]
#         else:
#             number -= T[s[i]]
#     return number


def roman_to_integer(s):
    T = {'I': 1, 'V': 5, "X": 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return reduce(lambda number, i: number + T[s[i]] if T[s[i]] >= T[s[i+1]] else number - T[s[i]], reversed(range(len(s) - 1)),
                  T[s[-1]])


print(roman_to_integer("LIX"))
