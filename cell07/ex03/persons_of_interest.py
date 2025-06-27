#!/usr/bin/env python3
def famous_births(scientists):
    listing = []
    for i in scientists:
        person = scientists[i]
        birth_year = int(person["date_of_birth"])
        listing.append((birth_year,person["name"]))
    listing.sort()

    for birth_year,name in listing:
        print(f"{name} is a great scientist born in {birth_year}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)