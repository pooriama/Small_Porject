import random

import stddraw

radious, DT = 0.05, 10.0

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

rx, ry = 0.480, 0.860
vx, vy = random.random() * 0.1, random.random() * 0.0927

while True:
    if abs(rx + vx) > 1.0:
        vx = -vx
    if abs(vy + ry) > 1.0:
        vy = -vy
    rx += vx
    ry += vy

    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, radious)
    stddraw.show(DT)
