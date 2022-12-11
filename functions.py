import random

def draw(p1, p2):
    dr = random.randint(0, 1)
    if dr == 0:
        return p1
    else:
        return p2
