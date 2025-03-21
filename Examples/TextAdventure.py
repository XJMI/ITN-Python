import random
from colorama import Fore

def randomEncounter():
    randomNumber = random.randint(1, 22)

    if randomNumber < 3:
        print(f"{Fore.RED}You encounter the christmas tree monster and of course you are dead{Fore.RESET}")
        return -1
    elif randomNumber > 19:
        print(f"{Fore.GREEN}You found a gold frog{Fore.RESET}")
        return 1
    elif randomNumber > 12:
        print(f"{Fore.YELLOW}You found a gold coin{Fore.RESET}")
        return 5
    else:
        return 0

def playGame():
    index = 0
    scenes = [
        "You face a great forrest with path leading to the north",
        "Through the trees you roam. The fig us dense with a bitter smell",
        "A small pond faces to your left side and a broken wood door lays in the middle of your path"
    ]
    hero = input("What is your name? ")
    print(f"Welcome to your denise {hero}")
    arr_len = len(scenes)
    score = 0
    cont = True

    print(scenes[index])

    while cont:
        value = input("What shall you do? ").lower().strip()
        if value.startswith("n"):
            index += 1
        elif value.startswith("s"):
            index -= 1
        elif value.startswith("l"):
            cont = False
        else:
            print("That makes little sense")

        if index < 0:
            index = arr_len - 1
        elif index >= arr_len:
            index = 0

        if cont:
            print(scenes[index])
        point = randomEncounter()
        if point == 1:
            score = point
        elif point > 0:
            score += point
            cont = False

    print(f"Your score was {score}")

playGame()
