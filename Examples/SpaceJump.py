import os, time

def print_diver(up):
    diver = [
        [1,0,2,0,1],
        [0,1,1,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,1,0,0,1],
        [0,1,0,0,1],
        [0,1,0,0,1]
    ]

    for row in diver[::up]:
        for cell in row:
            if cell == 1:
                print("███", end="")
            elif cell == 2:
                print("░░", end="")
            else:
                print("  ", end="")
        print()

def falling():
    up = 1
    os.system("cls")
    for i in range(1, 13, 1):
        print_diver(up)
        time.sleep(.3)
        os.system("cls")
        up = up*-1
        for v in range(1, i*2):
            print()

def print_parachute():
    para = [
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [1,1,1,1,1],
        [2,2,2,2,0],
        [2,2,2,2,0],
        [2,0,0,2,0],
        [2,0,0,2,0]
    ]

    for row in para:
        for cell in row:
            if cell == 1:
                print("░░░", end="")
            elif cell == 2:
                print(" | ", end="")
            else:
                print("  ", end="")
        print("")

def landing():
    os.system("cls")
    for i in range(2, 14, 1):
        print_parachute()
        print_diver(1)
        if i > 12:
            print("_"*30)
            time.sleep(.4)
            os.system("cls")
            for f in range(1, i*2): print()
            
def start():
    try:
        meters_up = int(input("How many meters up are you: ").strip())
        falls = int(input("How many falls per meter: ").strip())
    except ValueError:
        print("[*] Please provide a integer number.")

    for x in range(3):
        falling()
        landing()
        print("\nYou successfully have landed!")

start()
