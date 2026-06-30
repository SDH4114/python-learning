import pandas as pd
from scipy import stats

def pri(name):
    print(globals()[name])
    print()
    del globals()[name]

data = {"age":[32,76,11,34,94,21,47,13,87,34,66]}

df = pd.DataFrame(data)

mean_age = df['age'].mean() # средние арефметическое
write = f"Mean age - {mean_age}"
pri("write")

median_age = df['age'].median() # центральное значение
write = f"Median age - {median_age}"
pri("write")

mode_age = df['age'].mode() # самое частое значение
write = f"Mode age - {mode_age}"
pri("write")

variance_age = df['age'].var()
std_age = df["age"].std()
write = f"Variance - {variance_age} and standart - {std_age}"
pri("write")

quantities_age = df["age"].quantile([0.25,0.50,0.70]) # показывает данные по кусочкам
percentile_age = df["age"].quantile(0.9) # показывает данные которые ниже этого
write = f"""Квантильный возраст - {quantities_age}
90-й процентиль возроста - {percentile_age}"""
pri("write")


data = {
    "City_A":[23,53,25,74,35,54,47,21,17,46,43],
    "City_B":[37,38,71,42,17,27,19,35,23,38,34]
}

df = pd.DataFrame(data)
mean_age_A = df["City_A"].mean()
median_age_A = df["City_A"].median()
mode_age_A = df["City_A"].mode()[0]
variance_age_A = df["City_A"].var()
std_age_A = df["City_A"].std()

print(f"""City A
Mean - {mean_age_A}
Mode - {mode_age_A}
Medeian - {median_age_A}

variance - {variance_age_A}
Standart - {std_age_A}

""")

mean_age_B = df["City_B"].mean()
median_age_B = df["City_B"].median()
mode_age_B = df["City_B"].mode()[0]
variance_age_B = df["City_B"].var()
std_age_B = df["City_B"].std()

print(f"""City B
Mean - {mean_age_B}
Mode - {mode_age_B}
Medeian - {median_age_B}

variance - {variance_age_B}
Standart - {std_age_B}

""")


t_stat, p_value = stats.ttest_ind(df["City_A"],df["City_B"])

print(f"T_test - {t_stat}, P-value - {p_value}")
