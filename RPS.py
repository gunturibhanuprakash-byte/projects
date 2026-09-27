# Rock Paper Scissors Game
# Ask the user for their choice (rock, paper, or scissors)
# Generate a random choice for the computer
# Compare the user's choice with the computer's choice
# Determine the winner based on the rules of the game
# Repeat the process until the user decides to quit
import random

emojis={
    'r': '✊',  # Rock
    'p': '✋',  # Paper
    's': '✌️'   # Scissors
}#emojis to represent rock, paper, and scissors


print("Welcome to Rock, Paper, Scissors!")
print("Enter your choice (r, p, s) or 'q' to exit.")

while True:
    user_choice = input("Your choice: ").lower()
    if user_choice == 'q':
        print("Thanks for playing!")
        break
    elif user_choice not in ['r', 'p', 's']:
        print("Invalid choice. Please try again.")
        continue
    print(f"You chose: {emojis[user_choice]}")
    computer_choice = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("Computer wins!")
        print("Do you want to play again? (y/n)")
        play_again = input().lower()
        if play_again == 'n':
            print("Thanks for playing!")
            break    
