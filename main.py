from logger import logger
from task3 import task3_menu
from task4 import task4_menu
from task8 import task8_menu
from messages import MESSAGES

"""
Главный модуль программы.
Обеспечивает интерфейс верхнего уровня и доступ к заданиям программы.

Требования:
    — Меню верхнего уровня.
    — Вызов вложенных меню для выполнения отдельных задач.
    — Завершение работы программы.
"""

def main():
  """
    Запускает главное меню программы.

    Пользователь может:
        — перейти к выполнению задания №3,
        — перейти к выполнению задания №4,
        — перейти к выполнению задания №8,
        — завершить работу приложения.
    """
  msgs = MESSAGES["main_menu"]
  while True:
    print("\n=== ГЛАВНОЕ МЕНЮ ===")
    print("1. Задание 3 (Поворот матрицы)")
    print("2. Задание 4 (Операции над большими числами)")
    print("3. Задание 8 (Общие числа с реверсом)")
    print("4. Выход")

    print("\n" + msgs["title"])
    for option in msgs["options"]:
        print(option)

    choice = input(msgs["prompt"])
    logger.info(f"Пользователь выбрал главный пункт меню: {choice}")

    if choice == "1":
        task3_menu()
    elif choice == "2":
        task4_menu()
    elif choice == "3":
        task8_menu()
    elif choice == "4":
        print("Выход...")
        break
    else:
        print(msgs["invalid"])
        logger.info("Ошибка: неверный пункт главного меню")


if __name__ == "__main__":
    main()
