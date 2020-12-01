import datetime
import json
going = True
while going:
    userinput = input("Haluatko lukea vai kirjoittaa vieraskirjaan? (l/k)\n")
    if userinput == "l":
        with open('guestbook.json') as json_file:
            data = json.load(json_file)
            print(data)
    elif userinput == "k":
        txt_to_write = input("Kirjoita teksti:\n")
        with open('guestbook.json', 'w') as outfile:
            datetoday = datetime.datetime.today()
            formatted_datetime = datetoday.isoformat()
            json_datetime = json.dumps(formatted_datetime)
            json.dump(txt_to_write + " " + json_datetime, outfile)


