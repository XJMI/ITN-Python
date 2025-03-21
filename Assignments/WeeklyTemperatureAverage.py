import os, platform
from rich.console import Console
from rich_gradient import Gradient

console = Console()

high_temps = []
low_temps = []
days = ["1", "2", "3", "4", "5", "6", "7"]

def clearConsole():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system('clear')
    else:
        return None
    
def tempColors(value, text):
    tempValue = value
    unformattedText = text
    if tempValue > 50:
        return console.print(Gradient(unformattedText, colors=["#fa3123", "#fa6023"]))
    elif tempValue < 30:
            return console.print(Gradient(unformattedText, colors=["#4ed7fc", "#4efcfa"]))
    elif tempValue < 50:
            return console.print(Gradient(unformattedText, colors=["#2343fa", "#23affa"]))
    else:
        return None

def calculateTemperature():
    try:
        for day in days:
            high = float(console.input(f"\n[bold]What is the high for day {day}:[/] ").strip())
            low = float(console.input(f"[bold]What is the low for the day {day}:[/] ").strip())
            clearConsole()

            high_temps.append(high)
            low_temps.append(low)

        avg_high = sum(high_temps) / len(high_temps)
        avg_low = sum(low_temps) / len(low_temps)

        highTemp_p = f"\nAverage High Temperature for the week: {avg_high:.2f}"
        lowTemp_p = f"Average Low Temperature for the week: {avg_low:.2f}"

        tempColors(avg_high, highTemp_p)
        tempColors(avg_low, lowTemp_p)

    except Exception as err:
        console.log(err)

if __name__ == '__main__':
    try:
        clearConsole()
        calculateTemperature()
    except Exception as err2:
        console.log(err2)
