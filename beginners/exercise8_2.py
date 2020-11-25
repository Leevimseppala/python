from random import randint
from colorama import Back, Style, Fore

randomint = randint(1, 20)
helper = True
while helper:
    guess = input('Arvaa numero (1-20):\n')
    guess = int(guess)
    if guess > randomint:
        print(Back.RED + 'Liian korkea' + Style.RESET_ALL)
    elif guess < randomint:
        print(Back.BLUE + 'Liian matala' + Style.RESET_ALL)
    elif guess == randomint:
        print(Back.GREEN + Fore.MAGENTA + 'Onneksi olkoon!' + Style.RESET_ALL)
        helper = False
