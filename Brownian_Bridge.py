import math

import stddraw
import sys

import stdrandom



def curve(x0, y0, x1, y1, variance, scale_factor):
    if abs(x1 - x0) < 0.01:
        stddraw.line(x0, y0, x1, y1)
        return
    x = (x0 + x1) / 2
    y = (y0 + y1) / 2

    delta = stdrandom.gaussian(0, math.sqrt(variance))

    curve(x0, y0, x, y + delta, variance / scale_factor, scale_factor)
    curve(x, y + delta, x1, y1, variance / scale_factor, scale_factor)


def main(x0, y0, x1, y1, variance, scale_factor):
    curve(x0, y0, x1, y1, variance, scale_factor)
    stddraw.show()


if __name__ == "__main__":
    stddraw.setPenRadius(0.0)
    stddraw.clear(stddraw.LIGHT_GRAY)
    scale_factor = 2 ** (2 * 0.05)
    x0, y0, x1, y1, variance = 0, 0.5, 1, 0.5, 0.01
    main(x0, y0, x1, y1, variance, scale_factor)
