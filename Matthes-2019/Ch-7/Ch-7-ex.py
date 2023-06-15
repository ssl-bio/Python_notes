# -------------------------
# User input and while
# -------------------------
# 7-1
message = 'What type of car do you want?\n'
user_car = input(message)
print(f"Let's see if we have a {user_car.title()} available")

# 7-2
message = "How many people are dinning?\n"
customers = input(message)
i_customers = int(customers)
if isinstance(i_customers, int):
    if i_customers < 8:
        print("Please come this way")
    else:
        print("I'm sorry, you will have to wait for a table")

# 7-3
message = "Enter a number:\n"
inum = input(message)
inum = int(inum)
inum2 = 10
if inum % inum2 == 0:
    print(f"{inum} is a multiple of {inum2}")

# 7-4
print("Write the pizza topping you want:")
print("Type 'quit' to exit")
toppings = []
while True:
    topping = input("Topping: ")
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza")

# 7-5
iage = input("Enter your age: ")
iage = int(iage)
if iage < 3:
    print("Ticket is free")
elif iage <= 12 and iage >= 3:
    print("Ticket costs 10$")
elif iage > 12:
    print("Ticket costs 15$")

# 7-6
#
print("Enter your age: ")
print("Type 'q' to exit")
status = 'active'
while status == 'active':
    # while True:
    iage = input("Age: ")
    try:
        iage = int(iage)
    except ValueError:
        status = 'inactive'
    else:
        if iage < 3:
            print("Ticket is free")
        elif iage <= 12 and iage >= 3:
            print("Ticket costs 10$")
        elif iage > 12:
            print("Ticket costs 15$")

# 7-7
while True:
    print("_", end=" ")

# 7-8
sandwich_orders = ['egg', 'tuna', 'chicken', 'beef']
finished_orders = []
while sandwich_orders:
    order = sandwich_orders.pop()
    finished_orders.append(order)
    print(f"Making a {order.title()} sandwich")

print("This sandwiches were made")
for sandwich in finished_orders:
    print(f"- {sandwich.title()}")

# 7-9
miss = 'pastrami'
sandwich_orders = ['egg', miss, 'tuna', miss, 'chicken', 'beef', miss]
finished_orders = []
print(f"We are out of {miss.title()} sandwich")
while miss in sandwich_orders:
    sandwich_orders.remove(miss)

while sandwich_orders:
    order = sandwich_orders.pop()
    finished_orders.append(order)
    print(f"Making a {order.title()} sandwich")

print("This sandwiches were made")
for sandwich in finished_orders:
    print(f"- {sandwich.title()}")

# 7-10
poll_results = []
message = "If you could visit one place in the world, where would you go?"
print(message)
print("Type 'q' to exit")
while True:
    answer = input("Answer: ")
    if answer == "q":
        break
    else:
        poll_results.append(answer)

if poll_results:
    print("These are the answers:")
    for item in poll_results:
        print(f"- {item}")
