def get_user_input(valid_choices):

    user_choice = input("Enter rock, paper, or scissors: ")
    while True:
        if user_choice not in valid_choices:
            print("Oops! That's not a valid move. Please enter rock, paper, or scissors.")
            user_choice = input("Enter rock, paper, or scissors: ")
        else:
            return user_choice
            break
