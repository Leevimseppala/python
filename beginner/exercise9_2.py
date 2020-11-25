from functions import count_seconds

hrs = int(input("Anna tunnit:"))
mins = int(input("Anna minuutit:"))
scs = int(input("Anna sekunnit:"))
total = count_seconds(hrs, mins, scs)
print(f"Yhteensä {total} sekunttia.")