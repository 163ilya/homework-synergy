import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("C:/Users/Ilyapro163/Downloads/Customers.csv")

numeric_df = df.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numeric_df.corr()


plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Базовая тепловая карта корреляции')
plt.show()


mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", mask=mask)
plt.title('Треугольная тепловая карта корреляции')
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(df['Annual Income ($)'], df['Family Size'])
plt.title('Точечная диаграмма: Годовой доход vs Размер семьи')
plt.xlabel('Годовой доход ($)')
plt.ylabel('Размер семьи')
plt.show()

