#задание 1
import math                 #подключили модуль math для использования функций

x = 180 / math.pi           #радианы переводим в градусы
n = float(input('Сколько радиан перевести в градусы?'))

y = n * x
print(round(y, 5))          #выводим результат, округляя до 5 цифр, после запятой
