import pandas as pd
data = pd.read_csv('subset-covid-data.csv')
print(data.head())
cleaned_data = data[data.date == '2020-04-12']
print (cleaned_data.cases.mean())
print (cleaned_data.cases.median())
import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title("Phan bo so ca mac moi")
plt.xlabel("so ca mac moi")
plt.ylabel("So luong quoc gia")