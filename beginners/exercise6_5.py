#Luodaan lista
basket = [
    "omena",
    "banaani",
    "kirsikka",
    "porkkana",
    "peruna",
    "tomaatti",
    "kaali",
]
#Kysytään käyttäjältä sana ja tallennetaan se muuttujaan
fruit = input("Anna sana :\n")
#Käydään lista läpi ja verrataan sitä käyttäjän muuttujaan, jos osumaa ei tule printataan: Etsitään...
#Osuman sattuessa printataan löytyi ja poistutaan loopista
for x in range(len(basket)):
    if fruit != basket[x]:
        print("Etsitään...")
    elif fruit == basket[x]:
        print("Sana löytyi!")
        break
print("\n")
#Kysytään käyttäjältä seuraava muuttuja
str_or_num = input("Anna sana tai numero:\n")
#Tarkistetaan muuttujan tyyppi
input_type = str_or_num.isnumeric()
#Jos input_type on numero mennään sisään tästä
if input_type:
    #Muutetaan muuttujan tyyppi numeroksi
    str_or_num = int(str_or_num)
    #Poistetaan kyseisen indexin muuttuja listasta, -1 koska lista alkaa 0:llasta
    basket.remove(basket[str_or_num-1])
    #Tulostetaan muokattu lista
    for x in range(len(basket)):
        print(basket[x])
#Jos input on tyyppiä teksti mennään sisään tästä
elif not input_type:
    #Luodaan apumuuttuja joka pitää lukua kierroksista
    counter = 0
    #Käydään läpi lista
    while counter in range(len(basket)):
        #Jos annettu sana löytyy listasta
        if str_or_num in basket[counter]:
            #Poistetaan annettu sana listasta
            basket.remove(basket[counter])
            #Jatketaan listan läpikäymistä
            continue
        #Tulostetaan listaa apumuuttujan indeksin kohdalta
        print(basket[counter])
        #Lisätään apumuuttujaan +1 per kierros
        counter = counter + 1

