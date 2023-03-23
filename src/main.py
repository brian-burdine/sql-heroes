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

query_database = True

print("Welcome to the Internet Superpowered People Database")

while query_database:
    print("Enter a numbered option below, or enter 'Q' to quit")
    print("1. Get a list of active superheroes")
    print("2. Get information about a superhero by ID")

    term_input = input("Enter option: ")

    match term_input:
        case '1':
            display_active_heroes()
        case '2':
            hero_id = input("Enter a hero id to look up: ")
            display_hero_info(hero_id)
        case 'Q':
            print("Exiting database, have a nice day")
            query_database = False
        case _:
            print("Invalid option entered")
