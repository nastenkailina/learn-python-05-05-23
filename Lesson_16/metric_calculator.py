import uuid


class MetricCalculator:
    def __init__(self, data):
        self.data = data
        self.sku_index = self.create_index('sku')
        self.warehouse_index = self.create_index('warehouse')
        self.operation_index = self.create_index('operation')

    def genarate_uniq_id(self):
        """
        генерация уникального id
        """
        return uuid.uuid4()

    def create_index(self, index_name):
        """
        создание индексов
        """
        new_index = dict()
        for data_entry in self.data:
            value = data_entry.get_data()
            key = value[index_name]
            if key not in new_index:
                new_index[key] = list()
            new_index[key].append(value)

        return new_index

    def calculate_metric_income(self):
        """
        прибуток від усіх операцій типу sale
        """
        total_cost = 0

        for item in self.operation_index['sale']:
            total_cost += item['operation_cost']

        return total_cost

    def calculate_metric_lost_sku(self):
        """
        скільки унікальних SKU було втрачено (expiration_date минуло і sale не відбулося)
        """
        total = 0

        for item in self.data:
            if item.expired():
                total += 1

        return total

    def calculate_metric_move_through_warehouse(self):
        """
        скільки товарів "пройшло" через кожний склад (warehouse)
        """
        for warehouse in self.warehouse_index:
            print(f'Через склад {warehouse} прошло {len(self.warehouse_index[warehouse])}шт. товаров')

    def calculate_metric_sell_through_warehouse(self):
        """
        скільки товарів було продано з кожного складу (warehouse)
        """
        for warehouse in self.warehouse_index:
            total_sell = 0
            for item in self.warehouse_index[warehouse]:
                if item['operation'] == 'sale':
                    total_sell += 1
            print(f'Через склад {warehouse} было продано {total_sell}шт. товаров')

    def calculate_metric_dispose_through_warehouse(self):
        """
        скільки товарів було утилізовано (dispose) з кожного складу (warehouse)
        """
        for warehouse in self.warehouse_index:
            total_sell = 0
            for item in self.warehouse_index[warehouse]:
                if item['operation'] == 'dispose':
                    total_sell += 1
            print(f'Через склад {warehouse} было утилизировано {total_sell}шт. товаров')
