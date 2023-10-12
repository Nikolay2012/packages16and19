def create_table(coursor: object, name_table: str):
    coursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table} (ID INEGER PRIMARY KEY)")
