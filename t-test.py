# Two tailed test
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import t

# Load the CSV file with student scores for two teaching methods
file_path = 'https://raw.githubusercontent.com/Pavithran030/AI/refs/heads/main/teaching_methods_data_v2.csv'
data = pd.read_csv(file_path)

# Extract the scores for both methods
method_A = data['Method_A']
method_B = data['Method_B']

# Sample sizes
n1 = len(method_A)
n2 = len(method_B)

# Degrees of freedom (df)
df = (n1 - 1) + (n2 - 1)

# Perform independent two-sample t-test
t_stat= stats.ttest_ind(method_A, method_B)

# Absolute value of the calculated t-statistic
# Access the t-statistic from the TtestResult object
t_stat_abs = abs(t_stat.statistic)

# Significance level (alpha) and critical t-value
alpha = 0.05  # 95% confidence level
critical_t_value = t.ppf(1 - alpha/2, df)  # Two-tailed test

# Display results
print(f"Calculated t-statistic: {t_stat_abs:.3f}")
print(f"Critical(table) t-value: {critical_t_value:.3f}")
print(f"Degrees of Freedom: {df}")

# Compare the calculated t-statistic to the critical t-value
if t_stat_abs > critical_t_value:
    print("We reject the null hypothesis: There is a significant difference between the two teaching methods.")
else:
    print("We accept the null hypothesis: There is no significant difference between the two teaching methods.")

# Plotting histograms of the data for both teaching methods
plt.figure(figsize=(10,6))
plt.hist(method_A, alpha=0.5, label='Method A', bins=5, color='blue')
plt.hist(method_B, alpha=0.5, label='Method B', bins=5, color='green')
plt.title('Distribution of Scores for Teaching Methods A and B')
plt.xlabel('Scores')
plt.ylabel('Counts')
plt.legend()
plt.show()



#One tailed test
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import t

# Load the CSV file with student scores for two teaching methods
file_path = 'https://raw.githubusercontent.com/Pavithran030/AI/refs/heads/main/teaching_methods_data_v2.csv'
data = pd.read_csv(file_path)

# Extract the scores for both methods
method_A = data['Method_A']
method_B = data['Method_B']

# Sample sizes
n1 = len(method_A)
n2 = len(method_B)

# Degrees of freedom (df)
df = (n1 - 1) + (n2 - 1)

# Perform independent one-tailed t-test
# Hypothesis: Method_A < Method_B
t_stat, p_value = stats.ttest_ind(method_A, method_B)

# Significance level (alpha) and critical t-value for left-tailed test
alpha = 0.05  # 95% confidence level
critical_t_value = t.ppf(alpha, df)  # one-tailed test

# Display results
print(f"Calculated t-statistic: {t_stat:.3f}")
print(f"Critical t-value (one-tailed): {critical_t_value:.3f}")
print(f"Degrees of Freedom: {df}")

# Compare the calculated t-statistic to the critical t-value
if t_stat < critical_t_value:  #testing if Method A < Method B
    print("We reject the null hypothesis: Method A has a significantly lower mean score than Method B.")
else:
    print("We accept the null hypothesis: Method A does not have a significantly lower mean score than Method B.")

# Plotting histograms of the data for both teaching methods
plt.figure(figsize=(10,6))
plt.hist(method_A, alpha=0.5, label='Method A', bins=5, color='green')
plt.hist(method_B, alpha=0.5, label='Method B', bins=5, color='blue')
plt.title('Distribution of Scores for Teaching Methods A and B')
plt.xlabel('Scores')
plt.ylabel('Counts')
plt.legend()
plt.show()
