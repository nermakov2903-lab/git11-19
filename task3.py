def rotate_matrix(matrix, direction):

    if not matrix or not matrix[0]:
        return []

    # Поворот по часовой = транспонировать + развернуть строки
    return [list(row)[::-1] for row in zip(*matrix)]

#Простой тест
if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Исходная:")
    print(*m, sep="\n")

    cw = rotate_matrix(m, "clockwise")

    print("\nПо часовой:")
    print(*cw, sep="\n")

