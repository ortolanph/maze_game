import pygame

from core.elements.ColorPallete import BASE_PALLETE
from core.elements.CommonCoordinates import *
from core.elements.Obstacles import OBSTACLES
from core.elements.Wall import Wall


class GameRoom:
    kind = ""
    exits = []
    walls = []
    items = []
    obstacle = 0

    def __init__(self, exits, kind):
        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.exits = exits
        self.kind = kind

    def set_obstacle(self, obstacle):
        self.obstacle = obstacle

    def add_item(self, item):
        self.items.add(item)

    def room_walls(self):
        my_coordinates = []

        for corner in CORNERS:
            my_coordinates.append(corner)

        if self.obstacle > 0:
            my_obstacle = OBSTACLES[self.obstacle]
            for points in my_obstacle:
                my_coordinates.append(points)

        for my_exit in [1, 2, 3, 4]:
            if my_exit in self.exits:
                my_coordinates.append(ROOM_ITEMS[my_exit]["exit"][0])
                my_coordinates.append(ROOM_ITEMS[my_exit]["exit"][1])
            else:
                my_coordinates.append(ROOM_ITEMS[my_exit]["wall"][0])

        for coordinate in my_coordinates:
            self.walls.add(
                Wall(
                    coordinate[0],
                    coordinate[1],
                    coordinate[2],
                    coordinate[3],
                    BASE_PALLETE[self.kind]["WALLS"])
            )

        return self.walls

    def remove_item(self, item):
        self.items.remove(item)