from scipy import stats
from scipy.stats import norm 
# Z-score of 90% confidence interval 
stats.norm.ppf(0.95)

# Z-score of 94% confidence interval
stats.norm.ppf(0.97)

# Z-score of 60% confidence interval
stats.norm.ppf(0.8)
