rahat = input("Anna rahaa:\n")
rahat = int(rahat)
hinta = input("Ostosten hinta:\n")
hinta = int(hinta)
if rahat == hinta:
    print("Kiitos!")
elif rahat > hinta:
    print(f"Kiitos. Annetaan takaisin {rahat-hinta} €")
elif rahat < hinta:
    add = input(f"Rahat eivät riitä, anna lisää rahaa:\n")
    add = int(add)
    if rahat+add > hinta:
        print(f"Kiitos. Annetaan takaisin {rahat+add-hinta} €")
    else:
        print("Sinulla ei ole tarpeeksi rahaa.")
