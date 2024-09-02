print("Welcome to Treashure Island \n Your mission is to find a treasure!")
side = input("Enter which side right or left")

if side == "right":
    print("game over")
elif side == "left":
    print("continue game")
    howtoget = input(" enter how to get there  swim or wait")
    if howtoget == "swim":
        print("game over")
    elif howtoget == "wait":
        print("continue game")
        door = input("Enter the the which door you want to enter. blue red and yellow")
        if door == "blue":
            print("game over")
        elif door == "red":
            print("red")
        elif door == "yellow":
            print("you win")
        else:
            print("enter valid option")

    else:
        print("enter valid option")

else:
    print(" enter valid option")