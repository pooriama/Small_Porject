def even_odd(A):
    next_odd = len(A) - 1
    next_even = 0
    while(next_even != next_odd):
        if A[next_even]%2==0:
            next_even+=1
        else:
            A[next_even],A[next_odd]=A[next_odd],A[next_even]
            next_odd-=1

    return A


    