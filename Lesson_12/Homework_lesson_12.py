import csv
import uuid


def open_csv_file_dict(filename) -> list:
    """
    Функция читает ряды csv файла как dict (с заголовками),
     возвращает их и выводит на экран при надобности
    :param filename: путь к файлу, который нужно открыть
    :return: возвращаем содержимое файла списком рядов,
             каждый ряд - словарь,
             ключи словаря - заголовки csv файла
    """
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        return rows


def genarate_uniq_id():
    """
    Генеруе унікальні ид
    """
    return uuid.uuid4()


def create_uniq_index(all_data: list) -> dict:
    """
    Створює індекс унікальних айді для кожного запису
    """
    new_index = dict()
    for data_entry in all_data:
        new_index[genarate_uniq_id()] = data_entry
    return new_index


def create_index(all_data: dict, column_name: str) -> dict:
    """
    В этой функции создаётся индекс по колонке, чьё имя мы указываем
    :param all_data: данные в которых находятся колонки из которых мы строим индекс.
                    Данные представлены в виде список словарей
    :param column_name: имя колонки, по которой построить индекс
    :return: индекс, т.е. словарь,
            где ключи - это уникальные значения из колонки column_name,
            а значения под ключами - это список записей из all_data,
            у которых есть такое значение в column_name
    """
    new_index = dict()
    for data_entry in all_data:
        key = all_data[data_entry][column_name]
        if key not in new_index:
            new_index[key] = list()
        new_index[key].append(data_entry)
    return new_index


def show_statistic(all_data, type):
    """
    Виводить на екран статистику скільки товарів є по переданому словнику
    """
    title = ' в категории: '
    if type == 'brand':
        title = ' по брендам: '
    for data_entry in all_data:
        count = str(len(all_data[data_entry]))
        print('Товаров'+title+data_entry+' - '+count+'шт.')


def calc_items_by_category(uniq_index_data, data_index):
    """
    Рахує розподіл товарів по брендам для кожної категорії
    """
    new_index = dict()
    for category_key in data_index:
        for key in data_index[category_key]:
            item = uniq_index_data[key]

            if category_key not in new_index:
                new_index[category_key] = dict()
            brand = item['brand']
            if brand not in new_index[category_key]:
                new_index[category_key][brand] = 0
            new_index[category_key][brand] += 1

    return new_index


def show_items_by_category(items):
    """
    Виводить на єкран розподіл товарів по брендам для кожної категорії
    """
    for category in items:
        print('в категорії ' + category + ' представлено:')
        for model in items[category]:
            count = str(items[category][model])
            print('- ' + model + ' ' + count + ' шт.')


def show_full_info(uniq_index_data, data_index, name):
    """
    Виводить на екран перелік повної інформації про кожний товар одного обраного бренда чи однієї обраної категорії
    """
    for data in data_index[name]:
        print(uniq_index_data[data])


if __name__ == '__main__':
    file = open_csv_file_dict('tech_inventory.csv')

    uniq_index = create_uniq_index(file)

    category_index = create_index(uniq_index, 'category')
    brand_index = create_index(uniq_index, 'brand')

    show_statistic(category_index, 'category')
    show_statistic(brand_index, 'brand')

    items_by_category = calc_items_by_category(uniq_index, category_index)
    show_items_by_category(items_by_category)

    show_full_info(uniq_index, category_index, 'Laptop')
    show_full_info(uniq_index, brand_index, 'Asus')
