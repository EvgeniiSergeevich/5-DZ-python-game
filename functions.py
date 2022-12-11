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


def start_game_bot(name1, name2, start, candies):                           # Логика игры с ботом
    print(f'Всего конфет: {candies}')
    i = start + 1   

    if i == 1:                                                              # Объявление первого хода
        print(f'{name1}, начинай!')
    else:
        print(f'{name2}, начинай!')

    while candies > 0:                                                      
        if i % 2 != 0:                                                     
            take = int(input(f'{name1}, сколько конфет заберёшь? Введи число от 1 до 28:   '))  # Человеческая логика
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
        else:                                                                                   # Логика бота
            if candies < 29:
                # print('< 29')
                take = candies
                candies -= take
                print(f'{name2} забрал {take} конфет и оставил {candies}!')
                i += 1
                
            elif candies > 29 and candies < 58:
                # print('29 < < 58')
                c = [k for k in range(30, 58)]
                for j in range(len(c)):
                    if candies == c[j]:
                        take = j + 1
                candies -= take
                print(f'{name2} забрал {take} конфет и оставил {candies}!')
                i += 1
                

            elif candies > 58 and candies < 87:
                # print('58 <  < 87')
                c = [k for k in range(59, 87)]
                for j in range(len(c)):
                    if candies == c[j]:
                        take = j + 1
                candies -= take
                print(f'{name2} забрал {take} конфет и оставил {candies}!')
                i += 1    
                
            else:
                # print('Остальные случаи')
                take = random.randint(1, 29)
                candies -= take
                print(f'{name2} забрал {take} конфет и оставил {candies}!')
                i += 1

    if i % 2 == 0:                                          
        print(f'{name1} Победил!!! УРА!')                  
    else:
        print(f'{name2} Победил!!! УРА!')