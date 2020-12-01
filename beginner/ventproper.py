import random
import colorama
total = 0
dtotal = 0
bet = 0
wins = 0
loss = 0
totalbet = 0
on = True
dealing = False

def play(total=0, totalbet=0, bet=0):
    bet = int(input('Aseta panoksesi:\n'))
    totalbet = totalbet + bet
    first = random.randint(1, 13)
    print(f"Ensimmäinen korttisi on {first}!")
    total = first
    more = input("Haluatko lisää kortteja? (k/e)\n")
    while more == 'k':
        second = random.randint(1, 13)
        total = total + second
        print(f'Seuraava korttisi on {second}!')
        if total < 21:
            print(f'Korttiesi summa on {total} ')
            more = input("Haluatko lisää kortteja? (k/e)\n")
        elif total == 21:
            print(f'Korttiesi summa on {total} ')
            print("Ventti! Pelaajan voitto!")
            wins = wins + (bet * 3)
            endgame = input("Haluatko pelata uudestaan? (k/e)\n")
            total = 0
            print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins-loss}")
        elif total > 21:
            print(f"Yli meni! Korttiesi summa on {total}. Jakajan voitto!")
            loss = loss - bet
            more = input("Haluatko pelata uudestaan? (k/e)\n")
            total = 0
            elif more == 'e':
                print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins - loss}")
                on = False
                break

def deal():

def end():