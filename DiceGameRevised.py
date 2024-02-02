import random

def roll_single_dice():
    return random.randint(1, 6)

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ["yes", "no"]:
            return user_input
        else:
            print("Please enter 'yes' or 'no'.")

def roll_dice():
    total_score = 0

    while True:
        user_input = get_user_input("Do you want to roll a dice? (yes/no): ")
        
        if user_input == "yes":
            dice_roll = roll_single_dice()
            total_score += dice_roll
            print(f"You rolled a {dice_roll}. Total score: {total_score}.")
        elif user_input == "no":
            print(f"Game over. Your final score is {total_score}. Thank you for playing!")
            break

        roll_again = get_user_input("Would you like to roll again? (yes/no): ")
        if roll_again != "yes":
            print(f"Game over. Your final score is {total_score}. Thank you for playing!")
            break

if __name__ == "__main__":
    roll_dice()
