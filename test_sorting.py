import json


def test_superheroes():
    with open('SuperHero.json', 'r') as f:
        superheroes = json.load(f)

    sorted_superheroes = sorted(superheroes["members"], key=lambda x: x["age"])
    assert superheroes["members"] == sorted_superheroes
