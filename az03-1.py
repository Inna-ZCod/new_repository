# Задание 1
# Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.

import matplotlib.pyplot as plt
import numpy as np

mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=10)

plt.xlabel("ось x")
plt.ylabel("ось y")
plt.title("Гистограмма случайных чисел, \nраспределенных по нормальному распределению")

plt.show()