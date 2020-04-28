
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


#########################################################################
# # # 1. The best month for sales and how much earned in that month

merged_file['Quantity Ordered'] = merged_file['Quantity Ordered'].astype('float64', copy=False)
merged_file['Price Each'] = merged_file['Price Each'].astype('float64', copy=False)
merged_file['sales'] = (merged_file['Quantity Ordered'] * merged_file['Price Each'])

# sum of 'sales', to each 'Order Month' then max out of all.
best_sales = merged_file.groupby('Order Month')['sales'].sum().max()

merged_file['sales_sum'] = merged_file.groupby('Order Month')['sales'].sum()
best_sales_month = merged_file['Order Month'][best_sales == merged_file['sales_sum']]
#print(best_sales_month)


# # # Visualization
import numpy as np
import matplotlib.pyplot as plt

month = list(range(1,13))
#plt.bar(month, merged_file['sales_sum'][1:13])

#plt.title('Sales of each months')
#plt.ylabel('Sales')
#plt.xlabel('Month')
#plt.xticks(np.arange(1, 12, 1))
# use ticklabel_format to remove exponentional(scientific) notation on Y-axis
#plt.ticklabel_format(useOffset=False, style='plain')
#plt.show()



#########################################################################
# # # 2. Which city had the highest number of sales
# Create a new column for cities
merged_file['city'] = merged_file['Purchase Address'].str.split(",")
merged_file['city'] = merged_file['city'].str.get(1)
# To deal with the duplicates of the name of the cities, create state column
merged_file['state'] = merged_file['Purchase Address'].apply(lambda x: x.split(",")[2])
def split_state(address):
    return address.split(" ")[1]
merged_file['state'] = merged_file['state'].apply(lambda x: split_state(x))
merged_file['city'] = merged_file['city'] + " " + merged_file['state']

# Create Dataframe for sum of sales that grouped by cities and states
sales_sum_city = merged_file.groupby(['city', 'state'])['sales'].sum()
sales_sum_city = sales_sum_city.to_frame()      # convert series into dataframe
sales_sum_city = sales_sum_city.reset_index()
sales_sum_city['sales'] = sales_sum_city['sales'].astype('str')
sales_sum_city['sales'] = sales_sum_city['sales'].apply(lambda x: x.split(".")[0])
sales_sum_city['sales'] = sales_sum_city['sales'].astype('float')

# Visualize
ax = sales_sum_city.plot(kind='bar', x='city', y='sales', color='#5cb85c', figsize=(7,7))
ax.set_xticklabels(sales_sum_city['city'])
ax.set_yticklabels(sales_sum_city['sales'])
ax.set_title('Sales of each cities')
plt.ylabel('Sales($)', fontsize=15)
plt.xlabel('Cities', fontsize=15)
plt.title('Sales in each cities', fontsize=15)
plt.tight_layout()
#plt.show()


#########################################################################
# # # 3. What time should we display advertisements to maximize likelihood of customers' buying product?

merged_file['Order Date'] = pd.to_datetime(merged_file['Order Date'])
merged_file['Hour'] = merged_file['Order Date'].dt.hour
merged_file['Minute'] = merged_file['Order Date'].dt.minute

sales_sum_hour = merged_file['sales'].groupby(merged_file['Hour']).sum()
sales_sum_hour = sales_sum_hour.to_frame()
sales_sum_hour = sales_sum_hour.reset_index(inplace=False)
sales_sum_hour['Hour'] = list(map(str, range(1,25)))
#ax = merged_file.plot(kind='line', x='Hour', y='sales')
#ax.set_xticklabels(list(map(str, range(1,25)))
#ax.set_yticklabels(merged_file['sales'])
#plt.show()
print(sales_sum_hour)

