kkpalkka = input("Anna kuukausipalkkasi:\n")
kkpalkka = float(kkpalkka)
veroprosentti = input("Anna veroprosenttisi:\n")
veroprosentti = int(veroprosentti)
verot = round((kkpalkka/100*veroprosentti), 1)
verotonosuus = round((kkpalkka-verot), 1)
print(f"Käteenjäävä osuus: {verotonosuus} €")
print(f"Verot : {verot} €")

