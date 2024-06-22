


stack = [start]
direc = [(-1,0),(0,-1), (0,1), (1,0)]
n,m = len(maze)-1, len(maze[0])-1
seen = set(start)

while stack:
    r,c = stack.pop()
    if (r,c) == destination:
        return True
    for dr, dc in direc:
        nr,nc = r,c
        while 0<=dr+nr<=n and 0<=dc+nc<=m and maze[dr+nr][dc+nc]==1:
            nr = nr+dr
            nc = dc+nc
            if (nr,nc) in seen:
                continue
            else:
                stack.append((nr,nc))
                seen.add((nr,nc))

