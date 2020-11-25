from colorama import Fore, Style
import datetime
ages = []
counter = 1
while counter <= 5:
    inputyear = input(f"Anna henkilön {counter} syntymävuosi\n")
    inputyear = int(inputyear)
    counter = counter + 1
    ages.append(inputyear)
now = datetime.datetime.now()
for i in range(len(ages)):
    age = now.year - ages[i]
    if 0 <= age <= 125:
        print(Fore.GREEN + f'{age} vuotta, Ikä OK!')
    else:
        print(Fore.RED + f'{age} vuotta, ikä ei ole oikeassa muodossa!')
print(Style.RESET_ALL + 'Valmis!')
