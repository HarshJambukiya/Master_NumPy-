import numpy as np

orginal_array = np.arange(10)

'''
copyed_array = orginal_array.copy()
print(copyed_array)
'''
orginal_array1 = np.array([1,2,3,4,5])
view_array = orginal_array1.view()

view_array[4] = 0
print("\nModified array: ", view_array)

