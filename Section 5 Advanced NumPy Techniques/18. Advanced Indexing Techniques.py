import numpy as np

# EVEN NUMBER
arr = np.arange(10)
even_array = arr[arr % 2 == 0]
print("Original Array", arr)
print("Even Array", even_array)


#ADVANCE INDEXING IN ARRAY 2D
arry1 = np.array([[10,20,30], [ 40,50,60] , [70,80,90]])
print("Original Array\n", arry1)
selected_element = arry1[[0,1,2], [2,0,1]]
selected_element1 = arry1[[2,1,2], [2,1,1]] # [ 90 50 80 ]
print("Selected Element\n", selected_element1)
print(selected_element)

arry2 = np.arange(101)

every_other_element = arry2[::10]
print("Original Array\n", arry2)
print("Every other Array\n", every_other_element)