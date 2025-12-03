import random
from logger import logger


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
    logger.info(f"Вызов rotate_matrix(direction={direction})")

    if not matrix or not matrix[0]:
        logger.info("Получена пустая матрица")
        return []

    if direction == "clockwise":
        logger.info("Выполняется поворот по часовой стрелке")
        return [list(row)[::-1] for row in zip(*matrix)]
    else:
        logger.info("Выполняется поворот против часовой стрелки")
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
    logger.info(f"Генерация случайной матрицы {n}x{m}")
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
    6. Отключить логирование

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
                logger.info("Ошибка: попытка выполнить поворот без матрицы")
                continue

            direction = input("Направление (clockwise/counterclockwise): ")
            result = rotate_matrix(matrix, direction)
            logger.info("Поворот выполнен")

        elif choice == "4":
            if result is None:
                print("Нет результата!")
                logger.info("Ошибка: попытка вывести результат без алгоритма")
            else:
                print(*result, sep="\n")

        elif choice == "5":
            logger.info("Возврат в главное меню")
            return

        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Логи ниже уровня CRITICAL теперь отключены")
            # здесь запись в лог НЕ появится (оно отключено)

        else:
            print("Неверный пункт.")
            logger.info("Пользователь ввел неверный пункт меню")
