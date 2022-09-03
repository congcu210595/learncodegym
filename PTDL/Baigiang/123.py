import pandas as pd
df = pd.read_csv("FoodPrice_in_Turkey.csv")
print(df.pivot_table(values='Price',index='ProductName',columns='Year',aggfunc ='mean'))