from random import randrange, getrandbits

from maze_api.room import symbol_from

from core.elements.Obstacles import OBSTACLES_ARRAY, ObstacleFactory
from core.items.Item import Coin
from core.maze.GameRoom import GameRoom


class GameMaze:
    __maze = dict()
    skin_manager = None
    obstacle_factory = None

    def __init__(self, skin_manager):
        self.skin_manager = skin_manager
        self.obstacle_factory = ObstacleFactory(self.skin_manager.get_obstacles())

    def create_room(self, room):
        game_room = GameRoom(room.exits, room.kind)

        if room.kind == 1:
            random_obstacle = randrange(0, len(OBSTACLES_ARRAY))
            choosen_obstacle = OBSTACLES_ARRAY[random_obstacle]
            if choosen_obstacle > 0:
                obstacle = self.obstacle_factory.produce_obstacle(choosen_obstacle)
                game_room.add_obstacle(obstacle)

            put_coin = bool(getrandbits(1))

            if put_coin:
                coin_image = self.skin_manager.get_item("coin")
                coin = Coin(coin_image)
                game_room.add_item(coin)

        self.__maze[symbol_from(room.x, room.y)] = game_room

    def room_at(self, x, y):
        symbol = symbol_from(x, y)
        return self.__maze[symbol]
