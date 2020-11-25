tunnit = input("Syötä viikon työtunnnit:\n")
tunnit = int(tunnit)
palkka = input("Syötä tuntipalkkasi:\n")
palkka = float(palkka)
normipalkka = round((palkka * tunnit), 1)
ylityo = 0
if tunnit > 40:
    ylitys = tunnit - 40
    ylityo = (palkka * 1.5) * ylitys
    kokonaispalkka = round(((tunnit - ylitys) * palkka + ylityo), 1)
    print(f'Viikon ansiosi ovat: {kokonaispalkka}€')
else:
    print(f'Viikon ansiosi ovat: {normipalkka}€')
