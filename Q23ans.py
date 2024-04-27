from scipy import stats
from scipy.stats import norm

# t scores of 95% confidence interval for sample size of 25
stats.t.ppf(0.975,24)  # df = n-1 = 24

# t scores of 96% confidence interval for sample size of 25
stats.t.ppf(0.98,24)

# t scores of 99% confidence interval for sample size of 25
stats.t.ppf(0.995,24)
