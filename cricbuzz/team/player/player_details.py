from team.player.score.batting_score_card import BattingScoreCard
from team.player.score.bowling_score_card import BowlingScoreCard
from .person import Person
from .player_type import PlayerType

class PlayerDetails:
    def __init__(self, person: Person, player_type: PlayerType):
        self.person = person
        self.player_type = player_type
        self.batting_score_card = BattingScoreCard()
        self.bowling_score_card = BowlingScoreCard()

    def print_batting_score_card(self):
        print("PlayerName:", self.person.name, "-- totalRuns:", self.batting_score_card.total_runs,
              "-- totalBallsPlayed:", self.batting_score_card.total_balls_played,
              "-- 4s:", self.batting_score_card.total_fours,
              "-- 6s:", self.batting_score_card.total_six,
              "-- outby:", self.batting_score_card.wicket_details.taken_by.person.name if self.batting_score_card.wicket_details else "notout")

    def print_bowling_score_card(self):
        print("PlayerName:", self.person.name, "-- totalOversThrown:", self.bowling_score_card.total_overs_count,
              "-- totalRunsGiven:", self.bowling_score_card.runs_given,
              "-- WicketsTaken:", self.bowling_score_card.wickets_taken)