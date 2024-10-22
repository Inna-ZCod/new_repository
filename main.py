import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-card--hhzAtjuXrYFMBMspDjrF")

parsed_data = []

for vacancy in vacancies:
    try:
        title = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___pbpft_3-0-15").text
        company = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___tkzIl_4-3-2").text
        salary = vacancy.find_element(By.CSS_SELECTOR, "span.magritte-text___pbpft_3-0-15").text
        link = vacancy.find_element(By.CSS_SELECTOR, "a.magritte-button___Pubhr_5-1-12").get_attribute("href")
    except:
        print("Произошла ошибка")
        continue
    parsed_data.append([title, company, salary, link])

driver.quit()


with open('hh.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Вакансия', 'Компания', 'Оплата', 'Ссылка'])
    writer.writerows(parsed_data)
