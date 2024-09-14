# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    tasks = []  # Список для хранения всех задач

    def __init__(self, description, deadline, completed=False):
        self.description = description
        self.deadline = deadline
        self.completed = completed  # Статус задачи: по умолчанию не выполнена
        Task.tasks.append(self)  # Добавляем задачу в общий список задач

    def mark_completed(self):
        self.completed = True  # Отмечаем задачу как выполненную


def list_pending_tasks():
    pending_tasks = []  # Список для невыполненных задач
    for task in Task.tasks:
        if not task.completed:
            pending_tasks.append(task)

    if pending_tasks:  # Если список не пустой
        for task in pending_tasks:
            print(f"Задача: {task.description}, Срок: {task.deadline}")
    else:
        print("Нет невыполненных задач.")

def add_task():
    description = input("\nВведите описание новой задачи: ")
    deadline = input("Введите срок выполнения для этой задачи: ")
    task = Task(description, deadline,)
    return task

# Добавление задачи напрямую:
task1 = Task("Сделать домашку", "сегодня")
task2 = Task("Поздравить с днем рождения С.", "завтра")

# Показать список задач:
print("Невыполненные задачи:")
list_pending_tasks()

# Добавление задачи через диалог:
task3 = add_task()

# Показать список невыполненных задач:
print("Текущие задачи:")
list_pending_tasks()

# Отметить выполненную задачу:
task1.mark_completed()

# Показать список оставшихся задач:
print("\nПосле выполнения одной задачи:")
list_pending_tasks()  # Используем экземпляр для вызова метода


