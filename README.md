# Sales Analysis

***Installation***
```
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

# # To merge 12 months of sales data into a single file
import os
import glob
```

***Import then merge the dataset***
```
# selecting working folder
path="/Users/kitaeklee/PycharmProjects/sales/Sales_Data"

# collect all files needed to be combined
all_files = glob.glob(os.path.join(path, "Sales_*.csv"))

# read, concatenate
merged_file = pd.concat((pd.read_csv(f, sep=',') for f in all_files), ignore_index=True)

# export as CSV to the local directory
merged_file.to_csv("/Users/kitaeklee/PycharmProjects/sales/merged_file.csv", index=False)
```
Merged file looks like below:
![](image_sales/1.imported_data.png)

```
# To remove SettingWithCopyWarning
pd.options.mode.chained_assignment = None  # default='warn'
```

***Data Cleaning***
```
# # # Data Cleaning: Drop the rows with missing values or categorical values

# Drop rows with null values
merged_file.dropna(subset=['Order ID'], inplace=True, axis=0)
# Reassign the values to merged_file where the values of 'Order date'.str[0:2] are not 'Or' to drop categorical variables
merged_file = merged_file[merged_file['Order Date'].str[0:2] != 'Or']

merged_file.reset_index(inplace=True, drop=True)
```


***1. The best and the worst month for sales***
```
#########################################################################
# # # 1. The best month for sales and how much earned in that month

# add an additional column for the month of the Order Date
merged_file['Order Month'] = merged_file['Order Date'].str[:2]
merged_file['Order Month'] = merged_file['Order Month'].astype('int32', copy=False)

# change the data types to float
merged_file['Quantity Ordered'] = merged_file['Quantity Ordered'].astype('float64', copy=False)
merged_file['Price Each'] = merged_file['Price Each'].astype('float64', copy=False)
# Create Sales column
merged_file['sales'] = (merged_file['Quantity Ordered'] * merged_file['Price Each'])
```
- Create a new Dataframe for sales and month
```
# sum of 'sales', to each 'Order Month' then max out of all.
best_sales = merged_file.groupby('Order Month')['sales'].sum().max()

# create a new dataframe with months and sales
month_sales = merged_file.groupby('Order Month')['sales'].sum().reset_index()
```
- Plot the dataframe using bar graph
```
# Visualization

colors = list('ybbbbbbbbbbr')

month_sales.plot(x='Order Month', y='sales', kind='bar', color=colors,
                legend=None)
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xticks(rotation=360)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Total sales in each month')
```
![](image_sales/2.bargraph_no1.png)
