# real estate price prediction
import pandas as pd
import matplotlib as plt
housing=pd.read_csv("data.csv")
# print(housing.head())
# print(housing.info())
print(housing['CHAS'])
print(housing['CHAS'].value_counts())
print(housing.describe())
# %matplotlib inline
housing.hist(bins=50,figsize=(20,15))
# plt.show()