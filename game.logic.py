
def get_user_input(valid_choices):
    user_choice = input("Enter rock, paper, or scissors: ")
    while True:
        if user_choice not in valid_choices:
            print("Oops! That's not a valid move. Please enter rock, paper, or scissors.")
        else:
            return user_choice


def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        result = "Draw!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
    else:
        result = "You lose!"

    return(result)



