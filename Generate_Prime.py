def generate_prime(n):
    prime = []
    cand_list = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if cand_list[i]:
            prime.append(i)
            for j in range(i, n + 1, i):
                cand_list[j] = False
    return prime


print(generate_prime(24))
