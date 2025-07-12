import numpy as np


matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[1,1],[1,1]])

dot_product = np.dot(matrix1,matrix2)
print("Dot product: ", dot_product)

reult_set = matrix1 @ matrix2
print("Reult_set: ", reult_set)
 

# Like this 3x + 1y = 9 & 1x + 2y = 8

A = np.array([[3,1],[1,2]])
B = np.array([9,8])

print("A: ", A)
print("B: ", B)
print("\n Solution of linear algebra: ", np.linalg.solve(A,B))