import pygame
from pygame.sprite import AbstractGroup


class Player(pygame.sprite.Sprite):

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
