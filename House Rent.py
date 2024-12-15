import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("USA_Housing.csv")
print(df.head())

print(df.info())

print(df.describe())

print(df.columns)

df = df.drop(columns= ["Address"])

#sns.pairplot(df)

sns.heatmap(df.corr(), annot = True)

plt.show()