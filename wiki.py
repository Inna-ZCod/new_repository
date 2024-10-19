from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random


def menu():
    page = browser.title
    print(f"Сейчас вы находитесь на странице {page}")
    print("Выберите действие, которое вы хотите сделать на этой странице:")
    print("1. Листать параграфы страницы")
    print("2. Перейти по случайной ссылке на странице")
    print("3. Выйти из программы")
    user_choice = input().strip()
    return user_choice


def read_paragraph():
    # Найти все параграфы на странице
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    # Цикл по всем найденным параграфам
    for paragraph in paragraphs:
        text = paragraph.text.strip()
        if text:  # Проверка на наличие текста
            print(text)
            user_ch = input("Читать дальше? Д/Н ").strip().lower()
            if user_ch != "д":
                break


def link_go():
    hatnotes = []
    # Найти все параграфы на странице
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    # Цикл по всем найденным параграфам
    for paragraph in paragraphs:
        # Найти все ссылки в параграфе
        anchors = paragraph.find_elements(By.TAG_NAME, "a")
        # Добавить ссылки в список
        for anchor in anchors:
            href = anchor.get_attribute("href")
            if href:  # Проверка, что ссылка не пустая
                hatnotes.append(href)

    if hatnotes: # Если список ссылок не пустой, то случайный выбор ссылки и переход по ней
        link = random.choice(hatnotes)
        browser.get(link)
    else:
        print("Ссылок на странице не найдено")


def search_wikipedia(query): # стартовый запрос
    # Найти поле поиска
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()  # Очистить поле поиска
    # Ввести в поиск запрос пользователя
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


print("Добро пожаловать в программу автоматического просмотра Википедии")

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title

print("С какого запроса вы хотели бы начать исследование?")
user_text = input()
print("Поехали!")

search_wikipedia(user_text)

while True:
    user_choice = menu()
    if user_choice == "1":
        read_paragraph()
    elif user_choice == "2":
        link_go()
    elif user_choice == "3":
        browser.quit()
        break
    else:
        print("Ошибка ввода, попробуйте еще раз:")
