import random

# Convienice constants to use to reduce spelling errors
__ROCK = "Rock"
__PAPER = "Paper"
__SCISSORS = "Scissors"
__NOTHING = "Nothing"

# Used to correct inputs
__POSSIBLE_INPUTS = {
    "Rock": __ROCK, 
    "rock": __ROCK,
    "R": __ROCK,
    "r" : __ROCK,

    "Paper": __PAPER,
    "paper": __PAPER,
    "P": __PAPER,
    "p": __PAPER,

    "Scissors": __SCISSORS,
    "scissors": __SCISSORS,
    "S": __SCISSORS,
    "s": __SCISSORS,

    "Nothing": __NOTHING,
    "nothing": __NOTHING,
    "N": __NOTHING,
    "n": __NOTHING,
    "": __NOTHING
    }

# Used to inform user of the outcome, these are appended to the full message
__VICTORY_MESSAGE = "and you have won!"
__DEFEAT_MESSAGE = "and you have lost!"
__DRAW_MESSAGE = "and it's a draw!"

# Convienience dictionary to get the message appendix by using (user_choice, computer_choice) tuple
__RESOLUTION = {
    (__ROCK, __ROCK): __DRAW_MESSAGE,
    (__ROCK, __PAPER): __DEFEAT_MESSAGE,
    (__ROCK, __SCISSORS): __VICTORY_MESSAGE,
    (__PAPER, __ROCK): __VICTORY_MESSAGE,
    (__PAPER, __PAPER): __DRAW_MESSAGE,
    (__PAPER, __SCISSORS): __DEFEAT_MESSAGE,
    (__SCISSORS, __ROCK): __DEFEAT_MESSAGE,
    (__SCISSORS, __PAPER): __VICTORY_MESSAGE,
    (__SCISSORS, __SCISSORS): __DRAW_MESSAGE
}

def get_computer_choice() -> str:
    """
    Randomly pick between "Rock", "Paper" or "Scissors"
    """
    return random.choice([__ROCK, __PAPER, __SCISSORS])

def get_user_choice():
    """
    Prompts the user with an input message, will shutdown the app if "Nothing" is given
    """
    while True:
        user_input = input("Please pick between Rock, Paper or Scissors, (Nothing to quit): ")

        if user_input in __POSSIBLE_INPUTS:
            return __POSSIBLE_INPUTS[user_input]
        else:
            print(f"'{user_input}' is not a valid input")

def get_winner(user_choice: str, computer_choice: str):
    """
    Print a message informing the user if they have won
    """
    def message(resolution: str):
        print(f"You have chosen {user_choice} against {computer_choice}, {resolution}")

    if user_choice == __NOTHING:
        _ = input("You have chosen to exit, please press enter to close the application: ")
        quit()
    else:
        message(__RESOLUTION[(user_choice, computer_choice)])

def play():
    """
    Play the game in infinite loop, user can use "Nothing" input to stop
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(user_choice, computer_choice)

if __name__ == "__main__":
    
    while True:
        play()