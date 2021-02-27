import pygame
from pygame.sprite import AbstractGroup


CORNERS = [(0, 0), (750, 0), (750, 750), (0, 750)]

EXITS = {
    1: [(50, 0), (500, 0)],
    2: [(750, 50), (750, 500)],
    3: [(50, 750), (500, 750)],
    4: [(0, 50), (0, 500)]
}

WALLS = {
    1: (50, 0),
    2: (750, 50),
    3: (50, 750),
    4: (0, 50)
}


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, wall_image, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = wall_image

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class WallBuilder:

    __walls_source_images = []

    def __init__(self, wall_images):
        self.__walls_source_images = wall_images

    def build_walls(self, exits):
        walls = pygame.sprite.Group()
        hard_walls = list({1, 2, 3, 4} - set(exits))

        self.__add_corners(walls)
        self.__add_exits(walls, exits)
        self.__add_walls(walls, hard_walls)

        return walls

    def __add_corners(self, walls):
        corners = self.__walls_source_images["corners"]
        for corner in range(0, 4):
            walls.add(Wall(CORNERS[corner][0], CORNERS[corner][1], corners[corner]))

    def __add_exits(self, walls, exits):
        my_exits = self.__walls_source_images["exits"]
        for my_exit in exits:
            walls.add(Wall(EXITS[my_exit][0][0], EXITS[my_exit][0][1], my_exits[my_exit][0]))
            walls.add(Wall(EXITS[my_exit][1][0], EXITS[my_exit][1][1], my_exits[my_exit][1]))

    def __add_walls(self, walls, hard_walls):
        my_walls = self.__walls_source_images["hard_walls"]
        for my_wall in hard_walls:
            walls.add(Wall(WALLS[my_wall][0], WALLS[my_wall][1], my_walls[my_wall]))
