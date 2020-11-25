counter = 0
biggest = 0
while counter < 5:
    number = int(input("Anna numero:\n"))
    number = int(number)
    counter = counter + 1
    if number > biggest:
        biggest = number
print(f"Suurin käyttäjän luku: {biggest}")
