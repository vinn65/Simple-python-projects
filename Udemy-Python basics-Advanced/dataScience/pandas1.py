import pandas as pd
import numpy as np
ar = pd.Series([12,3,4,5], index=['a',2,3,4])# can use data in the series to pass an array

# print(ar)


# print(ar.loc['a'])

df = pd.DataFrame({'Age':[2,3,4],
                   'color':["blue",'red','yellow']})
# print(df)

ar2 = np.array([[1,2,3],
                 [2,5,6],
                 [2,3,4]
                 ])
df1 = pd.DataFrame(data=ar2, columns=['C1','C2','C3'], index=['A','B','C'])
print(df1.loc['B'])
print(df1.values[1,2])

