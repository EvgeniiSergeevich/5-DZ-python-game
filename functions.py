import random
import player

def draw():
    dr = random.randint(0, 1)
    if dr == 0:
        return 0
    else:
        return 1

def start_game(name1, name2, start, candies):
    i = start + 1
    if i == 1:
        print(f'{name1}, начинай!')
    else:
        print(f'{name2}, начинай!')
    while candies > 0:
        if i % 2 != 0:
            take = int(input(f'{name1}, сколько конфет заберёшь? Введи число от 1 до 28'))
            if take > 0 and take < 29:
                candies -= take
                print(f'{name1} оставил {candies} котфет')
                i += 1
            else:
                print('Не верно введено число! Повтори!')
                continue
        else:
            take = int(input(f'{name2}, сколько конфет заберёшь? Введи число от 1 до 28'))
            if take > 0 and take < 29:
                candies -= take
                print(f'{name2} оставил {candies} котфет')
                i += 1
            else:
                print('Не верно введено число! Повтори!')
                continue


# бери конфеты!! Конфет осталось {candies}