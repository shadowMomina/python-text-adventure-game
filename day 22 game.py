# Day 22 - Text Adventure Game with Loop

print("🏰 Welcome to the Adventure Game! 🏰")

while True:  # Game keeps running until user wants to quit
    print("\nYour mission is to find the hidden treasure.\n")

    # First choice
    choice1 = input("You are at a crossroad. Do you want to go LEFT or RIGHT? ").lower()

    if choice1 == "left":
        # Second choice
        choice2 = input("\nYou come to a river. Do you want to SWIM across or WAIT for a boat? ").lower()

        if choice2 == "wait":
            # Third choice
            choice3 = input("\nYou arrive safely at the castle. There are three doors: RED, BLUE, and YELLOW. Which do you choose? ").lower()

            if choice3 == "yellow":
                print("\n🎉 Congratulations! You found the treasure and won the game! 🎉")
            elif choice3 == "red":
                print("\n🔥 The room is full of fire. Game Over.")
            elif choice3 == "blue":
                print("\n🐉 A dragon attacks you. Game Over.")
            else:
                print("\n🚪 That door doesn’t exist. Game Over.")
        else:
            print("\n💦 You tried to swim but were eaten by a crocodile. Game Over.")

    elif choice1 == "right":
        print("\n🐺 You walked into a forest and were attacked by wolves. Game Over.")

    else:
        print("\n❌ Invalid choice. You got lost. Game Over.")

    # Ask if player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing! Goodbye.")
        break
