from math import floor, log10


def Is_palindorme_number(x):
    # str_x=str(x)
    # print(str_x[::-1])
    # return (str_x == str_x[::-1])
    right_num = x % 10
    print("right_num", right_num)
    x_len = floor(log10(x)) + 1
    print("x_len", x_len)
    if x_len == 1:
        print("palindrome")
        return True
    left_num = x // 10 ** (x_len - 1)
    print("left_num", left_num)
    if right_num != left_num:
        print("not palindrome")
        return False
    x = x - (left_num * 10 ** (floor(log10(x))))
    x = x // 10
    print("x", x)
    Is_palindorme_number(x)


print(Is_palindorme_number(51415))
