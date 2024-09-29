from abc import ABC, abstractmethod

# Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Дочерник класс для меча
class Sword(Weapon):
    def __init__(self):
        self.name = "меч"

    def attack(self):
        print("Боец бьет мечом")

# Дочерний класс для лука
class Bow(Weapon):
    def __init__(self):
        self.name = "лук"

    def attack(self):
        print("Боец стреляет из лука")

# Отдельный класс для бойца
class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

#   Функция для смены оружия
    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"Боец выбирает {self.weapon.name}")

#   Атака способом, соответствующим выбранному оружию
    def attack(self):
        self.weapon.attack()

# Класс для монстра
class Monster():
    def __init__(self):
        self.dead = False

# Поведение монстра при атаке на него
    def defeat(self):
        self.dead = True
        print("Монстр побежден!")

# Функция проведения поединка
def fight(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeat()

# Создание оружия
sword = Sword()
bow = Bow()

# Создание персонажей
fighter = Fighter(sword)
monster = Monster()

# Смена оружия
fighter.change_weapon(sword)

# Бой с применением меча
fight(fighter, monster)

# Смена оружия
fighter.change_weapon(bow)

monster = Monster() # Новый монстр для нового поединка

# Бой с применением лука
fight(fighter, monster)
