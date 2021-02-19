from random import randrange

from GameRoom import GameRoom
from core.elements.Obstacles import OBSTACLES_ARRAY
from maze_api.room import symbol_from


class GameMaze:
    __maze = dict()

    def create_room(self, room):
        obstacle = 0

        if room.kind == 1:
            obstacle = randrange(0, len(OBSTACLES_ARRAY))

        game_room = GameRoom(room.exits, room.kind, obstacle)
        self.__maze[symbol_from(room.x, room.y)] = game_room

    def room_at(self, x, y):
        symbol = symbol_from(x, y)
        return self.__maze[symbol]
