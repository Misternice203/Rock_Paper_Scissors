### Rock_Paper_Scissors
Simple rock, paper, scissors game using Command Line Interface.

## Overview
This is a command line Rock Paper Scissors game built using Python.
The user plays against the computer, using input validation, game logic, and score tracking.
I created this project as part of my Python learning journey.

## Features
* User vs Computer gameplay
* Randomized computer choices
* Input validation (handles invalid input by asking for correct choice)
* score tracking
* Replay option to continue playing the game

## Technologies Used
* Python 3.14
* VS Code

## Project Structure 
* Main.py (base game logic)
* game.logic (funcitons including get_user_input and determine_winner)
* player.py (functions for user choices)
* computer.py (functions for random computer choices)

## How to play
* Enter one of the choices:
  * Rock
  * Paper
  * Scissors
* Computer randomly selects a option that is in the valid choices list
* Winner decided based off the standard rules of the game
* Scoreboard shows score at the end of the game when user selects to quit

## What i learned
* How to structure programs using functions
* Handling user input and validation
* Using the random module
* Storing different functions in multiple folders for cleaner code
* How to add emojis to a project

## Future Improvements
* Add GUI version
* Track win/loss history across sessions
* Convert into web app using Flask
