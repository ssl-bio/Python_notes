# -------------------------
# Files and exceptions
# -------------------------
# 10-1
import datetime
import sys
import os
os.chdir('/home/saul/Documents/Apuntes/Python/Matthes-2019/Ch-10')
ifile = 'learning_python.txt'

# Read the entire file
with open(ifile) as fh:
    whole_txt = fh.read()
print(whole_txt)

# size of the object
isize = sys.getsizeof(whole_txt)
print(isize, "bytes")

# Read line by line
with open(ifile) as fh:
    for line in fh:
        print(line.strip())

# Store the lines in an object
with open(ifile) as fh:
    lines = fh.readlines()

for line in lines:
    print(line.strip())

isize2 = sys.getsizeof(lines)
print(isize2, "bytes")

# 10-2
with open(ifile) as fh:
    lines2 = fh.readlines()

for line in lines2:
    print(line.strip().replace('Python', 'R'))

# 10-3
u_name = input("Please write your name: ")
out_file = 'guests.txt'
with open(out_file, 'w') as fh:
    fh.write(u_name)

# 10-4
out_file = 'guests_book.txt'
with open(out_file, 'w') as fh:
    fh.write("List of guests\n")

print("Please write your name.\nType 'q' to exit")
while True:
    iname = input("Name: ")
    if iname == 'q':
        break
    else:
        with open(out_file, 'a') as fh:
            now_time = datetime.datetime.now()
            itime = now_time.strftime("%Y-%m-%d_%H:%M:%S")
            fh.write(f"- {itime}:\t {iname} \n")

# 10-5
out_file = 'programming_poll.txt'
with open(out_file, 'w') as fh:
    fh.write("Why do you like programming?\n")

print("Why do you like programming?\n")
print("Please write your answer.\nType 'q' to exit")
while True:
    ianswer = input("Answer: ")
    if ianswer == 'q':
        break
    else:
        with open(out_file, 'a') as fh:
            now_time = datetime.datetime.now()
            itime = now_time.strftime("%y-%m-%d_%H:%M:%S")
            fh.write(f"- {itime}:\t {ianswer} \n")

# 10-7
print("Insert two numbers. Their sum will be calculated")
print("Type 'q' to exit")

while True:
    inum1 = input("1st Number: ")
    inum2 = input("2nd Number: ")
    if inum1 == 'q' or inum2 == 'q':
        break

    try:
        inum1 = int(inum1)
        inum2 = int(inum2)
        
    except ValueError:
        print('The program needs a numeric input')
        print('Please try again')

    else:
        isum = inum1 + inum2
        print(f"{inum1} + {inum2} = {isum}")

# 10-8
in_files = ['Cats.txt', 'dogs.txt']
for ifile in in_files:
    try:
        with open(ifile) as fh:
            lines = fh.readlines()

    except FileNotFoundError:
        print(f"File '{ifile}' not found")

    else:
        print(f"'{ifile}' contents:")
        for line in lines:
            print(line.strip())
        print("")

# # 10-9
in_files = ['Cats.txt', 'dogs.txt']
for ifile in in_files:
    try:
        with open(ifile) as fh:
            lines = fh.readlines()

    except FileNotFoundError:
        pass

    else:
        print(f"'{ifile}' contents:")
        for line in lines:
            print(line.strip())
        print("")

# 10-10
ebooks = ['War_of_the_worlds.txt', 'Free_as_Freedom.txt']
word = 'the '
for ebook in ebooks:
    try:
        with open(ebook) as eb:
            content = eb.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Book: {ebook}")
        occurrences = content.lower().count(word)
        print (f"The word, '{word}' appears {occurrences} times")

# 10-11
import json

# Write part
print("Write your favorite number.\nType 'q' to exit")
fav_num = input("Number: ")
out_file = 'Favorite_number.json'
with open(out_file, 'w') as fh:
    json.dump(fav_num, fh)
    print('Input recorded')

# read part
try:
    with open(out_file) as fh:
        content = json.load(fh)
except FileNotFoundError:
    pass
else:
    print(f"Your favorite number is: {content}")

# 10-12
import json 

def get_stored_username(user):
     """Get stored username if available."""
     filename = f'{user}.json'
     try:
         with open(filename) as f:
             username = json.load(f)
     except FileNotFoundError:
         return None
     else:
         return username

def get_new_username(user):
    # """Prompt for a new username."""
    # username = input("What is your name? ")
    username = user
    filename = f'{username}.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username 

def greet_user(user):
    """Greet the user by name."""
    username = get_stored_username(user)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(user)
        print(
            f"We'll remember you when you come back, {username}!"
        )
        
greet_user('tim')
