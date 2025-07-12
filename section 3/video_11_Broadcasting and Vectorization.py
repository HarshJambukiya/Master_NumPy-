import numpy as np

array1 = np.array([1,2,3])
array2 = np.array([[10],[20],[30]])

result = array1 + array2
print(array1)
print("\n Broadcasting Addition result: ", result)

#Vectorziation

data = np.array([1,2,3,4,5])

squared_data = data**2
print("Original Data: ", data)
print("Squared Data: ", squared_data)