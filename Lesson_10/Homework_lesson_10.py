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


if __name__ == '__main__':
    list_note = []  # Сохраняет заметки в список.
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
        elif customer_input == 'end':
            break
            # Когда пользователь пишет команду 'end', программа завершает работу.
        else:
            print('Введите корректную команду')
            # Программа реагирует на некорректный ввод данных
