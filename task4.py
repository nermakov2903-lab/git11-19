import random
from logger import logger


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
        raise ValueError("op must be 'add' or 'sub'")

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
                logger.info("Ошибка: попытка выполнения операции без данных")
                continue

            op = input("Операция (add/sub): ")
            result = big_number_operation(a, b, op)
            logger.info("Операция выполнена")

        elif choice == "4":
            if result is None:
                print("Нет результата!")
                logger.info("Ошибка: попытка вывести результат без вычислений")
            else:
                print("Результат:", result)

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
            logger.info("Неверный пункт меню")












