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
    if serialnum[4] == "-":
        serialnum = serialnum.replace("-", "")
        if len(serialnum)==8:
            return True
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
            print(f"{i+1}. {people[i]}")

    
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
        people = [" ".join(reversed(p.split(" "))) for p in data]
        people.sort()
        for i in range(len(people)):
            print(f"{i+1}. {people[i]}")





    
