import re                                                      #импорт библиотеки re
input_string = input('Tell about yourself:')                   #Користувач вводить строку
input_string = input_string.lower()                            #Програма переводить строку в нижній регістр

input_string = re.sub('[,-:;?!)]', '', input_string)           #Програма видаляє зі строки такі символи пунктуації: .,-:;?!
input_string = input_string.rstrip()                           #Програма видаляє зайві пробіли\табуляції з правого кінця строки

input_replace = input('What do you want to replace?')          #Програма питає користувача яке слово він бажає замінити
print(input_replace, 'was found at position', input_string.find(input_replace))     #Програма повідомляє на якому індексі строки словосполучення присутнє

input_replacement = input('With what do you want to replace?')                      #Програма питає на яке слово треба замінити
print(input_string.replace(input_replace, input_replacement))                       #Програма змiнюю слова i виводить відформатовану строку





