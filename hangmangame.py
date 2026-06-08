import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    print("=" * 40)
    print("       🎮 HANGMAN GAME 🎮")
    print("       Hint: Guess a COMPANY NAMES")
    print("=" * 40)

def draw_hangman(wrong):
    stages = [
        """
           -----
               |
               |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
               |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |  
               |
               |
        ==========""",
        """
           -----
           |   |
           O   |
          /|\  |  
          / \  |
               |
        =========="""
    ]
    print(stages[wrong])

def check_win(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def play_game():
    words = ["google", "amazon", "disney", "paypal", "toyota", "oracle", "subway"]
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    while wrong_guesses < max_wrong_guesses:
        draw_hangman(wrong_guesses)
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("Word:", display_word)
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
        print(f"Guessed letters: {' '.join(guessed_letters)}")
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong!")

        # CHECK WIN
        if check_win(word, guessed_letters):
            draw_hangman(wrong_guesses)
            print("\n" + "=" * 40)
            print("🎉 CONGRATULATIONS! YOU WON THE GAME 🎉")
            print("=" * 40)
            print(f"\n✅ The Correct Word Was : {word.upper()}")
            print("\n🏆 Excellent Performance!")
            print("You guessed the hidden word successfully.")
            print("Thank you for playing Hangman Game!\n")
            return

    # GAME OVER
    draw_hangman(wrong_guesses)
    print("\n" + "=" * 40)
    print("💀 GAME OVER!")
    print("=" * 40)
    print(f"\n❌ The Correct Word Was : {word.upper()}")
    print("\nBetter Luck Next Time!\n")

# MAIN PROGRAM
def main():
    clear_screen()
    display_title()
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no) : ").lower()
        if play_again != "yes":
            print("\nThank You For Playing Hangman Game!")
            print("Program Closed Successfully.\n")
            break
        clear_screen()
        display_title()

# RUN PROGRAM
if __name__ == "__main__":
    main()
