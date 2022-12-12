import player
import functions

spl = '__________________________________________\n'                    # Просто разделитель
print(spl)

pl2_or_bot = int(input('Введите количество игроков: '))                 # Выбор 1 или 2х игроков

players = []                                                            # Список с игроками, ддля удобства

if pl2_or_bot == 2:                   
    print(spl)                                                          # Создаю 2х игроков. Изначально был класс Bot, 
    name_p1 = input('Введите имя первого игрока: ')                     # но решил обойтись без него.
    player1 = player.Player(name_p1)
    print(spl)
    name_p2 = input('Введите имя второго игрока: ')
    player2 = player.Player(name_p2)
    players = [player1, player2]
elif pl2_or_bot == 1:
    print(spl)
    name_p1 = input('Введите Ваше имя: ')
    print(spl)
    player1 = player.Player(name_p1)
    bot1 = player.Player('ИИ Джарвис')
    print(spl)
    players = [player1, bot1]
else:
    print('Введите 1 или 2!!')
    


start = functions.draw()                                                # Жеребъёвка. Получаю 1 или 0. 0 - первый игрок, 1 - второй

print(spl)
print('Жеребъёвка...')
print(spl)
print(f'Начинает игрок №{start + 1} - {players[start].name}')
print(spl)

candies = 117

if pl2_or_bot == 2:
    functions.start_game(players[0].name, players[1].name, start, candies) 
else:
    functions.start_game_bot(players[0].name, players[1].name, start, candies)
