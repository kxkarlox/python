people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravanclaw"},
    {"name": "Draco", "house": " Slytherin"}

]


def f(person):
    return person["name"]


people.sort(key=f)

print(people)
