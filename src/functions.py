from database.db_connection import execute_query

# Adds a record with passed values to a table and returns the id of the new entry
def add_record (table, **entries):
    # Build query from passed values
    columns, columns_str, values = [], "", []
    for key, value in entries.items():
        columns.append(key)
        columns_str += key + ", "
        values.append(value)
    # Cut off the last ", "
    columns_str = columns_str[0:-2]
    
    query = f"INSERT INTO {table} ({columns_str}) VALUES ({('%s, ' * len(columns))[0:-2]})"
    execute_query(query, tuple(values))

    # Get id for new entry and return it
    query = f"SELECT MAX(id) FROM {table}"
    id = execute_query(query).fetchone()[0]
    return id

# Updates values of the record with matching id in the target table with passed entries
def update_record (table, id, **entries):
    # Build query from passed values
    columns, columns_str, values = [], "", []
    for key, value in entries.items():
        columns.append(key)
        columns_str += key + " = %s, "
        values.append(value)
    # Cut off the last ", "
    columns_str = columns_str[0:-2]
    # Add id to tuple of values to execute query
    values.append(id)
    
    query = f"UPDATE {table} SET {columns_str} WHERE id=%s"
    execute_query(query, tuple(values))

# Deletes the record with matching id from target table
def delete_record (table, id):
    query = f"DELETE FROM {table} WHERE id=%s"
    execute_query(query, (id,))

# Retrieves the name of the hero with the given id
def get_hero_name (id):
    # Get the name of the current hero
    query = "SELECT name FROM heroes WHERE id=%s"
    hero = execute_query(query, (id,)).fetchone()
    
    # Check to see if passed id returned a record
    if hero == None:
        print(f'Hero {id} not found')
        return None
    hero_name = hero[0]
    return hero_name

# Displays the ids and names of all heroes in the heroes table
def display_active_heroes ():
    # Get a count of the number of entries in heroes
    query = "SELECT COUNT(id) FROM heroes"
    act_hero_count = execute_query(query).fetchone()[0]
    
    # Get the id and names of all heroes
    query = "SELECT id, name FROM heroes"
    heroes = execute_query(query)
    
    # Display retrieved information
    print(f"Active Heroes: {act_hero_count}")
    for hero_id, hero_name in heroes:
        print(f'{hero_id}: {hero_name}')

# Displays a hero's name, "about me" blurb, biography, powers, and 
# relationships with other heroes, given their id
def display_hero_info (id):
    # Get relevant information from heroes table
    query = "SELECT name, about_me, biography FROM heroes WHERE id=%s";
    hero = execute_query(query, (id,)).fetchone()
    
    # Don't try to destructure an empty query or it breaks!
    if hero == None:
        print(f'Hero {id} not found')
        return
    hero_name, hero_about_me, hero_biography = hero
    
    # Get hero abilities
    query = "SELECT at.name FROM ability_types as at JOIN abilities as a ON a.ability_type_id=at.id WHERE a.hero_id=%s"
    abilities = execute_query(query, (id,)).fetchall()
    hero_abilities = []
    for ability in abilities:
        hero_abilities.append(ability[0])

    # Get hero relationships
    query = "SELECT relationship_types.name, heroes.name FROM ((relationships JOIN heroes ON relationships.hero2_id = heroes.id) JOIN relationship_types ON relationships.relationship_type_id = relationship_types.id) WHERE relationships.hero1_id=%s"
    relationships = execute_query(query, (id,)).fetchall()
    hero_friends, hero_foes = [], []
    for relationship in relationships:
        if relationship[0] == "Friend":
            hero_friends.append(relationship[1]) 
        elif relationship[0] == "Enemy":
            hero_foes.append(relationship[1])
    
    # Display retrieved information
    print(f'{id}: {hero_name}')
    print("Tagline: " + hero_about_me)
    print("Abilities:")
    for ability in hero_abilities:
        print(ability)
    print("Biography:")
    print(hero_biography)
    print("Friends:")
    for friend in hero_friends:
        print(friend)
    print("Foes:")
    for foe in hero_foes:
        print(foe)

# Adds a new hero to the heroes table. Requires a name, other fields are optional
def add_hero():
    # Prompt the user for information about the hero they want to add
    hero_name = input("Enter a name for the hero: ")
    about_me_check = input("Enter a tagline? Y/N: ")
    hero_about_me = input("Tagline: ") if about_me_check.upper() == 'Y' else ""
    biography_check = input("Enter a biography? Y/N: ")
    hero_biography = input("Biography: ") if biography_check.upper() == 'Y' else ""
    
    # Insert the new hero into the database
    # query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    # execute_query(query, (hero_name, hero_about_me, hero_biography))
    hero_id = add_record("heroes", name = hero_name, about_me = hero_about_me, biography = hero_biography)

    # Get the new hero's id
    # query = "SELECT MAX(id) FROM heroes"
    # hero_id = execute_query(query).fetchone()[0]

    # Update the user that the hero was added, prompt them to modify other tables
    print(f"Hero {hero_name} was added to the database with id {hero_id}")
    ability_check = input(f"Would you like to give {hero_name} an ability? Y/N: ")
    if ability_check.upper() == 'Y':
        change_power(hero_id)
    relationship_check = input(f"Would you like to give {hero_name} some friends or foes? Y/N: ")
    if relationship_check.upper() == 'Y':
        change_relationship(hero_id)

# Updates the value of the name column of the record of the given id in the heroes table
def change_name (id):
    old_name = get_hero_name(id)

    if not old_name == None:
        name_check = input(f"Would you like to change {old_name}'s codename? Y/N: ")
        if name_check.upper() == 'Y':
            new_name = input("Enter new codename: ")
            update_record("heroes", id, name = new_name)

# Updates the value of the about_me column of the record of the given id in the heroes table
def change_about_me (id):
    hero_name = get_hero_name(id)

    if not hero_name == None:
        about_me_check = input(f"Would you like to change {hero_name}'s tagline? Y/N: ")
        if about_me_check.upper() == 'Y':
            new_about_me = input("Enter new tagline: ")
            update_record("heroes", id, about_me = new_about_me)

# Updates the value of the biography column of the record of the given id in the heroes table
def change_biography (id):
    hero_name = get_hero_name(id)

    if not hero_name == None:
        biography_check = input(f"Would you like to change {hero_name}'s biography? Y/N: ")
        if biography_check.upper() == 'Y':
            new_biography = input("Enter new tagline: ")
            update_record("heroes", id, biography = new_biography)

def change_power (id):
    pass

# Brings up a list of current relationships to other heroes, and prompts the 
# user to select another hero to alter the relationship with
def change_relationship (id):
    # Get the name of the target hero
    hero_name = get_hero_name(id)

    if hero_name == None:
        return
    
    # Three columns: id of hero, name of hero, their relationship to current hero
    # Get the ids and names of other heroes
    query = "SELECT h.id, h.name FROM heroes as h WHERE id<>%s"
    other_heroes = execute_query(query, (id,)).fetchall()
    if other_heroes == None:
        print("No other heroes were found, cannot update relationships")
        return
    
    relation_list = []
    for other_hero_id, other_hero_name in other_heroes:
        relation_list.append([other_hero_id, other_hero_name, "Unaffiliated"])

    # Get the relationships current hero already possesses
    query = "SELECT r.hero2_id, rt.name FROM relationships as r JOIN relationship_types as rt ON r.relationship_type_id=rt.id WHERE hero1_id=%s"
    relationships = execute_query(query, (id,)).fetchall()

    # Update relation_list if any pre-existing relationships exist
    if relationships != None:
        for hero_id, relationship in relationships:
            for item in relation_list:
                if hero_id == item[0]:
                    item[2] = relationship
    
    # Display current relationships
    print(f"Relationships of {hero_name}:")
    for item in relation_list:
        print(f"{item[0]}: {item[1]} --- {item[2]}")
    
    find_hero, new_relation_id = True, 0
    while find_hero:
        hero_check = input(f"Enter the id of the hero that you want to change {hero_name}'s relationship with: ")
        if hero_check == id:
            print("Only relationships with other people, please")
            continue
        hero_check = int(hero_check)
        for item in relation_list:
            if hero_check == item[0]:
                new_relation_id = hero_check
                find_hero = False
        
        if find_hero:
            continue_check = input("Id was not found. Input another id? Y/N: ")
            if continue_check.upper() == 'Y':
                continue
            else:
                return
    
    print(new_relation_id)


# Removes the hero from the heroes table
def retire_hero (id):
    # Confirm the user wants to delete this hero
    query = "SELECT name FROM heroes WHERE id=%s"
    hero_name = execute_query(query, (id,)).fetchone()[0]
    retire_check = input(f"Remove {hero_name} from the database? Y/N: ")

    # If yes, remove all records in the heroes, abilities, and relationships table that reference that hero
    if retire_check.upper() == 'Y':
        query = "DELETE FROM heroes WHERE id=%s"
        execute_query(query, (id,))
        query = "DELETE FROM abilities WHERE hero_id=%s"
        execute_query(query, (id,))
        query = "DELETE FROM relationships WHERE hero1_id=%s OR hero2_id=%s"
        execute_query(query, (id, id))

        print(f"{hero_name} was retired from the database")