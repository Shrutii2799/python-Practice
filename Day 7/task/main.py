print(r'''_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / ` | ' \ / ` | ' ` _ \ / ` | ' \ 
| | | | (| | | | | (| | | | | | | (_| | | | |
|| ||\,|| ||\, || || ||\,|| |_|
                    __/ |                      
                   |_/  '''
      )

import random

main_word = [
    "cat", "dog", "apple", "ball", "book",
    "car", "fish", "tree", "bird", "milk",
    "sun", "cup", "hat", "shoe", "egg",
    "pen", "cake", "frog", "star", "leaf"
]

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /     |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
chosen_word = random.choice(main_word)

# print("Chosen word (for testing):", chosen_word)

length = len(chosen_word)

display = []
for _ in range(length):
    display.append("-")

game_no_over = False

lives = 6
print("\n")
print(f"Choosen letter has {length} words")
while not game_no_over:

    print(display)  # print list structure every loop

    guess = input("Guess a letter: ").lower()

    for position in range(length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    # if guess!=letter:
    #            print("You have entered wrong word")
    # if guess == guess:
    #        print("you have already used this word.")

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You lost a life. Lives remaining: {lives}")
    if lives == 0:
        game_no_over == True
        print("you lose")
        exit()

    if "-" not in display:
        game_no_over = True
        print("you win")
        exit()
    print(stages[lives])