# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

import matplotlib.pyplot as plt
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

url = 'https://www.divan.ru/blagoveshchensk/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.CSS_SELECTOR, "span[data-testid='price']")

# Инициализация списка для хранения цен
price_values = []

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца
    # Записываем цены в CSV файл и собираем их в список
    for price in prices:
        # Извлекаем только числовую часть текста
        numeric_price = price.text.split('руб.')[0].strip()
        # Преобразуем строку в число
        price_value = float(numeric_price.replace(' ', '').replace(',', '.'))
        price_values.append(price_value)
        writer.writerow([price_value])

# Закрытие драйвера
driver.quit()

# Вычисление средней цены
if price_values:
    average_price = np.mean(price_values)
    print(f'Средняя цена дивана: {average_price:.2f} руб.')
else:
    print('Цены не найдены')

# Построение гистограммы
plt.hist(price_values, bins=10, edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Количество')

# Показать гистограмму
plt.show()