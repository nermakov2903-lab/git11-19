import random
from logger import logger


def array_to_int(arr):
    """
    Преобразует массив цифр в целое число.

    Parameters
    ----------
    arr : list of int
        Массив цифр, представляющий число, например: [1, 2, 3].

    Return
    -------
    int
        Число, составленное из элементов массива.

    Examples
    --------
    >>> array_to_int([1, 2, 3])
    123
    """
    
    logger.info(f"Преобразование массива в число: {arr}")
    return int("".join(map(str, arr)))


def int_to_array(num):
    """
    Преобразует целое число в массив цифр.

    Parameters
    ----------
    num : int
        Входное целое число.

    Return
    -------
    list of int
        Цифры числа, представленные в виде массива.

    Examples
    --------
    >>> int_to_array(456)
    [4, 5, 6]
    """
    
    logger.info(f"Преобразование числа в массив: {num}")
    return list(map(int, str(num)))


def big_number_operation(a, b, op):
    """
    Выполняет сложение или вычитание больших чисел,
    представленных массивами цифр.

    Parameters
    ----------
    a : list of int
        Первое число в виде массива цифр.
    b : list of int
        Второе число в виде массива цифр.
    op : {'add', 'sub'}
        Тип операции:
            - 'add' — сложение
            - 'sub' — вычитание

    Return
    -------
    list of int
        Результат операции в виде массива цифр.

    Notes
    ----------
    Для вычислений используется преобразование массивов в тип ``int``.
    В Python это безопасно, так как язык поддерживает произвольную длину целых чисел.

    Examples
    --------
    >>> big_number_operation([1, 2, 3], [4, 5, 6], 'add')
    [5, 7, 9]

    >>> big_number_operation([5, 0], [2, 5], 'sub')
    [2, 5]
    """
    logger.info(f"Вызов big_number_operation({a}, {b}, op={op})")

    if op not in ("add", "sub"):
        logger.info("Ошибка: неверная операция")
        raise ValueError("op must be 'add' or 'sub'")

    num1 = array_to_int(a)
    num2 = array_to_int(b)

    if op == "add":
        logger.info("Выполняется сложение")
        return int_to_array(num1 + num2)

    logger.info("Выполняется вычитание")
    return int_to_array(num1 - num2)


def generate_digits(n):
    """
    Генерирует массив случайных цифр от 0 до 9.

    Parameters
    ----------
    n : int
        Количество генерируемых цифр.

    Return
    -------
    list of int
        Массив случайных цифр.

    Examples
    --------
    >>> len(generate_digits(5))
    5
    """
    logger.info(f"Генерация массива случайных цифр длиной {n}")
    return [random.randint(0, 9) for _ in range(n)]


def task4_menu():
    """
    Меню для задачи 4: сложение и вычитание больших чисел,
    представленных массивами цифр.

    Menu options
    ----------------
    1. Ввод массивов вручную  
    2. Генерация массивов случайно  
    3. Выполнение операции (add/sub)  
    4. Вывод результата  
    5. Возврат в главное меню  
    6. Переключение уровня логирования на CRITICAL  

    Rules
    -------
    - Операция невозможна без введённых данных.
    - Результат невозможен без выполнения операции.
    - При повторном вводе массивов предыдущий результат сбрасывается.

    Notes
    ----------
    Функция интерактивна: принимает ввод пользователя
    и выводит результат в консоль.
    """

    a = None
    b = None
    result = None

    while True:
        print("\n=== ЗАДАНИЕ 4 ===")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Выполнить операцию")
        print("4. Показать результат")
        print("5. Назад")
        print("6. Отключить логирование(CRITICAL)")

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт task4: {choice}")

        if choice == "1":
            a = list(map(int, input("Массив 1: ").split()))
            b = list(map(int, input("Массив 2: ").split()))
            logger.info("Пользователь ввёл массивы вручную")
            result = None

        elif choice == "2":
            len1 = int(input("Длина массива 1: "))
            len2 = int(input("Длина массива 2: "))
            a = generate_digits(len1)
            b = generate_digits(len2)
            logger.info("Массивы сгенерированы автоматически")
            result = None

        elif choice == "3":
            if a is None or b is None:
                print("Сначала введите данные!")
                logger.info("Ошибка: выполнение операции без данных")
                continue

            op = input("Операция (add/sub): ")
            result = big_number_operation(a, b, op)
            logger.info("Операция выполнена")

        elif choice == "4":
            if result is None:
                print("Нет результата!")
                logger.info("Ошибка: попытка вывода результата без вычислений")
            else:
                print("Результат:", result)

        elif choice == "5":
            logger.info("Возврат в главное меню")
            return

        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Логи ниже уровня CRITICAL теперь отключены")

        else:
            print("Неверный пункт.")
            logger.info("Неверный пункт меню")
