from scipy import stats

ages = [32,76,11,34,94,21,47,13,87,34,66]

t_stat, p_value = stats.ttest_1samp(ages,popmean=30)
print(f"T-test - {t_stat}, P-value - {p_value}")


group1 = [23,25,31,35,45]
group2 = [45,51,61,35,23]

stat, p_value = stats.mannwhitneyu(group1,group2)
# чем меньше p тем значимее различие
print(f"U-test - {stat}, P-value - {p_value}")
