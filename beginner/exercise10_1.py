def editfile(filecontent):
    for i in range(len(filecontent)):
        filecontent[i] = filecontent[i].replace(",", "\t")
    return filecontent


artists = open("artists.txt", "r")
content = artists.readlines()
content = editfile(content)
for line in content:
    print(line)
    