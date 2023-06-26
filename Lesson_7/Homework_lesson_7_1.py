import math  # Подключили модуль math для использования функций.
def convert_radians_to_degrees(radian_input):   # Создаем функцию, вводим параметры
    return round(radian_input * (180 / math.pi), 5)
    # Возвращаем значение функции, округляя до 5 цифр, после запятой.
radian_input = float(input('Сколько радиан перевести в градусы?\n>'))
result = convert_radians_to_degrees(radian_input)
print(result)   # Выводим результат.














