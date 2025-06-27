#!/usr/bin/env python3

def find_the_redheads(family_info):
    redheads = []

    for name, hair_color in family_info.items():
        if hair_color == "red":  
            redheads.append(name) 

    return redheads 

def main():
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    redheaded_members = find_the_redheads(dupont_family)
    print(redheaded_members)
if __name__ == "__main__":
    main()
