class Table:
    def __init__(self, name, columns, primary_key=None, unique_keys=None):
        """
        columns: dict -> {column_name: type}
        """
        self.name = name
        self.columns = columns
        self.primary_key = primary_key
        self.unique_keys = unique_keys or []
        self.rows = []

    def insert(self, row):
        self._validate_row(row)
        self.rows.append(row)

    def select_all(self):
        return self.rows

    def _validate_row(self, row):
        # check missing columns
        for col in self.columns:
            if col not in row:
                raise ValueError(f"Missing column: {col}")

        # primary key constraint
        if self.primary_key:
            for r in self.rows:
                if r[self.primary_key] == row[self.primary_key]:
                    raise ValueError("Primary key constraint violated")

        # unique constraints
        for key in self.unique_keys:
            for r in self.rows:
                if r[key] == row[key]:
                    raise ValueError(f"Unique constraint violated on {key}")
