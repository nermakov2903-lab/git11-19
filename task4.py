import random

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

    if op not in ("add", "sub"):
        raise ValueError("op must be 'add' or 'sub'")

    # Преобразуем массивы в числа
    num1 = array_to_int(a)
    num2 = array_to_int(b)

    # Выполняем нужную операцию
    if op == "add":
        return int_to_array(num1 + num2)
    else:
        result = num1 - num2

        # Предупреждение о знаке
        if result < 0:
            print("Внимание: результат отрицательный, приводится к виду со знаком '-'")

        return int_to_array(result)


def generate_digits(n):
    """
    Генерирует массив случайных цифр.

    Параметры:
        n (int): длина массива

    Возвращает:
        list[int]: массив из случайных цифр 0–9
    """
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

    Правила:
        - Нельзя выполнять операцию без введённых данных
        - Нельзя выводить результат без выполнения операции
        - При вводе новых массивов результат сбрасывается
    """

    a = None    # Первое число в виде массива цифр
    b = None    # Второе число
    result = None

    while True:
        print("\n=== ЗАДАНИЕ 4 ===")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Выполнить операцию")
        print("4. Показать результат")
        print("5. Назад")

        choice = input("Выберите пункт: ")

        # --- Ввод массивов вручную ---
        if choice == "1":
            a = list(map(int, input("Массив 1: ").split()))
            b = list(map(int, input("Массив 2: ").split()))
            result = None

        # --- Генерация случайных массивов ---
        elif choice == "2":
            len1 = int(input("Длина массива 1: "))
            len2 = int(input("Длина массива 2: "))
            a = generate_digits(len1)
            b = generate_digits(len2)
            print("A =", a)
            print("B =", b)
            result = None

        # --- Выполнение операции ---
        elif choice == "3":
            if a is None or b is None:
                print("Сначала введите данные!")
                continue

            op = input("Операция (add/sub): ")
            result = big_number_operation(a, b, op)
            print("Операция выполнена.")

        # --- Вывод результата ---
        elif choice == "4":
            if result is None:
                print("Нет результата!")
            else:
                print("Результат:", result)

        # --- Выход ---
        elif choice == "5":
            return

        else:
            print("Неверный пункт.")
