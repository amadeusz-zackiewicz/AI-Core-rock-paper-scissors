class Constants:
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"
    NOTHING = "Nothing"

    # Used to correct inputs
    POSSIBLE_INPUTS = {
        "Rock": ROCK, 
        "rock": ROCK,
        "R": ROCK,
        "r" : ROCK,

        "Paper": PAPER,
        "paper": PAPER,
        "P": PAPER,
        "p": PAPER,

        "Scissors": SCISSORS,
        "scissors": SCISSORS,
        "S": SCISSORS,
        "s": SCISSORS,

        "Nothing": NOTHING,
        "nothing": NOTHING,
        "N": NOTHING,
        "n": NOTHING,
        "": NOTHING
        }

    # Used to inform user of the outcome, these are appended to the full message
    VICTORY_MESSAGE = "and you have won!"
    DEFEAT_MESSAGE = "and you have lost!"
    DRAW_MESSAGE = "and it's a draw!"
    NOTHING_MESSAGE = "and it will not be counted!"

    RESOLUTION_USER_NOTHING = 0
    RESOLUTION_USER_DRAW = 1
    RESOLUTION_USER_WIN = 2
    RESOLUTION_USER_LOST = 3

    # Convienience dictionary to get the score resolution and message appendix by using (user_choice, computer_choice) tuple
    RESOLUTION = {
        (ROCK, ROCK): (RESOLUTION_USER_DRAW, DRAW_MESSAGE),
        (ROCK, PAPER): (RESOLUTION_USER_LOST, DEFEAT_MESSAGE),
        (ROCK, SCISSORS): (RESOLUTION_USER_WIN, VICTORY_MESSAGE),
        (PAPER, ROCK): (RESOLUTION_USER_WIN, VICTORY_MESSAGE),
        (PAPER, PAPER): (RESOLUTION_USER_DRAW, DRAW_MESSAGE),
        (PAPER, SCISSORS): (RESOLUTION_USER_LOST, DEFEAT_MESSAGE),
        (SCISSORS, ROCK): (RESOLUTION_USER_LOST, DEFEAT_MESSAGE),
        (SCISSORS, PAPER): (RESOLUTION_USER_WIN, VICTORY_MESSAGE),
        (SCISSORS, SCISSORS): (RESOLUTION_USER_DRAW, DRAW_MESSAGE),
        (NOTHING, ROCK): (RESOLUTION_USER_NOTHING, NOTHING_MESSAGE),
        (NOTHING, PAPER): (RESOLUTION_USER_NOTHING, NOTHING_MESSAGE),
        (NOTHING, SCISSORS): (RESOLUTION_USER_NOTHING, NOTHING_MESSAGE),
    }