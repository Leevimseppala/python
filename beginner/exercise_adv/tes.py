def tulostaViestit(viestit):
    for i in range(len(viestit)):
        for y in range(len(viestit[i]) + 4):
            print('*', end="")
        print(f"\n* {viestit[i]} *")
        for y in range(len(viestit[i]) + 4):
            print('*', end="")
        print("\n")


lista = ["Tervetuloa", "ABC", "Hei hei!"];
tulostaViestit(lista);
