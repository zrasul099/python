import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Randomly select choices for the player and computer
random_my = random.choice(choices)
random_comp = random.choice(choices)

# Print the choices
print(f"You chose: {random_my}")
print(f"Computer chose: {random_comp}")

if random_my == random_comp:
    print("equal")
elif (random_my == "rock" and random_comp == "paper") \
        or (random_my == "paper" and random_comp == "scissors") \
        or (random_my == "scissors" and random_comp == "rock"):
    print("you are lost")
else:
    print(" you won")

my_choice = input("Enter rock paper or scissors")

if random_my == random_comp:
    print("equal")
elif (my_choice == "rock" and random_comp == "paper") \
        or (my_choice == "paper" and random_comp == "scissors") \
        or (my_choice == "scissors" and random_comp == "rock"):
    print("you are lost")
else:
    print(" you won")