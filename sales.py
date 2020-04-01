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



# # # 1. The best month for sales and how much earned in that month

# Data Cleaning: Drop the rows with missing values or categorical values

merged_file.dropna(subset=['Order ID'],inplace=True)
import numpy as np
merged_file = merged_file[merged_file['Order ID'].apply(lambda x: np.isreal(x))]
merged_file.reset_index(inplace=True, drop=True)


#f = 0

#value = merged_file.at[f, 'Order ID']
#for value in merged_file:
#    if value is None:
#        merged_file.drop(merged_file.index[f])
#        merged_file.reset_index(inplace=True, drop=True)
#        f+=1
#        continue
#    elif value == 'Order ID':
#        merged_file.drop(merged_file.index[f])
#        merged_file.reset_index(drop=True, inplace=True)
#        f+=1
#        continue
#    elif f==186845:
#        break
#    else:
#        f+=1
#        continue

#while f<186840:
#    if f<186840:
#        merged_file.dropna()
#        f+=1
#    else:
#        break




#print(merged_file.head())
print(merged_file.at[253, 'Order ID'])
print(merged_file.at[254, 'Order ID'])
print(merged_file.at[255, 'Order ID'])

# add an additional column for the month of order date
#merged_file['Order Month'] = merged_file['Order Date'].str[:2]
#merged_file['Order Month'] = merged_file['Order Month'].astype('int32', copy=False)






# get the revenue
#for df. in merged_file
 #   revenue = (merged_file.df['Quantity Ordered'] * merged_filed.df['Price Each'])