from inning.run_type import RunType
# from cricbuzz.inning.ball_details import BallDetails
from score_updater.score_updater_observer import ScoreUpdaterObserver
from inning.ball_type import BallType

class BowlingScoreUpdater(ScoreUpdaterObserver):
    def update(self, ball_details) -> None:
        if ball_details.ball_number == 6 and ball_details.ball_type == BallType.NORMAL:
            ball_details.bowled_by.bowling_score_card.total_overs_count += 1

        if ball_details.run_type == RunType.ONE:
            ball_details.bowled_by.bowling_score_card.runs_given += 1
        elif ball_details.run_type == RunType.TWO:
            ball_details.bowled_by.bowling_score_card.runs_given += 2
        elif ball_details.run_type == RunType.FOUR:
            ball_details.bowled_by.bowling_score_card.runs_given += 4
        elif ball_details.run_type == RunType.SIX:
            ball_details.bowled_by.bowling_score_card.runs_given += 6

        if ball_details.wicket is not None:
            ball_details.bowled_by.bowling_score_card.wickets_taken += 1

        if ball_details.ball_type == BallType.NOBALL:
            ball_details.bowled_by.bowling_score_card.no_ball_count += 1

        if ball_details.ball_type == BallType.WIDEBALL:
            ball_details.bowled_by.bowling_score_card.wide_ball_count += 1