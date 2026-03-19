import random

# Hangman stages
stages = [
'''
  +-----+
  |     |
        |
        |
        |
        |
==========
''',
'''
  +-----+
  |     |
  O     |
        |
        |
        |
==========
''',
'''
  +-----+
  |     |
  O     |
  |     |
        |
        |
==========
''',
'''
  +-----+
  |     |
  O     |
 /|     |
        |
        |
==========
''',
'''
  +-----+
  |     |
  O     |
 /|\    |
        |
        |
==========
''',
'''
  +-----+
  |     |
  O     |
 /|\    |
 / \    |
        |
==========
'''
]


word_list = ["tiger", "lion", "elephant", "panda", "zebra", "monkey"] # Word list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 5
display = ["_"] * word_length
guessed_letters = []
print("------------------------------------------")
print("!!! Welcome to Hangman Game !!!")
print("Guess the word before the man is hanged!")
print("Hint: Guess Animals Name...")

game_over = False

while not game_over:
    print("------------------------------------------")
    print("\nWord: ", " ".join(display))
    print("Remaining Lives:", lives)
    print("Guessed Letters:", guessed_letters)

    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")

        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print("Wrong guess!")

    print(stages[5 - lives])

    if "_" not in display:
        print("\n!!!! Congratulations !!! You Win !!!")
        print("The word was:", chosen_word)
        game_over = True

    if lives == 0:
        print("\n!!!! Game Over !!! You Lose !!!")
        print("The word was:", chosen_word)
        game_over = True