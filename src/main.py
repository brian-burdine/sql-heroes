from database.db_connection import execute_query

def display_active_heroes ():
    query = "SELECT id, name FROM heroes"
    heroes = execute_query(query)
    print("Active Heroes:")
    for hero in heroes:
        print(f'{hero[0]}: {hero[1]}')

display_active_heroes()