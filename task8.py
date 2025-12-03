import random


def count_common_with_reverse(array1, array2):
    count = 0
    for number in array1:
        if number < 0:
            reversed_number = -int(str(-number)[::-1])
        else:
            reversed_number = int(str(number)[::-1])

        if number in array2 or reversed_number in array2:
            count += 1

    return count


def generate_random_array(size, min_val=-999, max_val=999):
    return [random.randint(min_val, max_val) for _ in range(size)]


def task8_menu():
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

        #ввод вручную
        if choice == "1":
            try:
                array1 = list(map(int, input("Массив 1: ").split()))
                array2 = list(map(int, input("Массив 2: ").split()))
                result = None
            except ValueError:
                print("Ошибка: вводите целые числа.")

        #случайным образом
        elif choice == "2":
            try:
                size1 = int(input("Размер массива 1: "))
                size2 = int(input("Размер массива 2: "))
                array1 = generate_random_array(size1)
                array2 = generate_random_array(size2)
                print("Массив 1:", array1)
                print("Массив 2:", array2)
                result = None
            except ValueError:
                print("Ошибка ввода.")

        #выполнение алгоритма
        elif choice == "3":
            if array1 is None or array2 is None:
                print("Сначала введите данные!")
            else:
                result = count_common_with_reverse(array1, array2)
                print("Алгоритм выполнен.")

        #вывод результатa
        elif choice == "4":
            if result is None:
                print("Сначала выполните алгоритм!")
            else:
                print("Количество общих чисел:", result)

        elif choice == "5":
            return

        else:
            print("Неверный пункт меню.")
