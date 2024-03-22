from functools import reduce


# def decode_call_id(col):
#     result = 0
#     for i in range(len(col)):
#         result = result * 26 + ord(col[i]) - ord("A") + 1
#     return result


def decode_call_id(col):
    return reduce(lambda a, b: a * 26 + ord(b) - ord("A") + 1, col, 0)


print(decode_call_id("ZZ"))
