# Convienice constants to use to reduce spelling errors
from math import ceil
from .constants import constants as const
import random

YOLO = "YOLO"

class game:

    def __init__(self, best_of = 5):
        self.best_of = best_of
        self.max_score = int(ceil(best_of / 2))
        self.user_score = 0
        self.computer_score = 0
        self.round_count = 0


    def get_winner(self, user_choice: str, computer_choice: str):
        def construct_message(appendix: str):
            return 

        resolution = const.RESOLUTION[(user_choice, computer_choice)]
        if resolution[0] == const.RESOLUTION_USER_WIN:
            self.user_score += 1
        elif resolution[0] == const.RESOLUTION_USER_LOST:
            self.computer_score += 1

        return f"You have chosen {user_choice} against {computer_choice}, {resolution[1]}"
            

    def get_computer_choice(self) -> str:
        """
        Randomly pick between "Rock", "Paper" or "Scissors"
        """
        return random.choice([const.ROCK, const.PAPER, const.SCISSORS])

    def get_user_choice(self):
        pass

    def play(self):
        pass