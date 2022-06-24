# What is this project?
This project is a simple rock paper scissors game that can be played by using hand gestures via camera. I'm using OpenCV to detect user gestures and interact with the machine. 

The goal of the is to score 3 points before the computer does. 

# Milestone 1
I have created a simple model containing 4 classes; rock, paper, scissors and nothing. This model will be used to detect user gestures and play the game.
## Classes
### 1. Rock

<img src="readme_resources/rock.jpg" width="100">

One hand lifted up and clenched into a fist

### 2. Paper

<img src="readme_resources/paper.jpg" width="100">

One hand lifted up with palm fully visible

### 3. Scissors

<img src="readme_resources/scissors.jpg" width="100">

One hand lifted up with index and middle finger fully extended while rest is fully closed

### 4. Nothing
Both hands down

# Milestone 2
I have configured my python environment using miniconda3, I have then used a code snippet to see if I can run it and installed all prerequisites as required. Please see requirements.txt for full list of dependencies.

# Milestone 3
I have create the minimal logic required to make the game playable, currently the game can only be played by manually typing in a choice into the terminal. The game can be run by running main.py and picking the manual version with 'm'.

At this stage the entire game runs on only 4 functions, these are:

| Function | Definition |
| - | - |
get_computer_choice | This function simply picks between "Rock", "Paper or "Scissors" based on random.choice() function.
get_user_choice | This function asks the user to input their choice, it can also shutdown the game if it gets the "Nothing" input.
get_winner | This function determines a winner by comparing inputs and informs the user of the outcome.
play | This function runs the game.

# Milestone 4
I have created a version of the game that can be played using camera and hand gestures. I achieved this by integrating a tensorflow model into my game. The tensorflow model was trained by me. I have coverted the games into classes in order to not repeat myself and used ihneritance to override logic where needed, this has given me an ability to easily alter the flow of the game without having to re-write logic in both classes.

The user now has to pick between the two versions of the game when starting the main.py. 

How I would improve it further:

1. I would add UI letting the user click on which version of the game they want, alternatively perform a check to see if they got a camera and then run the appropriate version.
1. I would add UI elements clearly displaying the score and the number of rounds played above the user camera feedback, and also add a button to play next round.
1. There is some code within the play() function of both versions that is repeating. I could create a more generic function that would reduce the amount of repeated code.
1. Add option to reply the game after it is already finished.