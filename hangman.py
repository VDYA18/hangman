import random


def get_random_word():
    # A list of words for the game. You can expand this list with more words.
    words = ['python', 'hangman', 'programming', 'developer', 'challenge', 'game']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    guessed_word = set()

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining attempts: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print(f"'{guess}' is not in the word. You have {attempts} attempts left.")
            
        if attempts == 0:
            print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()
