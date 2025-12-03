import random


def count_common_with_reverse(array1, array2):
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

    count = 0

    for number in array1:
        # Формируем перевёрнутое число, сохраняя знак
        if number < 0:
            reversed_number = -int(str(-number)[::-1])
        else:
            reversed_number = int(str(number)[::-1])

        # Проверяем совпадение или совпадение с переворотом
        if number in array2 or reversed_number in array2:
            count += 1

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

    Правила:
        - Нельзя выполнять алгоритм без введённых данных
        - Нельзя выводить результат до выполнения алгоритма
        - При вводе новых массивов результат сбрасывается
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

        choice = input("Выберите пункт: ")

        # --- Ввод вручную ---
        if choice == "1":
            array1 = list(map(int, input("Массив 1: ").split()))
            array2 = list(map(int, input("Массив 2: ").split()))
            result = None

        # --- Генерация случайных массивов ---
        elif choice == "2":
            size1 = int(input("Размер массива 1: "))
            size2 = int(input("Размер массива 2: "))
            array1 = generate_random_array(size1)
            array2 = generate_random_array(size2)
            print("Массив 1:", array1)
            print("Массив 2:", array2)
            result = None

        # --- Выполнение алгоритма ---
        elif choice == "3":
            if array1 is None or array2 is None:
                print("Сначала введите данные!")
            else:
                result = count_common_with_reverse(array1, array2)
                print("Алгоритм выполнен.")

        # --- Вывод результата ---
        elif choice == "4":
            if result is None:
                print("Сначала выполните алгоритм!")
            else:
                print("Количество общих чисел:", result)

        # --- Выход ---
        elif choice == "5":
            return

        else:
            print("Неверный пункт меню.")
