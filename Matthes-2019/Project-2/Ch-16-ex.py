# -------------------------
# Downloading data
# -------------------------
# 16-1
# Get indexes
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, col_header in enumerate(header_row):
        print(index, col_header)

# Plot precipitation for sitka Alaska and Death valle, Tx
filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'
files = [filename1, filename2]
prpc_list = []
dates_list = []
for ifile in files:
    with open(ifile) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # Get precipitation data this file.
        dates, prcp = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                iprcp = float(row[3])
            except ValueError:
                pass
            else:
                dates.append(current_date)
                prcp.append(iprcp)
    prpc_list.append(prcp)
    dates_list.append(dates)

# Plot precipitation.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_list[0],
        prpc_list[0],
        c='blue', alpha=0.3)
ax.plot(dates_list[1],
        prpc_list[1],
        c='red', alpha=0.8)
# plt.fill_between(dates, highs, lows, facecolor='orange', alpha=0.1)

# Format plot.
plt.title("Precipitation in Sitka and Death valley - 2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (mm)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# 16-2
filename1 = "data/sitka_weather_2018_full.csv"
filename2 = 'data/death_valley_2018_full.csv'

# See indices
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    first_row = next(reader)
    for index, col_header in enumerate(first_row):
        print(index, col_header)

# Get max temperature for sitka
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get temperature data this file.
    dates_sitka, tmax_sitka, tmin_sitka = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            imax = int(row[8])
            imin = int(row[9])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            dates_sitka.append(current_date)
            tmax_sitka.append(imax)
            tmin_sitka.append(imin)


# Get max temperature for death_valley
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get precipitation data this file.
    dates_dv, tmax_dv, tmin_dv = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            imax = int(row[6])
            imin = int(row[7])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            dates_dv.append(current_date)
            tmax_dv.append(imax)
            tmin_dv.append(imin)

# plots
plt.style.use('seaborn')

# Plot the high and low temperatures for Sitka.
fig, plt1 = plt.subplots()
plt1.plot(dates_sitka, tmax_sitka, c='red', alpha=0.5)
plt1.plot(dates_sitka, tmin_sitka, c='blue', alpha=0.5)
plt.fill_between(dates_sitka, tmax_sitka, tmin_sitka,
                 facecolor='orange', alpha=0.1)
plt.ylim(-20, 140)

plt.savefig('Temp_Sitka_2018v2.png')

# Plot the high and low temperatures for Death valley.
fig2, plt2 = plt.subplots()
plt2.plot(dates_dv, tmax_dv, c='red', alpha=0.5)
plt2.plot(dates_dv, tmin_dv, c='blue', alpha=0.5)
plt.fill_between(dates_dv, tmax_dv, tmin_dv,
                 facecolor='orange', alpha=0.1)
plt.ylim(-20, 140)
plt.savefig('Temp_DeathValley_2018v2.png')

# Plot the high and low temperatures for Sitka and DeathValley.
fig, ax = plt.subplots()
ax.plot(dates_sitka, tmax_sitka, c='#aa0000', alpha=0.5)
ax.plot(dates_sitka, tmin_sitka, c='#14289c', alpha=0.5)

ax.plot(dates_dv, tmax_dv, c='#ff2a00', alpha=0.5)
ax.plot(dates_dv, tmin_dv, c='#0055ff', alpha=0.5)

plt.fill_between(dates_sitka, tmax_sitka, tmin_sitka,
                 facecolor='orange', alpha=0.1)
plt.fill_between(dates_dv, tmax_dv, tmin_dv,
                 facecolor='orange', alpha=0.1)

plt.ylim(-20, 140)
plt.show()

# 16-3
filename1 = "data/san_francisco_weather_2018.csv"
filename2 = 'data/death_valley_2018_full.csv'

# See indices
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    first_row = next(reader)
    for index, col_header in enumerate(header_row):
        print(index, col_header)

# Get max temperature for san francisco
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get temperature data this file.
    dates_sf, tmax_sf, tmin_sf = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            imax = int(row[4])
            imin = int(row[5])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            dates_sf.append(current_date)
            tmax_sf.append(imax)
            tmin_sf.append(imin)


# Get max temperature for death_valley
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get precipitation data this file.
    dates_dv, tmax_dv, tmin_dv = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            imax = int(row[6])
            imin = int(row[7])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            dates_dv.append(current_date)
            tmax_dv.append(imax)
            tmin_dv.append(imin)

fig, ax = plt.subplots()
ax.plot(dates_sf, tmax_sf, c='#a40f14', alpha=0.5,
        label='San Francisco T. max')
ax.plot(dates_sf, tmin_sf, c='#fa6a49', alpha=0.5,
        label='San Francisco T. min')

ax.plot(dates_dv, tmax_dv, c='#243493', alpha=0.5,
        label='Death Valley T. max')
ax.plot(dates_dv, tmin_dv, c='#41b6c4', alpha=0.5,
        label='Death Valley T. min')

plt.fill_between(dates_sf, tmax_sf, tmin_sf,
                 facecolor='#fb9271', alpha=0.1)
plt.fill_between(dates_dv, tmax_dv, tmin_dv,
                 facecolor='#7ecdba', alpha=0.1)

plt.ylim(20, 140)
# Add a legend
plt.legend()
plt.show()

# 16-4
filename1 = "data/san_francisco_weather_2018.csv"
filename2 = 'data/death_valley_2018_full.csv'

# Get indices
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    T_max = None
    T_min = None
    for index, col_header in enumerate(header_row):
        if col_header == 'TMAX':
            T_max = index
        elif col_header == 'TMIN':
            T_min = index

with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get temperature data this file.
    dates_sf, tmax_sf, tmin_sf = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            imax = int(row[T_max])
            imin = int(row[T_min])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            dates_sf.append(current_date)
            tmax_sf.append(imax)
            tmin_sf.append(imin)

# Death valley
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    T_max = None
    T_min = None
    for index, col_header in enumerate(header_row):
        if col_header == 'TMAX':
            T_max = index
        elif col_header == 'TMIN':
            T_min = index

with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get precipitation data this file.
    dates_dv, tmax_dv, tmin_dv = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            imax = int(row[T_max])
            imin = int(row[T_min])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            dates_dv.append(current_date)
            tmax_dv.append(imax)
            tmin_dv.append(imin)

# Plot
fig, ax = plt.subplots()
ax.plot(dates_sf, tmax_sf, c='#a40f14', alpha=0.5,
        label='San Francisco T. max')
ax.plot(dates_sf, tmin_sf, c='#fa6a49', alpha=0.5,
        label='San Francisco T. min')

ax.plot(dates_dv, tmax_dv, c='#243493', alpha=0.5,
        label='Death Valley T. max')
ax.plot(dates_dv, tmin_dv, c='#41b6c4', alpha=0.5,
        label='Death Valley T. min')

plt.fill_between(dates_sf, tmax_sf, tmin_sf,
                 facecolor='#fb9271', alpha=0.1)
plt.fill_between(dates_dv, tmax_dv, tmin_dv,
                 facecolor='#7ecdba', alpha=0.1)

plt.ylim(20, 140)
# Add a legend
plt.legend()
plt.title('Test', fontsize=16)
plt.show()

# 16-6 Refactor
# 16-7 Extract title
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'

# load data
with open(filename) as f:
    all_eq_data = json.load(f)

# make a list of all earthquakes
all_eq_dicts = all_eq_data['features']
ititle = all_eq_data['metadata']['title']

# Extract magnitudes and coordinates
mags, lons, lats, hover_texts = [], [], [], []
mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3.5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Electric',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=ititle)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_v4.html')

# 16-8
filename = 'data/eq_data_4-5_30_day.json'

# load data
with open(filename) as f:
    all_eq_data = json.load(f)

# make a list of all earthquakes
all_eq_dicts = all_eq_data['features']
ititle = all_eq_data['metadata']['title']

# Extract magnitudes and coordinates
mags, lons, lats, hover_texts = [], [], [], []
mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [2.5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Earth',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title=ititle)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes_v5.html')

# 16-9 world fires
# import numpy as np
import pandas as pd
import csv
filename = 'data/world_fires_1_day.csv'

# read data as csv
# data = np.loadtxt(filename, delimiter=',', skiprows=1)
data = pd.read_csv(filename, header=0)

# Get indices
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lat_indx = None
    lon_indx = None
    bright_indx = None
    for index, col_header in enumerate(header_row):
        if col_header == 'latitude':
            lat_indx = index
        elif col_header == 'longitude':
            lon_indx = index
        elif col_header == 'brightness':
            bright_indx = index

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get temperature data this file.
    brights, lons, lats = [], [], []
    counter = 0
    for row in reader:
        try:
            counter += 1
            lat = float(row[lat_indx])
            lon = float(row[lon_indx])
            bright = float(row[bright_indx])
        except ValueError:
            print(f'Error in line: {counter}')
        else:
            brights.append(bright)
            lons.append(lon)
            lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [bgt/100 for bgt in brights],
        'color': brights,
        'colorscale': 'Earth',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires_v1.html')
