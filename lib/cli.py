import inquirer
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import Session, declarative_base, validates
from models import *

engine = create_engine('sqlite:///darktide_builder.db')
Base.metadata.create_all(engine)


def main():
    with Session(engine) as session:
        #home menu
        def home_menu():
            questions = [
                inquirer.List(
                    "chosen_menu",
                    message = "Welcome to the RPG weapon perking simulator, what would you like to do?",
                    choices = [
                        "View Weapons List",
                        "View Perks List",
                        "View Perked Weapons",
                        "Exit"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["chosen_menu"] == "View Weapons List":
                view_weapon()
            elif response["chosen_menu"] == "View Perks List":
                view_perk()
            elif response["chosen_menu"] == "View Perked Weapons":
                view_perked_weapons()
            else:
                exit()
            
#full CRUD on Weapon

        #view weapons list
        def view_weapon():
            weapon = session.query(Weapons).all()
            questions = [
                inquirer.List(
                    "option",
                    message = "Choose a Weapon to add, or select a Weapon to Edit it",
                    choices = weapon + ["Add new weapon", "Back"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] =="Back":
                home_menu()
            elif answer["option"] == "Add new weapon":
                new_weapon()
            else:
                edit_weapon(answer["option"])

        #update or delete a weapon
        def edit_weapon(Weapons):
            questions = [
                inquirer.List(
                    "option",
                    message = "What would you like to do to this weapon?",
                    choices = ["Edit Name", "Edit Type", "Edit Subclass", "Delete", "Back"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] == "Back":
                view_weapon()
            if answer["option"] == "Edit Name":
                # update name
                new_name = input("Enter the new name:   ")
                Weapons.name = new_name 
                session.commit()
                edit_weapon(Weapons)
            if answer["option"] == "Edit Type":
                new_type = input("Update Weapon Type:   ")
                Weapons.type = new_type
                session.commit()
                edit_weapon(Weapons)
            if answer["option"] == "Edit Subclass":
                new_subclass = input("Update Subclass:   ")
                Weapons.subclass = new_subclass
                session.commit()
                edit_weapon(Weapons)
            if answer["option"] == "Delete":
                # delete the weapon
                session.delete(Weapons)
                session.commit()
                view_weapon()

        #Add a New Weapon
        def new_weapon():
            new_name = input("What is the name of the new weapon:   ")
            new_weapon = session.query(Weapons).filter(Weapons.name == new_name.title()).first()
            if new_weapon is None:
                new_weapon = Weapons(name = new_name.title())
                session.add(new_weapon)
                session.commit()
            new_type = input("What is the typing of the new weapon:   ")
            new_weapon.type = new_type
            session.add(new_weapon)
            session.commit()
            new_subclass = input("What is this weapon's subclass:   ")
            new_weapon.subclass = new_subclass
            session.add(new_weapon)
            session.commit()
            view_weapon()
#full CRUD on Perk

        #view perks list
        def view_perk():
            perk = session.query(Perks).all()
            questions = [
                inquirer.List(
                    "option",
                    message = "Choose a Perk to add, or select a Perk to Edit it",
                    choices = perk + ["Add new perk", "Back"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] =="Back":
                home_menu()
            elif answer["option"] == "Add new perk":
                new_perk()
            else:
                edit_perk(answer["option"])

        #update or delete a perk
        def edit_perk(perk):
            questions = [
                inquirer.List(
                    "option",
                    message = "What would you like to do to this perk?",
                    choices = ["Edit Name", "Edit Type", "Edit Subclass", "Delete", "Back"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] == "Back":
                view_perk()
            if answer["option"] == "Edit Name":
                # update name
                new_name = input("Enter new name:   ")
                perk.name = new_name 
                session.commit()
                edit_perk(perk)
            if answer["option"] == "Edit Type":
                new_type = input("Update Perk Type:   ")
                perk.type = new_type
                session.commit()
                edit_perk(Perks)
            if answer["option"] == "Edit Subclass":
                new_subclass = input("Update Subclass:   ")
                perk.subclass = new_subclass
                session.commit()
                edit_perk(perk)
            if answer["option"] == "Delete":
                # delete the perk
                session.delete(perk)
                session.commit()
                view_perk()

        #Add a New Perk
        def new_perk():
            new_name = input("What is the name of the new perk:   ")
            new_perk = session.query(Perks).filter(Perks.name == new_name.title()).first()
            if new_perk is None:
                new_perk = Perks(name = new_name.title())
                session.add(new_perk)
                session.commit()
            new_type = input("What is the typing of the new perk:   ")
            new_perk.type = new_type
            session.add(new_perk)
            session.commit()
            new_subclass = input("What is this perk's subclass:   ")
            new_perk.subclass = new_subclass
            session.add(new_perk)
            session.commit()
            view_perk()
            

# full CRUD on Perked Weapons:
        # view all Perked Weapons
        def view_perked_weapons():
            perkedup = session.query(Perked_Weapons).all()
            perkedup_names = []
            for perked_weapons in perkedup:
                perkedup_names.append(perked_weapons.name)
            questions = [
                inquirer.List(
                    "option",
                    message = "Choose a perked weapon to edit it, or add a new one",
                    choices = perkedup_names + ["Add a new perked weapon", "Back"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] == "Back":
                home_menu()
            elif answer["option"] == "Add a new perked weapon":
                new_perked_weapons_name = input("New perked weapon name: ")
                new_perked_weapons = Perked_Weapons(name = new_perked_weapons_name)
                session.add(new_perked_weapons)
                session.commit()
                edit_perked_weapons(new_perked_weapons)
            else:
                perked_weapons_to_edit = session.query(Perked_Weapons).filter(Perked_Weapons.name == answer["option"]).first()
                edit_perked_weapons(perked_weapons_to_edit)

        # edit a perked weapon
        def edit_perked_weapons(perked_weapons):
            print(perked_weapons)
            questions = [
                inquirer.List(
                    "option",
                    message = "What would you like to do with this perked weapon?",
                    choices = ["Change name", "Edit weapon", "Edit Perk", "Delete", "Back"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] == "Back":
                view_perked_weapons()
            if answer["option"] == "Delete":
                # delete the perked weapon
                session.delete(perked_weapons)
                session.commit()
                view_perked_weapons()
            elif answer["option"] == "Edit weapon":
                edit_weapons(perked_weapons)
            elif answer["option"] == "Change name":
                # Change the name
                new_name = input("New Name:  ")
                perked_weapons.name = new_name
                session.commit()
                edit_perked_weapons(perked_weapons)
            elif answer["option"] == "Edit Perk":
                edit_perk(perked_weapons)
                
        # specifically edit the weapons in a perked weapons
        def edit_weapons(perked_weapons):
            current_weapon = perked_weapons.weaps
            questions = [
                inquirer.List(
                    "option",
                    message = "How Would you like to edit this weapon?",
                    choices = ["Change Name","Change Type", "Change Subclass", "Back"] 
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["option"] == "Back":
                view_weapon()
            if answer["option"] == "Change Name":
                # update name
                new_name = input("Enter the new name:   ")
                Weapons.name = new_name 
                session.commit()
                edit_weapon(Weapons)
            if answer["option"] == "Change Type":
                new_type = input("Update Weapon Type:   ")
                Weapons.type = new_type
                session.commit()
                edit_weapon(perked_weapons)
            if answer["option"] == "Change Subclass":
                new_subclass = input("Update Subclass:   ")
                Weapons.subclass = new_subclass
                session.commit()
                edit_weapon(Weapons)
            
            else:
                session.delete(answer["option"])
                session.commit()
                edit_perked_weapons(perked_weapons)


# specifically edit the perks in a perked weapon
        def edit_perk2(perked_weapons):
            perk_list = perked_weapons.perks
            questions = [
                inquirer.List(
                    "option",
                    message = "Select a perk to edit or delete it, or add a new perk",
                    choices = perk_list + ["Add a new perk", "Back"] 
                )
            ]
            answer = inquirer.prompt(questions)
            
            if answer["option"] == "Back":
                edit_perked_weapons(perked_weapons)
            elif answer["option"] == "Add a new weapon":
                new_name = input("Perk Name: ")
                new_perk = session.query(Perks).filter(Perks.name == new_name.title()).first()
                if new_perk is None:
                    # if a perk does not exist make the perk
                    new_perk = Perks(name = new_name.title())
                    session.add(new_perk)
                    session.commit()

            else:
                session.delete(answer["option"])
                session.commit()
                edit_perked_weapons(perked_weapons)
    home_menu()


main()



""""
def main():
    with Session(engine) as session:
        def home_menu():
            questions = [
                inquirer.List(
                    'chosen_menu',
                    message = "All Hail The God Emperor of Mankind! Welcome Recruit, to the Armory, where you can customize your loadout for Warhammer: Darktide:", 
                    choices = [
                        "View your Inventory",
                        "View your Character Build",
                        "Mission Select",
                        "Exit"
                    ]
                )
            ]
            response = inquirer.prompt(questions)
            if response["chosen_menu"] == "Mission Select":
                view_mission_menu()
            elif response["chosen_menu"] == "View your Inventory":
                view_inventory()
            elif response["chosen_menu"] == "View your Character Builds":
                view_character_builds()
            else:
                exit()

#Mission Menu Stuff:
        def view_mission_menu():
            mission_list = session.query(Mission).all()
            questions = [
                inquirer.List(
                    "mission",
                    message = "Select a Mission",
                    choices = ["Submit Mission Proposal"]+mission_list+["Return to Main Deck"]
                )
            ]
            answer = inquirer.prompt(questions)
            if answer["mission"] == "Return to Main Deck":
                home_menu()
            elif answer["mission"] == "Submit Mission Proposal":
                new_mission_name = input("Enter New Mission Name")
"""