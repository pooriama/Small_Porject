import sys
import stdrandom
import stddraw

def main():
    n = int(sys.argv[1])
    for i in range(n):
        x = stdrandom.gaussian(0.5,0.1)
        y = stdrandom.gaussian(0.5, 0.1)
        stddraw.point(x,y)
    stddraw.show()





if __name__ == "__main__":
    main()