# Tuodaan random ja string kirjastot
import random
import string

# Haetaan string kirjastosta lista numeroista ja aakkosista
# tehtävännannosta kopioidaan erikoismerkit
# Pienet kirjaimet hoidetaan lower() metodilla
# Luodaan myös muuttuja joka sisältää nämä kaikki
LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = "-_~?*$#!+%@"
SMALL_LETTERS = LETTERS.lower()
ALL = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

# Kysytään käyttäjältä kuinka monen merkin salasanan tämä tahtoo
# ja tallennetaan se muuttujaan
length = int(input("Kuinka monta merkkiä haluat salasanaasi:\n"))
# Tarkistetaan onko se riittävän pitkä
while length < 8:
    print("Merkkimäärä on liian pieni")

# Luodaan salasana string ja lisätään siihen vaadittavat 1 kaikkia merkkejä
# Tämä oli vähän huijaus ratkaisu kun en keksinyt kätevämpää tapaa
password = ''
password += random.choice(LETTERS)
password += random.choice(NUMBERS)
password += random.choice(PUNCTUATION)
password += random.choice(SMALL_LETTERS)
# Lisätään loput merkit randomilla kaikista
while len(password) < length:
    password += random.choice(ALL)
# Vaihdetaan salasana listaksi sekoittamista varten
password = list(password)
random.shuffle(password)
# Palautetaan se muotoon string
password = ''.join(password)
print(password)
