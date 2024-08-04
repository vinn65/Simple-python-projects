import pandas as pd

data = pd.read_csv('trees.csv', names=['I','Girth','Height','Volume'] )

del data['I']
data.drop(0, inplace=True)

data['Girth'] = data['Girth'].astype(float)
data['Height'] = data['Height'].astype(float)
data['Volume'] = data['Volume'].astype(float)

data['Girth'] *= 0.0254
data['Height'] *= 0.305
data['Volume'] *= 0.0283
data = data.round(2)

max_g = data['Girth'].max()
max_h = data['Height'].max()
max_v = data['Volume'].max()

min_g = data['Girth'].min()
min_h = data['Height'].min()
min_v = data['Volume'].min()

avg_g = data['Girth'].mean()
avg_h = data['Height'].mean()
avg_v = data['Volume'].mean()

med_g = data['Girth'].median()
med_h = data['Height'].median()
med_v = data['Volume'].median()

mod_g = data['Girth'].mode()
mod_h = data['Height'].mode()
mod_v = data['Volume'].mode()
print(max_g)
print(data.head())


import matplotlib.pyplot as plt

plt.plot(data['Girth'])
plt.title('Girth')
plt.ylabel('Metres')
# plt.show()

plt.plot(data['Height'])
plt.title('Height')
plt.ylabel('Metres')
# plt.show()

plt.plot(data['Volume'])
plt.title('Volume')
plt.ylabel('Cubic Metres')
plt.show()