import random

def get_user_choice():
    """Prompts the user for a choice and validates the input."""
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("❌ Invalid choice. Please type 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Game Logic: Determines the winner.
    Returns: 'win', 'lose', or 'tie'.
    """
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_round_result(user_choice, computer_choice, result, user_score, computer_score):
    """Displays the result of the round and the current scores."""
    
    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

    if result == 'win':
        print("🎉 You win this round!")
    elif result == 'lose':
        print("💻 Computer wins this round!")
    else:
        print("🤝 It's a tie!")
    print(f"Current Score: You {user_score} | Computer {computer_score}")

def play_game():
    """Main function to run the Rock-Paper-Scissors game with multiple rounds."""
    
    user_score = 0
    computer_score = 0
    

    print("====================================")
    print("  ✊✋✌️ Rock-Paper-Scissors Game ")
    print("====================================")
    print("Rules: Rock > Scissors, Scissors > Paper, Paper > Rock.")

    while True:
        print("\n--- NEW ROUND ---")
        

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1
        
        display_round_result(user_choice, computer_choice, result, user_score, computer_score)
        
        play_again = input("\nDo you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            break
    print("\n====================================")
    print("           Game Over!             ")
    print(f"FINAL SCORE: You {user_score} | Computer {computer_score}")
    
    if user_score > computer_score:
        print("🏆 Congratulations! You won the game overall!")
    elif computer_score > user_score:
        print("😞 The computer won the game overall. Better luck next time!")
    else:
        print("🤝 It's an overall tie!")
    print("====================================")
    
    
if __name__ == "__main__":
    play_game()