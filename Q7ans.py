
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df=pd.read_csv("Q7.csv")
df
#mean
df.mean()

#median
df.median()

#mode
df.Points.mode()

df.Score.mode()

#standard deviation

df.std()
df.describe()

plt.boxplot(df.Points)
plt.show()

plt.boxplot(df.Score)
plt.show()

plt.boxplot(df.Weigh)
plt.show()





