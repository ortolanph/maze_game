import pygame


class GameRoom:
    kind = ""
    exits = []
    walls = []
    items = []

    def __init__(self, exits, kind):
        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.exits = exits
        self.kind = kind

    def add_obstacle(self, sprite_list):
        for sprite in sprite_list:
            self.walls.add(sprite)

    def add_walls(self, my_walls):
        for my_walls in my_walls:
            self.walls.add(my_walls)

    def room_walls(self):
        return self.walls

    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.remove(item)
