from core.items.Item import Coin
from core.observers.achievement_manager import AchievementManager
from core.observers.events import RoomVisitedEvent, TreasureCollectedEvent, MazeFinishedEvent


class EventManager(RoomVisitedEvent, TreasureCollectedEvent, MazeFinishedEvent):
    _manager = AchievementManager()

    def on_collect_treasure(self, coin: Coin):
        self._manager.add_coins(coin)

    def on_enter_room(self, roomId):
        self._manager.add_visited_room(roomId)

    def on_finish_maze(self):
        print(self._manager.report())
