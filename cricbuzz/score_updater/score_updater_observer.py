from abc import ABC, abstractmethod
# from inning.ball_details import BallDetails

class ScoreUpdaterObserver(ABC):
    @abstractmethod
    def update(self, ball_details) -> None:
        pass