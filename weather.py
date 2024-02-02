import random

def fall():
    print("It's Fall now.")
    print("The leaves are changing colors.")
def winter():
    print("Winter is coming soon.")
    print("It will be white everywhere.")        
while True:
    weather_choice = input("Which weather do you prefer(F/W): ").upper()
    
    if weather_choice == 'F':
        fall()
    elif weather_choice == 'W':
        winter()
    else:
        random_num = random.randrange(3)
        if random_num == 0:
            winter()
        else:
            fall()
    continue_choice = input("Do you wish to continue(y/n): ").lower()
    if continue_choice != 'y':
        break
