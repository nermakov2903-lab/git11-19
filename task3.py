def rotate_matrix(matrix, direction="clockwise"):
    if not matrix or not matrix[0]:
        return []

    # Поворот по часовой = транспонировать + развернуть строки
    if direction == "clockwise":
        return [list(row)[::-1] for row in zip(*matrix)]

    # Против часовой = транспонировать + развернуть порядок строк
    else:
        rotated = [list(row) for row in zip(*matrix)]
        return rotated[::-1]


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print("Исходная:")
    print(*m, sep="\n")

    cw = rotate_matrix(m, "clockwise")
    ccw = rotate_matrix(m, "counterclockwise")

    print("\nПо часовой:")
    print(*cw, sep="\n")

    print("\nПротив часовой:")
    print(*ccw, sep="\n")
