import numpy as np
import time

arr1 = np.random.rand(1000000)
arr2 = np.random.rand(1000000)

# Addition using a loop
start_time = time.time()
result_loop = np.zeros_like(arr1)
for i in range(len(arr1)):
    result_loop[i] = arr1[i] + arr2[i]
loop_duration = time.time() - start_time

# Addition using vectorized operation
start_time = time.time()
result_vectorized = arr1 + arr2
vectorized_duration = time.time() - start_time

print(loop_duration)
print(vectorized_duration)
