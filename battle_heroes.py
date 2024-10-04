import random

# Класс для героя в игре
class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    # Метод, который позволяет одному герою атаковать другого
    def attack(self, other):
        damage = random.randint(1, self.attack_power) # Генерируем случайное количество урона от 1 до attack_power
        other.health -= damage # Уменьшаем здоровье атакуемого героя на величину урона
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    # Метод для проверки, жив ли герой (есть ли у него здоровье больше 0)
    def is_alive(self):
        return self.health > 0 # Возвращает True, если здоровья больше 0 или False, если здоровья 0 или меньше

# Определяем класс 'Game', который представляет собой игру
class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name) # Создаем героя для игрока с заданным именем
        self.computer = Hero(computer_name) # Создаем героя для компьютера

    # Метод, который запускает игру
    def start(self):
        print("Игра началась!")
        # Цикл продолжается, пока оба героя живы
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока: он атакует компьютер
            self.player.attack(self.computer)
            # Проверяем, остался ли компьютер в живых после атаки
            if not self.computer.is_alive(): # Если нет, то:
                print(f"{self.computer.name} повержен!")  # Компьютер повержен
                print(f"{self.player.name} победил!")  # Игрок победил
                break  # Выходим из цикла, так как игра закончена

            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.") # Выводим оставшееся здоровье компьютера

            # Ход компьютера: он атакует игрока
            self.computer.attack(self.player)
            # Проверяем, остался ли игрок в живых после атаки
            if not self.player.is_alive(): # Если нет
                print(f"{self.player.name} повержен!")  # Игрок повержен
                print(f"{self.computer.name} победил!")  # Компьютер победил
                break  # Выход из цикла

            print(f"У {self.player.name} осталось {self.player.health} здоровья.") # Оставшееся здоровье игрока

        print("Игра окончена!")

player_name = input("Введите имя вашего героя: ") # Имя персонажа, которым играет человек
game = Game(player_name) # Создание персонажа для человека
game.start() # Запуск игры