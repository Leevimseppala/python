rimpsu = "The quick brown fox jumps over the lazy dog. That sentence contains every letter in the English alphabet. Isn’t that neat!"
print(rimpsu+"\n")
rimpsu = rimpsu.replace("fox", "duck")
print(rimpsu+"\n")
poisto = input("Anna poistettava sana:\n")
if poisto in rimpsu:
    rimpsu2 = rimpsu.replace(poisto, "")
else:
    print("Sanaa ei löytynyt\n")
print(rimpsu2+"\n")
rimpsuInt = len(rimpsu)
sanoja = len(rimpsu.split())
print("Merkkejä:", rimpsuInt)
print("Sanoja : ", sanoja,"\n")
rimpsu = rimpsu.replace(".", "\n")
print(rimpsu+"\n")
if len(rimpsu) > 20:
    print(rimpsu[0:20]+"...")




