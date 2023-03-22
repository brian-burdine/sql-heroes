# SQL Heroes

## Objective

Create an application that allows a user to interact with a database of superheroes in the terminal. The application should have full CRUD (Create Read Update Delete) functionality.

## Database Structure

- heroes
  - id
  - name
  - about_me
  - biography
  - image_url

- abilities
  - id
  - hero_id
  - ability_type_id
	
- ability_types
  - id
  - name

- relationships
  - id
  - hero1id
  - hero2id
  - relationship_type_id

- relationship_types
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
   - Display all heroes in the heroes table along with their id
2. **display_hero_info** (*id*)
   - Display:
     - ID: Name
     - "about_me"
     - Powers: abilities
     - Biography
     - Friends:
       - any friends
     - Foes:
       - any enemies
3. **add_hero**
   - Prompt for hero name
   - Prompt for optional about me blurb
   - Prompt for optional biography
   - Insert command
   - Ask if user want to execute functions 4 and or 5?
4. **change_power** (*id*)
   - List current powers
   - Ask if user wants to
     - a. add a power
     - b. remove a power
     - c. quit
    - If a.
	  - Provide a list of current powers
	  - Ask if user wants to add one of those, or a new one
        - if new one, INSERT new one into ability_types
        - UPDATE abilities with hero
	- If b.
5. change_relationship (id1, id2)
6. retire_hero (id)

### Procedure:
	Declare an input value
	Loop while input value != an escape value (like 'N' or something)
	Present a numbered list of options
	If the user enters a supported option, call a function that executes a query
	Many functions require further input to build the query

"Welcome to the Internet Superpowered People Database"
"Enter a numbered option below, or enter 'Q' to quit"
1. Get a list of active superheroes
2. Get information about a superhero by ID
3. Add a new hero to the database
4. Add or remove a power from a hero
5. Add or change a relationship between heroes
6. Retire a hero from the database

