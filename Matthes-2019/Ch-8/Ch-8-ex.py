# -------------------------
# Functions
# -------------------------
# 8-1
def display_message(message):
    print(message)


display_message("I'm learing functions")


# 8-2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book('The unwinding of a miracle')


# 8-3
def make_shirt(size, text):
    print(f"A shirt of size {size} was made")
    print(f"The message, '{text}' was printed")


make_shirt('small', 'what is up?')
make_shirt(text='Yo!', size='large')


# 8-4
def make_shirt(size='large', text='I love Python'):
    print(f"A shirt of size {size} was made")
    print(f"The message, '{text}' was printed")


make_shirt()


# 8-5
def describe_city(city, country='Bolivia'):
    print(f'{city.title()} is in {country.title()}')


describe_city('la paz')
describe_city(city='tokyo', country='japan')
describe_city('cochabamba')


# 8-6
def city_country(city, country):
    return (f'"{city.title()}, {country.title()}"')


cc1 = city_country('manila', 'philipines')
cc2 = city_country('athens', 'greece')
cc3 = city_country('washington', 'usa')
cities = [cc1, cc2, cc3]
for places in cities:
    print(places)


# 8-7
def make_album(artist, album, tracks=None):
    if tracks:
        return {'artist': artist.title(),
                'album': album.title(),
                'N tracks': tracks}
    else:
        return {'artist': artist.title(),
                'album': album.title()}


alb1 = make_album('bob marley', 'exodus')
alb2 = make_album('placebo', 'black market music', 13)
alb3 = make_album('silvio rodriguez', 'dominguez', 10)
albums = [alb1, alb2, alb3]

for album in albums:
    print(album)


# 8-8
import re
print("Please enter the name of a band/artist and an album")
print("Optionally, enter the number of tracks")
print("type 'q' to exit")

while True:
    artist = input('Artist: ')
    album = input('Album: ')
    tracks = input('N tracks: ')

    if artist == 'q' or album == 'q' or tracks == 'q':
        break

    if tracks is not None:
        pattern = r'\b[0-9]+\b'
        match = re.search(tracks, pattern)
        if match:
            print(make_album(artist, album, tracks))
        else:
            print(make_album(artist, album))
    else:
        print(make_album(artist, album))


# 8-9
def show_messages(msg_list):
    for msg in msg_list:
        print(msg)


my_msgs = ['Hello good morning',
           'Welcome back',
           'Would you like a report']

show_messages(my_msgs)


# 8-10
def send_messages(msg_list):
    sent_msgs = []
    while msg_list:
        msg = msg_list.pop()
        sent_msgs.append(msg)

    if sent_msgs:
        return sent_msgs


sent_msgs = send_messages(my_msgs)
print(my_msgs)
print("----------")
print(sent_msgs)

# 8-11
my_msgs = ['Hello good morning',
           'Welcome back',
           'Would you like a report']

sent_msgs = send_messages(my_msgs[:])  # A copy of the list is passed
print(my_msgs)
print("----------")
print(sent_msgs)


# 8-12
def sandwich_items(*items):
    if items:
        if len(items) == 1:
            print("This is the sandwich ingredient:")
        elif len(items) > 1:
            print("These are the sandwich ingredients:")

        for item in items:
            print(f"- {item.title()}")


ingredients = ['cheese', 'tomato', 'ham', 'onions', 'lettuce']
sandwich_items('cheese', 'tomato', 'ham', 'onions', 'lettuce')
sandwich_items('tomato')
sandwich_items(ingredients)  # Doesn't work with a list


# 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('saul', 'sotomayor',
                             location='la paz',
                             field='plant biology',
                             interest='bioinformatics')
print(user_profile)


# 8-14
def make_car(brand, model, **car_info):
    """Returns a dictionary with car info"""
    car_info['brand'] = brand
    car_info['model'] = model
    return car_info


icar = make_car('bmw', 'space', year=2019, millage=25_000)
print(icar)

# 8-15
from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 8-16
import send_messages

to_send = ['Hi', 'Bye', 'Como esta?', 'Ciao']
sent_msgs = send_messages.send_messages(to_send)

# -------------------------
from send_messages import send_messages as sm

to_send = ['Hola', 'Y Adios', 'Welcome back', 'Shutting down']
sent_msgs_2 = sm(to_send[:])

# -------------------------
import send_messages as sms

sent_msgs_3 = sms.send_messages(to_send[:])
