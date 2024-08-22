# import math

# def calculate_square_root(number):
#     if number < 0:
#         return "Помилка: неможливо обчислити квадратний корінь від'ємного числа."
#     else:
#         return math.sqrt(number)

# try:
#     input_number = float(input("Введіть число --Ю "))
#     result = calculate_square_root(input_number)
#     print(result)
# except ValueError:
#     print("Помилка: введене значення не є числом-->")




# import math

# def calculate_square_root(number):
#     return math.sqrt(number)

# input_number = input("Введіть число --> ")
# try:
#     input_number = float(input_number)
#     if input_number < 0:
#         print("Помилка: неможливо обчислити квадратний корінь від'ємного числа.")
#     else:
#         result = calculate_square_root(input_number)
#         print(f"Квадратний корінь --> {result}")
# except ValueError:
#     print("Помилка: введене значення не є числом.")




# import math

# def calculate_square_root(number):
#     if number < 0:
#         return "Помилка: неможливо обчислити квадратний корінь від'ємного числа."
#     else:
#         return math.sqrt(number)

# input_number = input("Введіть число --> ")
# try:
#     input_number = float(input_number)
#     result = calculate_square_root(input_number)
#     print(f"Квадратний корінь --> {result}")
# except ValueError:
#     print("Помилка: введене значення не є числом.")





# def display_menu():
#     print("\nМеню:")
#     print("1. Відображення словника")
#     print("2. Пошук значення в словнику")
#     print("3. Заміна значення в словнику")
#     print("4. Відображення значення за ключем")
#     print("5. Видалення значення за ключем")
#     print("6. Вихід")

# def display_dictionary(dictionary):
#     print("\nСловник:")
#     for key, value in dictionary.items():
#         print(f"{key}: {value}")

# def search_value(dictionary):
#     key = input("Введіть ключ для пошуку: ")
#     if key in dictionary:
#         print(f"Значення для ключа '{key}': {dictionary[key]}")
#     else:
#         print("Помилка: ключ не знайдено.")

# def replace_value(dictionary):
#     key = input("Введіть ключ для заміни значення: ")
#     if key in dictionary:
#         new_value = input("Введіть нове значення: ")
#         dictionary[key] = new_value
#         print(f"Значення для ключа '{key}' змінено на '{new_value}'.")
#     else:
#         print("Помилка: ключ не знайдено.")

# def display_value(dictionary):
#     key = input("Введіть ключ для відображення значення: ")
#     if key in dictionary:
#         print(f"Значення для ключа '{key}': {dictionary[key]}")
#     else:
#         print("Помилка: ключ не знайдено.")

# def delete_value(dictionary):
#     key = input("Введіть ключ для видалення значення: ")
#     if key in dictionary:
#         del dictionary[key]
#         print(f"Значення для ключа '{key}' видалено.")
#     else:
#         print("Помилка: ключ не знайдено.")

# def main():
#     dictionary = {}
#     while True:
#         key = input("Введіть ключ (або 'stop' для завершення введення): ")
#         if key.lower() == 'stop':
#             break
#         value = input("Введіть значення: ")
#         dictionary[key] = value

#     while True:
#         display_menu()
#         choice = input("Виберіть опцію: ")
#         if choice == '1':
#             display_dictionary(dictionary)
#         elif choice == '2':
#             search_value(dictionary)
#         elif choice == '3':
#             replace_value(dictionary)
#         elif choice == '4':
#             display_value(dictionary)
#         elif choice == '5':
#             delete_value(dictionary)
#         elif choice == '6':
#             print("Вихід з програми.")
#             break
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")

# if __name__ == "__main__":
#     main()




# def display_dictionary(dictionary):
#     print("\nСловник:")
#     for key, value in dictionary.items():
#         print(f"{key}: {value}")

# def search_value(dictionary, key):
#     return dictionary[key]

# def replace_value(dictionary, key, new_value):
#     dictionary[key] = new_value

# def display_value(dictionary, key):
#     return dictionary[key]

# def delete_value(dictionary, key):
#     del dictionary[key]

# def main():
#     dictionary = {}
#     while True:
#         key = input("Введіть ключ (або 'stop' для завершення введення): ")
#         if key.lower() == 'stop':
#             break
#         value = input("Введіть значення: ")
#         dictionary[key] = value

#     while True:
#         print("\nМеню:")
#         print("1. Відображення словника")
#         print("2. Пошук значення в словнику")
#         print("3. Заміна значення в словнику")
#         print("4. Відображення значення за ключем")
#         print("5. Видалення значення за ключем")
#         print("6. Вихід")
        
#         choice = input("Виберіть опцію: ")
#         if choice == '1':
#             display_dictionary(dictionary)
#         elif choice == '2':
#             key = input("Введіть ключ для пошуку: ")
#             try:
#                 print(f"Значення для ключа '{key}': {search_value(dictionary, key)}")
#             except KeyError:
#                 print("Помилка: ключ не знайдено.")
#         elif choice == '3':
#             key = input("Введіть ключ для заміни значення: ")
#             try:
#                 new_value = input("Введіть нове значення: ")
#                 replace_value(dictionary, key, new_value)
#                 print(f"Значення для ключа '{key}' змінено на '{new_value}'.")
#             except KeyError:
#                 print("Помилка: ключ не знайдено.")
#         elif choice == '4':
#             key = input("Введіть ключ для відображення значення: ")
#             try:
#                 print(f"Значення для ключа '{key}': {display_value(dictionary, key)}")
#             except KeyError:
#                 print("Помилка: ключ не знайдено.")
#         elif choice == '5':
#             key = input("Введіть ключ для видалення значення: ")
#             try:
#                 delete_value(dictionary, key)
#                 print(f"Значення для ключа '{key}' видалено.")
#             except KeyError:
#                 print("Помилка: ключ не знайдено.")
#         elif choice == '6':
#             print("Вихід з програми.")
#             break
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")

# if __name__ == "__main__":
#     main()






def display_dictionary(dictionary):
    print("\nСловник:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def search_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Помилка: ключ не знайдено."

def replace_value(dictionary, key, new_value):
    try:
        dictionary[key] = new_value
        return f"Значення для ключа '{key}' змінено на '{new_value}'."
    except KeyError:
        return "Помилка: ключ не знайдено."

def display_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Помилка: ключ не знайдено."

def delete_value(dictionary, key):
    try:
        del dictionary[key]
        return f"Значення для ключа '{key}' видалено."
    except KeyError:
        return "Помилка: ключ не знайдено."

def main():
    dictionary = {}
    while True:
        key = input("Введіть ключ (або 'stop' для завершення введення): ")
        if key.lower() == 'stop':
            break
        value = input("Введіть значення: ")
        dictionary[key] = value

    while True:
        print("\nМеню:")
        print("1. Відображення словника")
        print("2. Пошук значення в словнику")
        print("3. Заміна значення в словнику")
        print("4. Відображення значення за ключем")
        print("5. Видалення значення за ключем")
        print("6. Вихід")
        
        choice = input("Виберіть опцію: ")
        if choice == '1':
            display_dictionary(dictionary)
        elif choice == '2':
            key = input("Введіть ключ для пошуку: ")
            print(search_value(dictionary, key))
        elif choice == '3':
            key = input("Введіть ключ для заміни значення: ")
            new_value = input("Введіть нове значення: ")
            print(replace_value(dictionary, key, new_value))
        elif choice == '4':
            key = input("Введіть ключ для відображення значення: ")
            print(display_value(dictionary, key))
        elif choice == '5':
            key = input("Введіть ключ для видалення значення: ")
            print(delete_value(dictionary, key))
        elif choice == '6':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()