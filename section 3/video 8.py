import numpy as np
'''
array1 = np.array([1,2,3,4,5])
array2 = np.array([5,6,7,8,9])

addition_array = np.add(array2,array1)
print(addition_array)

subtract_array = np.subtract(array2,array1)
print(subtract_array)

multiplication_array = np.multiply(array2,array1)
print(multiplication_array)

division_array = np.divide(array2,array1)
print(division_array)
'''

angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

sine_result = np.sin(angles)
print("\nSine result: ",np.round( sine_result))

cosine_result = np.cos(angles)
print("\nCosine result: ",np.round( cosine_result))