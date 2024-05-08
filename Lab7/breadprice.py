import pandas as pd
import matplotlib.pyplot as plt

file_path = 'breadprice.csv'
df = pd.read_csv(file_path)

df_cleaned = df.dropna(axis=1, how='all')
df_cleaned = df_cleaned.dropna(axis=0, how='all')

df_cleaned['Average'] = df_cleaned.iloc[:, 1:].mean(axis=1)

years = df_cleaned['Year']
average_prices = df_cleaned['Average']

plt.figure(figsize=(10, 6))
plt.plot(years, average_prices, marker='o', linestyle='-')
plt.title('Average Bread Price Per Year')
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.grid(True)
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()
