import numpy as np
import matplotlib.pyplot as plt

# Let's assume we have a list of returns for each repetition of the task
# For example, task_returns could be a list of lists where each sublist contains the returns from one repetition
# Here we generate some random data to simulate this
np.random.seed(0)
task_returns = [np.random.normal(loc=0, scale=1, size=100) for _ in range(10)]

# Function to calculate the bootstrap confidence interval
def bootstrap_confidence_interval(data, num_bootstrap=10000, confidence_level=0.90):
    means = []
    for _ in range(num_bootstrap):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        means.append(np.mean(bootstrap_sample))
    lower_bound = np.percentile(means, (1 - confidence_level) / 2 * 100)
    upper_bound = np.percentile(means, (1 + confidence_level) / 2 * 100)
    return lower_bound, upper_bound

# Calculate the mean episode return and the 90% confidence interval
mean_returns = [np.mean(reps) for reps in task_returns]
mean_overall = np.mean(mean_returns)
ci_lower, ci_upper = bootstrap_confidence_interval(np.concatenate(task_returns), confidence_level=0.90)

# Print the results
print(f"Overall mean episode return: {mean_overall}")
print(f"90% Bootstrap confidence interval: [{ci_lower}, {ci_upper}]")

# Plotting the results
plt.bar(range(1, 11), mean_returns, color='blue', alpha=0.6, label='Mean Return per Repetition')
plt.axhline(mean_overall, color='red', linestyle='--', label='Overall Mean Return')
plt.fill_between(range(1, 11), ci_lower, ci_upper, color='red', alpha=0.2, label='90% Confidence Interval')

plt.xlabel('Repetition')
plt.ylabel('Episode Return')
plt.title('Performance Evaluation with 90% Bootstrap Confidence Interval')
plt.xticks(range(1, 11))
plt.legend()
plt.show()
