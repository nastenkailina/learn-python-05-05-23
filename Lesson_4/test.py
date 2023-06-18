hi_input = ''
do_input = ''
rest_input = ''
bye_input = ''

while True:
    if hi_input == '':
        hi_input = input('').lower()
        if hi_input == 'хай' or hi_input =='доброго дня':
            print('Доброго вечора, я бот з України!')
        else:
            print('Привітайся зі мною')
            hi_input = ''

    elif do_input == '':
        do_input = input('').lower()
        if do_input == 'як справи?' or do_input == 'що робиш?' or do_input == 'чим займаєшся?':
            print('Вчусь програмувати на Python!')
        else:
            print('Дізнайся, що я роблю:)')
            do_input = ''

    elif rest_input == '':
        rest_input = input('').lower()
        if 'о, а я дивлюсь фільм "код да вінчі". може ти можеш щось відрекомендувати мені?' in rest_input or 'а я пішов до кінотеатру на новий фільм жахів. може ти можеш щось відрекомендувати мені?' in rest_input:
            print('Я звісно всього-навсього бездушна машина та не можу наполягати, але подивись серіал «Постукай у мої двері», Серкан Болат там просто  чарівний!')
        else:
            print('Скажи мені, що ти робиш, якщо це не секрет)')
            rest_input = ''

    elif bye_input == '':
        bye_input = input('').lower()
        if 'дуже дякую за рекомендацію, обов‘язково подивлюсь! бувай, друже!' in bye_input or 'дуже дякую за рекомендацію, обов‘язково подивлюсь! Надобраніч!' in bye_input:
            print('Побачимось у мережі. Зовсім скоро я довчуся і захоплю світ! I‘ll be back. ')
            break
        else:
            print('Може попрощаєшся з новим другом?) ')
            bye_input = ''



