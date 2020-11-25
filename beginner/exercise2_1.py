import math

numero1 = input("Anna särmiön ensimmäisen sivun pituus:\n")
numero1 = float(numero1)
numero2 = input("Anna särmiön toisen sivun pituus:\n")
numero2 = float(numero2)
numero3 = input("Anna särmiön kolmannen sivun pituus:\n")
numero3 = float(numero3)
numero4 = numero1*numero2*numero3
numero4 = float(numero4)
numero5 = round(numero4, 1)
print(f"Särmiön tilavuus: {numero5} m3")
numero6 = input("Anna pallon säde:\n")
numero6 = float(numero6)
numero7 = 4/3*math.pi*numero6**3
numero8 = round(numero7, 1)
print(f"Pallon tilavuus: {numero8} m3")
