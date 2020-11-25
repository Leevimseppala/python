fruits = [
    "apple",
    "pear",
    "banana"]

berries = [
    "strawberry",
    "blueberry",
    "blackberry"]

vegetables = [
    "carrot",
    "kale",
    "cucumber"
]
inventory = [fruits, berries, vegetables]

for i in range(len(inventory)):
    for x in range(len(inventory[i])):
        print(inventory[i][x])
