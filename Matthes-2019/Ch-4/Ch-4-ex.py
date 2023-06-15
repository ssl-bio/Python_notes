# -------------------------
# Lists
# -------------------------
# 4-1
pizzas = ['pepperoni', 'cheese', 'ny']
for pizza in pizzas:
    print(f"- {pizza}")

for pizza in pizzas:
    print(f"I like {pizza} pizza")

for pizza in pizzas:
    print(f"I like {pizza} pizza")
print('...\nI really like pizza')

# 4-2
animals = ['llama', 'armadillo', 'puma']
for animal in animals:
    print(f"- {animal.title()}")

for animal in animals:
    ianimal = f"{animal.title()}"
    if ianimal[0] == 'A':
        print(f"An {ianimal} has four legs")
    else:
        print(f"A {ianimal} has four legs")

print('\nAll the above animals are found in Bolivia')

# 4-3
for i in range(1, 21):
    print(i)

# 4-4
million = list(range(1, 1_000_001))
for i in sorted(million, reverse=True):
    print(i)

# 4-5
million = list(range(1, 1_000_001))
print("There is a list of integers from 1 to 1000000")
print(f"The min value is: {min(million)}")
print(f"The max value is: {max(million)}")
print(f"The sum of all values is: {sum(million)}")

# 4-6
odd_n = range(1, 20, 2)
for odd in odd_n:
    print(odd)

# 4-7
imult = list(range(3, 33, 3))
for i in imult:
    print(i)

# 4-8
cubes = []
for i in range(1, 11):
    cube = i**3
    cubes.append(cube)
    print(cube)

# 4-9
cubes_2 = [i**3 for i in range(1, 11)]

# 4-10
print("The first 3 items of the list are:")
for i in cubes_2[:3]:
    print(i)


def sublist_even(ilist, n_subitems):
    n_items = len(ilist)
    # list even, sublist even
    if n_items % 2 == 0 and n_subitems % 2 == 0:
        mid_point = n_items / 2
        i_start = (mid_point + 1) - (n_subitems/2)

    # list odd, sublist even
    elif n_items%2 != 0 and n_subitems%2 == 0:
        mid_point = (n_items+1) / 2
        i_start = mid_point - (n_subitems/2)

    # list even, sublist odd
    elif n_items%2 == 0 and n_subitems%2 != 0:
        mid_point = (n_items) / 2
        i_start = mid_point - ((n_subitems-1)/2)

    # list odd, sublist odd
    elif n_items%2 != 0 and n_subitems%2 != 0:
        mid_point = (n_items + 1) / 2
        i_start = mid_point - ((n_subitems-1)/2)

    i_start = int(i_start - 1)
    i_end = i_start + n_subitems
    isublist = ilist[i_start:i_end]
    return isublist


print("The 3 items in the middle are:")
isublist = sublist_even(cubes_2, 8)
for i in isublist:
    print(i)

print(cubes_2)


print("The last 3 items are:")
for i in cubes_2[-3:]:
    print(i)

# 4-11
pizzas = ['pepperoni', 'cheese', 'ny']
friend_pizzas = pizzas[:]
pizzas.append('vegetarian')
friend_pizzas.insert(len(friend_pizzas), 'stone')

print("My pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("My friend's pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")

# 4-13
foods = ('quinoa', 'chicken soup', 'pork', 'fish')
for food in foods:
    print(food)

# This will generate an error
foods[0] = 'beans'

# Change tuple
print("The food items has changed")
foods = ('beans', 'pizza', 'pork', 'fish')

for food in foods:
    print(food)
