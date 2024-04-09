def matrix_search(A, x):
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] > x:
            col -= 1
        else:
            row += 1
    return False
