class Player:
    player_number = 0
    def __init__(self, name) -> None:
        self.name = name
        print(f"{name} вошёл в игру!")