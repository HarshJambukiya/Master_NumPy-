from cProfile import label

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# NUMPY WITH PANDAS

data = np.random.randn(2,2)

df = pd.DataFrame(data , columns =['A', 'B' ])

print("Numpy Data",data)
print("Pandas Dataframe\n",df)



#NUMPY WITH MATPLOTLIB PLOT

X =np.linspace(0,10,100)
Y =np.sin(X)

plt.plot(X,Y , label = 'sin(X)')
plt.xlabel('X')
plt.ylabel('sin(X)')
plt.title('Plot of the sin(x)')
plt.legend()
plt.show()


