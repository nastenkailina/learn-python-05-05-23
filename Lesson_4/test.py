while True:  # Використовуємо «while» для циклу. Задаємо умови
    all_input = input('').lower()  # Користувач вводить строку
    if 'хай' in all_input or 'доброго дня' in all_input:  # Умова, за якої бот надасть корректну відповідь.
        print('Доброго вечора, я бот з України!')  # Відповідь бота, якщо умова виконується.
    elif 'як справи?' in all_input or 'що робиш?' in all_input:  # Умова, за якої бот надасть корректну відповідь.
        print('Вчусь програмувати на Python!')  # Відповідь бота, якщо умова виконується.
    elif 'о, а я дивлюсь фільм "код да вінчі". може ти можеш щось відрекомендувати мені?' in all_input:
        # Умова, за якої бот надасть корректну відповідь.
        print('Я звісно всього-навсього бездушна машина та не можу наполягати, але подивись серіал «Постукай у мої двері», Серкан Болат там просто  чарівний!')
        # Відповідь бота, якщо умова виконується.
    elif 'дуже дякую за рекомендацію, обов‘язково подивлюсь! бувай, друже!' in all_input or 'дуже дякую за рекомендацію, обов‘язково подивлюсь! Надобраніч!' in all_input:
        # Умова, за якої бот надасть корректну відповідь.
        print('Побачимось у мережі. Зовсім скоро я довчуся і захоплю світ! I‘ll be back. ')
        # Відповідь бота, якщо умова виконується.
        break  # Завершили виконання програми

    else:
        print('На жаль, я не розумію вашого запиту. Можливо, ви можете пояснити більш детально?')
        # Бот відповідає, якщо не розуміє введений текст.
        continue  #Продовжити виконання програми

