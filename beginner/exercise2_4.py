matkakm = input("Matka-ajon kilometrit:\n")
matkakm = float(matkakm)
kaupunkikm = input("Kaupunki-ajon kilometrit:\n")
kaupunkikm = float(kaupunkikm)
matkakulutus = 5.1/100*matkakm
kaupunkikulutus = 7.5/100*kaupunkikm
kulutus = round((matkakulutus+kaupunkikulutus), 2)
print(f"Kulutus: {kulutus} l")