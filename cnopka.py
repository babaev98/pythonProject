import pygame as pg
import sys
import cletaka as cl

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

WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
BLACK = (0, 0, 0)
FPS = 30
CNOPKA_START = (200, 100)
pg.init()
sc = pg.display.set_mode((1200, 800))
#pg.Rect.collidepoint()

cl_red = cl.Сletka(sc, GREEN)
def inician (pole):
    for x in range(10):
        for y in range(10):
            cells = pole[x][y]
            if cells == 0:
                cl_red.changecletka(x, y)
            y += 1
        x += 1


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        pg.display.flip()
    for event in pg.mouse.get_pressed():
        if event == 1:
            inician(CANSPOLE)
            cl_red.changecolor(RED, 0, 0)
        elif event == 3:
            cl_red.changecolor(RED, 0, 0)
            pg.display.update()