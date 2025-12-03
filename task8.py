
def count_common_with_reverse(array1, array2):
    count = 0
    for number in array1:
        # Переворачиваем число, сохраняя знак
        if number < 0:
            reversed_number = -int(str(-number)[::-1])
        else:
            reversed_number = int(str(number)[::-1])

        if number in array2 or reversed_number in array2:
            count += 1
    return count



if __name__ == "__main__":
    arr1 = [52, 14, -13, 78]
    arr2 = [-31, 25, 98, 14]
    result = count_common_with_reverse(arr1, arr2)
    print(result)
