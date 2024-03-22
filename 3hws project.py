import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Задание 1: Загрузка датасета и вывод его содержимого
df = pd.read_csv("C:/Users/Ilyapro163/Downloads/2018.csv")
print(df.head())

# Задание 2: Основные статистические показатели и гистограмма по столбцу "Social support"
print(df.describe())
plt.figure(figsize=(10, 6))
sns.histplot(df["Social support"], kde=True, color='skyblue')
plt.title('Гистограмма социальной поддержки')
plt.xlabel('Социальная поддержка')
plt.ylabel('Частота')
plt.show()

# Задание 3: Расчет корреляции и построение тепловой карты корреляции
numeric_df = df.select_dtypes(include=['float64', 'int64'])
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Тепловая карта корреляции')
plt.show()

# Задание 4: Линейный график между столбцами Score и Country or region
plt.figure(figsize=(12, 8))
sns.boxplot(x='Country or region', y='Score', data=df)
plt.title('Распределение оценок по странам или регионам')
plt.xlabel('Страна или регион')
plt.ylabel('Оценка (Score)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Задание 5: Первые 10 стран с максимальным уровнем счастья и barplot по ним
top_10_countries = df.nlargest(10, 'Score')
plt.figure(figsize=(10, 6))
sns.barplot(x='Country or region', y='Score', data=top_10_countries)
plt.title('Топ 10 стран по уровню счастья')
plt.xlabel('Страна или регион')
plt.ylabel('Рейтинг')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
