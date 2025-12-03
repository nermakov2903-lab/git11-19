import random
from logger import logger
from exceptions import DataNotSetError, InvalidValueError
from messages import MESSAGES

def count_common_with_reverse(array1, array2):
    logger.info(f"Вызов count_common_with_reverse({array1}, {array2})")
    """
    Подсчитывает количество чисел, которые встречаются в обоих массивах,
    включая случаи, когда одно число является перевёрнутой версией другого.

    Пример:
        array1 = [12, -34]
        array2 = [21, -43]
        → оба числа считаются совпадающими

    Алгоритм:
        1. Для каждого числа из array1 вычисляем его перевёрнутую версию.
        2. Проверяем:
           - есть ли само число в array2
           - или есть ли его перевёрнутый вариант
        3. Если да — увеличиваем счётчик.

    Параметры:
        array1 (list[int]): первый массив
        array2 (list[int]): второй массив

    Возвращает:
        int: количество совпадающих элементов
    """
    if array1 is None or array2 is None:
        raise DataNotSetError("Массивы не заданы")
    count = 0
    for number in array1:

        if not isinstance(number, int):
            raise InvalidValueError("Массив должен содержать только целые числа")

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
    Создаёт массив случайных целых чисел.

    Параметры:
        size (int): длина массива
        min_val (int): минимально возможное значение
        max_val (int): максимально возможное значение

    Возвращает:
        list[int]: массив случайных чисел
    """
    logger.info(f"Генерация случайного массива длиной {size}")
    return [random.randint(min_val, max_val) for _ in range(size)]


def task8_menu():
    """
    Меню задачи 8:
    Определение количества общих чисел между двумя массивами,
    включая случаи совпадения числа с его перевёрнутой версией.

    Функциональность меню:
        1. Ввод массивов вручную
        2. Генерация случайных массивов
        3. Выполнение алгоритма
        4. Вывод результата
        5. Возврат в главное меню
        6. Отключение логирования

    Правила:
        - Нельзя выполнять алгоритм без введённых данных
        - Нельзя выводить результат до выполнения алгоритма
        - При вводе новых массивов результат сбрасывается
    """

    array1 = None
    array2 = None
    result = None
    msgs = MESSAGES["task8"]

    while True:

        print("\n" + msgs["title"])
        for option in msgs["menu"]:
            print(option)

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт task8: {choice}")

        if choice == "1":
            try:
                array1 = list(map(int, input("Массив 1: ").split()))
                array2 = list(map(int, input("Массив 2: ").split()))
                result = None
                logger.info("Массивы введены вручную")
            except Exception as e:
                logger.info(f"Ошибка ввода: {e}")
                print(msgs["input_error"])

        elif choice == "2":
            try:
                size1 = int(input("Размер массива 1: "))
                size2 = int(input("Размер массива 2: "))
                array1 = generate_random_array(size1)
                array2 = generate_random_array(size2)
                print("Массив 1:", array1)
                print("Массив 2:", array2)
                result = None
                logger.info("Массивы сгенерированы")
            except Exception as e:
                logger.info(f"Ошибка генерации: {e}")
                print(msgs["input_error"])

        elif choice == "3":
            try:
                if array1 is None or array2 is None:
                    raise DataNotSetError(msgs["no_data"])
                result = count_common_with_reverse(array1, array2)
                print(msgs["algorithm_done"])
                logger.info("Алгоритм выполнен")
            except Exception as e:
                logger.info(f"Ошибка выполнения алгоритма: {e}")
                print("Ошибка:", e)

        elif choice == "4":
            if result is None:
                print("Нет результата!")
            else:
                print("Количество общих чисел:", result)
                logger.info("Результат показан")

        elif choice == "5":
            logger.info("Выход из task8")
            return

        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено!")
            logger.critical("Логи ниже уровня CRITICAL теперь отключены")
            
        else:
            print(msgs["invalid_choice"])
            logger.info("Неверный пункт меню пользователем")
