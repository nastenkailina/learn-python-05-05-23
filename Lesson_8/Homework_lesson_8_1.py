def time(x):
    day = divmod(x, 1 * 60 * 60 * 24)
    hour = divmod(day[1], 60 * 60)
    minute = divmod(hour[1], 1 * 60)
    seconds = divmod(minute[1], 1)
    d = {'day': day[0], 'hour': hour[0], 'minute': minute[0], 'seconds': seconds[0]}
    return d
    """
    Создаем функцию для конвертации дней. часов, минут в секунды, с помощью "divmod".
    Создаем словарь с ключами days, hours, minutes, seconds и их значениями.
    Возвращаем значение функции.
    """


if __name__ == '__main__':
    number_input = int(input('Напишите ваше число\n>'))
    # Пользователь вводит строку, преобразовывая в ‘int’.
    print(time(number_input))
    # Выводим результат, вызывая функцию.
