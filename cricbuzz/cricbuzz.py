from match import Match
from t20_match_type import T20MatchType
from team.team import Team
from team.player.player_details import Person, PlayerDetails, PlayerType

class Main:
    def main(self):
        ob = Main()
        team_a = ob.add_team("India")
        team_b = ob.add_team("SriLanka")
        match_type = T20MatchType()
        match = Match(team_a, team_b, None, "SMS STADIUM", match_type)
        match.start_match()

    def add_team(self, name: str) -> Team:
        player_details = []
        for i in range(1, 12):
            player_details.append(self.add_player(f"{name}{i}", f"{i+20}", PlayerType.ALLROUNDER))

        bowlers = player_details[7:]
        team = Team(name, player_details, [], bowlers)
        return team

    def add_player(self, name: str,age, player_type: str) -> PlayerDetails:
        person = Person(name, age, "")
        player_details = PlayerDetails(person, player_type)
        return player_details

if __name__ == "__main__":
    main = Main()
    main.main()