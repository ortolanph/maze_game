import pygame
from pygame.sprite import AbstractGroup

ROCK = (200, 200)

COLUMNS = [
    (150, 150),
    (450, 150),
    (150, 450),
    (450, 450),
]

ROCKS = [
    [150, 150, 150, 250],
    [400, 150, 250, 150],
    [150, 500, 250, 150],
    [500, 400, 150, 250],
]

SMALL_ROCKS = [
    (150, 150, 0),
    (350, 200, 1),
    (500, 150, 0),
    (200, 400, 1),
    (375, 375, 1),
    (550, 350, 1),
    (150, 500, 0),
    (400, 550, 1),
    (500, 500, 0),
]

CROSS = [
    (300, 150, "cross-arm-north"),
    (500, 300, "cross-arm-east"),
    (300, 500, "cross-arm-south"),
    (150, 300, "cross-arm-west"),
    (300, 300, "cross-middle"),
]

OBSTACLES = {
    1: ROCK,
    2: COLUMNS,
    3: ROCKS,
    4: SMALL_ROCKS,
    5: CROSS,
}

OBSTACLES_ARRAY = [0, 0, 0, 0, 0, 1, 2, 1, 4, 5]


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x, y, obstacle_image, *groups: AbstractGroup):
        super().__init__(*groups)

        self.image = obstacle_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class ObstacleFactory:

    obstacles_source_images = dict()

    def __init__(self, obstacle_images):
        self.obstacles_source_images = obstacle_images

    def produce_obstacle(self, obstacle):
        return self._get_obstacle_images(obstacle)

    def _get_obstacle_images(self, obstacle_id):
        if obstacle_id == 1:
            return self._get_rock()
        if obstacle_id == 2:
            return self.get_columns()
        if obstacle_id == 4:
            return self.get_small_rocks()
        if obstacle_id == 5:
            return self.get_cross()

    def _get_rock(self):
        my_obstacle = pygame.sprite.Group()

        obstacle_image = self.obstacles_source_images["big-rock"]
        obstacle_rock = Obstacle(ROCK[0], ROCK[1], obstacle_image)
        my_obstacle.add(obstacle_rock)

        return my_obstacle

    def get_columns(self):
        my_obstacle = pygame.sprite.Group()

        obstacle_image = self.obstacles_source_images["column"]
        for column in COLUMNS:
            obstacle_column = Obstacle(column[0], column[1], obstacle_image)
            my_obstacle.add(obstacle_column)

        return my_obstacle

    def get_small_rocks(self):
        my_obstacle = pygame.sprite.Group()

        image_array = [
            self.obstacles_source_images["rock-medium"],
            self.obstacles_source_images["rock-small"]
        ]

        for rock in SMALL_ROCKS:
            obstacle_column = Obstacle(rock[0], rock[1], image_array[rock[2]])
            my_obstacle.add(obstacle_column)

        return my_obstacle

    def get_cross(self):
        my_obstacle = pygame.sprite.Group()

        for cross in CROSS:
            obstacle_cross = Obstacle(cross[0], cross[1], self.obstacles_source_images[cross[2]])
            my_obstacle.add(obstacle_cross)

        return my_obstacle
