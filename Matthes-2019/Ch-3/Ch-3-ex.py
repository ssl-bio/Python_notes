# 3-1
names = ['tim', 'tom', 'sam']
for i in names:
    print(i.title())

# 3-2
for name in names:
    print(f"Hello {name.title()}, welcome back!")

# 3-3
transportation_modes = ['bicycle', 'train', 'bus']
print(f"I rarely move by {transportation_modes[0]}")
print(f"I used to ride the {transportation_modes[1]} a lot")
print(f"Nowadays I mainly use the {transportation_modes[2]}")

# 3-4
guests = ['linus', 'tim', 'tom']
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

# 3-5
guests = ['linus', 'tim', 'tom']
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

print(f"Unfortunatelly, {guests[0].title()} won't come for dinner")
# guests.replace('linus', 'steve') # Invalid
guests.remove('linus')
guests.append('steve')
print(f"Dear {guests[len(guests)-1].title()},\
I would like to invite you to have dinner")

# 3-6
guests = ['linus', 'tim', 'tom']
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

print("We found a bigger place to host the dinner")
guests.insert(0, "tina")
guests.insert(2, "anna")
guests.insert(len(guests), "maya")
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

# 3-7
guests = ['linus', 'tim', 'tom']
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

print("We found a bigger place to host the dinner")
guests.insert(0, "tina")
guests.insert(2, "anna")
guests.insert(len(guests), "maya")
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

print("Change of plans, now only two people can come to dinner")
while len(guests) > 2:
    out_guest = guests.pop()
    print(f"Sorry we can't have you, {out_guest.title()}")

for guest in guests:
    print(f"Dear {guest.title()}, please come to dinner")

# guest_n = len(guests)
while guests:
    del guests[0]

print(guests)

# 3-8
itravel = ['thailand', 'colombia', 'chile', 'tanzania', 'madagascar']
for place in itravel:
    print(f"- {place.title()}")

# sorted without modification
for place in sorted(itravel):
    print(f"- {place.title()}")

for place in itravel:
    print(f"- {place.title()}")

# reverse sorted without modification
for place in sorted(itravel, reverse=True):
    print(f"- {place.title()}")

for place in itravel:
    print(f"- {place.title()}")

# Reverse list
itravel.reverse()
for place in itravel:
    print(f"- {place.title()}")

# Re-reverse list
itravel.reverse()
for place in itravel:
    print(f"- {place.title()}")

# Sort list
itravel.sort()
for place in itravel:
    print(f"- {place.title()}")

# Sort in reverse order
itravel.sort(reverse=True)
for place in itravel:
    print(f"- {place.title()}")

# 3-9
guests = ['linus', 'tim', 'tom']
for guest in guests:
    print(f"Dear {guest.title()}, I would like to invite you to have dinner")

print("We found a bigger place to host the dinner")
guests.insert(0, "tina")
guests.insert(2, "anna")
guests.insert(len(guests), "maya")

print(f"There will be {len(guests)} people at the dinner")

# 3-10
languages = ['spanish', 'chinese', 'english', 'korean', 'swahili']

# length of a list
print(f"The list has {len(languages)} elements")
print(f"The first item is: {languages[0].title()}")
languages[0] = 'quechua'
print(f"Now the first element is: {languages[0].title()}")
languages.append('aymara')
languages.insert(0, 'guarani')
print(f"Now the first element is: {languages[0].title()}")
print(f"And the last is: {languages[-1].title()}")

# Removing elements
print(languages)
print("I will now remove the 4th, the 1st and last elements")
del languages[3]
languages.pop()
languages.pop(0)
print(languages)

# sort
print(sorted(languages))
languages.sort(reverse=True)
print(languages)
