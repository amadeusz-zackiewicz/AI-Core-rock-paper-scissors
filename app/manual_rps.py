from app.shared.game import Game
from app.shared.constants import Constants as Const

class ManualRPS(Game):

    def get_user_choice(self):
        """
        Prompts the user with an input message, will shutdown the app if "Nothing" is given
        """
        while True:
            user_input = input("Please pick between Rock, Paper or Scissors: ")

            if user_input in Const.POSSIBLE_INPUTS:
                return Const.POSSIBLE_INPUTS[user_input]
            else:
                print(f"'{user_input}' is not a valid input")

            
    def play(self):
        """
        Play the game in infinite loop, user can use "Nothing" input to stop
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"Round: {self.round_count}")
        print(self.get_winner(user_choice, computer_choice))
        print(f"You {self.user_score} : {self.computer_score} Computer, playing to best of {self.best_of}")
        print("")
        self.round_count += 1

        if self.user_score == self.max_score:
            print("Well done! You have won!")
            quit()
        if self.computer_score == self.max_score:
            print("Sorry, it looks like you lost")
            quit()

if __name__ == "__main__":
    
    g = ManualRPS()

    while True:
        g.play()