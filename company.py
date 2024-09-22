# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

# Родительский класс User
class User:
    def __init__(self, user_id, name):
        self._user_id = user_id # защищенный атрибут
        self._name = name # защищенный атрибут
        self._access_level = 'user' # защищенный атрибут

    # Метод для получения ID пользователя
    def get_user_id(self):
        return self._user_id

    # Метод для получения имени пользователя
    def get_name(self):
        return self._name

    # Метод для получения уровня доступа
    def get_access_level(self):
        return self._access_level

# Дочерний класс Admin
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name) # наследование атрибутов
        self._access_level = 'admin' # защищенный атрибут
        self._user_list = [] # защищенный атрибут

    # Метод для добавления пользователя
    def add_user(self, user):
        if user not in self._user_list: # Если пользователя нет в списке пользователей
            self._user_list.append(user) # То добавить его туда
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Ошибка: такой пользователь уже существует")

    # Метод для удаления пользователя
    def remove_user(self, user_id):
        for user in self._user_list: # Перебор списка пользователей
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален")
                return
        print("Пользователь не найден")

    # Метод для получения списка пользователей
    def get_users(self):
        return self._user_list


# Создаем администратора
admin = Admin(1, "Мария")

# Создаем пользователей
user1 = User(2, "Владимир")
user2 = User(3, "Александр")

# Администратор добавляет пользователей в свой список
admin.add_user(user1)
admin.add_user(user2)

# Выводим всех пользователей
print("Список пользователей:")
for user in admin.get_users():
    print(user.get_name())

# Администратор удаляет пользователя
admin.remove_user(2)

# Выводим всех пользователей после удаления
print("Список пользователей после удаления:")
for user in admin.get_users():
    print(user.get_name())