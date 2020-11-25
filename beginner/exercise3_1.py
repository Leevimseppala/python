luku1 = input("Anna ensimmäinen luku:\n")
luku1 = int(luku1)
luku2 = input("Anna toinen luku: \n")
luku2 = int(luku2)
if luku1 > luku2:
    print(f"Suurempi luku = {luku1}")
elif luku2 > luku1:
    print(f"Suurempi luku = {luku2}")
else:
    print("Luvut ovat yhtä suuria.")


