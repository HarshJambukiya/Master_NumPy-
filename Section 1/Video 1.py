import numpy as np

# Create a one-dimensional array
'''
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(arr)

print("First Element " ,arr[0])
print("Last Element " ,arr[-1])

'''

# Create a two-dimensional array
'''
matrix = np.array([[1,2,3],[4,5,6]])

print(matrix)
print("First Element " ,matrix[0,0]) # 1
print("First Element " ,matrix[0,1]) # 2
print("First Element " ,matrix[0,2]) # 3
print("First Array But Last Element " ,matrix[1,0]) # 4
print("First Array But Last Element " ,matrix[1,1]) # 5
print("First Array But Last Element " ,matrix[1,2]) # 6

print("First Array But Last Element " ,matrix[0]) # 1 2 3
print("First Array But Last Element " ,matrix[1]) # 4 5 6

print("First Array But Last Element " ,matrix[-1]) # 4 5 6
print("First Array But Last Element " ,matrix[-2]) # 1 2 3

print("First Array But Last Element " ,matrix[-2, -1]) # 3
print("First Array But Last Element " ,matrix[-1 ,-2]) # 5
'''

# Reshape The Array
'''
reshaped_matrix = matrix.reshape(1, 6) # Here 1 row & 6 Column
reshaped_matrix1 = matrix.reshape(6, 1) # Here 6 row & 1 Column
reshaped_matrix2 = matrix.reshape(2, 3) # Here 2 row & 3 Column
reshaped_matrix3 = matrix.reshape(3, 2) # Here 3 row & 2 Column
reshaped_matrix4 = matrix.reshape(-1, 6) # Here 1 row & 6 Column


print(reshaped_matrix)
print(reshaped_matrix1)
print(reshaped_matrix2)
print(reshaped_matrix3)
print(reshaped_matrix4)

'''

# Matrix Arithmetic operation

matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])

added_matrix = matrix1 + matrix2
multiplication_matrix = matrix1 * matrix2
minus_matrix = matrix2 - matrix1

scalar_matrix = matrix1 * 3

print(scalar_matrix)

print(added_matrix)
print(multiplication_matrix)
print(minus_matrix)

