lampo = input("Syötä päivän lämpötila:\n")
lampo = int(lampo)
if lampo >= 0 and lampo < 11:
    print("KYLMÄÄ")
elif lampo > 10 and lampo < 16:
    print("KOLEAA")
elif lampo > 15 and lampo < 21:
    print("MELKO LÄMMINTÄ")
elif lampo > 20 and lampo < 26:
    print("LÄMMINTÄ")
elif lampo > 26 and lampo <=30:
    print("HELLETTÄ")
else:
    print("Syötteen tulee olla välillä 0-30")
