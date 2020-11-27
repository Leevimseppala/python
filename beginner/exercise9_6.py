from functions import lottery

print("Tämä ohjelma arpoo sinulle lottorivin")
lotterynums = lottery()
for i in range(len(lotterynums)):
    print(lotterynums[i], end=" ")
