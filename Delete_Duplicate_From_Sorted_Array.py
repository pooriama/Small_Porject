


def delete_duplicate(A):
    write_idx = 1

    for i in range(1,len(A)):
        if A[write_idx-1] != A[i]:
            A[write_idx] = A[i]
            write_idx+=1


    return  A[:write_idx]

A=[1,2,2,2,2,2,5,6,7,8,8,9]
print(delete_duplicate(A))


