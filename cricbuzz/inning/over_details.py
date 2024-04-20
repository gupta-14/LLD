from inning.ball_type import BallType
# from team.team import Team
from inning.run_type import RunType
# from team.wicket import Wicket
# from team.player.player_details import PlayerDetails


class OverDetails:
    def __init__(self, over_number: int, bowled_by) -> None:
        self.over_number = over_number
        self.balls = []
        self.extra_balls_count = 0
        self.bowled_by = bowled_by

    def start_over(self, batting_team, bowling_team, runs_to_win: int) -> bool:
        from inning.ball_details import BallDetails
        ball_count = 1
        while ball_count <= 6:
            ball = BallDetails(ball_count)
            ball.start_ball_delivery(batting_team, bowling_team, self)
            if ball.ball_type == BallType.NORMAL:
                self.balls.append(ball)
                ball_count += 1
                if ball.wicket:
                    batting_team.choose_next_batsman()

                if runs_to_win != -1 and batting_team.get_total_runs() >= runs_to_win:
                    batting_team.is_winner = True
                    return True
            else:
                self.extra_balls_count += 1

        return False
