import random

def rotate_matrix(matrix, direction):

    if not matrix or not matrix[0]:
        return []

    # Поворот по часовой = транспонировать + развернуть строки
    return [list(row)[::-1] for row in zip(*matrix)]


def generate_random_matrix(n, m, low=0, high=9):
    return [[random.randint(low, high) for _ in range(m)] for _ in range(n)]


def task3_menu():
    matrix = None
    result = None

    while True:
        print("\nЗАДАНИЕ 3")
        print("1. Ввести матрицу вручную")
        print("2. Сгенерировать случайную матрицу")
        print("3. Выполнить поворот")
        print("4. Показать результат")
        print("5. Выход")

        choice = input("Выберите пункт: ")

        # --- ввод вручную ---
        if choice == "1":
            n = int(input("Введите N: "))
            m = int(input("Введите M: "))
            print("Введите матрицу построчно:")
            matrix = [list(map(int, input().split())) for _ in range(n)]
            result = None

        # --- случайная матрица ---
        elif choice == "2":
            n = int(input("N: "))
            m = int(input("M: "))
            matrix = generate_random_matrix(n, m)
            print("Матрица:")
            print(*matrix, sep="\n")
            result = None

        # --- выполнение поворота ---
        elif choice == "3":
            if matrix is None:
                print("Сначала введите матрицу!")
                continue

            result = rotate_matrix(matrix, direction='clockwise')
            print("Поворот выполнен.")

        # --- вывод ---
        elif choice == "4":
            if result is None:
                print("Нет результата!")
            else:
                print("Результат:")
                print(*result, sep="\n")

        elif choice == "5":
            return

        else:
            print("Неверный пункт.")
