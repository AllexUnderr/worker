from datetime import datetime
from typing import List


class WORKER:
    """Класс для представления работника организации"""

    def __init__(self, surname: str = "", initials: str = "",
                 position: str = "", salary: float = 0.0,
                 hire_year: int = 2020):
        """Конструктор по умолчанию и с параметрами"""
        self.__surname = surname  # фамилия
        self.__initials = initials  # инициалы
        self.__position = position  # должность
        self.__salary = salary  # зарплата
        self.__hire_year = hire_year  # год поступления на работу

    def __del__(self):
        """Деструктор"""
        print(f"Объект WORKER {self.__surname} удалён")

    # Методы изменения полей (сеттеры)
    def set_surname(self, surname: str):
        self.__surname = surname

    def set_initials(self, initials: str):
        self.__initials = initials

    def set_position(self, position: str):
        self.__position = position

    def set_salary(self, salary: float):
        if salary >= 0:
            self.__salary = salary

    def set_hire_year(self, hire_year: int):
        current_year = datetime.now().year
        if 1950 <= hire_year <= current_year:
            self.__hire_year = hire_year

    # Методы отображения полей (геттеры)
    def get_surname(self) -> str:
        return self.__surname

    def get_initials(self) -> str:
        return self.__initials

    def get_position(self) -> str:
        return self.__position

    def get_salary(self) -> float:
        return self.__salary

    def get_hire_year(self) -> int:
        return self.__hire_year

    def get_experience(self) -> int:
        """Расчёт стажа работы на текущий год"""
        return datetime.now().year - self.__hire_year

    def display(self) -> str:
        """Форматированный вывод информации о работнике"""
        return (f"{self.__surname} {self.__initials} | "
                f"Должность: {self.__position} | "
                f"Зарплата: {self.__salary:.2f} ₽ | "
                f"Стаж: {self.get_experience()} лет")


class WorkerManager:
    """Класс для управления списком работников"""

    def __init__(self):
        self.__workers: List[WORKER] = []

    def add_worker(self, worker: WORKER):
        self.__workers.append(worker)

    def find_by_experience(self, min_experience: int) -> List[WORKER]:
        """Поиск работников со стажем больше заданного"""
        return [w for w in self.__workers if w.get_experience() > min_experience]

    def display_all(self):
        if not self.__workers:
            print("Список работников пуст.")
            return
        print("\nСписок всех работников:")
        for i, worker in enumerate(self.__workers, 1):
            print(f"{i}. {worker.display()}")