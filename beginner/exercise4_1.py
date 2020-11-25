from datetime import datetime
today = datetime.now()
pvm = today.strftime("%d.%m.%Y")
nimi = str("Testi Henkilöinen")
synt = str(1982)
saldo = str(1698)
print(nimi + " ("+ synt +"), saldo: " + saldo+" €, päivitetty " + pvm)




