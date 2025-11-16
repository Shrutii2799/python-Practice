print("welcome to the tresure island")
print("Your mission is to find tresure")

choice1 = input("Your at a cross road, where do you want to go?\n  Type left or right ")

if choice1 == "right":
    print("Game over")

elif choice1 == "left":
    print(" You've come to lake. There is an island in the middle of the lake ")
    choice2 = input("Type wait to wait for a boat.Type swim to swim across")

    if choice2 == "wait":
        print("You arrvied at the island. there is a house with three doors")
        choice3 = input("One red,one yellow and one blue. which colour do you choose")

        if choice3 == "red":
            print("It's a room full of fire. game over")

        elif choice3 == "yellow":
            print("You found the treasure! YOU WON!")

        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")

        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("you typed wrong input")

else:
    print("you typed wrong input")

