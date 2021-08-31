import sys, random, stddraw
from stddraw import RED, GREEN, BLUE

n = int(sys.argv[1])
cx = [0.0 ,1.0 , 0.5]
cy = [0.0, 0.0, 0.866]
colors = [RED, GREEN, BLUE]
x, y = 0, 0

for i in range(n):
    randomchoise = random.randrange(3)
    x = (x + cx[randomchoise])/2.0
    y = (y + cy[randomchoise])/2.0
    stddraw.setPenColor(colors[randomchoise])
    stddraw.point(x,y)
    stddraw.show(0)
stddraw.show()



