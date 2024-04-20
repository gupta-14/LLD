from inning.run_type import RunType
# from inning.ball_details import BallDetails
from score_updater.score_updater_observer import ScoreUpdaterObserver

class BattingScoreUpdater(ScoreUpdaterObserver):
    def update(self, ball_details) -> None:
        run = 0

        if ball_details.run_type == RunType.ONE:
            run = 1
        elif ball_details.run_type == RunType.TWO:
            run = 2
        elif ball_details.run_type == RunType.FOUR:
            run = 4
            ball_details.played_by.batting_score_card.total_fours += 1
        elif ball_details.run_type == RunType.SIX:
            run = 6
            ball_details.played_by.batting_score_card.total_six += 1

        ball_details.played_by.batting_score_card.total_runs += run
        ball_details.played_by.batting_score_card.total_balls_played += 1

        if ball_details.wicket is not None:
            ball_details.played_by.batting_score_card.wicket_details = ball_details.wicket