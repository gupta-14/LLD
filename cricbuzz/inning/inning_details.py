from typing import List

from match_type import MatchType
from team.team import Team
from inning.over_details import OverDetails


class InningDetails:
    def __init__(self, batting_team: Team, bowling_team: Team, match_type: MatchType) -> None:
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.match_type = match_type
        self.overs: List[OverDetails] = []

    def start(self, runs_to_win: int) -> None:
        try:
            self.batting_team.choose_next_batsman()
        except Exception as e:
            pass

        no_of_overs = self.match_type.no_of_overs()
        for over_number in range(1, no_of_overs + 1):
            self.bowling_team.choose_next_bowler(self.match_type.max_over_count_bowlers())

            over = OverDetails(over_number, self.bowling_team.get_current_bowler())
            self.overs.append(over)

            try:
                won = over.start_over(self.batting_team, self.bowling_team, runs_to_win)
                if won:
                    break
            except Exception as e:
                break

            self.batting_team.striker, self.batting_team.non_striker = self.batting_team.non_striker, self.batting_team.striker

    def get_total_runs(self) -> int:
        return self.batting_team.get_total_runs()