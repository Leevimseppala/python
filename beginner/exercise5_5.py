thistuple = ('Tammikuu', "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
month = input("Anna kuukauden numero: \n")
month = int(month)
print(thistuple[month-1])