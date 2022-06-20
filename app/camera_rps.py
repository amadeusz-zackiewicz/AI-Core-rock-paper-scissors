from locale import normalize
from app.shared.game import Game
from app.shared.constants import Constants as Const

import time
import cv2
from keras.models import load_model
import numpy as np

class CameraRPS(Game):

    PREDICTION_TO_STRING = [Const.ROCK, Const.PAPER, Const.SCISSORS, Const.NOTHING]

    def __init__(self, best_of = 5, timer = 4.0):
        super().__init__(best_of)

        self.model = load_model("app/model/keras_model.h5")
        self.camera = cv2.VideoCapture(0)
        self.current_frame = None
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        print("\nPress 'p' when you are ready")


    def get_capture(self):
        ret, self.current_frame = self.camera.read()
        cv2.imshow("frame", self.current_frame)

    def get_user_choice(self):
        resized_frame = cv2.resize(self.current_frame, (224, 224), interpolation=cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1
        self.data[0] = normalized_image
        prediction = self.model.predict(self.data)

        best_prediction = 3
        highest_prediction = 0.0
        for i, p in enumerate(prediction[0]):
            if p > highest_prediction:
                highest_prediction = p
                best_prediction = i

        return self.PREDICTION_TO_STRING[best_prediction]

    def play(self) -> bool:
        self.get_capture()

        if cv2.waitKey(1) & 0xFF == ord("p"):
            user_input = self.get_user_choice()
        else:
            user_input = None

        if user_input != None:
            print(f"Round: {self.round_count}")
            print(self.get_winner(user_input, self.get_computer_choice()))
            print(f"You {self.user_score} : {self.computer_score} Computer, playing to best of {self.best_of}")
            print("")
            self.round_count += 1
            if self.user_score == self.max_score:
                print("Well done! You have won!")
                return False
            if self.computer_score == self.max_score:
                print("Sorry, it looks like you lost")
                return False

        return True

        

    def quit(self):
        self.camera.release()
        cv2.destroyAllWindows()