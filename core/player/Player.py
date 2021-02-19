from random import randrange

import pygame
from pygame.sprite import AbstractGroup

from core.elements.ColorPallete import BASE_PALLETE
from core.items.Item import Coin


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    gold = 0

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        super().__init__()

        self.image = pygame.Surface([64, 64])

        self.image.fill(BASE_PALLETE["PLAYER"])
        self.rect = self.image.get_rect()

        x = randrange(50, 685)
        y = randrange(50, 685)

        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def stop(self):
        self.change_x = 0
        self.change_y = 0

    def move(self, game_room):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, game_room.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, game_room.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        item_hit_list = pygame.sprite.spritecollide(self, game_room.items, False)

        for item in item_hit_list:
            if isinstance(item, Coin):
                self.gold += item.budget
                game_room.remove_item(item)
                print(f"You have {self.gold} golds")
