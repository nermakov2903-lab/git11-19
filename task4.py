import random
from logger import logger
from messages import MESSAGES
from exceptions import DataNotSetError, InvalidValueError


def array_to_int(arr):
    """
    Преобразует массив цифр в целое число.
    
    Пример:
        [1, 2, 3] → 123

    Параметры:
        arr (list[int]): массив цифр

    Возвращает:
        int: число, составленное из цифр массива
    """

    logger.info(f"Преобразование массива в число: {arr}")
    if not all(isinstance(x, int) for x in arr):
        raise InvalidValueError("Массив должен содержать только цифры")
    return int("".join(map(str, arr)))


def int_to_array(num):
    """
    Преобразует число в массив цифр.

    Пример:
        456 → [4, 5, 6]

    Параметры:
        num (int): входное число

    Возвращает:
        list[int]: массив цифр
    """

    logger.info(f"Преобразование числа в массив: {num}")
    return list(map(int, str(num)))


def big_number_operation(a, b, op):
    """
    Складывает или вычитает большие числа, представленные массивами цифр.

    Параметры:
        a (list[int]): массив цифр первого числа
        b (list[int]): массив цифр второго числа
        op (str): 'add' — сложение, 'sub' — вычитание

    Возвращает:
        list[int]: массив цифр результата

    Примечания:
        Для простоты используется преобразование в int.
        Это корректно для учебной задачи и Python поддерживает большие числа.
    """
    logger.info(f"Вызов операции big_number_operation({a}, {b}, op={op})")

    if op not in ("add", "sub"):
        logger.info("Ошибка: неверная операция")
        raise InvalidValueError("op must be 'add' or 'sub'")

    num1 = array_to_int(a)
    num2 = array_to_int(b)

    if op == "add":
        logger.info("Выполняется сложение")
        return int_to_array(num1 + num2)
    else:
        logger.info("Выполняется вычитание")
        result = num1 - num2
        return int_to_array(result)


def generate_digits(n):
    
    """
    Генерирует массив случайных цифр.

    Параметры:
        n (int): длина массива

    Возвращает:
        list[int]: массив из случайных цифр 0–9
    """
    logger.info(f"Генерация массива случайных цифр длиной {n}")
    return [random.randint(0, 9) for _ in range(n)]


def task4_menu():
    """
    Меню для задачи 4: выполнение сложения или вычитания больших чисел,
    представленных массивами цифр.

    Функции меню:
        1. Ввод массивов вручную
        2. Генерация массивов случайно
        3. Выполнение операции (add/sub)
        4. Вывод результата
        5. Возврат в главное меню
        6. Отключить логирование

    Правила:
        - Нельзя выполнять операцию без введённых данных
        - Нельзя выводить результат без выполнения операции
        - При вводе новых массивов результат сбрасывается
    """

    a = None
    b = None
    result = None
    msgs = MESSAGES["task4"]

    while True:

        print("\n" + msgs["title"])
        for option in msgs["menu"]:
            print(option)

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт task4: {choice}")

        if choice == "1":
            try:
                a = list(map(int, input("Массив 1: ").split()))
                b = list(map(int, input("Массив 2: ").split()))
                result = None
                logger.info("Массивы введены вручную")
            except Exception as e:
                logger.info(f"Ошибка ввода массивов: {e}")
                print(msgs["input_error"])

        elif choice == "2":
            try:
                len1 = int(input("Длина массива 1: "))
                len2 = int(input("Длина массива 2: "))
                a = generate_digits(len1)
                b = generate_digits(len2)
                print("A:", a)
                print("B:", b)
                result = None
                logger.info("Случайные массивы сгенерированы")
            except Exception as e:
                logger.info(f"Ошибка генерации: {e}")
                print(msgs["input_error"])

        elif choice == "3":
            try:
                if a is None or b is None:
                    raise DataNotSetError(msgs["no_data"])
                op = input("Операция (add/sub): ")
                result = big_number_operation(a, b, op)
                print(msgs["operation_done"])
                logger.info("Операция выполнена")
            except Exception as e:
                logger.info(f"Ошибка операции: {e}")
                print("Ошибка:", e)

        elif choice == "4":
            if result is None:
                print("Нет результата!")
            else:
                print("Результат:", result)
                logger.info("Результат показан")

        elif choice == "5":
            logger.info("Выход из task4")
            return
            
        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Логи ниже уровня CRITICAL теперь отключены")
            # здесь запись в лог НЕ появится (оно отключено)
        
        else:
            print(msgs["invalid_choice"])
            logger.info("Неверный пункт меню")












