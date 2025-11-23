 Import the random module to allow the computer to make a random choice.
import random

# Define the main function to encapsulate the game logic.
def play_rock_paper_scissors_extended():
    # List of valid choices for the game.
    choices = ['rock', 'paper', 'scissors']
    
    # Initialize player and computer scores to zero.
    player_score = 0
    computer_score = 0
    
    # Display a welcome message to the player.
    print("\n======================================")
    print("  Welcome to Rock, Paper, Scissors!   ")
    print("======================================")
    
    # Start an infinite loop for the game rounds.
    # The loop will break when the player decides to 'quit'.
    while True:
        print("\n--------------------------------------")
        print("          --- New Round ---           ")
        print("--------------------------------------")
        
        # Prompt the player to enter their choice.
        # Convert the input to lowercase for case-insensitive matching.
        player_input = input("Enter your choice (rock, paper, scissors) or 'quit' to end the game: ").lower()
        
        # Check if the player wants to quit the game.
        if player_input == 'quit':
            print("\nThanks for playing! Exiting the game.")
            break # Exit the game loop.
        
        # Validate the player's choice.
        # If the choice is invalid, print an error and continue to the next iteration.
        if player_input not in choices:
            print("Invalid input. Please choose 'rock', 'paper', 'scissors', or 'quit'.")
            print("Let's try that again!")
            continue # Skip the rest of the current round and ask for input again.
            
        # Computer makes a random choice from the list of options.
        computer_choice = random.choice(choices)
        
        # Display both the player's and the computer's choices for the current round.
        print(f"\nYou chose:       {player_input.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determine the winner of the round based on game rules.
        # A tie occurs if both choices are the same.
        if player_input == computer_choice:
            print("It's a tie this round!")
        # Conditions for the player to win.
        elif (
            (player_input == 'rock' and computer_choice == 'scissors') or
            (player_input == 'paper' and computer_choice == 'rock') or
            (player_input == 'scissors' and computer_choice == 'paper')
        ):
            print("Congratulations! You win this round!")
            player_score += 1 # Increment player's score.
        # If not a tie and player didn't win, then the computer wins.
        else:
            print("Oops! Computer wins this round.")
            computer_score += 1 # Increment computer's score.
            
        # Display the current scores after each round.
        print(f"\nCurrent Score: You {player_score} - {computer_score} Computer")
        
    # --- Game Summary after the player quits ---
    print("\n======================================")
    print("            --- Game Over ---         ")
    print("======================================")
    print(f"Final Score: You {player_score} - {computer_score} Computer")
    
    # Determine the overall winner of the game.
    if player_score > computer_score:
        print("Congratulations! You are the ultimate winner!")
    elif computer_score > player_score:
        print("Better luck next time! The Computer reigned supreme.")
    else:
        print("It's a grand tie! What a game!")
    print("\n")

# To play the game, uncomment the line below and run this cell:
# play_rock_paper_scissors_extended()
