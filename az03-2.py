# Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.

import matplotlib.pyplot as plt
import numpy as np

random_array_1 = np.random.rand(10)  # массив из 10 случайных чисел
random_array_2 = np.random.rand(10)
print(random_array_1)
print(random_array_2)

plt.scatter(random_array_1, random_array_2)

plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Диаграмма рассеяния двух наборов случайных данных")

plt.show()


