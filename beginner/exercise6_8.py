# Käytettyjen autojen myyntihinnanlasku ohjelma
# Alussa määritetään muuttujan arvoksi True,
# jotta looppi pyörii niin kauan kuin halutaan
cont = True
while cont:
    # Kysytään käyttäjältä vaadittavat tiedot
    price = float(input("Anna auton alkuperäinen hinta:\n"))
    # Otetaan talteen alkuperäinen hinta
    original = price
    year = int(input("Auton valmistusvuosi:\n"))
    kms = int(input("Anna auton ajokilometrit:\n"))
    category = int(input("Anna auton valmistajan hintakategoria (1 vai 2):\n"))
    exported = input("Onko kyseessä tuontiauto (k/e):\n")
    # Lasketaan keskimääräiset kilometrit per vuosi
    # Tässä olisi voinut hifistellä ja hakea vuoden jostain kirjastosta.
    avg = kms / (2020 - year)
    # Valitaan aluksi kategoria ja sitten keskimääräiset kilometrit.
    # Sitten tarkistetaan onko auto yli 5 vuotta vanha.
    # Otetaan auton hinnasta ensiksi pois 10% ja vähennetään vuosista viis
    # Sen jälkeen auton hintaa lasketaan 7% per vuosi
    # Seuraavaksi tarkistetaan ettei auton hinta pääse liian matalaksi
    if category == 2:
        if avg >= 30000:
            if 2020 - year > 5:
                price = price * 0.9
                for i in range(2020 - year - 5):
                    price = price * 0.93
                if price < original * 0.12:
                    price = original * 0.12
            elif 2020 - year < 5:
                price = price * 0.9
        if avg <= 30000:
            if 2020 - year > 5:
                price = price * 0.92
                for i in range(2020 - year - 5):
                    price = price * 0.95
                if price < original * 0.12:
                    price = original * 0.12
            elif 2020 - year < 5:
                price = price * 0.9
    # Suoritetaan samat toimenpiteet kategorian 1 autoille.
    if category == 1:
        if avg >= 30000:
            if 2020 - year > 5:
                price = price * 0.93
                for i in range(2020 - year - 5):
                    price = price * 0.96
                    if price < original * 0.18:
                        price = original * 0.18
            elif 2020 - year < 5:
                price = price * 0.93
        if avg <= 30000:
            if 2020 - year > 5:
                price = price * 0.95
                for i in range(2020 - year - 5):
                    price = price * 0.97
                    if price < original * 0.18:
                        price = original * 0.18
            elif year - 2020 < 5:
                price = price * 0.95
    # Tarkistetaan onko exported =  k, jos näin on lisätään
    # hintaan ALV 24%
    if exported == 'k':
        price = price * 1.24
    # Printataan hinta pyöristettynä
    print(f"Auton jälleenmyyntihinta on: {round(price)}")
    # Kysytään haluaako käyttäjä jatkaa vielä ohjelman käyttöä
    # jos ei, vaihdetaan cont = False ja breikataan ulos loopista
    # Tämän jälkeen ohjelman suoritus keskeytyy.
    another = input("Haluatko syöttää uuden auton tiedot ohjelmaan (k/e):\n")
    if another == 'e':
        print("Suljetaan ohjelma. Kiitos käytöstä!")
        cont = False
        break
