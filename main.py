import json
import pytest

with open('SuperHero.json', 'r') as f:
    superheroes = json.load(f)
    new_heroes = [
        {
            "name": "Black Panther",
            "age": 53,
            "secretIdentity": "T'Challa",
            "powers": ["superhuman strength", "speed", "durability", "reflexes", "agility", "healing", "endurance"]
        },
        {
            "name": "Captain Marvel",
            "age": 26,
            "secretIdentity": "Carol Danvers",
            "powers": ["superhuman strength", "speed", "durability", "energy blasts", "flight", "healing", "endurance"]
        },
    ]

    superheroes["members"].extend(new_heroes)

superheroes["members"].sort(key=lambda x: x["age"])

with open('SuperHero.json', 'w') as f:
    json.dump(superheroes, f, indent=2)

print(json.dumps(superheroes, indent=2))
