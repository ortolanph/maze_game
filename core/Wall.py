import pygame
from pygame.sprite import AbstractGroup


class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
