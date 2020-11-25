pisteet = input("Anna pistemäärä:\n")
pisteet = int(pisteet)
if 0 <= pisteet < 51:
    print("Arvosana: 0")
elif 50 < pisteet < 61:
    print("Arvosana: 1")
elif 60 < pisteet < 71:
    print("Arvosana: 2")
elif 70 < pisteet < 81:
    print("Arvosana: 3")
elif 80 < pisteet < 91:
    print("Arvosana: 4")
elif 90 < pisteet <= 100:
    print("Arvosana: 5")
else:
    print("Pistemäärä ei ole mahdollinen.")
