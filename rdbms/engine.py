from rdbms.table import Table


class Database:
    def __init__(self):
        self.tables = {}

    def create_table(self, name, columns, primary_key=None, unique_keys=None):
        if name in self.tables:
            raise ValueError("Table already exists")
        self.tables[name] = Table(name, columns, primary_key, unique_keys)

    def insert(self, table_name, row):
        table = self._get_table(table_name)
        table.insert(row)

    def select_all(self, table_name):
        table = self._get_table(table_name)
        return table.select_all()

    def _get_table(self, table_name):
        if table_name not in self.tables:
            raise ValueError("Table does not exist")
        return self.tables[table_name]
