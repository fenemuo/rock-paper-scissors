'''
create a simple rock, paper, scissors game
provide a welcome message
get the user's choice
generate a random choice for the computer
compare the choices and determine the winner
display the result
ask the user if they want to play again
say goodbye and end the game when the user chooses not to play again
use one function for the logic
'''
import random

def play_rps():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    key_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    while True:
        raw = input("Enter your choice (r=rock, p=paper, s=scissors): ").strip().lower()
        if raw in key_map:
            user_choice = key_map[raw]
        elif raw in choices:  # optional: allow full words too
            user_choice = raw
        else:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
        else:
            result = "You lose!"

        print(result)

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    play_rps()

