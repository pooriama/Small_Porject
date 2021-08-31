import sys
import random


def avoiding_random_walk(trial, shape):
    dead_total = 0
    for i in range(trial):
        matrix2d = [[0] * shape for j in range(shape)]
        x, y = shape // 2, shape // 2

        while 0 < x < shape - 1 and 0 < y < shape - 1:
            if matrix2d[x][y - 1] and matrix2d[x][y + 1] and matrix2d[x - 1][y] and matrix2d[x + 1][y]:
                dead_total += 1
                break
            matrix2d[x][y] = 1

            movedirection = random.random()
            if movedirection < 0.25:
                if not matrix2d[x - 1][y] == 1:
                    x = x - 1
            elif movedirection < 0.5:
                if not matrix2d[x][y - 1] == 1:
                    y = y - 1
            elif movedirection < 0.75:
                if not matrix2d[x + 1][y] == 1:
                    x = x + 1
            else:
                if not matrix2d[x][y + 1] == 1:
                    y = y + 1
    print("the total loss", 100 * dead_total // trial)

def main():
    trial = int(sys.argv[1])
    shape = int(sys.argv[2])
    avoiding_random_walk(trial, shape)

if __name__ == "__main__":
    main()
