from functions import box_volume, ball_volume, pipe_volume
going = True
while going:
    print("Valitse toimenpide (1-3), 0 Lopettaa ohjelman:")
    choice = input()
    if choice == "1":
        width = int(input("Anna laatikon leveys:\n"))
        height = int(input("Anna laatikon korkeus:\n"))
        depth = int(input("Anna laatikon syvyys:\n"))
        volume = box_volume(width, height, depth)
        print(f"Laatikon tilavuus: {volume} m3")
    elif choice == "2":
        radius = int(input("Anna laatikon säde:\n"))
        volume = ball_volume(radius)
        print(f"Pallon tilavuus: {volume} m3")
    elif choice == "3":
        radius = int(input("Anna putken säde:\n"))
        length = int(input("Anna putken pituus:\n"))
        volume = pipe_volume(radius, length)
        print(f"Putken tilavuus: {volume}")
    elif choice == "0":
        print("Kiitos ohjelman käytöstä!")
        going = False
    else:
        print("Väärä syöte. Ohjelma toimii ainoastaan syötteillä 1-3 tai 0!")
