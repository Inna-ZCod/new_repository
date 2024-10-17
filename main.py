import requests
import pprint

img = ""

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)
    