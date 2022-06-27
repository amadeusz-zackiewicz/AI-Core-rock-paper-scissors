# Convienice constants to use to reduce spelling errors
from math import ceil
from .constants import Constants as Const
import random

class Game:

    def __init__(self, best_of = 5):
        self.best_of = best_of
        self.max_score = int(ceil(best_of / 2))
        self.user_score = 0
        self.computer_score = 0
        self.round_count = 0


    def get_winner(self, user_choice: str, computer_choice: str):
        def construct_message(appendix: str):
            return 

        resolution = Const.RESOLUTION[(user_choice, computer_choice)]
        if resolution[0] == Const.RESOLUTION_USER_WIN:
            self.user_score += 1
        elif resolution[0] == Const.RESOLUTION_USER_LOST:
            self.computer_score += 1

        return f"You have chosen {user_choice} against {computer_choice}, {resolution[1]}"
            

    def get_computer_choice(self) -> str:
        """
        Randomly pick between "Rock", "Paper" or "Scissors"
        """
        return random.choice([Const.ROCK, Const.PAPER, Const.SCISSORS])

    def get_user_choice(self):
        pass

    def play(self) -> bool:
        pass

    def quit(self):
        pass
