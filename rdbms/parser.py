import re


def parse(command):
    command = command.strip().rstrip(";")

    if command.upper().startswith("CREATE TABLE"):
        return parse_create(command)

    if command.upper().startswith("INSERT INTO"):
        return parse_insert(command)

    if command.upper().startswith("SELECT"):
        return parse_select(command)

    raise ValueError("Unsupported command")


def parse_create(cmd):
    match = re.match(r"CREATE TABLE (\w+)\s*\((.+)\)", cmd, re.I)
    if not match:
        raise ValueError("Invalid CREATE TABLE syntax")

    table_name = match.group(1)
    raw_columns = match.group(2).split(",")

    columns = {}
    primary_key = None
    unique_keys = []

    for col in raw_columns:
        parts = col.strip().split()
        name = parts[0]
        dtype = parts[1]
        columns[name] = dtype

        if "PRIMARY" in col.upper():
            primary_key = name
        if "UNIQUE" in col.upper():
            unique_keys.append(name)

    return ("CREATE", table_name, columns, primary_key, unique_keys)


def parse_insert(cmd):
    match = re.match(r"INSERT INTO (\w+) VALUES\s*\((.+)\)", cmd, re.I)
    if not match:
        raise ValueError("Invalid INSERT syntax")

    table_name = match.group(1)
    values = [v.strip().strip("'") for v in match.group(2).split(",")]

    return ("INSERT", table_name, values)


def parse_select(cmd):
    parts = cmd.split()
    return ("SELECT", parts[-1])

