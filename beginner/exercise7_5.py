import json
import urllib.request

url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)
highest = float(0)
lowest = float(0)
lowest_place = ''
highest_place = ''
for i in range(len(weather)):
    if lowest == 0:
        lowest = weather[i]['wind']
        lowest_place = weather[i]['location']
        if highest == 0:
            highest = weather[i]['wind']
            highest_place = weather[i]['location']
    elif weather[i]['wind'] > highest:
        highest = weather[i]['wind']
        highest_place = weather[i]['location']
    elif weather[i]['wind'] < lowest:
        lowest = weather[i]['wind']
        lowest_place = weather[i]['location']

print(f"Tänään eniten tuulee sijainnissa: {highest_place}, {highest}m/s")
print(f"Tänään vähiten tuulee sijainnissa {lowest_place}, {lowest}m/s")

avglappi = float(0)
countl = 0
avgmiddle = float(0)
countm = 0
avgsouth = float(0)
counts = 0
for i in range(len(weather)):
    if weather[i]['area'] == 'lapland':
        avglappi += weather[i]['wind']
        countl += 1
    elif weather[i]['area'] == 'middle':
        avgmiddle += weather[i]['wind']
        countm += 1
    elif weather[i]['area'] == 'south':
        avgsouth += weather[i]['wind']
        counts += 1
avglappi = avglappi / countl
avgmiddle = avgmiddle / countm
avgsouth = avgsouth / counts
print(f"Keskimääräinen tuuli, Lappi {round(avglappi, 1)}m/s")
print(f"Keskimääräinen tuuli, Maan keskiosa {round(avgmiddle, 1)}m/s")
print(f"Keskimääräinen tuuli, Etelä-Suomi {round(avgsouth, 1)}m/s")
