import random

def array_to_int(arr):
    return int("".join(map(str, arr)))


def int_to_array(num):
    return list(map(int, str(num)))


def big_number_operation(a, b, op):
    #
    #Складывает или вычитает большие числа, представленные массивами цифр.
    #op = 'add' или 'sub'

    if op not in ("add", "sub"):
        raise ValueError("op must be 'add' or 'sub'")

    num1 = array_to_int(a)
    num2 = array_to_int(b)

    if op == "add":
        return int_to_array(num1 + num2)
    else:
        result = num1 - num2
        if result < 0:
            print("Внимание: результат отрицательный, приводится к виду со знаком '-'")
        return int_to_array(result)


def generate_digits(n):
    return [random.randint(0, 9) for _ in range(n)]


def task4_menu():
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

        choice = input("Выберите пункт: ")

        # --- ввод вручную ---
        if choice == "1":
            a = list(map(int, input("Массив 1: ").split()))
            b = list(map(int, input("Массив 2: ").split()))
            result = None

        # --- случайные ---
        elif choice == "2":
            len1 = int(input("Длина массива 1: "))
            len2 = int(input("Длина массива 2: "))
            a = generate_digits(len1)
            b = generate_digits(len2)
            print("A =", a)
            print("B =", b)
            result = None

        # --- выполнение ---
        elif choice == "3":
            if a is None or b is None:
                print("Сначала введите данные!")
                continue

            op = input("Операция (add/sub): ")
            result = big_number_operation(a, b, op)
            print("Операция выполнена.")

        # --- вывод ---
        elif choice == "4":
            if result is None:
                print("Нет результата!")
            else:
                print("Результат:", result)

        elif choice == "5":
            return

        else:
            print("Неверный пункт.")

