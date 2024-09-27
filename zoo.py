# Животные
class Animal(): # родительский класс животных
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издает звуки")

    def eat(self):
        print(f"{self.name} ест")


class Bird(Animal): # дочерний класс птиц
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(f"{self.name} поет: {self.sound}")

class Mammal(Animal): # дочерний класс млекопитающих
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(f"{self.name} говорит: {self.sound}")

class Reptile(Animal): # дочерний класс рептилий
    def __init__(self, name, age, sound, food):
        super().__init__(name, age)
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(f"{self.name} шипит: {self.sound}")


# Сотрудники
class ZooKeeper: # смотритель зоопарка
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal): # функция кормления животных
        print(f"{self.name} кормит {animal.name}, он дает ему {animal.food}")

class Veterinarian: # ветеринар
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal): # функция лечения животных
        print(f"{self.name} лечит {animal.name}")


# Класс Zoo (композиция)
class Zoo:
    def __init__(self):
        self.animals = [] # список для животных
        self.staff = [] # список для сотрудников

    def add_animal(self, animal): # функция для добавления животных в список
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.name}")

    def add_staff(self, staff_member): # функция для добавления сотрудников в список
        self.staff.append(staff_member)
        print(f"Добавлен сотрудник: {staff_member.name}")


# Полиморфизм - функция вызывает для каждого животного свой собственный звук
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Создание зоопарка
zoo = Zoo()

# Добавление животных
parrot = Bird("Попугай", 3, "дай кушать, кушать дай!", "семечки и червячки")
lion = Mammal("Лев", 5, "р-р-р!", "мясо")
snake = Reptile("Змея", 2, "ш-ш-ш-ш!", "мелкую дичь")

zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

# Добавление сотрудников
zookeeper = ZooKeeper("Алексей")
veterinarian = Veterinarian("Ирина")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Методы сотрудников
zookeeper.feed_animal(snake)
veterinarian.heal_animal(lion)

# Звуки животных
animal_sound(zoo.animals)

