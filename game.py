import player
import functions



spl = '__________________________________________'

name_p1 = input('Введите имя первого игрока: ')
player1 = player.Player(name_p1)
name_p2 = input('Введите имя второго игрока: ')
player2 = player.Player(name_p2)
players = [player1, player2]
start = functions.draw()

print(spl)
print('Жеребъёвка...')
print(spl)
print(f'Начинает игрок №{start + 1} - {players[start].name}')

