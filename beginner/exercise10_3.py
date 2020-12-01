import random

wisewords = open("wisewords.txt", "r")
content = wisewords.readlines()
fortune_list = []

for line in content:
    fortune_list.append(line)

print(f"Päivän mietelause: \n{fortune_list[random.randint(0,19)]}")


