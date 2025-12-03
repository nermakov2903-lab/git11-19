import random

def rotate_matrix(matrix, direction="clockwise"):
    """
    Поворачивает матрицу на 90 градусов.

    Параметры:
        matrix (list[list[int]]): входная матрица N×M
        direction (str): направление поворота:
                         "clockwise" — по часовой стрелке
                         "counterclockwise" — против часовой стрелки

    Возвращает:
        list[list[int]]: новая повернутая матрица

    Описание алгоритма:
    Поворот достигается через транспонирование матрицы:
        zip(*matrix)
    Далее выполняется зеркальное отражение:
        - Для clockwise: разворот строк
        - Для counterclockwise: разворот порядка строк
    """
    if not matrix or not matrix[0]:
        return []

    # Поворот по часовой = транспонировать + развернуть строки
    if direction == "clockwise":
        return [list(row)[::-1] for row in zip(*matrix)]

    # Против часовой = транспонировать + развернуть порядок строк
    else:
        rotated = [list(row) for row in zip(*matrix)]
        return rotated[::-1]

def generate_random_matrix(n, m, low=0, high=9):
    """
    Генерирует случайную матрицу N×M.

    Параметры:
        n (int): количество строк
        m (int): количество столбцов
        low (int): минимальное значение в матрице (включительно)
        high (int): максимальное значение (включительно)

    Возвращает:
        list[list[int]]: созданная матрица
    """
    return [[random.randint(low, high) for _ in range(m)] for _ in range(n)]


def task3_menu():
     """
    Меню для задачи 3: поворот матрицы.

    Позволяет:
    1. Ввести матрицу вручную
    2. Сгенерировать случайную матрицу
    3. Выполнить поворот матрицы
    4. Вывести результат
    5. Вернуться назад

    Правила:
    - Нельзя выполнять поворот без введённой матрицы
    - Нельзя выводить результат до выполнения поворота
    - При вводе новой матрицы результат сбрасывается
    """
    matrix = None
    result = None

    while True:
        print("\nЗАДАНИЕ 3")
        print("1. Ввести матрицу вручную")
        print("2. Сгенерировать случайную матрицу")
        print("3. Выполнить поворот")
        print("4. Показать результат")
        print("5. Назад")

        choice = input("Выберите пункт: ")

        # --- ввод вручную ---
        if choice == "1":
            n = int(input("Введите N: "))
            m = int(input("Введите M: "))
            print("Введите матрицу построчно:")
            matrix = [list(map(int, input().split())) for _ in range(n)]
            result = None

        # --- случайная матрица ---
        elif choice == "2":
            n = int(input("N: "))
            m = int(input("M: "))
            matrix = generate_random_matrix(n, m)
            print("Матрица:")
            print(*matrix, sep="\n")
            result = None

        # --- выполнение поворота ---
        elif choice == "3":
            if matrix is None:
                print("Сначала введите матрицу!")
                continue

            direction = input("Направление (clockwise(по часовой)/counterclockwise(против)): ")
            result = rotate_matrix(matrix, direction)
            print("Поворот выполнен.")

        # --- вывод ---
        elif choice == "4":
            if result is None:
                print("Нет результата!")
            else:
                print("Результат:")
                print(*result, sep="\n")

        elif choice == "5":
            return

        else:
            print("Неверный пункт.")
