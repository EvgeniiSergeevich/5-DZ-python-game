import random
import player

def draw():
    return random.randint(0, 1)
    

def start_game(name1, name2, start, candies):
    i = start + 1
    print(f'Всего конфет: {candies}')
    if i == 1:
        print(f'{name1}, начинай!')
    else:
        print(f'{name2}, начинай!')
    while candies > 0:
        if i % 2 != 0:
            take = int(input(f'{name1}, сколько конфет заберёшь? Введи число от 1 до 28:   '))
            if candies - take < 0:
                print(f"Столько конфет нет! Число должно быть меньше {candies + 1}!!!")
                continue
            if take > 0 and take < 29:
                candies -= take
                print(f'{name1} оставил {candies} котфет')
                i += 1
            else:
                print('Не верно введено число! Повтори!')
                continue
        else:
            take = int(input(f'{name2}, сколько конфет заберёшь? Введи число от 1 до 28:   '))
            if candies - take < 0:
                print(f"Столько конфет нет! Число должно быть меньше {candies + 1}!!!")
                continue
            if take > 0 and take < 29:
                candies -= take
                print(f'{name2} оставил {candies} котфет')
                i += 1
            else:
                print('Не верно введено число! Повтори!')
                continue
    if i % 2 == 0:
        print(f'{name1} Победил!!! УРА!')
    else:
        print(f'{name2} Победил!!! УРА!')


# бери конфеты!! Конфет осталось {candies}