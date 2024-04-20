from collections import deque

class PlayerBattingController:
    def __init__(self, playing_11) -> None:
        self.yet_to_play = deque(playing_11)
        self.striker = None
        self.non_striker = None

    def get_next_player(self):
        if not self.yet_to_play:
            raise Exception('No more players available to play')
        
        if self.striker is None:
            self.striker = self.yet_to_play.popleft()
        
        if self.non_striker is None:
            self.non_striker = self.yet_to_play.popleft()

    def get_striker(self):
        return self.striker

    def get_non_striker(self):
        return self.non_striker

    def set_striker(self, player_details):
        self.striker = player_details

    def set_non_striker(self, player_details):
        self.non_striker = player_details