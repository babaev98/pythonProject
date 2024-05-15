import random as rd

import list_pole as ls

CANSPOLE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


class GamePlayer:
    def __init__(self, player):
        self.player = player
        self.last_shot = False

    def move(self):
        cordinat = input("Введите кординаты куда хотите нанести удар? (Слитно)  :")
        x, y = cordinat[0], cordinat[1]
        return x, y

    def victory_check(self, pole=list):
        victory = False
        for x in pole:
            for y in pole:
                if y == 1:
                    victory = True
                    break
        return victory


class GameBot(GamePlayer):
    def __init__(self, bot):
        super().__init__(player=bot)
        self.selected_coordinates = []
        self.list_cordinat = ls.def_list_cordinat()

    def move(self):
        cordinat = rd.choice(self.list_cordinat)
        self.list_cordinat.remove(cordinat)
        x, y = cordinat[0], cordinat[1]
        self.selected_coordinates.append(cordinat.copy())
        return x, y

    def logic_bot(self, pole):
        coordinates = self.selected_coordinates[len(self.selected_coordinates - 1)]
        if pole[coordinates[0]][coordinates[1]] == 2:
