
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("Q9_a.csv")
df

#Skewness

df.skew()

df.kurt()


plt.boxplot(df.speed)
plt.show()

plt.boxplot(df.dist)
plt.show()

