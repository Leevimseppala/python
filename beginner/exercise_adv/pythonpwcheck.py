import random
import string
bl_lenght = False
bl_capital = False
bl_num = False
bl_special = False
def new_pw():
    LETTERS = string.ascii_letters
    NUMBERS = string.digits
    PUNCTUATION = "-_~?*$#!+%@"
    SMALL_LETTERS = LETTERS.lower()
    ALL = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    lenght = 12
    password = ''
    password += random.choice(LETTERS)
    password += random.choice(NUMBERS)
    password += random.choice(PUNCTUATION)
    password += random.choice(SMALL_LETTERS)
    while len(password) < lenght:
        password += random.choice(ALL)
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    return password

password = input("Anna salasanasi:\n")
sum_capital = sum(1 for c in password if c.isupper())
sum_numbers = sum(c.isdigit() for c in password)
special_char= 0

for i in range(0, len(password)):
    
    if (password[i].isalpha()):  
            continue
    elif (password[i].isdigit()):
            continue
    else: 
        special_char += 1

if len(password) >= 12:
    bl_lenght = True
if special_char >= 1:
    bl_special = True
if sum_capital >= 1:
    bl_capital =True
if sum_numbers >= 1:
    bl_num = True
if bl_special and bl_capital and bl_lenght and bl_num == True:
    print("Salasanasi on turvalinen!")
else:
    print("Salasanasi ei ole turvallinen!")
    print(f"Uusi turvallinen salasanasi on: " + new_pw())
