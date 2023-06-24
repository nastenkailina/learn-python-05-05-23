import re  # Імпорт бібліотеки 're'
palindrom_input = input().lower().strip()
# Користувач вводить строку, переводить строку в нижній регістр, видаляє зайві пробіли\табуляції.
punctuation = ',._ -:;?!"/()'
for x in palindrom_input:  # Цикл 'for'
    if x in punctuation:
        palindrom_input = palindrom_input.replace(x, '')  # Програма видаляє зі строки розділові знаки.

if palindrom_input[::-1] == palindrom_input:  # Програма перевіряє чи є введена строка паліндромом.
    print('Так, строка є паліндромом')
else:
    print('Ні, строка не є паліндромом')
