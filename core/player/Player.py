from random import randrange

import pygame
from pygame.sprite import AbstractGroup

from core.elements.ColorPallete import BASE_PALLETE


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

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
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y

    def stop(self):
        self.change_x = 0
        self.change_y = 0

    def move(self, walls):
        """ Find a new position for the player """

        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
