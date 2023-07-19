from os import walk
from data_entry import DataEntry


class FileProcessor:
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.processed_filenames = self.get_filenames()
        self.data = []

    def get_filenames(self):
        """
        получаем все имена файлов в директории
        """
        for (dirpath, dirnames, filenames) in walk(self.dir_path):
            return filenames

    def add_data_entry(self, item):
        """
        добавляем в поле data новый товар
        """
        value = DataEntry(item['date'], item['time'], item['sku'], item['warehouse'], item['warehouse_cell_id'], item['operation'], item['invoice'], item['expiration_date'], item['operation_cost'], item['comment'])
        self.data.append(value)

    def process_directory(self):
        raise NotImplementedError
