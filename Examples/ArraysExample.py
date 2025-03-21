import winsound
import time
import os

def et1():
    anim1 = [
            [1,1,1,1,1,1,1,1,0],
            [1,0,1,1,1,1,1,1,0],
            [1,1,1,1,0,1,1,1,0],
            [0,0,0,0,0,1,1,1,0],
            [1,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,0,0],
            [0,1,0,0,0,0,0,1,0],
            [1,1,0,0,0,0,1,1,0]
        ]
    return anim1

def et2():
    anim2 = [
            [1,1,1,1,1,1,1,1,0],
            [1,0,1,1,1,1,1,1,0],
            [1,1,1,1,0,1,1,1,0],
            [0,0,0,0,0,1,1,1,0],
            [1,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,1,0],
            [0,1,1,1,1,1,1,0,0],
            [0,1,0,0,0,0,0,1,0],
            [0,1,1,0,0,0,0,1,1]
        ]
    return anim2

def et_walking():
    bln = True
    for i in range(10, 0, -1):
        if bln:
            et = et1()
            bln = False
        else:
            et = et2()
            bln = True

        os.system("cls")
        print()

        for row in et:
            print("".ljust(i), end="")
            for col in row:
                if col == 1:
                    print("██", end="")
                else:
                    print("  ", end="")

            print()
        winsound.Beep(200, 30)
        time.sleep(.5)

et_walking()
