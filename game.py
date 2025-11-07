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
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
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
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Goodbye!")
            break
if __name__ == "__main__":
    play_rps()

    