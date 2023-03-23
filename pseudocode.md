# SQL Heroes

## Objective

Create an application that allows a user to interact with a database of superheroes in the terminal. The application should have full CRUD (Create Read Update Delete) functionality. psycopg is used to query the database.

## Database Structure

- **heroes**
  - id
  - name
  - about_me
  - biography
  - image_url

- **abilities**
  - id
  - hero_id
  - ability_type_id
	
- **ability_types**
  - id
  - name

- **relationships**
  - id
  - hero1id
  - hero2id
  - relationship_type_id

- **relationship_types**
  - id
  - name

## Application Structure
### CRUD
- C:
  - Add a hero
- R:
  - Look at a list of current heroes
  - Get a heroe's about_me, biography, relationships, and powers
- U:
  - Add or remove a power (or powers) from a hero
  - Change a heroe's relationships
- D:
  - Retire a hero
	
### Functions
1. **display_active_heroes**
   - Display all heroes in the **heroes** table along with their id
   - Procedure:
     1. START **display_active_heroes**
     2. QUERY the **heroes** table for the count of entries in the *id* column (everything should have an id, at least), STORE the value in *act_hero_count*
     3. QUERY the **heroes** table for the *id* and *name* columns, STORE the value in *heroes*
     4. PRINT the string "Active Hero Count:" and the value of *act_hero_count*
     5. FOR every item in *heroes* (should be a tuple containing the id and name for each record in **heroes**)
        1. PRINT a string with the format "(id): (name)"
     6. ENDFOR
     7. END **display_active_heroes**
2. **display_hero_info** (*id*)
   - Receives the id of a hero in heroes to display
   - Displays:
     - ID: Name
     - "about_me"
     - Abilities: 
       - any abilities
     - Biography:
       - biography
     - Friends:
       - any friends
     - Foes:
       - any enemies
   - Procedure: 
     1. START **display_hero_info**
     2. QUERY the **heroes** table for the name, about_me, and biography columns of the record where the passed *id* matches the value of the id column, store the value in *hero*
     3. IF *hero* is empty (the passed id was not in the **heroes** table)
        1. PRINT "Hero (id) was not found"
        2. RETURN
     4. ELSE
        1. STORE the values of the name, about_me, and biography columns in *hero_name*, *hero_about_me*, *hero_biography*
     5. ENDIF
     6. QUERY the **abilities** table for the *ability_type_id* of all records where the passed *id* matches the value of the *hero_id* column, and then QUERY the **ability_types** table for the name column that matches those *ability_type_id* keys
     7. STORE the values of the name column in **ability_types** in *hero_abilities*
     8. QUERY the **heroes**, **relationships**, and **relationship_types** tables to retrieve the records where the passed *id* matches the value of *hero1_id* in **relationships**, and retrieve the *name*s from **heroes** that match the values of *hero2_id* in those records, and retrieve the *name*s from **relationship_types** that match the values of *relationship_type_id* in those records
     9. Store the values with the relationship named "Friend" in *hero_friends*, and those with the relationship named "Enemy" in *hero_foes*
     10. PRINT a string with the format "*id*: *hero_name*"
     11. PRINT *hero_about_me*
     12. Print "Abilities:"
     13. FOR every ability in *hero_abilities*
         - PRINT the ability
     14. ENDFOR
     15. PRINT "Biography:"
     16. PRINT *hero_biography*
     17. PRINT "Friends:"
     18. FOR every friend in *hero_friends*
         - PRINT the name of the friend
     19. ENDFOR
     20. PRINT "Foes:"
     21. FOR every foe in *hero_foes*
         - PRINT the name of the enemy
     22. ENDFOR
     23. END **display_hero_info**
3. **add_hero**
   - Prompt for hero name
   - Prompt for optional about me blurb
   - Prompt for optional biography
   - Insert command
   - Ask if user want to execute functions 4 and or 5?
4. **change_power** (*id*)
   - List hero's current powers
   - Ask if user wants to
     - a. add a power
     - b. remove a power
     - c. quit
    - If a.
	    - Provide a list of current powers
	    - Ask if user wants to add one of those, or a new one
        - if new one
          - INPUT new ability
          - INSERT new ability into ability_types
          - GET the id from ability_types (name matches new ability)
          - UPDATE abilities with hero id and ability type id
    - Else if b.

5. change_relationship (*id*)
6. retire_hero (*id*)
   - Query the **heroes** table for the *name* that matches the passed *id*, store the value in *hero_name*
   - Ask the user if they want to delete the record for *hero_name*
   - If yes:
     - Delete the record that matches the passed *id* from the table
     - Print "*hero_name* was retired from the database"

### Procedure:
	Declare an input value
	Loop while input value != an escape value (like 'N' or something)
	Present a numbered list of options
	If the user enters a supported option, call a function that executes a query
	Many functions require further input to build the query

The prompts:
"Welcome to the Internet Superpowered People Database"
"Enter a numbered option below, or enter 'Q' to quit"
1. Get a list of active superheroes
2. Get information about a superhero by ID
3. Add a new hero to the database
4. Add or remove a power from a hero
5. Add or change a relationship between heroes
6. Retire a hero from the database

