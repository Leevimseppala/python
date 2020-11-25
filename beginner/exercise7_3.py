from typing import Type

shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
]
print("Kuitti ostoksista:\n")
total = float(0)
alv = float(0)
for i in range(len(shopcart)):
    print("-", shopcart[i]['name'])
    total = total + shopcart[i]["price"]
    alv = alv + round(shopcart[i]["price"] - (shopcart[i]["price"] / 1.24), 1)
print("\n")
print(f"Yhteensä {total} €.\nALV:n osuus hinnasta {alv}.\nTervetuloa uudelleen!")
