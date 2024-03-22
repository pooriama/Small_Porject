#
# def int_to_str(x):
#     sign=1
#     if x<0:
#         x, sign=-x, -1
#     digit=[]
#     while True:
#         if x!=0:
#            digit.append(chr(ord("0")+(x%10)))
#            x=x//10
#         else:
#             break
#     return  "-"+"".join(reversed(digit)) if sign==-1 else "".join(reversed(digit))
#
#
#
# print((int_to_str(765834)))


def int_to_str(x):
    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1
    result = []
    while x > 0:
        result.append(chr(ord("0") + x % 10))
        x = x // 10
    return "-" + "".join(reversed(result)) if sign == -1 else "".join(reversed(result))


res = (int_to_str(-765834))
print(type(res))
print(res)
