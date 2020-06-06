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

***Import dataset***
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

```
