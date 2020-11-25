cafe = {
    "name": "Imaginary Cafe Oy",
    "website": "https://edu.frostbit.fi/sites/cafe",
    "categories": [
        "cafe",
        "tea",
        "lunch",
        "breakfast"
    ],
    "location": {
        "city": "Rovaniemi",
        "address": "Testikuja 22",
        "zip_code": "96200"
    }
}
print(cafe["name"], "\n" + cafe['location']['address'], "\n"
      + cafe['location']['zip_code'], cafe['location']['city'], "\n")
separator = ', '
print(cafe['website'])
print(f"Palvelut: {separator.join(cafe['categories'])} ")

