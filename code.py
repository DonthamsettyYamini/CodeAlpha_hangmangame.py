import random

# Step 1: List of words
words = ["red", "blue", "green",  "pink", "black", "white", "brown"]
# Step 2: Choose random word
secret_word = random.choice(words)
# Step 3: Store guessed letters
guessed_letters = []
# Step 4: Limit wrong guesses
wrong_guesses = 0
max_wrong_guesses = 5

print("Welcome to Hangman Game!")
print("Hint: The word is a COLOR")

# Game loop
while wrong_guesses < max_wrong_guesses:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Good guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong! {max_wrong_guesses - wrong_guesses} guesses left.")
    if "_" not in display_word:
        print("Congratulations! You guessed the word!")
        break

if wrong_guesses >= max_wrong_guesses:
    print(f"Game over! The word was: {secret_word}")