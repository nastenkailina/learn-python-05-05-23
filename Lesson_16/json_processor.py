import json
from file_processor import FileProcessor


class JSONProcessor(FileProcessor):
    def __init__(self, file_processor: FileProcessor, dir_path):
        super().__init__(
            dir_path=dir_path,
        )
        self.file_processor = file_processor

    def get_data(self, filename):
        """
        читаем данные из файла
        """
        with open(f'{self.dir_path}/{filename}', newline='') as json_file:
            reader = json.load(json_file)
            return reader['data']

    def process_directory(self):
        """
        добавляем в поле родительского класса новый товар
        """
        for filename in self.processed_filenames:
            if '.json' in filename:
                data = self.get_data(filename)
                for item in data:
                    self.file_processor.add_data_entry(item)
