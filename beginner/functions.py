import math
import random

def show_personal_info():
    name = "Matti Meikälänen"
    home = "Sodankylä"
    job = "Ohjelmistosuunnittelija"
    print(name + "\n" + home + "\n" + job)

def count_seconds(hours, minutes, seconds):
    total = hours*3600+minutes*60+seconds
    return total

def magazine_serial_check(serial):
    serialnum = serial
    if len(serialnum)==9:
        if serialnum[4] == "-":
            serialnum = serialnum.replace("-", "")
            if serialnum.isdigit():
                if len(serialnum)==8:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False


def show_numbered_list(title, data):
    if title == "Ilmoittautumisjärjestys:":
        print("Ilmoittautumisjärjestys:")
        people = data
        people = [p.strip() for p in people]
        people = data.split(",")
        for i in range(len(people)):
            print(f"{i+1}.{people[i]}")

    
    elif title == "Aakkosjärjestys etunimen perusteella:":
        print("Aakkosjärjestys etunimen perusteella:")
        people = data.split(",")
        people = [p.strip() for p in people]
        people.sort()
        for i in range(len(people)):
            print(f"{i+1}. {people[i]}")



    elif title == "Aakkosjärjestys sukunimen perusteella:":
        print("Aakkosjärjestys sukunimen perusteella:")
        people = data
        people = people.split(",")
        people = [p.strip() for p in people]
        people = [" ".join(reversed(p.split(" "))) for p in people]
        people.sort()
        for i in range(len(people)):
            print(f"{i+1}. {people[i]}")



def box_volume(width, height, depth):
    volume = round(width*height*depth, 2)
    return volume


def ball_volume(radius):
    volume = round(((4*math.pi*radius**3)/3),2)
    return volume


def pipe_volume(radius, length):
    volume = round(math.pi*radius**2*length,2)
    return volume

def lottery():
    lotterynums = []
    while len(lotterynums)<7:
        newnum = random.randint(1,40)
        while newnum in lotterynums:
            newnum = random.randint(1,40)
        lotterynums.append(newnum)
    lotterynums.append("Lisänumerot:")
    for i in range(2):
        extranum = random.randint(1,40)
        if extranum in lotterynums:
            extranum = random.randint(1,40)
        lotterynums.append(extranum)
    
    return lotterynums


