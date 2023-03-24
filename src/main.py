from functions import *

query_database = True

print("Welcome to the Internet Superpowered People Database")

while query_database:
    print("Enter a numbered option below, or enter 'Q' to quit")
    print("1. Get a list of active superheroes")
    print("2. Get information about a superhero by ID")
    print("3. Add a new hero to the database")
    print("4. Change a hero's codename")
    print("5. Change a hero's tagline")
    print("6. Change a hero's biography")
    print("7. Add or remove an ability from a hero")
    print("8. Update a hero's relationships")
    print("9. Retire a hero from the database")

    term_input = input("Enter option: ")

    match term_input.upper():
        case '1':
            display_active_heroes()
        case '2':
            hero_id = input("Enter a hero id to look up: ")
            display_hero_info(hero_id)
        case '3':
            add_hero()
        case '4':
            hero_id = input("Enter a hero id to modify: ")
            change_name(hero_id)
        case '5':
            hero_id = input("Enter a hero id to modify: ")
            change_about_me(hero_id)
        case '6':
            hero_id = input("Enter a hero id to modify: ")
            change_biography(hero_id)
        case '7':
            hero_id = input("Enter a hero id to modify: ")
            change_power(hero_id)
        case '8':
            hero_id = input("Enter a hero id to modify: ")
            change_relationship(hero_id)
        case '9':
            hero_id = input("Enter a hero id to retire: ")
            retire_hero(hero_id)
        case 'Q':
            print("Exiting database, have a nice day")
            query_database = False
        case _:
            print("Invalid option entered")
