import random
import sys
import stddraw
from stddraw import GREEN

n = int(sys.argv[1])
x = 0.0
y = 0.0

for i in range(n):
    randomchoice = random.random()
    if randomchoice < 0.02:
        x = 0.50
        y = 0.27 * y
    elif randomchoice < 0.17:
        x = -0.14 * x + 0.26 * y + 0.57
        y = 0.25 * x + 0.22 * y - 0.04
    elif randomchoice < 0.30:
        x = 0.17 * x - 0.21 * y + 0.41
        y = 0.22 * x + 0.18 * y + 0.09
    else:
        x = 0.78 * x + 0.03 * y + 0.11
        y = -0.03 * x + 0.74 * y + 0.27
    stddraw.setPenColor(GREEN)
    stddraw.point(x,y)
stddraw.show()