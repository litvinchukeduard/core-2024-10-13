# pip freeze > requirements.txt
# pip install -r requirements.txt

'''
Завдання 3

Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.


Вимоги до завдання:

    Створіть віртуальне оточення Python для ізоляції залежностей проекту.
    Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
    Використання бібліотеки colorama для реалізації кольорового виведення.
    Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
    Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.

Рекомендації для виконання:

    Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
    Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
    Для роботи з файловою системою використовуйте модуль pathlib.
    Забезпечте належне форматування виводу, використовуючи функції colorama.

'''

# 1) Створіть віртуальне оточення Python для ізоляції залежностей проекту.

# 2) Використання бібліотеки colorama для реалізації кольорового виведення.
    # Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).

# 3) Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.

# python exercise_3.py folder

from colorama import Fore, Back, Style
from pathlib import Path
import sys

def print_folder(folder_path: str):
    p = Path('.')
    # print([x for x in p.iterdir() if x.is_dir()])
    for x in p.iterdir():
        if x.is_dir():
            print(Fore.YELLOW + str(x) + Style.RESET_ALL) # TODO: add recursive calls
        else:
            print(Fore.BLUE + str(x) + Style.RESET_ALL)

# print(Fore.BLUE + 'some red text')
# print(Back.YELLOW + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# print(Fore.GREEN + Back.YELLOW + 'some green text with blue background')
# value = input(Fore.GREEN + Back.YELLOW + "Please enter value: " + Style.RESET_ALL + Fore.BLUE)
# print("Hello!")
# print(sys.argv)

print(Fore.BLUE + "hello")

if len(sys.argv) <= 1:
    print("No arguments")
else:
    # print(sys.argv[1:])
    # for argument in sys.argv:
    #     print(argument)
    # first_argument = sys.argv[1]
    # if first_argument == 'hello':
    #     print('Welcome!')
    folder_path = sys.argv[1]
    
    print_folder(folder_path)
    # if folder_path 
