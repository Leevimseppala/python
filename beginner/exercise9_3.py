from functions import magazine_serial_check


ISSN = input("Anna ISSN-sarjanumero:")
validate = magazine_serial_check(ISSN)
if validate:
    print("Oikea ISSN.")
else:
    print("Väärä ISSN.")
