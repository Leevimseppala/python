number = input("Anna luku:\n")
number = int(number)
good_division = False
jaettuna3 = number % 3
jaettuna5 = number % 5
if jaettuna3 == 0 and jaettuna5 == 0:
    good_division = True
if good_division:
    print("Luku on sopiva.")
else:
    print("Luku ei ole sopiva.")



