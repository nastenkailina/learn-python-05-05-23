"""
    Создаем функцию "add" для добавления заметок.
    Ввод пользователем заметки.
    Добавляем заметки в существующий список.
    """


def add(note):
    ask_note = input('Введите заметку: ')
    note.append(ask_note)


"""
    Создаем функцию "earliest" для вывода заметок от ранней к последней.
    Выводим список.
    """


def earliest(note):
    print(note)


"""
     Создаем функцию "latest" для вывода заметок от последней к ранней.
     Выводим список.
     """


def latest(note):
    print(note[::-1])


"""
    Создаем функцию "longest" для вывода заметок от длиннейших к более коротким.
    Выводим список.
    """


def longest(note):
    long = sorted(note, key=len, reverse=True)
    print(long)


"""
    Создаем функцию "shortest" для вывода заметок от более коротких к длиннейшим.
    Выводим список.
    """


def shortest(note):
    short = sorted(note, key=len)
    print(short)


if __name__ == '__main__':
    list_note = []  # Сохраняет заметки в список.
    while True:
        customer_input = input()
        if customer_input == 'add':
            add(list_note)
        elif customer_input == 'earliest':
            earliest(list_note)
        elif customer_input == 'latest':
            latest(list_note)
        elif customer_input == 'longest':
            longest(list_note)
        elif customer_input == 'shortest':
            shortest(list_note)
        elif customer_input == 'end':
            break
            # Когда пользователь пишет команду 'end', программа завершает работу.
        else:
            print('Введите корректную команду')
            # Программа реагирует на некорректный ввод данных
