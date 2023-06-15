# -------------------------
# Dictionaries
# -------------------------
# 6-1
iuser = {"first_name": "kakushi", "last_name": "goto", "age": 36, "city": "tokyo"
for key, val in iuser.items():
    print(f"{key}: {val}")

# 6-2
inumbers = {"anna": 24, "kira": 12, "jane": 39, "joan": 45, "justine": 50}
print("Favorite numbers")
for key, val in inumbers.items():
    print(f"{key.title()}: {val}")

# 6-3
iglossary = {'tupple': 'Unmodifiable list',
             'list': 'Array of objects',
             'comprehension list': 'A list created from a single linefor loop',
             'floating': 'A number with decimals',
             'integer': 'Integer'}

for term, meaning in iglossary.items():
    print(f"- {term.title()}:\n\t{meaning}")

# 6-5
southAmerica_rivers = {
    'Argentina': 'Paraná',
    'Bolivia': 'Beni',
    'Brazil': 'Amazon',
    'Chile': 'Loa',
    'Colombia': 'Magdalena',
    'Ecuador': 'Napo',
    'Guyana': 'Essequibo',
    'Paraguay': 'Paraguay',
    'Peru': 'Marañón',
    'Suriname': 'Suriname',
    'Uruguay': 'Uruguay',
    'Venezuela': 'Orinoco'}

for country, river in southAmerica_rivers.items():
    print(f"The river {river} runs trough {country}")

# 6-6
people = ['jen', 'sarah', 'tom', 'martha']
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for person in people:
    if person in favorite_languages.keys():
        print("Thank you for your cooperation")
    else:
        print("Tell me your favorite computer language:")

# 6-7
iuser1 = {"first_name": "kumi",
          "last_name": "ko",
          "age": 36,
          "city": "tokyo"}

iuser2 = {"first_name": "ian",
          "last_name": "yang",
          "age": 34,
          "city": "new orleans"}

iuser3 = {"first_name": "pedro",
          "last_name": "perez",
          "age": 36,
          "city": "bogota"}

people = [iuser1, iuser2, iuser3]
for iuser in people:
    for key, val in iuser.items():
        print(f"{key}: {val}")
    print("")

# 6-8
ipet1 = {'name': 'timio',
         'type': 'hamster',
         'owner': 'tim'}

ipet2 = {'name': 'homer',
         'type': 'parrot',
         'owner': 'ale'}

ipet3 = {'name': 'sasha',
         'type': 'cat',
         'owner': 'mayra'}

pets = [ipet1, ipet2, ipet3]

for pet in pets:
    for data, value in pet.items():
        print(f"{data}: {value}")
    print("----------")

# 6-9
favorite_places = {'juana': ['tokyo', 'san francisco'],
                   'carlos': 'gainesville',
                   'newtow': ['morogoro', 'gainesville']}

for user, places in favorite_places.items():
    print(f"{user.title()} favorite places are:")
    if type(places) is list:
        for place in places:
            print(f"- {place}")
    else:
        print(f"- {places}")

# 6-10
inumbers = {"anna": 24,
            "kira": 12,
            "jane": [39, 12, 15],
            "joan": 45,
            "justine": 50}
print("Favorite numbers")
for key, val in inumbers.items():
    if isinstance(val, int):
        print(f"{key.title()}: {val}")
    else:
        print(f"{key.title()}:", end=" ")
        print(*val, sep=', ')

# 6-11
cities_info = {
    "New York City": {
        "Average Population": 8800000,
        "Average Age": 36,
        "Main Language": "English"
    },
    "Tokyo": {
        "Average Population": 14000000,
        "Average Age": 45,
        "Main Language": "Japanese"
    },
    "Seoul": {
        "Average Population": 9700000,
        "Average Age": 42,
        "Main Language": "Korean"
    }
}

for city, info in cities_info.items():
    print(f"Information about {city}:")
    for key, data in info.items():
        print(f"{key}: {data}")
    print("")

# 6-12
for city, info in cities_info.items():
    print(f"Information about {city}:")
    for key, data in info.items():
        if isinstance(data, int):
            f_data = "{:,}".format(data)
            print(f"{key}: {f_data}")
        else:
            print(f"{key}: {data}")
    print("")
