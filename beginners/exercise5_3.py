import math

cont = True

while cont:
    radius = input("Anna säde:\n")
    radius = int(radius)
    surface = math.pi * radius ** 2
    print(f"Ympyrän pinta-ala: {round(surface, 2)}")
    question = input("Haluatko jatkaa? (k/e)\n")
    if question == "e":
        cont = False
