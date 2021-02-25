from random import randrange, choice

import pygame
from pygame.sprite import AbstractGroup

""" Abstract Item """


class GameItem(pygame.sprite.Sprite):

    def __init__(self, x, y, loaded_image, *groups: AbstractGroup):
        super().__init__(*groups)

        self.image = loaded_image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


""" Coin Item """

COIN_POSITION = {
    0: {"x": 75, "y": 75},
    1: {"x": 675, "y": 75},
    2: {"x": 675, "y": 675},
    3: {"x": 75, "y": 675}
}

BUDGETS = [100, 200, 300, 400, 500]


class Coin(GameItem):
    budget = 0

    def __init__(self, loaded_image, *groups: AbstractGroup):
        my_budget = choice(BUDGETS)
        self.budget = my_budget

        position = randrange(0, 4)
        x = COIN_POSITION[position]["x"]
        y = COIN_POSITION[position]["y"]

        super().__init__(x, y, loaded_image, *groups)
