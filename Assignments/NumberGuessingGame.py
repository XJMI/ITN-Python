import random
from colorama import Fore, Style

def main():
    print(f"Welcome to the {Fore.RED}Number {Fore.CYAN}Guessing {Fore.YELLOW}Game!{Style.RESET_ALL}")

    rand_answer = random.randint(1, 100)
    total_attempts = 0

    while True:
        try:
            attempt = int(input("Enter your number guess (1-100): "))
            if attempt < rand_answer:
                print(f"{Fore.LIGHTRED_EX}{attempt} is too low, Try again!{Style.RESET_ALL}")
                total_attempts += 1
            elif attempt > rand_answer:
                print(f"{Fore.LIGHTRED_EX}{attempt} is too high, Try again!{Style.RESET_ALL}")
                total_attempts += 1
            else:
                print(f"{Fore.MAGENTA}\n{attempt} is correct, You win!\n{Style.RESET_ALL}{Fore.LIGHTMAGENTA_EX}Total Attempts: {total_attempts}{Style.RESET_ALL}")
                break
        except ValueError:
            print("Error, Please input a valid integer number.")

if __name__ == '__main__':
    main()
