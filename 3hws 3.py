# Задание 1
import matplotlib.pyplot as plt

grades = [2, 3, 3, 2, 5, 5, 3, 4, 5, 4]

plt.hist(grades, bins=5, edgecolor='black')

plt.xlabel('Оценки')
plt.ylabel('Частота')
plt.title('Распределение оценок учеников по математике')

plt.show()


# Задание 2
import numpy as np

random_array = np.random.randint(1, 11, size=(4, 4))

print(random_array)


#Задание 3
import matplotlib.pyplot as plt

labels = ['Мальчики', 'Девочки']
sizes = [2, 22
