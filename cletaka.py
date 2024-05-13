import pygame as pg


class Сletka:
    def __init__(self, sc, color):
        self.color = color
        self.sc = sc
        self.x = 0
        self.y = 0

    def changecletka(self, i_1, i_2):
        self.x = i_1 * 30 + 15
        self.y = i_2 * 30 + 15
        cl_rect = pg.Rect(self.x, self.y, 15, 15)
        pg.draw.rect(self.sc, self.color, cl_rect, 0)

    def changecolor(self, col, i_1, i_2):
        self.x = i_1 * 30 + 15
        self.y = i_2 * 30 + 15
        cl_rect = pg.Rect(self.x, self.y, 15, 15)
        pg.draw.rect(self.sc, col, cl_rect, 0)
