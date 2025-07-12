import numpy as np

data = np.array([ (1 ,'Harsh', 21) , (1 ,'raj', 25), (1 ,'tapu', 14 )],
                dtype= [('ID', int), ('Name','U10'), ('Age',int )])
print(data)

print(("\nAccessing specific fields"))
print("NAME :- ", data['Name'] )
print("NAME :- ", data['Age'] )
