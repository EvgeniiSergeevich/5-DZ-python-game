class Player:
    player_number = 0
    def __init__(self, name, ids) -> None:
        self.name = name
        self.ids = ids
        print(f"{name} вошёл в игру!")