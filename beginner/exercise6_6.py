# Kysytään käyttäjältä rajat
lowpoint = int(input("Anna alueen alaraja:\n"))
highpoint = int(input("Anna alueen yläraja:\n"))
# Luodaan kaksi boolean muuttujaa, cont ja found
cont = True
found = False
# Mennään looppiin jossa pysytään niin kauan kunnos cont = False
while cont:
    # Käydään läpi jokainen luku rajojen sisällä
    for x in range(lowpoint, highpoint + 1):
        # Jos luku ei ole jaollinen viidellä se hylätään heti
        if x % 5 > 0:
            print(f"Luku {x} ei ole jaollinen viidellä, hylätään")
        # Jos luku on jaollinen viidellä
        # mutta ei jaollinen seitsemällä, se hylätään silti.
        elif x % 5 == 0 and x % 7 > 0:
            print(f"Luku {x} ei ole jaollinen seitsemällä, hylätään")
        # Jos luku on 5 ja 7 jaollinen
        # muutetaan found muuttuja Trueksi ja breikataan ulos loopista
        elif x % 5 == 0 and x % 7 == 0:
            print(f"Luku {x} on jaollinen 5:llä ja 7:llä.")
            found = True
            break
    # Tarkistetaan löytyikö sopiva luku
    # printataan teksti ja breikataan ulos loopista.
    if found:
        print("Lopetaan haku.")
        cont = False
        break
    elif not found:
        print("Alueelta ei löytynyt sopivaa arvoa.")
        cont = False
        break
