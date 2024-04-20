from team.player.player_batting_controller import PlayerBattingController
from team.player.player_bowling_controller import PlayerBowlingController

class Team:
    def __init__(self, team_name, playing_11, bench, bowlers) -> None:
        self.team_name = team_name
        self.playing_11 = playing_11
        self.bench = bench
        self.batting_controller: PlayerBattingController = PlayerBattingController(self.playing_11)
        self.bowling_controller: PlayerBowlingController = PlayerBowlingController(bowlers)
        self.is_winner = False

    def get_team_name(self):
        return self.team_name
    
    def choose_next_batsman(self):
        self.batting_controller.get_next_player()

    def choose_next_bowler(self, max_over_count_per_bowler):
        self.bowling_controller.get_next_bowler(max_over_count_per_bowler)

    def get_striker(self):
        return self.batting_controller.get_striker()

    def get_non_striker(self):
        return self.batting_controller.get_non_striker()

    def set_striker(self, player):
        self.batting_controller.set_striker(player)

    def set_non_striker(self, player):
        self.batting_controller.set_non_striker(player)

    def get_current_bowler(self):
        return self.bowling_controller.get_current_bowler()

    def print_batting_score_card(self):
        for player_details in self.playing_11:
            player_details.print_batting_score_card()

    def print_bowling_score_card(self):
        for player_details in self.playing_11:
            if player_details.bowling_score_card.total_overs_count > 0:
                player_details.print_bowling_score_card()

    def get_total_runs(self):
        total_runs = 0
        for player in self.playing_11:
            total_runs += player.batting_score_card.total_runs
        return total_runs