import player
import functions
import bot


spl = '__________________________________________\n'                    # Просто разделитель

pl2_or_bot = int(input('Введите количество игроков: '))                 # Выбор 1 или 2х игроков

players = []                                                            # Список с игроками, ддля удобства

if pl2_or_bot == 2:                                                     # Создаю 2х игроков. Изначально был класс Bot, 
    name_p1 = input('Введите имя первого игрока: ')                     # но решил обойтись без него.
    player1 = player.Player(name_p1)
    name_p2 = input('Введите имя второго игрока: ')
    player2 = player.Player(name_p2)
    players = [player1, player2]
elif pl2_or_bot == 1:
    name_p1 = input('Введите Ваше имя: ')
    player1 = player.Player(name_p1)
    bot1 = player.Player('Джарвис')
    players = [player1, bot1]
else:
    print('Введите 1 или 2!!')


start = functions.draw()                                                # Жеребъёвка. Получаю 1 или 0. 0 - первый игрок, 1 - второй

print(spl)
print('Жеребъёвка...')
print(spl)
print(f'Начинает игрок №{start + 1} - {players[start].name}')

candies = 117

if pl2_or_bot == 2:
    functions.start_game(players[0].name, players[1].name, start, candies) 
else:
    