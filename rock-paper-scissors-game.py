import random
choices = ['Rock', 'Paper', 'Scissors']
user_score = 0
computer_score = 0

def get_user_choice():
    """
    Get the user's choice of Rock, Paper, or Scissors.
    """
    while True:
        try:
            user_input = int(input("Choose your option:\n1. Rock\n2. Paper\n3. Scissors\nEnter 1, 2, or 3: "))
            if user_input in [1, 2, 3]:
                user_choice = choices[user_input - 1]
                print(f"You chose: {user_choice}")
                return user_choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    """
    Randomly generate the computer's choice of Rock, Paper, or Scissors.
    """
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    return computer_choice

def determiner(user_choice, computer_choice):
    """
    Determine the winner of the round and update scores.
    """
    global user_score, computer_score

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif ((user_choice == 'Rock' and computer_choice == 'Scissors') or
          (user_choice == 'Paper' and computer_choice == 'Rock') or
          (user_choice == 'Scissors' and computer_choice == 'Paper')):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    """Showing current scores"""
    print(f"Current Scores - you: {user_score}, computer: {computer_score}\n")

def overall_winner(user_score, computer_score):
    """
    Announce the overall winner after all rounds.
    """
    print(f"Final Scores - you: {user_score}, computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif computer_score > user_score:
        print("Computer is the overall winner! Better luck next time.")
    else:
        print("It's a tie!")

"""
Main code
"""
if __name__ == "__main__":
    print("Let's Play Rock, Paper, Scissors!")
    while True:
        try:
            option = int(input("1. Start Game\n2. Exit\nChoose an option: "))
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

        if option == 1:
            try:
                rounds = int(input("Enter number of rounds to play: "))
            except ValueError:
                print("Invalid input. Please enter a valid number of rounds.")      
                continue
            print(f"This game is best of {rounds} rounds.\n")
            
            for r in range(1, rounds + 1):
                print(f"Round {r}:")
                user_choice = get_user_choice()
                computer_choice = get_computer_choice()
                determiner(user_choice, computer_choice)
            
            overall_winner(user_score, computer_score)

        elif option == 2:
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1 or 2.")