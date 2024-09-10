import random

words = ["aardvark","baboon","camel"]
chosen_word = random.choice(words)
print(chosen_word)

guess = input("Enter the letter. In small letter:  ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("incorrect")