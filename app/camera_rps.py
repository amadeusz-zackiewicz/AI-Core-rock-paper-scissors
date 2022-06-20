from app.shared.game import Game
from app.shared.constants import Constants as Const
import time

class CameraRPS(Game):
    def __init__(self, best_of = 5, timer = 3.0):
        super(self, best_of)

        self.max_time = timer
        self.time = time.time()

    def get_user_choice(self):
        pass

    def play(self):
        pass