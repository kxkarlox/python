people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravanclaw"},
    {"name": "Draco", "house": " Slytherin"}

]


# def f(person):
#     return person["name"]
# lambda replace this function

people.sort(key=lambda person: person["name"])

print(people)
