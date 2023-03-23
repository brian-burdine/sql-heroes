def add_record (table, **entries):
    columns, columns_str, values = [], "", []
    for key, value in entries.items():
        columns.append(key)
        columns_str += key + ", "
        values.append(value)
    columns_str = columns_str[0:-2]
    query = f"INSERT INTO {table} ({columns_str}) VALUES ({('%s, ' * len(columns))[0:-2]})"
    print(query)

def update_record (table, id, **entries):
    columns, columns_str, values = [], "", []
    for key, value in entries.items():
        columns.append(key)
        columns_str += key + " = %s, "
        values.append(value)
    columns_str = columns_str[0:-2]
    query = f"UPDATE {table} SET {columns_str} WHERE id=%s"
    print(query)

def delete_record (table, id):
    query = f"DELETE FROM {table} WHERE id=%s"
    print(query)

list_a = [1, 2, 3]
print(str(tuple(list_a)))

add_record("heroes", name = "BB", about_me = "Me!", biography = "Also me!")
update_record("heroes", 10, name = "Bloody Mary", about_me = "She's made of blood!")
delete_record("heroes", -1)