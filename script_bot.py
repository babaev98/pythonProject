import random as rd

import list_pole as ls


class GamePlayer:
    def __init__(self):
        self.player = "player"

    def move(self):
        cordinat = input("Введите кординаты куда хотите нанести удар? (Слитно)  :")
        x, y = int(cordinat[0]), int(cordinat[1])
        return x, y

    def victory_check(self, pole=list):
        victory = False
        a = 0
        for x in pole:
            for y in x:
                if y == 1:
                    a += 1
                    break
                if a > 0:
                    break
        if a == 0:
            victory = True
        return victory


class GameBot(GamePlayer):

    def __init__(self):
        super().__init__()
        self.player = "bot"
        self.selected_coordinates = []
        self.list_coordinates = ls.def_list_cordinat()
        self.last_shot_destroyed = False
        self.shooting_target = []

    def move(self):
        cordinat = rd.choice(self.list_coordinates)
        self.list_coordinates.remove(cordinat)
        x, y = cordinat[0], cordinat[1]
        self.selected_coordinates.append(cordinat.copy())
        return x, y

    def logic_bot(self, pole, ob=object):
        coordinates_0 = self.selected_coordinates[len(self.selected_coordinates - 1)]
        x, y = coordinates_0[0], coordinates_0[1]
        if pole[x][y] == 3:
            self.shooting_target.clear()
            self.last_shot_destroyed = True
        elif pole[x][y] == 2:
            self.last_shot_destroyed = False
            list_x_y = []
            if len(self.shooting_target) == 0:
                list_x_y.append([x - 1, y])
                list_x_y.append([x + 1, y])
                list_x_y.append([x, y - 1])
                list_x_y.append([x, y + 1])
            elif len(self.shooting_target) != 0:
                self.shooting_target.clear()
                coordinates_1 = self.selected_coordinates[len(self.selected_coordinates - 1)]
                result = [coordinates_1[0] - coordinates_0[0], coordinates_1[1] - coordinates_0[1]]
                self.shooting_target.append(result)
        else:
            ob()


player = GamePlayer()
bot = GameBot()
