import pandas as pd
import numpy as np

# Define a series
series = pd.Series([12, -4, 7, 9], index=["a", "b", "c", "d"])

# Return the values
series.values

# Return the indices
series.index

# Return the second value
series[1]

# Return the first 2 values
series[0:3]

# Return the value associated with label 'c'
series["c"]

# Return the values associated with labels 'a' and 'b''
series[["a", "b"]]

arr = np.array([1, 2, 3, 4])
s3 = pd.Series(arr)
arr[0] = 0

s = pd.Series([12, -4, 7, 9], index=["a", "b", "c", "d"])

# Filtering. Returns a series
s[s > 8]

# Arithmetic operations
s / 2
s * 3
s + 3
s - 5

# numpy math function
np.log(s)

# Unique values not indices.
s.unique()

# count number of occurrences
s.value_counts()

# are any of the values of s in [7,9]. Returns bool.
s.isin([7, 9])

# checks for missing values NaN. Returns bool
s.isnull()

# removes NaN
s.notnull()
s[s.notnull()]

my_dict = {"red": 2000, "blue": 1000, "yellow": 100}
my_series = pd.Series(my_dict)

my_dict2 = {'red': 400, 'green': 100}
my_series2 = pd.Series(my_dict2)

# From a dictionary
data = {
    "color": ["blue", "green", "yellow", "red", "white"],
    "object": ["ball", "pen", "pencil", "peper", "mug"],
    "price": [4.2, 1.0, 0.6, 0.9, 1.7],
}

frame1 = pd.DataFrame(data)

# Only selected data/columns
frame2 = pd.DataFrame(data, columns=["object", "price"])

# Specify index
frame3 = pd.DataFrame(data, index=["one", "two", "three", "tour", "five"])

# From a matix with specific index and columns.
frame4 = pd.DataFrame(
    np.arange(16).reshape((4, 4)),  # 4 by 4 matrix
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "peper"],
)

# returns Index object
frame1.columns
frame1.index

# returns an array
frame1.values

# returns a single column (series abject)
frame1["price"]
frame1.price

# To select a row, returns a series object with columns as index.
# Second example is for multiple rows.
frame1.loc[2]
frame1.loc[[2, 4]]

# Returns the first row as a date frame
frame1[0:1]

# Single cell. For column 'object' and index 3
frame1["object"][3]

data = {
    "color": ["blue", "green", "yellow", "red", "white"],
    "object": ["ball", "pen", "pencil", "peper", "mug"],
    "price": [4.2, 1.0, 0.6, 0.9, 1.7],
}

frame0 = pd.DataFrame(data)  # backup for comparison
frame1 = pd.DataFrame(data)

# change the mame of index array
frame1.index.name = "id"

# Change name of colum array
frame1.columns.name = "item"

# Add a new column full of 10's
frame1["new"] = 10

# Add a new column
frame1["new"] = [3, 2, 1, 4, 5]

# Add a new column
frame1["new"] = pd.Series(np.arange(5))

# check if cell is either 1.0 or 'pen' returns bool ditatame
frame1.isin([1.0, 'pen'])

del frame1['new']

nest_dict = {
    "red": {2012: 22, 2013: 33},
    "white": {2011: 13, 2012: 22, 2013: 16},
    "blue": {2011: 17, 2012: 27, 2013: 18},
}
frame2 = pd.DataFrame(nest_dict)

# Find minimum value
frame2.idxmin()  # 2011

# Find maximum value
frame2.idxmax()  # 2013

# Test if all indices are unique
frame2.index.isunique  # bool

# 'Change' the indices
frame1.reindex(['a', 'b', 'c', 'd', 'e'])
# may not be useful for large data frames

# Fill missing indices over a range
ser = pd.Series([1, 5, 6, 3], index=[0, 3, 5, 6])
ser1 = ser.reindex(range(6), method='ffill')
ser2 = ser.reindex(range(6), method='bfill')

frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['red','blue','yellow','white'],
                     columns=['ball','pen','pencil','paper'])

# Delete 1 or multiple rows
frame_drop_row = frame.drop('yellow')
frame_drop_rows = frame.drop(['white', 'blue'])

# Delete columns (axis=1)
frame_drop_cols = frame.drop(['pen', 'pencil'], axis=1)

frame = pd.DataFrame(
  np.arange(16).reshape((4, 4)),
  index=["red", "blue", "yellow", "white"],
  columns=["ball", "pen", "pencil", "paper"],
)
ser = pd.Series([0, 1, 2, 3],
                index=["ball", "pen", "pencil", "paper"])

# Function definition, returns a series
def f(x):
    return x.max() - x.min()


frame1 = pd.DataFrame(
  np.arange(16).reshape((4, 4)),
  index=["red", "blue", "yellow", "white"],
  columns=["ball", "pen", "pencil", "paper"],
)

# Function applied to rows
row_range = frame1.apply(f)

# Function applied to columns
col_range = frame1.apply(f, axis=1)


# Re-define function, returns a data frame
def f(x):
    return pd.Series([x.min(), x.max()], index=["min", "max"])


row_range2 = frame1.apply(f)

frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

frame.sum()
frame.mean()
frame.describe()  # summary statistics

# Correlation and covariance
frame.corr() #Returns a data trame with correlation matrix.
frame.cov()
frame.corrwith(ser) # pairwise correlation with matching objects.

# Sorting indices (don´t change object)
# Sort from low to high (default)
frame_sort_rows = frame.sort_index()  # operates on rows
frame_sort_cols = frame.sort_index(axis=1)  # operates on columns

# Inverse sorting
frame_sort_rows_rev = frame.sort_index(ascending=False)

# Sorting values. It needs one or more ref. columns
frame_sort_rows_val1 = frame.sort_values(by='pen')
frame_sort_rows_val2 = frame.sort_values(by=['pen', 'pencil'])

# Ranking
ser = pd.Series([5, 0, 3, 8, 4],
                index=['red', 'blue', 'yellow', 'white', 'green'])

# Ascending (default)
ser.rank()

# As they occurr (Doesn´t work)
# ser.rank(method='first')

# Inverse ranking
ser.rank(ascending=False)

# Assign NaN value
ser = pd.series([0, 1, 2, np.NaN, 4])
ser['0'] = None

# Removing NaN values.
ser.dropna()
ser[ser.notnull()]

# Remove row only if all the values are NaN
frame_nan = pd.DataFrame(
  np.arange(16).reshape((4, 4)),
  index=["red", "blue", "yellow", "white"],
  columns=["ball", "pen", "pencil", "paper"],
)
frame_nan.loc['blue'] = None  # Convert whole row to NaN
frame_nan['pen'][0] = np.NaN  # Convert a single cell to NaN

frame_noNaN = frame_nan.dropna()
frame_noNaN_row = frame_nan.dropna(how='all')

# Replace all NaN with 0
frame_noNaN_zero = frame_nan.fillna(0)

# Specific replacement of NaN
frame_noNaN_custom = frame_nan.fillna({'ball': 1,
                                       'pencil': -1,
                                       'paper': 0,
                                       'pen': 99})

# Colors
w = 'white'; b = 'blue'; r = 'red'
# Directions
u = 'up'; d = 'down'; rg = 'right'; l = 'left'
# Values
ivalues = np.random.rand(8)

# Series
mser = pd.Series(ivalues,
                 index=[[w, w, w, b, b, r, r, r],
                        [u, d, rg, u, d, u, d, l]])

mser.unstack() # Returns a regular df. 2nd index -> column

frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

frame_stacked = frame.stack()

w = 'white'; r = 'red'
u = 'up'; d = 'down'
pn = 'pen'; pp = 'paper'
ivalues = np.random.randn(16).reshape(4, 4)
mframe = pd.DataFrame(ivalues,
                      index=[[w, w, r, r], [u, d, u, d]],
                      columns=[[pn, pn, pp, pp], [1, 2, 1, 2]])

# set the names of indices. Second value is the nested index
mframe.columns.names = ['object', 'id']
mframe.index.names = ['colors', 'status']

# swap row indices
mframe_swaped = mframe.swaplevel('colors', 'status')

# sort the indices (level should be specified)
# axis=1 is used to sort columns
mframe_sorted_cols = mframe.sort_index(level='object', axis=1)

# mframe.sum(level='colors') # Deprecated
mframe.groupby(level='colors').sum()

# mframe.sum(level='id', axis=1) # Deprecated
mframe.groupby(level='id', axis=1).sum()
