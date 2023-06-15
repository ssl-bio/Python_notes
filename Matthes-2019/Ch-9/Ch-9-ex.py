# -------------------------
# Classes
# -------------------------
import os
os.chdir('/home/saul/Documents/Apuntes/Python/Matthes-2019/Ch-9')


# 9-1
class Restaurant():
    """Displays basic information of a restaurant

    """
    def __init__(self, name, cuisine_type):
        # super(Restaurant, self).__init__()
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"'{self.name.title()}' information:")
        print(f"Cuisine: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The restaurant '{self.name.title()}' is open")


pacena = Restaurant('la pacena', 'bolivian')
pacena.describe_restaurant()
pacena.open_restaurant()


# 9-2
tokio = Restaurant('tokio', 'japanese')
cocha = Restaurant('Cocha', 'bolivian')
gg = Restaurant('gg', 'chinese')

tokio.describe_restaurant()


# 9-3
class User():
    """Displays information for a user

    """
    def __init__(self, first_name, last_name, age, location, language):
        # super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.language = language

    def describe_user(self):
        user_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Name: {user_name}")
        print(f"Location: {self.location.title()}")
        print(f"Language: {self.language.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        iname = self.first_name.title()
        print(f"Welcome {iname}")


saul = User('saul', 'sotomayor', age=40, location='la paz', language='spanish')
saul.describe_user()
saul.greet_user()

tim = User('tim', 'burton', age=55, location='LA', language='English')
tim.describe_user()
tim.greet_user()


# 9-4
class Restaurant():
    """Displays basic information of a restaurant

    """
    def __init__(self, name, cuisine_type, number_served=0):
        # super(Restaurant, self).__init__()
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"'{self.name.title()}' information:")
        print(f"Cuisine: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The restaurant '{self.name.title()}' is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


# A
italo = Restaurant('italo', 'italian')
italo.number_served
italo.number_served = 12

# B
italo.set_number_served(2)
italo.number_served

# C
italo.increment_number_served(2)
italo.number_served


# 9-5
class User():
    """Displays information for a user

    """
    def __init__(self, first_name,
                 last_name, age,
                 location, language,
                 login_attempts=0):
        # super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.language = language
        self.login_attempts = login_attempts

    def describe_user(self):
        user_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Name: {user_name}")
        print(f"Location: {self.location.title()}")
        print(f"Language: {self.language.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        iname = self.first_name.title()
        print(f"Welcome {iname}")

    def increment_login(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


saul = User('saul', 'soto', 40, 'la paz', 'spanish')
saul.increment_login()
saul.login_attempts
saul.reset_login_attempts()
saul.login_attempts


# 9-6
class Restaurant():
    """Displays basic information of a restaurant

    """
    def __init__(self, name, cuisine_type):
        # super(Restaurant, self).__init__()
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"'{self.name.title()}' information:")
        print(f"Cuisine: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The restaurant '{self.name.title()}' is open")


class IceCreamStand(Restaurant):
    """Class to model a Ice cream dely

    """
    def __init__(self, name, cuisine_type, flavors=None):
        super(IceCreamStand, self).__init__(name, cuisine_type)
        self.name = name
        self.cuisine = cuisine_type
        self.flavors = flavors

    def show_flavors(self):
        if self.flavors:
            print(f"These are the available flavors at {self.name.title()}")
            for flavor in self.flavors:
                print(f"- {flavor.title()}")
        else:
            print("We don't have any ice creams, for now")


frigo_flavors = ['canela', 'frutilla', 'chirimoya', 'uva']
frigo = IceCreamStand('frigo', 'ice cream', frigo_flavors)
frigo.show_flavors()
panda = IceCreamStand('panda', 'ice cream', frigo_flavors)
panda.show_flavors()


# 9-7
class User():
    """Displays information for a user
    """
    def __init__(self, first_name, last_name, location, language):
        # super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.language = language

    def describe_user(self):
        user_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Name: {user_name}")
        print(f"Location: {self.location.title()}")
        print(f"Language: {self.language.title()}")
        print(f"Age: {self.age}")

    def greet_user(self):
        iname = self.first_name.title()
        print(f"Welcome {iname}")


class Admin(User):
    """Defines privileges of a root user
    """
    default_powers = ['add post',
                   'flag post',
                   'edit post',
                   'delete post']

    def __init__(self, first_name, last_name, location, language, sudo_powers=default_powers):
        super(Admin, self).__init__(first_name, last_name, location, language)
        self.sudo_powers = sudo_powers

    def show_privileges(self):
        print("As an Admin you can:")
        for power in self.sudo_powers:
            print(f"- {power}")
        print("----------")


root = Admin('root', 'debian', 'la paz', 'spanish')
root.show_privileges()


# 9-8
class Privilege():
    """Describes privileges of a user
    """
    default_powers = ["add post", "flag post", "edit post", "delete post"]

    def __init__(self, privileges=default_powers):
        # super(Privilege, self).__init__()
        self.privileges = privileges

    def show_privileges(self):
        print("As an Admin you can:")
        for power in self.privileges:
            print(f"- {power}")
        print("----------")


class Admin(User):
    """Defines privileges of a root user
    """

    def __init__(self, first_name,
                 last_name, location,
                 language):
        super(Admin, self).__init__(first_name, last_name, location, language)
        self.sudo_powers = Privilege()


root2 = Admin('saul', 'soto', 'lp', 'spanish')
root2.sudo_powers.show_privileges()


# 9-9
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            print(f"Battery can't be upgraded, size is {self.battery_size}")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


audi = ElectricCar('audi', 'evo', '2020')
audi.battery.get_range()
audi.battery.describe_battery()
audi.battery.upgrade_battery()

audi.battery.get_range()
audi.battery.describe_battery()


# 9-10
from Restaurant import Restaurant, IceCreamStand

riel = Restaurant('la riel', 'bolivian')
riel.describe_restaurant()

# 9-11
import user as user
iuser = user.User('sam', 'smith', 'US', 'english')
iuser.describe_user()
iuser.greet_user()

# 9-12
from  user import User
from user_extension import Admin, Privilege

filio = User('ale', 'filio', 'mexico', 'spanish')
filio.describe_user()

root = Admin('root', 'of tree', 'land', 'leaf')
root.describe_user()

# 9-14
from random import randint


class Dice():
    """Simulates a dice with n sides

    """
    def __init__(self, sides=6):
        # super(Die, self).__init__()
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)


dado6 = Dice()
dado10 = Dice(10)
dado20 = Dice(20)

# resultados = []
# for _ in range(1, 11):
#     resultados.append(dado10.roll_dice())

# for i in resultados:
#     print(i, end=" ")
# print("")

for _ in range(1, 11):
    print(dado20.roll_dice(), end=" ")
print("")

# 9-14
from random import choice
import string


def draw_number(n):
    num_pool = list(range(1, 11))
    all_lett = list(string.ascii_lowercase)
    lett_pool = all_lett[0:5]
    ipool = num_pool + lett_pool
    inum = None
    for _ in range(1, n+1):
        i = choice(ipool)
        i = str(i)
        if inum is None:
            inum = i
        else:
            inum += i
    return inum


winner_num = draw_number(4)
print(f"Any ticket matching '{winner_num}' will win 1 million $")

# 9-15
my_ticket = draw_number(4)
n_attempt = 1
while my_ticket != winner_num:
    my_ticket = draw_number(4)
    n_attempt += 1

print(f"I took {n_attempt} attempts to win the lottery")

# 9-16
# Module of the week
"""
The syntax used in Python’s re module is based on the syntax used for regular expressions in Perl, with a few Python-specific enhancements.

Although re includes module-level functions for working with regular expressions as text strings, it is more efficient to compile the expressions a program uses frequently. The compile() function converts an expression string into a RegexObject.
"""
