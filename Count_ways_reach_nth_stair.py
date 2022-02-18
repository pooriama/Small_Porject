



def fib(n):
    if (n == 0):
        return 0
    result = [0 for i in range(n + 1)]
    result[0] = 1
    result[1] = 1
    for j in range(2, n + 1):
        result[j] = result[j - 1] + result[j - 2]

    return result[n]


print(fib(4))
