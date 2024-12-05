import random
# Todo-9 - Update the word list to sue the 'word_list' from hangman_words.py

from hangman_words import word_list
from hangmanArt import stages
from HangmanLogo import logo


print(logo)


# Todo-8 - Create a variable called lives to keep track of the number of lives left. set lives to equal to 6
lives = 6

# Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. then print it

chosen_word = random.choice(word_list)
print(chosen_word)

# Todo-4: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase letters
# todo-6 - Use a while to let the user guess again
game_over = False
correct_letters = []
# Todo-5 - Create a "Display" that puts the guess letter in the right position and _ in the rest of the string.
while not game_over:
    print(f"********{lives}/6 Lives Left********")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""

    # Todo-3 - Check if the letter the user guessed (guess) is on of the Letter in the chosen_word. Print "Right" if it is , "Wrong" if it's not
    # Todo-7 - Change the for loop so that you keep the previous correct letters

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    # Todo-9 - if guess is no a letter in the chosen_word, then Reduce lives by 1. if lives goes down to 0 then the game should end, and it should print "You lose"

    if guess not in chosen_word:
        lives -= 1
        print(f"You gessed {guess}, that's not in the word, you lose a life.")
        if lives == 0:
            game_over = True
            # update the print statement below to give the user the correct word that they are trying to guess
            print(f"******** IT WAS{chosen_word}!YOU LOSE ********")

    if "_" not in display:
        game_over = True
        print("You Win.")

    # Todo-10 - print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.

    print(stages[lives])
