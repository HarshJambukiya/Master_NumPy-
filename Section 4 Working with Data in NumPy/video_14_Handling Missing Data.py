import numpy as np

# GENERATE MISSING DATA MANUALLY
data = np.array([1,np.nan , 2 , 3])
print("Original Data:\n", data)

print("Indentify Missing Values:\n", np.isnan(data))

data2 =np.array([1, np.nan, 2, np.nan , np.nan, 3 , np.nan ,5])

# REPLACE MISSING VALUE TO -1
data_replaced = np.nan_to_num(data2 ,nan = -1)
print(data_replaced)

# REMOVED MISSING VALUE FROM ARRAY
data_removed= data[~np.isnan(data)]
print(data_removed)