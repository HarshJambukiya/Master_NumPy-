import numpy as np
'''
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

array_hstack = np.hstack((array1 , array2))
print(array_hstack)

'''

array = np.array([[1,2,3,4,5,6],
                 [7,8,9,10,11,12]])

array_hspilt = np.hsplit(array,3)

print(array)
for arr in array_hspilt:
    print(arr)