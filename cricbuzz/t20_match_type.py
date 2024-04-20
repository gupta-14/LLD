from match_type import MatchType

class T20MatchType(MatchType):
    def no_of_overs(self) -> int:
        return 20

    def max_over_count_bowlers(self) -> int:
        return 4