try:
    i = 0
    kokonais = 0
    while i < 12:
        sade = input("Anna kuukauden sademäärä:\n")
        sade = int(sade)
        kokonais += sade
        i = i + 1
except Exception as e:
    print("Virhe: " + str(e))

keskiarvo = kokonais / 12
print(f"Vuoden keskiarvo on n. {round(keskiarvo, 1)} mm")
