import collections

black, white = range(2)

cordinate = collections.namedtuple("cordinate", ("x", "y"))


# def search_maze(maze, s, e):
#     def search_maze_helper(cur):
#         if not ((0 <= cur[0] < len(maze)) and (0 <= cur[1] < len(maze[cur[0]])) and (maze[cur[0]][cur[1]] == white)):
#             return False
#         path.append(cur)
#         maze[cur[0]][cur[1]] = black
#         if cur == e:
#             return True
#         if any(map(search_maze_helper,
#                    ((cur[0] - 1, cur[1]), (cur[0] + 1, cur[1]), (cur[0], cur[1] - 1), (cur[0], cur[1] + 1)))):
#             return True
#         del path[-1]
#         return False
#
#     path = []
#     if not search_maze_helper(s):
#         return []
#     return path
#
#
# if __name__ == "__main__":
#     mat = [
#         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
#         [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
#         [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
#         [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#         [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
#         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
#         [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
#         [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
#     ]
#     print(search_maze(mat, (0, 0), (9, 9)))


def search_maze(maze, s, e):
    def search_maze_helper(s):


        if not (0 <= s[0] < len(maze)) or not (0 <= s[1] < len(maze[0])) or maze[s[0]][s[1]] != 1:
            return False
        path.append(s)
        maze[s[0]][s[1]]=0
        if s == e:
            return True
        if any(map(search_maze_helper, ((s[0] + 1, s[1]), (s[0] - 1, s[1]), (s[0], s[1] - 1), (s[0], s[1] + 1)))):
            return True
        del path[-1]
        return False


    path = []
    if not search_maze_helper(s):
        return []
    return path




if __name__ == "__main__":
    mat = [
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    ]
    print(search_maze(mat, (0, 0), (9, 9)))