running = True

while running:
    number = int(input("Minkä luvun kertotaulun haluat nähdä? (1-10). 0 lopettaa ohjelman.\n"))
    if number == 0:
        running = False
    elif number in range(11):
        counter: int = 1
        while counter <= 10:
            print(f"{number} x {counter} = {number * counter}")
            counter = counter + 1
    else:
        print("Vääränlainen luku.")


