import numpy as np

data = np.random.rand(3,3)
print("\nGenerated Data: ", data)

#data = np.loadtxt('data.csv', delimiter=',')
#print("Loaded Data: ", data)

data2 = np.load('data2.npy')
print("\nLoaded Data : ", data2)