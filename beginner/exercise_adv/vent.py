import random
import colorama
total = 0
dtotal = 0
wins = 0
loss = 0
totalbet = 0
on = True
dealing = False
print("Tervetuloa venttipeliin!")
bet = int(input('Aseta panoksesi. Mieti tarkkaan, sillä panoksen voi asettaa vain kerran:\n'))
while on:
    more = 'k'
    first = random.randint(1, 13)
    print(f"Ensimmäinen korttisi on {first}!")
    total = first
    more = input("Haluatko lisää kortteja? (k/e)\n")
    if more == 'e':
        dealing = True
    while more == 'k':
        totalbet = totalbet + bet
        second = random.randint(1, 13)
        total = total + second
        print(f'Seuraava korttisi on {second}!')
        if total < 21:
            print(f'Korttiesi summa on {total} ')
            more = input("Haluatko lisää kortteja? (k/e)\n")
            if more == 'e':
                dealing = True
        elif total == 21:
            print(f'Korttiesi summa on {total} ')
            print("Ventti! Pelaajan voitto!")
            wins = wins + (bet * 3)
            endgame = input("Haluatko pelata uudestaan? (k/e)\n")
            total = 0
            if more == 'k':
                dealing = True
            elif endgame == 'e':
                print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins-loss}")
                on = False
                break
        elif total > 21:
            print(f"Yli meni! Korttiesi summa on {total}. Jakajan voitto!")
            loss = loss + bet
            more = input("Haluatko pelata uudestaan? (k/e)\n")
            total = 0
            if more == 'k':
                dealing = True
            elif more == 'e':
                print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins - loss}")
                on = False
                break
    print('Seuraavaksi jakaja arpoo kortit!')
    dealer1st = random.randint(1, 13)
    print(f"Jakajan ensimmäinen on {dealer1st}")
    dtotal = dealer1st
    while dealing:
        if dtotal <= 17:
            dealer3rd = random.randint(1, 13)
            dtotal = dtotal + dealer3rd
            print(f"Jakajan seuraava kortti on {dealer3rd} ja summa {dtotal}")
        elif dtotal > 21:
            print("Voitit! Jakajan käsi meni yli.")
            wins = wins + (bet * 2)
            more = input("Haluatko pelata uudestaan? (k/e)\n")
            dtotal = 0
            if more == 'e':
                on = False
                print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins - loss}")
                break
            dealing = False
        elif 17 < dtotal <= 21 and dtotal >= total:
            print("Jakaja voitti!")
            loss = loss + bet
            more = input("Haluatko pelata uudestaan? (k/e)\n")
            dtotal = 0
            if more == 'e':
                on = False
                print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins - loss}")
                break
            dealing = False
        elif dtotal > 21:
            print("Voitit! Jakajan käsi meni yli.")
            wins = wins + (bet * 2)
            more = input("Haluatko pelata uudestaan? (k/e)\n")
            dtotal = 0
            if more == 'e':
                on = False
                print(f"Kiitos pelaamisesta. Panostit:{totalbet} Voitit: {wins} Hävisit: {loss} Lopputulos: {wins-loss}")
                break
            dealing = False










