from game_logic import determine_winner
from player import get_user_input
from computer import get_computer_choice

player_score = 0
computer_score = 0
EMOJI_MAP = {
    "rock": "✊",
    "paper": "👋",
    "scissors": "✌️",
}
def get_emoji(choice):
    return EMOJI_MAP.get(choice)
def welcome_user():
    print("Welcome to Rock, Paper, Scissors!")
while True:
    welcome_user()
    play_again = "yes"
    valid_choices = ["rock", "paper", "scissors"]

    user_choice = get_user_input(valid_choices)

    print(f"You chose: {get_emoji(user_choice)}")

    computer_choice = get_computer_choice(valid_choices)

    print(f"Computer chose: {get_emoji(computer_choice)}")

    result = determine_winner(user_choice, computer_choice)

    print(result)

    if result == "You win!":
        player_score += 1
    elif result == "You lose!":
        computer_score += 1
    else:
        continue

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing")
        print(f"Your score: {player_score}")
        print(f"Computer score: {computer_score}")
        break
