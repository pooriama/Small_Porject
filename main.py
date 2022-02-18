

import sys
import random
import stddraw
# Suits=["Diamonds","Clubs","Hearts","Spades"]
# Ranks=["1","2","3","4","5","6"]
#
# for i in range(10):
#     # randsuits = random.randrange(len(Suits))
#     # randrank = random.randrange(len(Ranks))
#     # print(Ranks[randrank] + Suits[randsuits])
#     randsuits=random.choice(Suits)
#     randrank = random.choice(Ranks)
#     print(randrank  + randsuits)

n = int(sys.argv[1])
cx = [0.0, 1.0, 0.500]
cy = [0.0,0.0,0.866]

x,y=0,0

for i in range(n):
    rn=random.randrange(3)
    x=(x+cx[rn])/2
    y=(y+cy[rn])/2
    stddraw.point(x,y)
stddraw.show()
