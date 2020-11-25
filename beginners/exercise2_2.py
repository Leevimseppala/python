import math

numero1 = input("Anna kolmion ensimmäinen kateetti:\n")
numero1 = float(numero1)
numero2 = input("Anna kolmion toinen kateetti:\n")
numero2 = float(numero2)
numero3 = numero1**2+numero2**2
numero3 = float(numero3)
hypotenuusa = round(math.sqrt(numero3), 1)
print(f"Hypotenuusan pituus: {hypotenuusa} m")
