import random

def fall():
    print("It's Fall now.")
    print("The leaves are changing colors.")
def winter():
    print("Winter is coming soon.")
    print("It will be white everywhere.")
def spring():
    print("Spring is close.")
    print("April showers bring May flowers!")
def summer():
    print("Its summer time!")
    print("Make hay while the sun shines.")

seasons = {
    'F': fall,
    'W': winter,
    'SP': spring,
    'SU': summer
}

while True:
    weather_choice = input("Which weather do you prefer(F/W/Sp/Su): ").upper()
    
    if weather_choice in seasons:
        seasons[weather_choice]()
    else:
        random.choice(list(seasons.values()))()
        
    continue_choice = input("Do you wish to continue(y/n): ").lower()
    if continue_choice != 'y':
        break
