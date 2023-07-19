from datetime import datetime


class DataEntry:
    def __init__(self, date, time, sku, warehouse, warehouse_cell_id, operation, invoice, expiration_date, operation_cost, comment):
        self.date = datetime.strptime(date, '%d-%b-%Y').date()
        self.time = datetime.strptime(time, '%H:%M:%S').time()
        self.sku = sku
        self.warehouse = warehouse
        self.warehouse_cell_id = int(warehouse_cell_id)
        self.operation = operation
        self.invoice = invoice
        self.expiration_date = datetime.strptime(expiration_date, '%d-%b-%Y').date()
        self.operation_cost = float(operation_cost)
        self.comment = comment

    def get_data(self):
        """
        возвращаем словарь данных
        """
        data = dict()
        data['date'] = self.date
        data['time'] = self.time
        data['sku'] = self.sku
        data['warehouse'] = self.warehouse
        data['warehouse_cell_id'] = self.warehouse_cell_id
        data['operation'] = self.operation
        data['invoice'] = self.invoice
        data['expiration_date'] = self.expiration_date
        data['operation_cost'] = self.operation_cost
        data['comment'] = self.comment
        return data

    def expired(self):
        """
        проверяем истек ли товар
        """
        return self.date >= self.expiration_date or self.operation == 'sale'
