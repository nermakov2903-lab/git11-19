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



if __name__ == "__main__":
    a = [9,9,9]
    b = [1]

    print("Сумма:", big_number_operation(a, b, "add"))
    print("Разность:", big_number_operation(a, b, "sub"))

