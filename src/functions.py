from database.db_connection import execute_query

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
    print(hero_about_me)
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
    about_me_check = input("Enter an 'about me' phrase? Y/N: ")
    hero_about_me = input("About me: ") if about_me_check.upper() == 'Y' else ""
    biography_check = input("Enter a biography? Y/N: ")
    hero_biography = input("Biography: ") if biography_check.upper() == 'Y' else ""
    
    # Insert the new hero into the database
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    execute_query(query, (hero_name, hero_about_me, hero_biography))

    # Get the new hero's id
    query = "SELECT MAX(id) FROM heroes"
    hero_id = execute_query(query).fetchone()[0]

    # Update the user that the hero was added, prompt them to modify other tables
    print(f"Hero {hero_name} was added to the database with id {hero_id}")
    ability_check = input(f"Would you like to give {hero_name} an ability? Y/N: ")
    if ability_check.upper() == 'Y':
        change_power(hero_id)
    relationship_check = input(f"Would you like to give {hero_name} some friends or foes? Y/N: ")
    if relationship_check.upper() == 'Y':
        change_relationship(hero_id)

def change_power (id):
    pass

def change_relationship (id):
    pass

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