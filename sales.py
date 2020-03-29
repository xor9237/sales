import pandas as pd

# # merge 12 months of sales data into a single file

import os
import glob

# selecting working folder
path="/Users/kitaeklee/PycharmProjects/sales/Sales_Data"

# collect all files needed to be combined
all_files = glob.glob(os.path.join(path, "Sales_*.csv"))

# read, concatenate
merged_file = pd.concat((pd.read_csv(f, sep=',') for f in all_files), ignore_index=True)

# export as CSV to the local directory
merged_file.to_csv("/Users/kitaeklee/PycharmProjects/sales/merged_file.csv", index=False)

#add an additional column for the date
merged_file2 = merged_file.assign(merged_file.at['Order Date'])


# # The best month for sales and how much earned in that month
# find and drop the rows with missing values or categorical values
f = 0

value = merged_file.at[f, 'Order ID']
for value in merged_file:
    if value is None:
        merged_file.drop(merged_file.index[f])
        merged_file.reset_index(inplace=True, drop=True)
    elif value == 'Order ID':
        merged_file.drop(merged_file.index[f])
        merged_file.reset_index(drop=True, inplace=True)
    elif f==186845:
        break
    else:
        f+=1

while f<186840:
    if f<186840:
        merged_file.dropna()
        merged_file.select_dtypes(exclude=['object'])
        f+=1
    else:
        break







print(merged_file.head())
print(merged_file.at[253, 'Order ID'])
print(merged_file.at[254, 'Order ID'])
print(merged_file.at[255, 'Order ID'])


# get the revenue
#for df. in merged_file
 #   revenue = (merged_file.df['Quantity Ordered'] * merged_filed.df['Price Each'])