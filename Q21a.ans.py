
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm

cars=pd.read_csv("cars.csv")
cars.head()
cars['MPG'].mean()

cars['MPG'].median()

cars['MPG'].mode()

cars['MPG'].hist()

sns.distplot(cars['MPG'])
plt.grid(True)
plt.show()

cars['MPG'].skew()

cars['MPG'].kurt()