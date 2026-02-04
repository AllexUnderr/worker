from worker import WORKER, WorkerManager


def main():
    manager = WorkerManager()

    # Ввод данных с клавиатуры
    n = int(input("Введите количество работников: "))
    for i in range(n):
        print(f"\nРаботник #{i + 1}:")
        surname = input("Фамилия: ")
        initials = input("Инициалы (И.О.): ")
        position = input("Должность: ")
        salary = float(input("Зарплата: "))
        hire_year = int(input("Год поступления на работу: "))

        worker = WORKER(surname, initials, position, salary, hire_year)
        manager.add_worker(worker)

    # Поиск по стажу
    min_exp = int(input("\nВведите минимальный стаж (лет): "))
    experienced = manager.find_by_experience(min_exp)

    # Вывод результатов
    if experienced:
        print(f"\nРаботники со стажем более {min_exp} лет:")
        for w in experienced:
            print(f"• {w.get_surname()} {w.get_initials()} ({w.get_experience()} лет стажа)")
    else:
        print(f"\nНет работников со стажем более {min_exp} лет.")


if __name__ == "__main__":
    main()