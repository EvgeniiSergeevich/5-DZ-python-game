import random
import player

def draw():
    dr = random.randint(0, 1)
    if dr == 0:
        return 0
    else:
        return 1

# def start_game(p1, p2, start, candies):
#     if start == 0:
#         p1.
