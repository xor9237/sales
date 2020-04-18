
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


# # # Data Cleaning: Drop the rows with missing values or categorical values
# Drop rows with null values
merged_file.dropna(subset=['Order ID'], inplace=True, axis=0)
# Reassign the values to merged_file where the values of 'Order date'.str[0:2] are not 'Or'
# to drop categorical variables
merged_file = merged_file[merged_file['Order Date'].str[0:2] != 'Or']

merged_file.reset_index(inplace=True, drop=True)


# add an additional column for the month of the Order Date
merged_file['Order Month'] = merged_file['Order Date'].str[:2]
merged_file['Order Month'] = merged_file['Order Month'].astype('int32', copy=False)



# # # 1. The best month for sales and how much earned in that month

merged_file['Quantity Ordered'] = merged_file['Quantity Ordered'].astype('float64', copy=False)
merged_file['Price Each'] = merged_file['Price Each'].astype('float64', copy=False)
merged_file['sales'] = (merged_file['Quantity Ordered'] * merged_file['Price Each'])

# sum of 'sales', to each 'Order Month' then max out of all.
best_sales = merged_file.groupby('Order Month')['sales'].sum().max()

merged_file['sales_sum'] = merged_file.groupby('Order Month')['sales'].sum()
best_sales_month = merged_file['Order Month'][best_sales == merged_file['sales_sum']]



# # # Visualization
import numpy as np
import matplotlib.pyplot as plt

month = list(range(1,13))
plt.bar(month, merged_file['sales_sum'][1:13])

plt.title('Sales of each months')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.xticks(np.arange(1, 12, 1))
# use ticklabel_format to remove exponentional(scientific) notation on Y-axis
plt.ticklabel_format(useOffset=False, style='plain')
plt.show()

plt.show()
# # # 2. Which city had the highest number of sales


