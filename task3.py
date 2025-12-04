import random
from logger import logger


def rotate_matrix(matrix, direction="clockwise"):
    """
    Rotate a matrix by 90 degrees.

    Parameters
    ----------
    matrix : list of list of int
        Входная матрица размера N×M.
    direction : {"clockwise", "counterclockwise"}, optional
        Направление поворота:
        - ``"clockwise"`` — поворот по часовой стрелке,
        - ``"counterclockwise"`` — поворот против часовой.

    Returns
    -------
    list of list of int
        Новая повернутая матрица.

    Notes
    -----
    Поворот выполняется через транспонирование:

    >>> zip(*matrix)

    После транспонирования выполняется зеркальное отражение:
    - Для ``"clockwise"`` — отражение строк по горизонтали.
    - Для ``"counterclockwise"`` — инверсия списка строк.

    Examples
    --------
    >>> rotate_matrix([[1, 2], [3, 4]], "clockwise")
    [[3, 1], [4, 2]]

    >>> rotate_matrix([[1, 2], [3, 4]], "counterclockwise")
    [[2, 4], [1, 3]]
    """
    
    logger.info("Вызов rotate_matrix()")

    if not matrix or not matrix[0]:
        logger.info("Получена пустая матрица")
        return []

    if direction == "clockwise":
        logger.info("Поворот по часовой стрелке")
        return [list(row)[::-1] for row in zip(*matrix)]
    else:
        logger.info("Поворот против часовой стрелки")
        rotated = [list(row) for row in zip(*matrix)]
        return rotated[::-1]


def generate_random_matrix(n, m, low=0, high=9):
    """
    Generate a random matrix of size N×M.

    Parameters
    ----------
    n : int
        Количество строк.
    m : int
        Количество столбцов.
    low : int, optional
        Минимальное возможное значение (включительно).
    high : int, optional
        Максимальное возможное значение (включительно).

    Returns
    -------
    list of list of int
        Сгенерированная матрица.

    Notes
    -----
    Используется ``random.randint`` для генерации каждого элемента.
    """
    
    logger.info(f"Генерация случайной матрицы {n}x{m}")
    return [[random.randint(low, high) for _ in range(m)] for _ in range(n)]


def task3_menu():
    """
    Меню задания №3: поворот матрицы.

    Description
    -----------
    Меню позволяет пользователю:

    1. Ввести матрицу вручную.
    2. Сгенерировать случайную матрицу.
    3. Выполнить поворот матрицы.
    4. Просмотреть результат.
    5. Вернуться назад.
    6. Отключить логирование (установить уровень CRITICAL).

    Notes
    -----
    - Поворот невозможен без предварённого ввода матрицы.
    - При вводе или генерации новой матрицы предыдущий результат сбрасывается.
    - Логи фиксируют действия пользователя.

    Examples
    --------
    >>> task3_menu()
    # Появится интерактивное меню
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
        print("6. Отключить логирование (CRITICAL)")

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт меню task3: {choice}")

        if choice == "1":
            n = int(input("Введите N: "))
            m = int(input("Введите M: "))
            matrix = [list(map(int, input().split())) for _ in range(n)]
            logger.info("Матрица введена вручную")
            result = None

        elif choice == "2":
            n = int(input("N: "))
            m = int(input("M: "))
            matrix = generate_random_matrix(n, m)
            logger.info("Матрица сгенерирована автоматически")
            result = None

        elif choice == "3":
            if matrix is None:
                print("Сначала введите матрицу!")
                logger.info("Ошибка: поворот без матрицы")
                continue

            direction = input("Направление (clockwise/counterclockwise): ")
            result = rotate_matrix(matrix, direction)
            logger.info("Поворот выполнен")

        elif choice == "4":
            if result is None:
                print("Нет результата!")
                logger.info("Ошибка: вывод без выполнения алгоритма")
            else:
                print(*result, sep="\n")

        elif choice == "5":
            logger.info("Возврат в главное меню")
            return

        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Установлен уровень CRITICAL")

        else:
            print("Неверный пункт.")
            logger.info("Неверный пункт меню")
