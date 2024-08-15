import random

# Assuming these lists are defined elsewhere in your 'wordss' module
from wordss import easy, intermediate, hard

def actually_word():
    level = input("Enter the level (easy, intermediate, hard): ").strip().lower()
    if level == "easy":
        return random.choice(easy)
    elif level == "intermediate":
        return random.choice(intermediate)
    elif level == "hard":
        return random.choice(hard)
    else:
        print("Invalid level.")
        return None  # Ensure a return value is provided when level is invalid

def display_word(guessed_word, main_word):
    displayed = []
    for letter in main_word:
        if letter in guessed_word:
            displayed.append(letter)
        else:
            displayed.append("_")
    return ''.join(displayed)

def hangman():
    print("Welcome to Hangman!")

    # Get number of players
    while True:
        try:
            num_players = int(input("Enter how many players want to play (2 to 4): "))
            if num_players < 2 or num_players > 4:
                print("Invalid number of players. Please choose between 2 and 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Initialize player names and scores
    player_names = []
    scores = {}
    for i in range(num_players):
        player_name = input(f"Enter the name for player {i + 1}: ").strip()
        player_names.append(player_name)
        scores[player_name] = 0

    # Play game
    while True:
        for player_name in player_names:
            main_word = actually_word()
            guessed_word = set()
            attempts = 6
            
            print(f"\n{player_name}'s turn!")
            print(f"The word has {len(main_word)} letters.")

            while attempts > 0:
                print(display_word(guessed_word, main_word))
                print(f"Guessed letters: {''.join(sorted(guessed_word))}")
                print(f"Remaining attempts: {attempts}")
                
                guess = input("Enter a letter: ").strip().lower()
                
                if len(guess) != 1 or not guess.isalpha():
                    print("Invalid input. Please enter a single letter.")
                    continue
                
                if guess in guessed_word:
                    print("You already guessed that letter.")
                    continue
                
                guessed_word.add(guess)
                
                if guess in main_word:
                    print(f"Good guess! '{guess}' is in the word.")
                    if all(letter in guessed_word for letter in main_word):
                        print(f"Congratulations {player_name}! You guessed the word: {main_word}")
                        scores[player_name] += 1  # Correctly update the player's score
                        break
                else:
                    attempts -= 1
                    print(f"'{guess}' is not in the word. You have {attempts} attempts left.")
                    
                if attempts == 0:
                    print(f"Game over for {player_name}! The word was: {main_word}")

        # Display scores
        print("\nScores:")
        for player, score in scores.items():
            print(f"{player}: {score}")
        
        # Ask if players want to play again
        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again == 'no':
            print("Thanks for playing!")
            break

# Ensure this code is run only if this script is executed directly
if __name__ == "__main__":
    hangman()


                             
                
