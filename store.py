# Ты разрабатываешь программное обеспечение для сети магазинов.
# Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store,
# который можно будет использовать для создания различных магазинов.

class Store():
    def __init__(self, name, address, items={}):
        self.name = name
        self.address = address
        self.items = items

    # метод для добавления товара в ассортимент:
    def add_items(self, item, price):
        self.items.setdefault(item, price)

    # метод для удаления товара из ассортимента:
    def del_items(self, item):
        try:
            del self.items[item]
            print(f"Товар '{item}' успешно удален из ассортимента.")
        except KeyError:
            print(f"Товар '{item}' не найден в ассортименте.")

    # метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None:
    def sea_price(self, item):
        price = self.items.get(item)
        return price

    # метод для обновления цены товара.
    def new_price(self, item, price):
        self.items[item] = price

# Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.

shop1 = Store("Карамелька", "Москва, Петровка, 37", {"Леденец на палочке" : 150, "Тянучка" : 230})
shop2 = Store("Буратино", "Екатеринбург, ул.8 марта, 43", {"Азбука" : 500, "Колпачок" : 200})
shop3 = Store("Маляр", "Санкт-Петербург, Дворцовая набережная, 34", {"Кисть" : 180, "Краски" : 380})

# Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
# обнови цену, убери товар и запрашивай цену.

print(f"Тестирование магазина {shop1.name}, расположенного по адресу: {shop1.address}:")
print(f"Ассортимент на начало тестирования: {shop1.items}")

# Добавление нового товара
shop1.add_items("Орешек в шоколаде", 185)
print("\nПосле того, как был добавлен новый товар, ассортимент магазина стал:")
print(shop1.items)

# Обновление цены на товар
shop1.new_price("Леденец на палочке", 215)
print("\nПосле обновления цены на товар: ")
print(shop1.items)

# Удаление товара
print("\nАссортимент после удаления одного из товаров: ")
shop1.del_items("Тянучка")
print(shop1.items)

# Ошибочное удаление товара:
print("\nПопытка удалить товар, которого нет: ")
shop1.del_items("Тянучка")

# Показать цену на товар
new_price = shop1.sea_price("Леденец на палочке")
print("\nСмотрим цену на товар: ")
print(f"Цена товара 'Леденец на палочке' равна {new_price} рублей")

# Показать цену на товар, которого нет (должно вывести None)
err_price = shop1.sea_price("Сгущенка")
print("\nПопытка узнать цену на товар, которого нет: ")
print(f"Цена товара 'Сгущенка' равна {err_price}")

