from file_processor import FileProcessor
from cvs_reader import CSVProcessor
from json_processor import JSONProcessor
from metric_calculator import MetricCalculator


if __name__ == '__main__':
    reader = FileProcessor('SKU')
    csv = CSVProcessor(reader, 'SKU')
    json = JSONProcessor(reader, 'SKU')

    csv.process_directory()
    json.process_directory()

    calculator = MetricCalculator(reader.data)

    print(calculator.calculate_metric_income())
    print(calculator.calculate_metric_lost_sku())
    print(calculator.calculate_metric_move_through_warehouse())
    print(calculator.calculate_metric_sell_through_warehouse())
    print(calculator.calculate_metric_dispose_through_warehouse())
