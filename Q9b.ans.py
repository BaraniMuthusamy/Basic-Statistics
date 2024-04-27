
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("Q9_b.csv")
df

#Skewness

df.skew()

df.kurt()


plt.boxplot(df.SP)
plt.show()

plt.boxplot(df.WT)
plt.show()

