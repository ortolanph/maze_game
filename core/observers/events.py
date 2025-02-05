class RoomVisitedEvent:

    def on_enter_room(self, roomId):
        pass


class TreasureCollectedEvent:

    def on_collect_treasure(self, amount):
        pass


class MazeFinishedEvent:

    def on_finish_maze(self):
        pass
