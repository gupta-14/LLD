from typing import List
import random

from inning.ball_type import BallType
from inning.run_type import RunType
from inning.over_details import OverDetails

from team.wicket_type import WicketType
from score_updater.batting_score_updater import BattingScoreUpdater
from score_updater.bowling_score_updater import BowlingScoreUpdater
from score_updater.score_updater_observer import ScoreUpdaterObserver


class BallDetails:
    def __init__(self, ball_number: int) -> None:
        self.ball_number = ball_number
        self.ball_type = BallType.NORMAL
        self.run_type = None
        self.played_by = None
        self.bowled_by = None
        self.wicket = None
        self.score_updater_observer_list: List[ScoreUpdaterObserver] = [
            BowlingScoreUpdater(),
            BattingScoreUpdater()
        ]

    def start_ball_delivery(self, batting_team, bowling_team, over: OverDetails) -> None:
        from team.wicket import Wicket
        self.played_by = batting_team.striker
        self.bowled_by = over.bowled_by
        # THROW BALL AND GET THE BALL TYPE, assuming here that ball type is always NORMAL
        self.ball_type = BallType.NORMAL

        # wicket or no wicket
        if self.is_wicket_taken():
            self.run_type = RunType.ZERO
            # considering only BOLD
            self.wicket = Wicket(WicketType.BOLD, bowling_team.current_bowler, over, self)
            # making only striker out for now
            batting_team.striker = None
        else:
            self.run_type = self.get_run_type()

            if self.run_type in [RunType.ONE, RunType.THREE]:
                # swap striker and non striker
                batting_team.striker, batting_team.non_striker = batting_team.non_striker, batting_team.striker

        # update player scoreboard
        self.notify_updaters()

    def notify_updaters(self) -> None:
        for observer in self.score_updater_observer_list:
            observer.update(self)

    def get_run_type(self) -> RunType:
        val = random.random()
        if val <= 0.2:
            return RunType.ONE
        elif 0.3 <= val <= 0.5:
            return RunType.TWO
        elif 0.6 <= val <= 0.8:
            return RunType.FOUR
        else:
            return RunType.SIX

    def is_wicket_taken(self) -> bool:
        # random function returns a value between 0 and 1
        return random.random() < 0.2
