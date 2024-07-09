import pandas as pd
df = pd.read_csv("module_2/week_1_numpy/advertising.csv")

data = df.to_numpy()

# Q15:
max_value = df['Sales'].max()
max_index = df['Sales'].idxmax()

print(max_value, max_index)


# Q16:
average_value = df['TV'].mean()

print(average_value)

# Q17:
count_radio = df[df['Sales'] >= 20].shape[0]

print(count_radio)

# Q18:
radio_by_sales_over_15_mean = df[df['Sales'] >= 15]['Radio'].mean()

print(radio_by_sales_over_15_mean)

# Q19:

newspaper_mean = df['Newspaper'].mean()
newspaper_over_mean_by_sales_sum = df[df['Newspaper']
                                      >= newspaper_mean]['Sales'].sum()
print(newspaper_over_mean_by_sales_sum)

# Q20:

average_sales = df['Sales'].mean()
scores = ['Good' if x > average_sales else 'Bad' if x <
          average_sales else 'Average' for x in df['Sales']]

print(scores[7:10])

# Q21:

average_median = df['Sales'].median()
scores = ['Good' if x > average_median else 'Bad' if x <
          average_median else 'Average' for x in df['Sales']]

print(scores[7:10])
