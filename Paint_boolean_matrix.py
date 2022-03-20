import collections


def flip_color(x, y, A):
    # cordinate = collections.namedtuple("cordinate", ("x", "y"))
    # cordinate = (x,y)
    color = A[x][y]
    q = collections.deque([(x, y)])
    A[x][y] = 1 - color
    while q:
        x, y = q.popleft()
        for d in (-1, 0), (1, 0), (0, -1), (0, 1):
            next_x, next_y = x + d[0], y + d[1]
            if 0 <= next_x < len(A) and 0 <= next_y < len(A[0]) and A[next_x][next_y] == color:
                q.append((next_x, next_y))
                A[next_x][next_y] = 1 - color
    return A


starting = [[1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
            ]
print(flip_color(0, 0, starting))
