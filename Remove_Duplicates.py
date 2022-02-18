def remove_duplicates(A):
    write_inx = 1

    for inx in A[1:]:
        if inx != A[write_inx - 1]:
            A[write_inx] = inx
            write_inx += 1
    del A[write_inx:]
    return A


A = [1, 2, 2, 3, 4, 4, 5, 5, 6, 7]
print(remove_duplicates(A))
