import random

# 5 predefined words
words = ["apple", "mango", "grape", "peach", "melon"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses:

    # Display the word
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")

    elif guess in word:
        guessed_letters.append(guess)
        print("Correct!")

    else:
        guessed_letters.append(guess)
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# Game Over
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The word was:", word)
