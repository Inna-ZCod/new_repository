import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://divan.ru/category/svet"
driver.get(url)

time.sleep(5)

svets = driver.find_elements(By.CSS_SELECTOR, 'div.WdR1o')

parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'div.lsooF span').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2 span').text
        link = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
    except:
        print("Произошла ошибка")
        continue
    parsed_data.append([name, price, link])

driver.quit()


with open('svet.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)
