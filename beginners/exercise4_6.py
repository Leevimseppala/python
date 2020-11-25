temp = input("Anna tämän hetkinen lämpötila:\n")
temp = int(temp)
moist = input("Anna kosteusprosentti:\n")
moist = int(moist)
freezing = False
heatwave = False
raining = False
hailstorm = False

if temp < 0:
    freezing = True
if moist >= 80 and temp <= -20:
    hailstorm = True
if moist >= 80 and temp >= -20:
    raining = True
if temp >= 20:
    heatwave = True

print(f"Annettu lämpötila {temp}")
if freezing:
    print("Pakkasta.")
if raining:
    print("Sataa.")
if hailstorm:
    print("Sataa rakeita!")
if heatwave:
    print("Helleaalto!")
if raining and heatwave:
    print("Kosteaa ja tukalaa.")


