import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


df = pd.read_csv("C:/Users/Ilyapro163/Desktop/ds_salaries.csv")
print(df.head())


plt.figure(figsize=(10, 6))
sns.barplot(x='job_title', y='salary_in_usd', data=df)
plt.title('Уровень дохода по профессиям')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Профессия')
plt.ylabel('Средний доход ($)')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
df.drop(['work_year', 'salary_currency', 'employee_residence', 'company_location', 'company_size'], axis=1).plot(kind='line', marker='o')
plt.title('Линейная диаграмма по всем столбцам')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend(title='Параметры')
plt.show()


plt.figure(figsize=(12, 8))
sns.scatterplot(x='salary_in_usd', y='job_title', data=df, hue='job_title')
plt.title('Диаграмма рассеяния зарплаты по профессиям')
plt.xlabel('Зарплата ($)')
plt.ylabel('Профессия')
plt.legend(title='Профессия', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 8))
sns.lineplot(x='company_location', y='salary_in_usd', data=df)
plt.title('Линейный график зависимости зарплаты от региона')
plt.xlabel('Регион')
plt.ylabel('Средний доход ($)')
plt.xticks(rotation=45)
plt.show()
