import random

words = ["aardvark","baboon","camel"]
chosen_word = random.choice(words)

word_len = len(chosen_word)
placeholder = ""
for position in range(word_len):
    placeholder = placeholder + "_"
print(placeholder)

guess = input("Enter the letter. In small letter:  ").lower()
print(guess)

display  = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)