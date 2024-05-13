from typing import Type


def region_ship(x=Type[int], y=Type[int], directorion=str, paluba=Type[int]):
    x_lis = []
    y_lis = []
    if directorion == "up":
        i = 0
        while i < paluba:
            x_lis.append(x)
            i += 1
            x -= 1
    elif directorion == "down":
        i = 0
        while i < paluba:
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
        while i < paluba:
            y_lis.append(y)
            i += 1
            y += 1
    elif directorion == "left":
        i = 0
        while i < paluba:
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

print(region_ship(5, 5, "up", 4))