from typing import Type

import list_pole as lp

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

KEY = [1, 2, 3, 4]
ship_slov = {1: 4, 2: 3, 3: 2, 4: 1}
name_ship = {1: "Однопалубный", 2: "Двухпалубный", 3: "Трехпалубный", 4: "Четырехпалубный"}


def LisInLis(lis=list) -> Type[list]:
    lis_perem = lis
    return lis_perem


def LenShipObject(key=Type[int]) -> object:
    a1, a2, a3, a4 = object
    slov_comand = {1: a1, 2: a2, 3: a3, 4: a4}
    return slov_comand[key]


"""Создание    поля    игрока"""


class Player:
    def __init__(self, name):
        self.name = name
        self.pole = CANSPOLE.copy()
        self.ship = ship_slov

    def striking(self, coordinates):
        x, y = coordinates
        if self.pole[x][y] == 1:
            x_list, y_list = a1.region_ship(x, y, "up")
            for x_1 in x_list:
                for y_1 in y_list:
                    if self.pole[x_1][y_1] == 1:
                        destroyed = False
                    else:
                        destroyed = True
            if destroyed:
                self.pole[x][y] = 2
            else:
                self.pole[x][y] = 3
        elif self.pole[x][y] == 0:
            self.pole[x][y] = 4

    def PrinPole(self, pole):
        for i in pole:
            print(i)

    def player_or_bot(self):
        if self.name == "bot":
            self.pole = lp.bot_pole()
        else:
            choice = int(input("Если вы хотите выбрать поле сами введите '1', а если хотите рандомное поле то '0'  :"))
            if choice == 1:
                self.InstallationPole()
            elif choice == 0:
                self.pole = lp.bot_pole()
        return self.pole

    def InstallationPole(self):
        for i in range(1, 5):
            i_2 = 0
            while i_2 < ship_slov[i]:
                self.InstallationShip(i)
                i_2 += 1
        return self.pole

    def InputCoordinates(self, key=int):
        a = LenShipObject(key).paluba
        b = name_ship[a]
        coordinates = input(str(f"введите кардинаты места куда хотите поставить {b} карабль  :"))
        direction = input(str(f"введите напровление коробля (up,down,right,left) и учтите ширену поля  :"))
        x = int(coordinates[0])
        y = int(coordinates[1])
        try:
            self.input_erorr(coordinates, direction)
        except Exception:
            self.InputCoordinates(key)
        return x, y, direction

    def InstallationShip(self, key=int):
        x, y, direction = self.InputCoordinates(key)
        try:
            self.cordinat_error(x, y, direction, key)
        except Exception:
            print("данный кораболь нельзя поставить в даном напровлении")
            self.InstallationShip(key)
        try:
            self.cordinat_error2(x, y, direction, key)
        except Exception:
            print("данный корабль пересекает область другого коробля")
            self.InstallationShip(key)
        lis_coordinates = LenShipObject(key).LenShip(x, y, direction)
        for i, i_2 in lis_coordinates:
            self.pole[i][i_2] = 1
        self.PrinPole(self.pole)

    # Создание исключений при работе с вво дом

    def cordinat_error2(self, x=Type[int], y=Type[int], directorion=Type[str], key=Type[int]):
        bool_error = False
        x_lis, y_lis = LenShipObject(key).region_ship(x, y, directorion)
        for x in x_lis:
            for y in y_lis:
                if self.pole[x][y] == 1:
                    raise Exception("Некорректные коррдинаты")

    def cordinat_error(self, x=Type[int], y=Type[int], directorion=Type[str], key=int):
        L = int(LenShipObject(key).paluba)
        if directorion == "up":
            if L == 4:
                if y < 3:
                    raise Exception("Некорректные коррдинаты")
            if L == 3:
                if y < 2:
                    raise Exception("Некорректные коррдинаты")
            if L == 2:
                if y < 1:
                    raise Exception("Некорректные коррдинаты")
        if directorion == "down":
            if L == 4:
                if x > 6:
                    raise Exception("Некорректные коррдинаты")
            if L == 3:
                if x > 7:
                    raise Exception("Некорректные коррдинаты")
            if L == 2:
                if x > 8:
                    raise Exception("Некорректные коррдинаты")
        if directorion == "left":
            if L == 4:
                if y < 3:
                    raise Exception("Некорректные коррдинаты")
            if L == 3:
                if y < 2:
                    raise Exception("Некорректные коррдинаты")
            if L == 2:
                if y < 1:
                    raise Exception("Некорректные коррдинаты")
        if directorion == "right":
            if L == 4:
                if y > 6:
                    raise Exception("Некорректные коррдинаты")
            if L == 3:
                if y > 7:
                    raise Exception("Некорректные коррдинаты")
            if L == 2:
                if y > 8:
                    raise Exception("Некорректные коррдинаты")

    def input_erorr(self, coordinates=str, directorion=str):
        check = 0
        list_directorion = ['up', 'down', 'right', 'left']
        len_coordinates = len(coordinates)
        if len_coordinates != 2:
            raise Exception("Некорректные коррдинаты")
        for i in list_directorion:
            if directorion != i:
                check += 1
                if check == 4:
                    raise Exception("Некорректное направление")


class Ship:

    def __init__(self, paluba=Type[int]) -> None:
        self.paluba = paluba
        self.name = name_ship[self.paluba]

    def LenShip(self, x=Type[int], y=Type[int], direction=str) -> list:
        lis_coordinates = []
        for i in range(self.paluba):
            lis_perem = []
            if direction == "up":
                lis_perem.append(x - i)
                lis_perem.append(y)
                lis_coordinates.append(LisInLis(lis_perem))
            elif direction == "down":
                lis_perem.append(x + i)
                lis_perem.append(y)
                lis_coordinates.append(LisInLis(lis_perem))
            elif direction == "left":
                lis_perem.append(x)
                lis_perem.append(y - i)
                lis_coordinates.append(LisInLis(lis_perem))
            elif direction == "right":
                lis_perem.append(x)
                lis_perem.append(y + i)
                lis_coordinates.append(LisInLis(lis_perem))
        return lis_coordinates

    def region_ship(self, x=Type[int], y=Type[int], directorion=str):
        x_lis = []
        y_lis = []
        if directorion == "up":
            i = 0
            while i < self.paluba:
                x_lis.append(x)
                i += 1
                x -= 1
        elif directorion == "down":
            i = 0
            while i < self.paluba:
                x_lis.append(x)
                i += 1
                x += 1
        elif directorion == "right" or directorion == "left":
            x1, x2, x3 = x - 1, x, x + 1
            x_lis.append(x1)
            x_lis.append(x2)
            x_lis.append(x3)
        if directorion == "up" or directorion == "down":
            y1, y2, y3 = y - 1, y, y + 1
            y_lis.append(y1)
            y_lis.append(y2)
            y_lis.append(y3)
        elif directorion == "right":
            i = 0
            while i < self.paluba:
                y_lis.append(y)
                i += 1
                y += 1
        elif directorion == "left":
            i = 0
            while i < self.paluba:
                y_lis.append(y)
                i += 1
                y -= 1
        for x in x_lis:
            if x < 0 or x > 9:
                x_lis.remove(x)
        for y in y_lis:
            if y < 0 or y > 9:
                y_lis.remove(y)
        return x_lis, y_lis

def init_ship():
    a1 = Ship(1)
    a2 = Ship(2)
    a3 = Ship(3)
    a4 = Ship(4)

