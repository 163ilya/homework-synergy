import matplotlib.pyplot as plt
import numpy as np

# Задание 1
grades = [2, 3, 3, 2, 5, 5, 3, 4, 5, 4]

plt.hist(grades, bins=[1.5, 2.5, 3.5, 4.5, 5.5], edgecolor='black')

plt.xlabel('Оценки')
plt.ylabel('Частота')
plt.title('Распределение оценок учеников по математике')

plt.show()

# Задание 2
random_array = np.random.randint(1, 11, size=(4, 4))
print(random_array)

# Задание 3
labels = ['Мальчики', 'Девочки']
sizes = [15, 17]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Соотношение мальчиков и девочек в классе')

plt.show()
