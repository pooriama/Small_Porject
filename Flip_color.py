


def flip_color(x,y,A):
    color = A[x][y]
    A[x][y] = 1 -A[x][y]
    queue = [(x,y)]
    while queue:
        for d in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=(x+d[0])<len(A) and 0<=(y+d[1])<len(A[0]) and  A[x+d[0]][y+d[1]] == color:
                A[x + d[0]][y + d[1]]= 1-color
                queue.append((x + d[0], y + d[1]))




