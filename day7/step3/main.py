import random


words = ["aardvark","baboon","camel"]
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
    if "_" not in display:
        game_over = True
        print("you won")
