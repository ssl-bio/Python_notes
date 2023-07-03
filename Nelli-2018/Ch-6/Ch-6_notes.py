import pandas as pd
import numpy as np

# Define data frames
# Define data frames
frame1 = pd.DataFrame({
    "id": ["ball", "pencil", "pen", "mug", "ashtray"],
    "price": [12.33, 11.44, 33.21, 13.23, 33.62],
})
frame2 = pd.DataFrame({
    "id": ["pencil", "pencil", "ball", "pen"],
    "color": ["white", "red", "red", "black"],
})

# Merge. It uses 'id'. 'mug' and 'ashtray' from frame1 are excluded
frame1_2_merged = pd.merge(frame1, frame2)

# Define data frames with 2 columns in common
frame1 = pd.DataFrame({
    'id': ['ball', 'pencil', 'pen', 'mug', 'ashtray'],
    'color': ['white', 'red', 'red', 'black', 'green'],
    'brand': ['OMG', 'ABC', 'ABC', 'POD', 'POD']
})
frame2 = pd.DataFrame({
    'id': ['pencil', 'pencil', 'ball', 'pen'],
    'brand': ['OMG', 'POD', 'ABC', 'POD']
})

# Merge specifying the column to work on
merged_df_id = pd.merge(frame1, frame2, on='id')
merged_df_brand = pd.merge(frame1, frame2, on='brand')

# Merge using multiple columns (merging method 'how' is needed)
merged_df_all = pd.merge(frame1, frame2, on=['id', 'brand'], how='outer')

# rename columns on dataframe2
frame2.columns = ['sid', 'brand']

# Merge specifying which columns to use
pd.merge(frame1, frame2, left_on='id', right_on='sid')

# revert changes in dataframe2
frame2.columns = ['id', 'brand']

# merge using 'outer' method
merged_df_id_outer = pd.merge(frame1, frame2, on='id', how='outer')

# merge by index using merge() method
pd.merge(frame1, frame2, right_index=True, left_index=True)

# merge by index using the join() method.
# requires unique columns
frame2.columns = ['id2', 'brand2']
frame1.join(frame2)

# Define series
ser1 = pd.Series(np.random.rand(4), index=[1, 2, 3, 4])
ser2 = pd.Series(np.random.rand(4), index=[5, 6, 7, 8])

# Concatenates series, key arg is used to distinguish them
pd.concat([ser1, ser2], keys=[1, 2])

# Build data frames. Note indices on frame2
frame1 = pd.DataFrame(np.random.rand(9).reshape(3, 3),
                      index=[1, 2, 3],
                      columns=["A", "B", "C"])
frame2 = pd.DataFrame(np.random.rand(9).reshape(3, 3),
                      index=[4, 5, 6],
                      columns=["A", "B", "C"])
# Combine over rows (axis=0 is not needed, default)
comb_df_rows = pd.concat([frame1, frame2], axis=0)

# Combine over columns
comb_df_cols = pd.concat([frame1, frame2], axis=1)

# Define series with overlapping indices
ser1 = pd.Series([10, 20, 30, 40, 50], index=[1, 2, 3, 4, 5])
ser2 = pd.Series([21, 41, 51, 61], index=[2, 4, 5, 7])

# combine series while keeping those of ser1
comb_ser1_2 = ser1.combine_first(ser2)

# combine series focusing on ser2
comb_ser2_1 = ser2.combine_first(ser1)

# Combine parts of ser1 and ser2. Note the command below
# ser1[:3].combine_first(ser2[:3])  # Deprecate
ser1.iloc[:3].combine_first(ser2.iloc[:3])

# stacking and unstacking
frame1 = pd.DataFrame(
    np.arange(9).reshape(3, 3),
    index=["white", "black", "red"],
    columns=["ball", "pen", "pencil"],
)
# Create a long table
frame_stacked = frame1.stack()

# Revert to a wide table
frame_unstacked = frame_stacked.unstack()

# Specify which level to be unstacked
frame_unstacked_l0 = frame_stacked.unstack(0)
frame_unstacked_l1 = frame_stacked.unstack(1)  # same as no specifying level

longframe = pd.DataFrame({
    "color": [
        "white", "white", "white", "red", "red", "red", "black", "black",
        "black"
    ],
    "item": ["ball", "pen", "mug", "ball", "pen", "mug", "ball", "pen", "mug"],
    "value":
    np.random.rand(9),
})
wideframe = longframe.pivot(index='color', columns='item')

# Define dataframe
frame1 = pd.DataFrame(np.arange(9).reshape(3, 3),
                      index=['white', 'black', 'red'],
                      columns=['ball', 'pen', 'pencil'])

# Remove column
del frame1['ball']

# Remove row
frame1_norow = frame1.drop('white')

dframe = pd.DataFrame({
    'color': ['white', 'white', 'red', 'red', 'white'],
    'value': [2, 1, 3, 3, 2]
})

# Find duplicates. Returns a bool
duplicates = dframe.duplicated()
dframe_dedup = dframe[~duplicates]
dframe_dedup2 = dframe.drop_duplicates()  # same as dframe_dedup

frame = pd.DataFrame({
    'item': ['ball', 'mug', 'pen', 'pencil', 'ashtray'],
    'color': ['white', 'rosso', 'verde', 'black', 'yellow'],
    'price': [5.56, 4.20, 1.30, 0.56, 2.75]
})

newcolors = {'rosso': 'red', 'verde': 'green'}

frame_v2 = frame.replace(newcolors)

# Define a dictionary with item: prices
prices = {
    'ball': 5.56,
    'mug': 4.20,
    'bottle': 1.30,
    'scissors': 3.41,
    'pen': 1.30,
    'pencil': 0.56,
    'ashtray': 2.75
}

# create a new 'price' column and match the items to prices
frame['price'] = frame['item'].map(prices)

# Dictionary with new indices
reindex = {0: 'first', 1: 'second', 2: 'third', 3: 'fourth', 4: 'fifth'}
recolumn = {'item': 'object', 'price': 'value'}

# Rename indices
frame_v2 = frame.rename(reindex)

# Rename indices and columns
frame_v3 = frame.rename(index=reindex, columns=recolumn)

# Inplace replacement
frame.rename(columns={'item': 'object'}, inplace=True)

# map defined in function
frame.rename(index={1: 'first', 2: 'dos'}, columns={'item': 'object'})

# generate a list of 100 random integers between 1:100
random_integers = np.random.randint(1, 101, size=100)

# define categories (bins)
bins = [0, 25, 50, 75, 100]

# divide (cut) the array into the defined bins
cat = pd.cut(random_integers, bins)

# Add labels to bins
bin_names = ['unlikely', 'less likely', 'likely', 'highly likely']
cat_labels = pd.cut(random_integers, bins, labels=bin_names)

# Divide results based on the min and max value into n intervals
cat_2 = pd.cut(random_integers, 5)

# check that the categories match the bins
cat.categories

# check that the code numbers match the number of categories
pd.Series(cat.codes).unique()

# Count the number of ocurrences
pd.value_counts(cat)

# Divide the array into quartiles
quartiles = pd.qcut(random_integers, 4)

# Create a working data frame
randframe = pd.DataFrame(np.random.randn(1000, 3))

# Calculate threshold
thr = 3 * randframe.std()

# Filter
randframe_3sd = randframe[(np.abs(randframe) > thr).any(axis=1)]

# Modify data frame to add a row with all values above threshold
randframe_mod = randframe.copy()  # Makes an independent copy
randframe_mod.loc[1] = pd.Series([4, 4, 4])  # Add custom values
randframe_mod_3sd = randframe_mod[(np.abs(randframe_mod)
                                   > thr)]  # Uses same threshold
randframe_mod_3sd = randframe_mod_3sd.dropna()  # Removes NaN

# Working data frame
nframe = pd.DataFrame(np.arange(35).reshape(7, 5))

# Array of index in random order
new_order = np.random.permutation(7)

# Re-order data frame
nframe_v2 = nframe.take(new_order)

# Define and apply subsample
subsample = np.random.randint(0, len(nframe), size=3)
nframe_sub = nframe.take(subsample)

# Split string on a character
text = '16 Bolton Avenue , Boston'
text_split = [s.strip() for s in text.split(',')]
address, city = [s.strip() for s in text.split(',')]

# concatenate - join strings
text_concat = address + ',' + city  # Cumbersome for many objects
text_join = ','.join(text_split)  # Requires a list

# search for text
'Boston' in text  # Returns a boolean
text.index('Boston')  # Returns index, error if not found
text.find('Boston')  # Returns index, '-1' if not found

# Count ocurrences
text.count('e')  # Returns '2'
text.count('Avenue')  # Returns '1'

# Replace strings
text_v1 = text.replace('Avenue', 'Street')
text_v2 = text.replace('1', '')  # Deletes '1'

import re

# Dummy example of a text with white spaces
text = "This is   an\t odd  \n text!"

# Remove spaces (split() function)
text_noSpaces = re.split('\s+', text)

# Compile a regular expression for re-use
regex = re.compile('\s+')

# Remove spaces (similar to text_noSpaces)
text_noSpaces_v2 = regex.split(text)

# Define text
# address = 'This is my address: 16 Bolton Avenue, Boston'  # Original sentence
address = 'This a temporary address: 16 Bolton Avenue, Boston'

# Find all words starting with 'A' or 'a'
# text_aA = re.findall('[A,a]\w+',text) # Doesn't work
pattern1 = r'\b[Aa]\w*'
text_aA = re.findall(pattern1, address)

# Find all the words containing an 'a' or 'A'
pattern2 = r'\b[Aa]\w+|a\w+|a'
text_aA_v2 = re.findall(pattern2, address)

# Find the first occurrence of a word that starts with A or a
index_aA_first = re.search(pattern1, address)  # returns a match object

# Extract the first match
text_aA_first = address[index_aA_first.start():index_aA_first.end()]

# Search only at the beginning of the string (match() function)
text_T_first = re.match('T\w+', text)
text_T_first_v2 = re.search('^T\w+', address)  # same as text_T_first

# Define working dataframe
frame = pd.DataFrame({
    'color': ['white', 'red', 'green', 'red', 'green'],
    'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
    'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
    'price2': [4.75, 4.12, 1.60, 0.75, 3.15]
})

# Group price1 column based on color
group = frame['price1'].groupby(by=frame['color'], axis=0)

# Calculate the mean price of objects grouped by color
price1_mean_color = group.mean()

# Group multiple columns explicitly or implicitly
# The second raises a warning if the mean argument is not provided
prices_mean_color = frame[['price1', 'price2']].groupby(frame['color']).mean()
prices_mean_color_v2 = frame.groupby(frame['color']).mean(numeric_only=True)

group2 = frame.groupby('color')
for name, group in group2:
    print(name)
    group['total'] = group['price1'] + group['price2']
    print(group)

# Select column before grouping
mean_1 = frame['price1'].groupby(frame['color']).mean()

# Select column after grouping
mean_2 = frame.groupby(frame['color'])['price1'].mean()

# Select column after applying a function
mean_3 = (frame.groupby(frame['color']).mean(numeric_only=True))['price1']

# working group object
group = frame.groupby('color')


# Define custom function
def range(series):
    return series.max() - series.min()


# apply multiple functions with agg()
isummary = group['price1'].agg(['mean', 'std', range])

# Working dataframe 1
frame = pd.DataFrame({
    'color': ['white', 'red', 'green', 'red', 'green'],
    'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
    'price2': [4.75, 4.12, 1.60, 0.75, 3.15]
})

# Calculate totals per color
totals = frame.groupby('color').transform(np.sum).add_prefix('tot_')

# Merge totals to working dataframe
frame_updated = pd.merge(frame, totals, right_index=True, left_index=True)

# Working dataframe 2
frame2 = pd.DataFrame({
    'color': ['white', 'black', 'white', 'white', 'black', 'black'],
    'status': ['up', 'up', 'down', 'down', 'down', 'up'],
    'value1': [12.33, 14.55, 22.34, 27.84, 23.40, 18.33],
    'value2': [11.23, 31.80, 29.99, 31.18, 18.25, 22.44]
})

# Calculate max value per color and status
max_values = frame2.groupby(['color', 'status'
                             ]).apply(lambda x: x.max()).add_prefix('max_')

# Modify multi-index as it is redundant with columns
max_values = max_values.droplevel(0)
max_values.index = range(4)
