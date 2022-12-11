import random
import player

def draw():
    dr = random.randint(1, 2)
    if dr == 1:
        return 1
    else:
        return 2

