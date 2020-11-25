txt = input("Anna jokin teksti:\n")
txt = str(txt)
txt2 = str(txt[::-1])
print(txt2)
palindromi = str
if txt == "":
    print("Antamasi teksti on tyhjä")
elif txt2 == txt:
    palindromi = "KYLLÄ"
    print("Palindromi: " + palindromi)
elif txt != txt2:
    palindromi = "EI"
    print("Palindromi: " + palindromi)



