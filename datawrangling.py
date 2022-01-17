import pandas as pd
df = pd.read_csv("Mobile_Food_Facility_Permit.csv")
# print(df)

# Step 1: Exploration
# Print basic information about the dataset. 

# Number of rows
# print('Number of rows:',len(df.index))

# Number of columns
# shape = df.shape
# print('Number of columns:', shape[1])

# Step 2: Select, Filter, Sort

# Sort applicants alphabetically
# app_asc = df.sort_values('Applicant', ascending=True)
# print('Applicants assorted alphabetically:\n', app_asc)

# Sort by the type of Facility Type
# ft_asc = df.sort_values('FacilityType', ascending=True)
# print('Facility Type assorted alphabetically\n', ft_asc)

# Sort by cnn column
# sort_ccn = df.sort_values(by=['cnn'])
# print('Sorted by cnn:\n', sort_ccn)

# Step 3: Clean Data

#print(df.isnull())
#There are no null values so there is nothing to replace

# Step 4: Transform Data

# Resetting index and dropping the original index being set to a column)
# print(df.reset_index(drop=True))

