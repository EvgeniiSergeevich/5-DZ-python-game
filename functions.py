import random
import player

def draw():                                                                 # Жеребъёвка
    return random.randint(0, 1)
    

def start_game(name1, name2, start, candies):                               # Логика игры для 2х игроков
    i = start + 1                                                           # Счётчик для выявления победителя, привязан к жребию                     

    print(f'Всего конфет: {candies}')

    if i == 1:                                                              # Объявление первого хода
        print(f'{name1}, начинай!')
    else:
        print(f'{name2}, начинай!')

    while candies > 0:                                                      # Логика игры. Отнимаю от общего количества конфеты,
        if i % 2 != 0:                                                      # обрабатываю различные исключения, увеличиваю счётчик
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
    if i % 2 == 0:                                          # Такое условие, потому что после последнего хода счётчик прибавляется
        print(f'{name1} Победил!!! УРА!')                   # Сначала была ошибка, но я потестировал и разобрался
    else:
        print(f'{name2} Победил!!! УРА!')


def start_game_bot(name1, name2, start, candies):
    print(f'Всего конфет: {candies}')
