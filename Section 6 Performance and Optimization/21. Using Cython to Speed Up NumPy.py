import numpy as np
import time
from sum_of_squarexs_cython import sum_of_squares_cython

# WITHOUT CYTHON
'''
def sum_of_squares(x):
    return np.sum(x**2)

x = np.random.rand(5)
start = time.time()
result = sum_of_squares(x)
end = time.time()

print(f"Result is {result}")
print(f"Time taken: {end - start}")"
'''

'''
print(result) 
print(end - start)

''' # Not Good

# WITH CYTHON

x = np.random.rand(1000)

start = time.time()
result = sum_of_squares_cython(x)
end = time.time()

print(f"Result is {result}")
print(f"Time taken: {end - start}")

