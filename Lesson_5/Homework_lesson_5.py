numbers = []
while True:  # Використовуємо «while» для циклу. Задаємо умови
    number_input = input('Введите число (или "sum" для подсчета суммы):')  # Користувач вводить строку
    if number_input.isdigit():
        number = int(number_input)  # Завдаємо тип "int"
        numbers.append(number)  # Використали "append" щоб додати елемент у кінець списка.

    elif 'sum' in number_input:  # Якщо користувач вводить ключове слово.
        result = sum(numbers)  # Використовуємо функцію "sum".
        print(result)  # Виводимо результат додавання.
        break  # Завершили виконання програми.
    else:
        print('Invalid Input. Пожалуйста, введите число или "sum"')
        # Програма відповідає, якщо не розуміє введений текст.

