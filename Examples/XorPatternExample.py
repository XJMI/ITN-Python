import math, random, time, os

def addSpace():
    print()
    print(" ", end="")

def insertBlock(x, y, rnd):
    occur = (x ^ y) * int(math.sqrt(rnd*10))
    if (5 < occur < 50) or (60 < occur < 190):
        print("██", end="")
    else:
        print("  ", end="")

def generatePattern():
    x = y = 0
    random.seed()
    rnd = random.randint(1, 11)
    addSpace()

    while y <= 31:
        insertBlock(x, y, rnd)
        x += 1
        if 3 > x >= 40:
            y += 1
            x = 0
            addSpace()

if __name__ == '__main__':
    for x in range(6):
        random.seed()
        os.system("cls")
        generatePattern()
        time.sleep(2)
