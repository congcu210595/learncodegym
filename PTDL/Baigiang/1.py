import pandas as pd
import numpy as np

data = pd.read_csv('OnlineRetail.csv')

#print(data.info())
#print(data.shape[0])
#print(data.shape[1])
print(data.columns)
data['Ten cot moi'] = np.nan
data["Ten cot moi"] = 10
print(data.info())
data.drop("Ten cot moi",axis=1, inplace=True)
print(data)
cell = data.iloc[0,1]
print("*"*30)
print(data.iloc[0])
print(cell)