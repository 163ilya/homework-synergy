# Задание 1/2
import pandas as pd

data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

index_keys = ['a', 'c', 'e']

series = pd.Series(data_dict, index=index_keys)

print("Серия с заданным индексом:")
print(series)

# Задание 3
import pandas as pd

numbers = pd.Series([x**2 for x in range(1, 21)])

filtered_numbers = numbers[numbers.index % 3 != 0]
print(filtered_numbers)

# Задание 4
import pandas as pd

students_df = pd.read_csv("students.csv")

print("Первые 3 строки датафрейма:")
print(students_df.head(3))

print("Последние 2 строки датафрейма:")
print(students_df.tail(2))

print("Общая информация о датафрейме:")
print(students_df.info())
