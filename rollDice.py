import random

def roll_dice():
    while True:
        # Ask the user if they want to roll the dice
        user_input = input("Do you want to roll a dice? (yes/no): ").strip().lower()
        if user_input == "yes":
            # Generate a random number between 1 and 6
            dice_roll = random.randint(1, 6)
            print(f"You rolled a {dice_roll}.")
        elif user_input == "no":
            print("Game over. Thank you for playing!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

        # Ask if the user wants to roll again
        roll_again = input("Would you like to roll again? (yes/no): ").strip().lower()
        if roll_again != "yes":
            print("Game over. Thank you for playing!")
            break

if __name__ == "__main__":
    roll_dice()
