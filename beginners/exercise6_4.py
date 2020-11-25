codes = ['T1565_2020',
         'T2432_2019',
         'T8551_2018',
         'T3342_2019',
         'T9814_2018',
         'T7733_2020']
year = input("Anna vuosiluku:\n")
# Etsitään osumat listasta
matchingcodes = [i for i in codes if year in i]
# Pilkotaan ja tulostetaan osumat oikeassa muodossa
for x in range(len(matchingcodes)):
    splitmatch = matchingcodes[x].split("_")
    print(splitmatch[0])
