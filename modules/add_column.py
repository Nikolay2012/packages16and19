def add_column(coursor: object, name_table: str, name_column: str, type_column: str):
    try:    
        coursor.execute(f"ALTER TABLE {name_table} ADD COLUMN {name_column} {type_column}")
    except:
        print(f"Try to create duplicate column '{name_column}'")
