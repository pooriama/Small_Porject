
import random
def random_sampling(k,A):
    for i in range(k):
        randnum=random.randint(i,len(A)-1)
        A[randnum],A[i]=A[i],A[randnum]
    return A[:k]
