import os  # Импортируем "os"


def add(note):
    """
        Создаем функцию "add" для добавления заметок.
        Ввод пользователем заметки.
        Добавляем заметки в существующий список.
        """
    ask_note = input('Введите заметку: ')
    note.append(ask_note)
    return note


def earliest(note):
    """
        Создаем функцию "earliest" для вывода заметок от ранней к последней.
        Выводим список.
        """
    return note


def latest(note):
    """
         Создаем функцию "latest" для вывода заметок от последней к ранней.
         Выводим список.
         """
    return note[::-1]


def longest(note):
    """
        Создаем функцию "longest" для вывода заметок от длиннейших к более коротким.
        Выводим список.
        """
    long = sorted(note, key=len, reverse=True)
    return long


def shortest(note):
    """
        Создаем функцию "shortest" для вывода заметок от более коротких к длиннейшим.
        Выводим список.
        """
    short = sorted(note, key=len)
    return short


def make_file(file_f):
    """
        Создаем функцию "make_file" для создания или чтения существующего файла.
        Если файл существует, то читаем его. Если нет - он создается.
        Выводим список.
        """
    if os.path.isfile(file_f):
        with open(file_f, mode='r', encoding='utf-8') as file:
            return list(file.read().split(' '))
    else:
        open(file_f, mode='w', encoding='utf-8')
        return []


if __name__ == '__main__':
    file_name = 'file_name.txt'  # Сохраняем названия файлов в переменную.
    list_note = make_file(file_name)  # Присваиваем результат выполнения функции в переменную.

    while True:
        customer_input = input()
        if customer_input == 'add':
            list_note = add(list_note)
        elif customer_input == 'earliest':
            print(earliest(list_note))
        elif customer_input == 'latest':
            print(latest(list_note))
        elif customer_input == 'longest':
            print(longest(list_note))
        elif customer_input == 'shortest':
            print(shortest(list_note))
        elif customer_input == 'save & exit':
            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write(' '.join(list_note))
                break
            # Когда пользователь пишет команду 'save & exit', программа завершает работу, сохранив заметки в файл.
        else:
            print('Введите корректную команду')
            # Программа реагирует на некорректный ввод данных
