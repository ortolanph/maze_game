import pygame


class GameRoom:
    kind = ""
    exits = []
    walls = []
    steps = []
    items = []

    def __init__(self, exits, kind):
        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.steps = pygame.sprite.Group()
        self.exits = exits
        self.kind = kind

    def add_obstacle(self, sprite_list):
        for sprite in sprite_list:
            self.walls.add(sprite)

    def add_walls(self, my_walls):
        for my_wall in my_walls:
            self.walls.add(my_wall)

    def room_walls(self):
        return self.walls

    def add_steps(self, my_steps):
        for my_step in my_steps:
            self.steps.add(my_step)

    def room_steps(self):
        return self.steps

    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.remove(item)
