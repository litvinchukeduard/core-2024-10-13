'''
1. Команда "hello", тут можна обійтись поки без функції та використати звичайний print:

    Введення: "hello"
    Вивід: "How can I help you?"


2. Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:

    Введення: "add John 1234567890"
    Вивід: "Contact added."


3. Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:

    Введення: "change John 0987654321"
    Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено


4. Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:

    Введення: "phone John"
    Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено


5. Команда "all". Для цієї команди зробимо функцію show_all:

    Введення: "all"
    Вивід: усі збережені контакти з номерами телефонів


6. Команда "close" або "exit". Оскільки тут треба перервати виконання програми, можна поки обійтись без функції для цих команд:

    Введення: будь-яке з цих слів
    Вивід: "Good bye!" та завершення роботи бота

Будь-яка команда, яка не відповідає вищезазначеним форматам, буде вважатися нами невірною, і бот буде виводити повідомлення "Invalid command."
'''

# 1) Написати додаток, який буде постійно отримувати інформацію
# 2) Написати код, який буде реагувати на цю інформацію
# 3) Створити словник
# 4) Додати інформацію у словник

def main():
    user_dict = {}
    while True:
        # user_input = input("Enter command:").strip().split(' ') # Ctrl C
        # command = user_input[0]
        # args = user_input[1:]
        # print(input("Enter command:").strip().split(' '))
        command, *args = input("Enter command:").strip().split(' ')
        print(command, args)

        if command == 'exit':
            break
        elif command == 'add':
            print("Adding a user")
            # name = args[0]
            # phone = args[1]
            name, phone = args
            user_dict[name] = phone
            print(args)
        elif command == 'change':
            name, phone = args
            if name in user_dict:
                print('User is present')
        elif command == 'all':
            print(user_dict)
        # print(command)

main()