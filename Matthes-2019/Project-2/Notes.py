import matplotlib.pyplot as plt

# Basic plot
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()  # fig=entire collection, ax=single plot
ax.plot(squares)
plt.show()

# Customize
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()

# Correct
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# (...) Code to customize plot  
plt.show()

# plot styles
plt.style.available
plt.style.use('ggplot')

# styling individual points
ax.scatter(x_values, y_values, s=100)  # s=size of dot
ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# save graphs
plt.savefig('squares_plot.png')
plt.savefig('squares_plot.png', bbox_inches='tight')  # trims borders


# Random walk
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

# Continuos random walk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)  # full screen
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.summer, edgecolors='none', s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1],
               rw.y_values[-1],
               c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_going = input("Make another walk? (y/n): ")
    if keep_going == 'n':
        break

# Roll dice with plotly
from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

idice = Dice()

results = []
for roll_num in range(1000):
    result = idice.roll_dice()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, idice.sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, idice.sides+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

# Roll two dices
idice1 = Dice()
idice2 = Dice()

results = []
for roll_num in range(1000):
    result = idice1.roll_dice() + idice2.roll_dice()
    results.append(result)

# Get frequencies of results.
frequencies = []
max_result = idice1.sides + idice2.sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
