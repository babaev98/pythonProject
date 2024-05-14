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
    def __init__(self, player1=object, player2=object):
        self.player1 = player1
        self.player2 = player2
        self.selected_coordinates = []
        self.list_cordinat = ls.def_list_cordinat()
        self.last_shot = False

    def move_player(self):
        cordinat = input("Введите кординаты куда хотите нанести удар? (Слитно)  :")
        x, y = cordinat[0], cordinat[1]
        return x, y

    def move_bot(self):
        cordinat = rd.choice(self.list_cordinat)
        self.list_cordinat.remove(cordinat)
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

    def logic_bot(self, x=int, y=int):
