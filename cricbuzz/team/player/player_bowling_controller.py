from typing import List, Deque
from collections import deque

from .player_details import PlayerDetails

class PlayerBowlingController:
    def __init__(self, bowlers: List[PlayerDetails]):
        self.bowlers_list: Deque[PlayerDetails] = deque()
        self.bowler_vs_over_count = {}
        self.current_bowler = None
        self.set_bowlers_list(bowlers)

    def set_bowlers_list(self, bowlers_list: List[PlayerDetails]):
        self.bowlers_list = deque(bowlers_list)
        self.bowler_vs_over_count = {bowler: 0 for bowler in bowlers_list}

    def get_next_bowler(self, max_over_count_per_bowler: int):
        player_details = self.bowlers_list.popleft()
        if self.bowler_vs_over_count[player_details] + 1 == max_over_count_per_bowler:
            self.current_bowler = player_details
        else:
            self.current_bowler = player_details
            self.bowlers_list.append(player_details)
            self.bowler_vs_over_count[player_details] += 1

    def get_current_bowler(self):
        return self.current_bowler