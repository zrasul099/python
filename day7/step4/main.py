import random

stages = ['''
    +---
    |   |
    0   |
   /|\  |
   / \  |
        |
=========  
''',  '''
    +---
    |   |
    0   |
   /|\  |
   /    |
        |
=========  
''',  '''
    +---
    |   |
    0   |
   /|\  |
        |
        |
=========  
''',  '''
    +---
    |   |
    0   |
   /|   |
        |
        |
=========  
''',  '''
    +---
    |   |
    0   |
   /    |
        |
        |
=========  
''',  '''
    +---
    |   |
    0   |
        |
        |
        |
=========  
''',  '''
    +---
    |   |
        |
        |
        |
        |
=========  
'''

]

words = ["aardvark","baboon","camel"]
lives = 6
chosen_word = random.choice(words)

word_len = len(chosen_word)
placeholder = ""
for position in range(word_len):
    placeholder = placeholder + "_"
print(placeholder)
game_over = False
correct_letters = []
while not game_over :
    guess = input("Enter the letter. In small letter:  ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        game_over = True
        print("you lose")
    if "_" not in display:
        game_over = True
        print("you won")

    print(stages[lives])
    print("hello")
