import sqlite3

def add_value(coursor: object, name_table: str, name_column: str, id: str, column_values: str):
    try:
        coursor.execute(f"INSERT INTO {name_table} (ID, {name_column}) VALUES (?, ?)", (id, column_values))
    except sqlite3.IntegrityError:
        print(f"\nIntegrityError:\nTry to rewrite value of column '{name_column}' in row '{id}'\n")
    except sqlite3.InterfaceError:
        print("\ninvalid value error\n")
        



    
