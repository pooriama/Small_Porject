


def count_bits(x):
    num_bits = 0
    while x>1:
        if x%2==1:
            num_bits+=1
        x=x/2
    return num_bits


print(count_bits(10))
