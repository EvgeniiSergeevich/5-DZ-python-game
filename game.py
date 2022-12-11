import player
import functions




# player1 = player.Player(input('Введите имя первого игрока: '))
# player2 = player.Player(input('Введите имя второго игрока: '))
name_p1 = input('Введите имя первого игрока: ')
player1 = player.Player(name_p1)
name_p2 = input('Введите имя второго игрока: ')
player2 = player.Player(name_p2)

start = functions.draw()

print(start)

