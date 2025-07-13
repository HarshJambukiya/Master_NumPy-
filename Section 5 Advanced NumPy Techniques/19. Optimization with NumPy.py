import numpy as np
import time

array = np.random.rand(10)

def sum_with_loop(array):
    total = 0
    for num in array:
        total += num
    return total
print("Sum with loop - ",sum_with_loop(array))



