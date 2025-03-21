def averageTips():
    tips = []
    num = 5
    for x in range(num):
        tip = float(input(f"Enter tip # {x + 1}: "))
        tips.append(tip)

    print(f"Total Was ${sum(tips):.2f}")
    print(f"The lowest tip received was: ${min(tips):.2f}")
    print(f"The highest tip received was: ${max(tips):.2f}")
    print(f"The average on tips received was: {sum(tips)/num:.2f}")

if __name__ == '__main__':
    averageTips()
