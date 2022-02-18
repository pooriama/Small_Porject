import sys



n = int(sys.argv[1])


def factoriel(n):
    if n == 1:
        return 1
    return n*factoriel(n-1)



if __name__ == "__main__":
    result = factoriel(n)
    print(result)


