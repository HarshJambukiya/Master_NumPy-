import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('data1.csv.txt', data )
#np.savetxt('data.csv.txt', data , delimiter=',')
print("\nData Saved to'data.csv' successfully!")
