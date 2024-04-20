import random
from inning.inning_details import InningDetails
from team.team import Team
from match_type import MatchType

class Match:
    def __init__(self, teamA, teamB, match_date, venue, match_type) -> None:
        self.teamA: Team = teamA
        self.teamB: Team = teamB
        self.match_date = match_date
        self.venue = venue
        self.toss_winner = None
        self.innings: InningDetails = [None, None]
        self.match_type: MatchType = match_type

    def start_match(self):
        self.toss_winner = self.toss(teamA=self.teamA, teamB=self.teamB)
        
        # Start innings, there are 2 innings in a match
        for inning in range(2):
            batting_team = self.toss_winner if inning == 0 else self.teamA if self.toss_winner == self.teamB else self.teamB
            bowling_team = self.teamB if batting_team == self.teamA else self.teamA
            inning_details = InningDetails(batting_team, bowling_team, self.match_type)
            inning_details.start(-1 if inning == 0 else self.innings[0].get_total_runs())
            self.innings[inning] = inning_details

            # Print inning details
            print()
            print(f"INNING {inning + 1} -- total Run: {batting_team.get_total_runs()}")
            print(f"--- Batting ScoreCard : {batting_team.team_name} ---")
            batting_team.print_batting_score_card()
            print()
            print(f"--- Bowling ScoreCard : {bowling_team.team_name} ---")
            bowling_team.print_bowling_score_card()

        print()
        print("--- WINNER ---")
        print(self.teamA.team_name if self.teamA.is_winner else self.teamB.team_name)



    def toss(self, teamA, teamB):
        if random.random() < 0.5:
            return teamA
        else:
            return teamB