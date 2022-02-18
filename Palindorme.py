import math


def palindrome(x):
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    for i in range(num_digits // 2):
        if (x % 10) == (math.floor(x / (10 ** (num_digits - 1)))):
            x %= 10 ** (num_digits - 1)
            x //= 10
            num_digits = num_digits - 2
        else:
            return 0
    return 1


if __name__ == "__main__":
    result = palindrome(2147447412)
    if result == 1:
        print("palindrome")
    else:
        print("is not palindrome")
