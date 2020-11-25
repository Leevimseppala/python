movies = [
    {"name": "Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas Pilvet Karkaavat", "year": 1996},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Komisario Palmun erehdys 2", "year": 1980},
    {"name": "Kauas Pilvet Karkaavat 2", "year": 1999},
    {"name": "Mies vailla menneisyyttä 2", "year": 2020}
    ]
new_movies = []
old_movies = []

for i in range(len(movies)):
    if movies[i]["year"] >= 2000:
        new_movies.append(movies[i]["name"])
    elif movies[i]["year"] <= 2000:
        old_movies.append(movies[i]["name"])
separator = ', '
print(f"Seuraavat elokuvat on julkaistu 2000-luvulla:\n{separator.join(new_movies)}")
print("\n")
print(f"Seuraavat elokuvat on julkaistu ennen vuotta 2000:\n{separator.join(old_movies)}")




