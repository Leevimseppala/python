try:
    number1 = input("Anna ensimmäinen numero:\n")
    number1 = int(number1)
    number2 = input("Anna toinen numero:\n")
    number2 = int(number2)
    result = number1/number2
    print(f"{result}")

except ValueError:
    print("Virheellinen muoto.")
except ZeroDivisionError:
    print("Nollalla ei saa jakaa.")