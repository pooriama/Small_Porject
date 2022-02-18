def smallest_nonconstractible_value(A):
    max_cons_value = 0
    for a in A:
        if a > max_cons_value + 1:
            break
        else:
            max_cons_value += a
    return max_cons_value + 1
