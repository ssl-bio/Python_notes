# -------------------------
# If statements
# -------------------------
# 5-1
home_town = 'la paz'
print("Is this town La Paz? I predict True.")
home_town_f = home_town.title()
print(home_town_f == "La Paz")

print("Is this town Beni? I predict False")
print(home_town_f == 'Beni')

# 5-2
# Tests for equality and inequality with strings
str1 = 'la paz'
str2 = 'La Paz'
print(str1 == str2)

# Tests using the lower() method
print (str1 == str2.lower())

# Numerical tests involving equality and inequality,
# greater than and less than, greater than or equal to,
# and less than or equal to
inum1 = 25
inum2 = 40

print(inum1 == inum2)
print(inum1 != inum2)
print(inum1+25 < inum2)
print(inum1 >= inum2-25)

# Tests using the and keyword and the or keyword
print(25 < 35 and 34 > 23)
print(inum1 == inum2 or inum2 > inum1)

# Test whether an item is in a list
my_foods = ['pizza', 'fried chicken', 'tuna', 'chicken soup']
my_food = 'chicken'
my_food in my_foods

# Test whether an item is not in a list
my_food not in my_foods

# 5-3
alien_color = 'green'
alien_color = 'blue' 
if alien_color == 'green':
    print('You have earned 5pts')

# 5-4
alien_color = 'blue'
alien_color = 'green'
if alien_color == 'green':
    print('You have earned 5pts')
else:
    print("You have earned 10pts")

# 5-5
alien_color = 'red'
if alien_color == 'green':
    print('You have earned 5pts')
elif alien_color == 'red':
    print("You have earned 15pts")
elif alien_color == 'yellow':
    print("You have earned 10pts")

# 5-6
iage = 40
imessage = "You are classified as,"
if iage < 2:
    print(imessage, "baby")
elif iage <4 and iage >= 2:
    print(imessage, "toddler")
elif iage <13 and iage >= 4:
    print(imessage, "kid")
elif iage <20 and iage >= 13:
    print(imessage, "teenager")
elif iage <65 and iage >= 20:
    print(imessage, "adult")
elif iage >= 65:
    print(imessage, "elder")

# 5-7
my_fruits = ['kiwi', 'apple', 'banana', 'pineapple']
my_fruit = 'kiwi'

if my_fruit in my_fruits:
    print(f"You really like, {my_fruit.title()}")

# 5-8

user = 'tom'
if user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, welcome!")

# 5-9
users = []
if users:
    if user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, welcome!")
else:
    print("There are no registered users")

# 5-10
current_users = ['tim', 'tom', 'Mike', 'saul', 'anna', 'admin']
new_users = ['jane', 'mikah', 'liah', 'Tom', 'mike']
current_users_test = [user.lower() for user in current_users]

for user in new_users:
    user = user.lower()
    if user in current_users_test:
        print(f"The name, {user} is already taken")
        print('Note that usernames are case-insensitive')
    else:
        print(f"The name, {user} is available")

# 5-11
inumbers = list(range(1, 10))
for i in inumbers:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
