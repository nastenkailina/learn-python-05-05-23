text = input().lower()  # Користувач вводить строку, переводить строку в нижній регістр.
def remove_text_in_parentheses(text):  # Функція для видалення дужок
    while '(' in text:  # Цикл
        start_index = text.find('(')
        # Використовуємо метод find() для знаходження індексу першого входження символу '('.
        end_index = text.find(')')  #  Шукаємо індекс ')'
        if end_index != -1:
            text = text[:start_index] + text[end_index + 1:]  # Якщо ')' також знайдений, ми використовуємо зрізи.
        else:
            break
        return text
output_text = remove_text_in_parentheses(text)  # Програма видаляє дужки
print(output_text)  # Програма виводить текст без дужок і тексту в них







