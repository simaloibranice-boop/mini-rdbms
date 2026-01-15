from rdbms.engine import Database
from rdbms.parser import parse


def run():
    db = Database()
    print("MiniRDBMS started. Type 'exit' to quit.")

    while True:
        command = input("db> ")

        if command.lower() == "exit":
            break

        try:
            result = parse(command)

            if result[0] == "CREATE":
                _, name, columns, pk, uq = result
                db.create_table(name, columns, pk, uq)
                print("Table created")

            elif result[0] == "INSERT":
                _, table, values = result
                cols = list(db.tables[table].columns.keys())
                row = dict(zip(cols, values))
                db.insert(table, row)
                print("Row inserted")

            elif result[0] == "SELECT":
                _, table = result
                rows = db.select_all(table)
                for r in rows:
                    print(r)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    run()

