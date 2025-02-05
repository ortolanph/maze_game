from core.items.Item import Coin


class AchievementManager:
    _collected_coins = []
    _visited_rooms = []

    def add_coins(self, coin: Coin):
        self._collected_coins.append(coin)

    def add_visited_room(self, room_id):
        if room_id not in self._visited_rooms:
            self._visited_rooms.append(room_id)

    def report(self):
        return f'''
        Total Collected Coins: {self._collected_coins} 
        Total Visited Rooms: {len(self._visited_rooms)} 
        '''
