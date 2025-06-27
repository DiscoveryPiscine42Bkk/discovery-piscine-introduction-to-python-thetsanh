#!/usr/bin/env python3

def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names


people = {
    "Thet San": "Htar",
    "Aung Bhone": "Thant",
    "Ricky": "Shen",
    "Phoebe": "Bridgers"
}

print(array_of_names(people))