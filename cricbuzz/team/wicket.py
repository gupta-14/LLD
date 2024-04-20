from inning.ball_details import BallDetails
from inning.over_details import OverDetails
# from team.player.player_details import PlayerDetails

class Wicket:
    def __init__(self, wicket_type, taken_by, over_detail, ball_detail):
        self.wicket_type = wicket_type
        self.taken_by = taken_by
        self.over_detail: OverDetails = over_detail
        self.ball_detail: BallDetails = ball_detail