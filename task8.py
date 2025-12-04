import random
from logger import logger


def count_common_with_reverse(array1, array2):
    """
    Подсчитывает количество чисел, которые встречаются в обоих массивах,
    включая случаи, когда одно число является перевёрнутой версией другого.

    Algoritm
    --------
    1. Для каждого числа из ``array1`` вычисляется его перевёрнутая версия.
    2. Проверяется:
        - содержится ли число в ``array2``;
        - содержится ли его перевёрнутый вариант.
    3. Каждое совпадение увеличивает счётчик.

    Parameters
    ----------
    array1 : list of int
        First integer array.
    array2 : list of int
        Second integer array.

    Returns
    -------
    int
        Number of matching elements.

    Examples
    --------
    >>> count_common_with_reverse([12, -34], [21, -43])
    2
    """
    logger.info(f"Вызов count_common_with_reverse({array1}, {array2})")

    count = 0
    for number in array1:

        if number < 0:
            reversed_number = -int(str(-number)[::-1])
        else:
            reversed_number = int(str(number)[::-1])

        logger.info(f"Проверка числа {number}, обратное {reversed_number}")

        if number in array2 or reversed_number in array2:
            count += 1
            logger.info(f"Совпадение найдено: {number}")

    return count


def generate_random_array(size, min_val=-999, max_val=999):
    """
    Генерирует массив случайных целых чисел.

    Parameters
    ----------
    size : int
        Number of elements to generate.
    min_val : int
        Minimum possible value.
    max_val : int
        Maximum possible value.

    Returns
    -------
    list of int
        Generated random integer array.

    Examples
    --------
    >>> len(generate_random_array(5))
    5
    """
    logger.info(f"Генерация случайного массива длиной {size}")
    return [random.randint(min_val, max_val) for _ in range(size)]


def task8_menu():
    """
    Меню задачи 8:
    Определяет количество общих чисел между двумя массивами,
    включая случаи совпадения числа с его перевёрнутой версией.

    Menu
    ----------------
    1. Ввод массивов вручную  
    2. Генерация случайных массивов  
    3. Выполнение алгоритма  
    4. Вывод результата  
    5. Возврат в главное меню  
    6. Отключение логирования  

    Rules
    -------
    - Выполнение алгоритма невозможно без введённых массивов.
    - Результат нельзя вывести до выполнения алгоритма.
    - При повторном вводе массивов результат сбрасывается.

    Notes
    -----
    Функция предназначена для интерактивной работы через консоль.
    """

    array1 = None
    array2 = None
    result = None

    while True:
        print("\n=== ЗАДАНИЕ 8 ===")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Выполнить алгоритм")
        print("4. Показать результат")
        print("5. Назад в главное меню")
        print("6. Отключить логирование(CRITICAL)")

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт task8: {choice}")

        if choice == "1":
            array1 = list(map(int, input("Массив 1: ").split()))
            array2 = list(map(int, input("Массив 2: ").split()))
            logger.info("Массивы введены вручную")
            result = None

        elif choice == "2":
            size1 = int(input("Размер массива 1: "))
            size2 = int(input("Размер массива 2: "))
            array1 = generate_random_array(size1)
            array2 = generate_random_array(size2)
            logger.info("Массивы сгенерированы случайно")
            result = None

        elif choice == "3":
            if array1 is None or array2 is None:
                print("Сначала введите данные!")
                logger.info("Ошибка: попытка выполнить алгоритм без данных")
            else:
                result = count_common_with_reverse(array1, array2)
                logger.info("Алгоритм выполнен")

        elif choice == "4":
            if result is None:
                print("Сначала выполните алгоритм!")
                logger.info("Ошибка: вывод результата без выполнения алгоритма")
            else:
                print("Количество общих чисел:", result)

        elif choice == "5":
            logger.info("Возврат в главное меню")
            return

        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено!")
            logger.critical("Логи ниже уровня CRITICAL теперь отключены")

        else:
            print("Неверный пункт меню.")
            logger.info("Неверный пункт меню пользователем")
