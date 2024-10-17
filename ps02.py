# Задание 1
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

params = {
    'q' : 'html'
}

response = requests.get("https://api.github.com", params=params)

print("Задание 1")
print(f"Статус-код запроса: {response.status_code}")
print("Содержимое ответа на запрос в формате JSON:")
response_json = response.json()
pprint.pprint(response_json)


# Задание 2
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

params_id = {
    'userId' : 1
}

response_id = requests.get("https://jsonplaceholder.typicode.com/posts", params=params_id)

print("\nЗадание 2")
print("Ответ на запрос с параметром userId равным 1:")
pprint.pprint(response_id.json())


# Задание 3
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.

data = {
    'title' : 'foo',
    'body' : 'bar',
    'userId' : '1'
}

response_post = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)

print("\nЗадание 3")
print(f"Статус-код ответа на POST-запрос: {response_post.status_code}")
print("Содержимое ответа на POST-запрос:")
pprint.pprint(response_post.json())

